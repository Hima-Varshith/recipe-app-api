from django.urls import path
from user import views

app_name ='user'

urlpatterns = [path('create/',views.CreateUserView.as_view(),name ='create'),
               path('token/', views.CreateTokenView.as_view(), name='token'),
               path('me/', views.ManageUserView.as_view(), name='me'),]

# PUT : updates and replaces the entire object,have to provide all the fields
# PATCH : only updates the values that we provide
