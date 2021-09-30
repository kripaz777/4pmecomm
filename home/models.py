from django.db import models
from django.urls import reverse

STATUS = (('active','active'),('','default'))
LABELS = (('new','new'),('hot','hot'),('sale','sale'),('','default'))
STOCK = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length= 500,unique = True)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	status = models.CharField(choices = STATUS,max_length = 200,blank = True)
	def __str__(self):
		return self.title

class Subcategory(models.Model):
	title = models.CharField(max_length = 400)
	category = models.ForeignKey(Category,models.CASCADE)
	slug = models.CharField(max_length= 500,unique = True)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	def __str__(self):
		return self.title
	def get_subcat_url(self):
		return reverse ('home:subcategory',kwargs = {'slug':self.slug})

class Item(models.Model):
	title = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500,unique = True)
	price = models.IntegerField()
	discounted_price = models.IntegerField(default = 0)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	category = models.ForeignKey(Category,models.CASCADE)
	subcategory = models.ForeignKey(Subcategory,models.CASCADE)
	stock = models.CharField(choices = STOCK,max_length = 50)
	labels = models.CharField(choices = LABELS,max_length = 50)

	def __str__(self):
		return self.title

class Ad(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField(default = 1)

	def __str__(self):
		return self.title

class Slider(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField(blank = True)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField(default = 1)
	status = models.CharField(choices = STATUS,blank = True,max_length = 50)

	def __str__(self):
		return self.title

class Contact(models.Model):
	name = models.CharField(max_length = 500)
	email = models.EmailField(max_length = 500)
	message = models.TextField()

	def __str__(self):
		return self.title