from django.shortcuts import render,redirect
from .models import Category

# Create your views here.
def gallery(request):
    category = request.GET.get('category_name')
    if category==None:
        photos=Image.objects.all()
    else:
        photos=Image.objects.filter(category_name__name=category)
    categories= Category.objects.all()
    context= {'categories':categories, 'photos':photos}
    
    return render(request,'gallery.html',context)