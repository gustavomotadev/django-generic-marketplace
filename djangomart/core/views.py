from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):

    items = Item.objects.filter(is_sold=False).order_by('-created_at')[:6]
    
    category_data = [{'name': category.name, 'id': category.id, 
        'for_sale_count': category.items.filter(is_sold=False).count()
        } for category in Category.objects.all()]

    return render(request, 'core/index.html', {
            'category_data': category_data,
            'items': items,
        })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('/login/')
    
    #else

    form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
