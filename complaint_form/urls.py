from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  CategoriesrViewsSet

router = DefaultRouter()
router.register('categories' , CategoriesrViewsSet , basename='categories')


urlpatterns = router.urls