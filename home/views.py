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
		self.views['subcategories'] = Subcategory.objects.all()
		self.views['sliders'] = Slider.objects.all()

		return render(request,'index.html',self.views)

class SubCategory(BaseView):
	def get(self,request,slug):
		ids = Subcategory.objects.get(slug = slug).id
		self.views['subcat_items'] = Item.objects.filter(subcategory_id = ids)
		return render(request,'subcategory.html',self.views)