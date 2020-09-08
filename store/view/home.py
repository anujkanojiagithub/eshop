from django.shortcuts import render, HttpResponse, redirect
from store.models.product import Product, Category

def index(request):

    categories = Category.getAllCategory()
    cat_id = request.GET.get('category')
    if cat_id:
        products = Product.getProductByCat(cat_id)
    else:
        products = Product.get_all_product()

    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)
