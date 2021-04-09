from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from sub_admin.models import Category, Product
from django.contrib import messages

def index(request):
    categoryList = Category.objects.all()
    products = Product.objects.all()

    # for product in products:
    #     for productimage in product.productimage_set.all():
    #         print(productimage.image)

    data = {
        "categoryList": categoryList,
        "products": products,
        "page_name": "Home"
    }
    return render(request, "index.html", data)


def category(request):
    if(request.method == "POST"):
        categoryName = request.POST['name']
        category = Category(name = categoryName)
        category.save()
        messages.success(request, f'{categoryName} saved successfully')


    categoryList = Category.objects.all()
    return render(request, "category.html", {"categoryList" : categoryList})


def product(request):

    if request.method == "POST":

        category = Category(id = int(request.POST['category']))

        product = Product(name = request.POST['name'], short_description = request.POST['short_description'], long_description = request.POST['long_description'], discount = int(request.POST['discount']), price = float(request.POST['price']), rating = int(request.POST['rating']), qty = int(request.POST['qty']), category = category)

        product.save()

        

    categoryList = Category.objects.all()


    context = {
        "categoryList" : categoryList
    }

    return render(request, "product.html", context)

