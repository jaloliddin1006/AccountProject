

from django.urls import path
from .views import IndexPage,IndexDetail,Addpro,UpProduct,DeletePro

urlpatterns = [

    path('Products/<int:pk>/update', UpProduct.as_view(), name='updatepro'),
    path('Products/<int:pk>/delete', DeletePro.as_view(), name='deletepro'),
    path('Products/<int:pk>',IndexDetail.as_view(), name='detail'),
    path('Products/add',Addpro.as_view(), name='addpro'),
    path('', IndexPage.as_view(), name='products_list'),
]