from django.urls import path
from ebdecl.views import *

urlpatterns = [
    path('',index),
    path('firms/',firms),
    path('decladd/', decladd),





]