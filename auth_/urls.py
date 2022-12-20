from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
# from auth_.views.cbv import ProfileApiView

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('profiles/<int:pk>/', ProfileApiView.as_view())
]