from ast import Return
from django.shortcuts import get_object_or_404, render
from store.models import Product, ProductsCategory
from django.db.models import Q
from .cart import Cart

def StoreView(request):
    categories = ProductsCategory.objects.all()
    products = Product.objects.all()[0:10]
    active_category = request.GET.get('c','')
    
    if active_category:
        products = Product.objects.filter(category__slug=active_category)
    
    query = request.GET.get('query', '')
    
    if query:
        products.filter(Q(name__iconains=query) | Q(description__iconains=query))
    context = {'products': products, 'categories': categories, 'active_category': active_category}
    return render(request,'store_index.html', context)

def ProductView(request, pk):
    product = get_object_or_404(Product,id=pk)
    return render(request,'product_detail.html', {'product': product})

def CartView(request):
    return {'cart': Cart(request)}

def Add_to_Cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    
    return render(request, 'addtocart.html')