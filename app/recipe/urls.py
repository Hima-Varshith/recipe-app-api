from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

#def-router automatically generates/registers all the URLs for our user : /api/recipe/tags/id
router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients',views.IngredientViewSet)
#regsiters the viewset with the router
app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
#all urls generated are included in the path
