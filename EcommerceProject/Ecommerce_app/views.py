from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import category,product
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.




# def index(request):
#       return render(request,'test.html')

def allprodCat(request,cslug=None):
      cpage=None
      product_list=None
      if cslug!=None:
            cpage=get_object_or_404(category,slug=cslug)
            product_list=product.objects.all().filter(ctg=cpage,available=True)
      else:
            product_list=product.objects.all().filter(available=True)
      paginator=Paginator(product_list,6)
      try:
            page=int(request.GET.get('page','1'))
      except:
            page=1
      try:
            products=paginator.page(page)
      except (EmptyPage,InvalidPage):
            products=paginator.page(paginator.num_pages)

      return render(request,'category.html',{'cpage':cpage,'products':products})

def ProDetail(request,cslug,product_slug):
      try:
            prod=product.objects.get(ctg__slug=cslug,slug=product_slug)
      except Exception as e:
            raise e
      return render(request,'product.html',{'prod':prod})