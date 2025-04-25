from django.urls import path, include
from . import views
from polls.views import listpolls
from .views import productDetailsView, listproducts, productviewset
from rest_framework.routers import defaultRouter

router = defaultRouter()
router.register(
    'productviewset',Productviewset,basename='product'
)

urlpatterns = [

    path('pollslist/',views.listPolls,name='listPolls'),
    path('messagelist/',views.listmessages,name='message'),
    path('classpollslist/', listproducts.as_view(), name='listproducts'),
    path('classDetailed/', productDetailedView.as_view, name='detailedProduct'
    path('mixinpath/',views.listproductsMixins.as_view(),name='mp')
    path('productmixin/<int:pk>',views.DetailedProductMixins.as_view(),name='mdp')
    path('productgenericlist/',views.listproductGenerics.as_view(),name='lpg')
    path('productgenericdetailed/<int:pk>',views.DetailedproductGenerics.as_view(),name='dpg')
    path('special/<int:pk>', views.specialproductGenerics.as_view(), name='spg')

]+router.urls
