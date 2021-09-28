from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseView(View):
	views = {}


class HomeView(BaseView):
	def get(self,request):
		self.views['items'] = Item.objects.all()
		self.views['categories'] = Category.objects.all()
		self.views['sliders'] = Slider.objects.all()

		return render(request,'index.html')