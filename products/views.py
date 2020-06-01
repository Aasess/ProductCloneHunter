from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from datetime import datetime

# Create your views here.
def home(request):
    product = Product.objects
    return render(request, 'products/home.html',{'product':product})


@login_required
def create(request):
    if request.method == "POST":
        if request.POST["title"] and request.POST["body"] and request.POST["url"] and request.FILES["image"] and request.FILES["icon"]:
            product = Product()
            product.title = request.POST["title"]
            product.body = request.POST["body"]
            product.url = request.POST["url"]
            product.image = request.FILES["image"]
            product.icon = request.FILES["icon"]
            product.pub_date = datetime.now()
            product.usernameID = request.user
            product.save()
            return redirect("/" + str(product.id))

        else:
            return render(request, 'products/create.html', {'error': "fields are empty!!"})
    else:
        return render(request, 'products/create.html')

def details(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})

@login_required
def upvote(request,product_id):
    if request.method == "POST":
        product = get_object_or_404(Product,pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect("/"+str(product.id))

@login_required
def upvotehome(request,product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect("/")
