from django.urls import path
from . import views
from .views import AddCustomer, UpdateAccount, DeleteAccount, AccountDetail, AddBalance
urlpatterns = [
        path('',views.home,name='home1'),
        path('home',views.index,name='home'),
        path('view_all/',views.showall,name='view_all'),
        path('add_customer/',AddCustomer.as_view(),name='add_customer'),
        path('opening_balance/',AddBalance.as_view(),name='opening_balance'),
        path('detail/<int:pk>/',AccountDetail.as_view(),name='detail'),
        path('update/<int:pk>/',UpdateAccount.as_view(),name='update'),
        path('delete/<int:pk>/',DeleteAccount.as_view(),name='delete'),
        path('transaction/', views.transaction, name='transaction'),
        path('balance/',views.balance,name='balance'),
        path('transfer/',views.transfer,name='transfer')



]