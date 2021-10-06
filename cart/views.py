from django.shortcuts import render
from home.views import *
from .models import *
# Create your views here.
class CartView(BaseView):
	def get(self,request):
		self.views['carts'] = Cart.objects.filter(user = request.user,checkout = False)
		return render(request,'wishlist.html',self.views)