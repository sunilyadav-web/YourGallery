from django.urls import path
from mygallery.views import *


urlpatterns = [
    path('',index,name='home'),
    path('signup',signup,name='signup'),
    path('save-user',saveUser,name='saveuser'),
    path('login',login,name='login'),
    path('login-validation',loginValidation,name='loginvalidation'),
    path('logout',logout,name='logout'),
    path('my-gallery',mygallery,name='mygallery'),
    path('make-gallery',makegallery,name='makegallery'),
    path('save-gallery',saveGallery,name='savegallery'),
    path('delete-image',deleteImage,name='deleteimage'),
    
]
