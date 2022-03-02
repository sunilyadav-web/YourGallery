from django.urls import path
from mygallery.views import *


urlpatterns = [
    path('',index),
    path('signup',signup),
    path('save-user',saveUser),
    path('login',login),
    path('login-validation',loginValidation),
    path('logout',logout),
    path('my-gallery',mygallery),
    path('make-gallery',makegallery),
    path('save-gallery',saveGallery),
    path('delete-image',deleteImage),
    
]
