from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import OpenAccount, Status



# Create your views here.

def home(request):
    return render(request,'home1.html')

@login_required
def index(request):
    return render(request,'home.html')


@login_required()
def showall(request):
    custms= OpenAccount.objects.all()
    context={
        'custms': custms
    }
    return render(request,'list.html',context)

class AddCustomer(CreateView,LoginRequiredMixin):
    model = OpenAccount
    fields = '__all__'
    template_name = 'add_customer.html'
    success_url = reverse_lazy('opening_balance')

class AddBalance(CreateView,LoginRequiredMixin):
    model = Status
    fields ='__all__'
    template_name = 'add_balance.html'
    success_url = reverse_lazy('view_all')

class AccountDetail(DetailView,LoginRequiredMixin):
    model= OpenAccount
    template_name='detail.html'
    context_object_name = 'customers'


class UpdateAccount(UpdateView,LoginRequiredMixin):
    model = OpenAccount
    fields = '__all__'
    template_name = 'add_customer.html'
    success_url = reverse_lazy('view_all')


class DeleteAccount(DeleteView,LoginRequiredMixin):
    model= OpenAccount
    context_object_name = 'accounts'
    success_url = reverse_lazy('view_all')
    template_name = 'delete.html'

@login_required()
def transaction(request):
   if request.method=='POST':
      user_name= request.POST.get('name')
      acc  = request.POST.get('account_number')
      amount = int(request.POST.get('amount'))
      customer= Status.objects.get(account_number=acc)
      if request.POST['transaction'] == 'Deposit':
         customer.amount+=amount
         customer.save()
      else:
        customer.amount-= amount
        customer.save()

      return redirect('balance')
   return render(request,'depositwithdraw.html')


@login_required()
def balance(request):
    custms=Status.objects.all()
    context={
        'custms': custms
    }
    return render(request,'balance.html',context)

@login_required()
def transfer(request):

    if request.method=='POST':
        try:
            user_one=request.POST.get('user_one')
            acc_num1 = request.POST.get('acc_num1')
            user_two = request.POST.get('user_two')
            acc_num2=request.POST.get('acc_num2')
            amount=int(request.POST.get('amount'))
            user_one_obj = Status.objects.get(account_number=acc_num1)
            user_two_obj=Status.objects.get(account_number= acc_num2)
            user_one_obj.amount=user_one_obj.amount-amount
            user_two_obj.amount=user_two_obj.amount+amount
            user_one_obj.save()
            user_two_obj.save()

            messages.success(request,'Amount transferred successfully')
        except:
            messages.success(request, 'Something went wrong')
    return render(request,'transfer_money.html')



























# def search(request):
#     query=request.GET['q']
#     objs=Status.objects.filter(name__icontains=query)
#     params={"objs": objs}
#     return render(request,'balance.html',params)




# class NameSearchView(ListView):
#     model = Status
#     context_object_name = 'customers'
#     template_name = 'balance.html'
#
#     def get_queryset(self):
#         query=self.request.GET.get('q')
#         return Status.objects.filter(name__icontains=query)
