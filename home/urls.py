from django.urls import path
from .views import *

app_name = "home"

urlpatterns = [
   path('', HomeView.as_view(), name='home'),
   path('subcategory/<slug>', SubCategory.as_view(), name='subcategory'),
]
