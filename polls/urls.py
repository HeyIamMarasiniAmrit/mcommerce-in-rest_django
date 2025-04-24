
from django.urls import path, include
from . import views
from polls.views import listpolls

urlpatterns = [

    path('pollslist/',views.listPolls,name='listPolls'),
    path('messagelist/',views.listmessages,name='message'),
    path('classpollslist/', listproducts.as_view(), name='listproducts'),
    path('classDetailed/', productDetailedView.as_view, name='detailedProduct'
    path('mixinpath/',views.listproductsMixins.as_view(),name='mp')
    path('productmixin/<int:pk>',views.DetailedProductMixins.as_view(),name='mdp')
]

