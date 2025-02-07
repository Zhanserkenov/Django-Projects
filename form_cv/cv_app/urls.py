from django.urls import path
from .views import create_cv, cv_list, share_cv_email

urlpatterns = [
    path('create/', create_cv, name='create_cv'),
    path('list/', cv_list, name='cv_list'),
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
]
