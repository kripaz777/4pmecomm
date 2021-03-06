from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
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

class ProductView(BaseView):
	def get(self,request,slug):
		self.views['product_details'] = Item.objects.filter(slug = slug)
		self.views['hot_product'] = Item.objects.filter(labels = 'hot')
		return render(request,'single.html',self.views)


class SearchView(BaseView):
	def get(self,request):

		query = request.GET.get('query',None)
		if not query:
			return redirect('/')
		self.views['search_query'] = Item.objects.filter(title__icontains = query)
		return render(request,'search.html',self.views)


def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['cpassword']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		if password == cpassword:
			if User.objects.filter(username = username).exists():
				messages.error(request,'The username is already exists')
				return redirect('/signup')
			elif User.objects.filter(email = email).exists():
				messages.error(request,'The email is already exists')
				return redirect('/signup')
			else:
				user = User.objects.create_user(
					username = username,
					email = email,
					password = password,
					first_name = first_name,
					last_name = last_name)
				user.save()
				messages.success(request,'You are registered!')
				return redirect('/')
	return render(request,'register.html')