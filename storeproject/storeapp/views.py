from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import logging
from datetime import datetime, timedelta
from .models import Client, Product, Order
from .forms import ProductForm


def home_page(request):
    #logger.info(f'{datetime.now().strftime("%H:%M:%S")} Открыта главная страница')
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
       <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #FDF5E6;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
                color: #666;
            }
            footer {
                text-align: center;
                margin-top: 20px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container", width = 100%>
            <h1>Добро пожаловать на мой первый интернет-магазин!</h1>
            <p>В дальнейшем здесь вы найдете уникальные товары и аксессуары, которые нельзя найти нигде еще.</p>
            <p>Мы гордимся тем, что предоставляем экспертное обслуживание и заботу для наших клиентов.</p>
            <p>Наша миссия — следовать модным тенденциям, создавать стильные образы и предоставлять клиентам то, что они хотят.</p>
            <p>Наша цель — изменить взаимодействие общества с индустрией моды, предоставляя клиентам продукты, которые производятся этично и ответственно.</p>
            <footer>© 2024 Мой первый интернет-магазин. Все права защищены.</footer>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)

def clients(request):
    all_clients = Client.objects.all()

    context = {'all_clients': all_clients}

    return render(request, "storeapp/clients.html", context)



def products(request):
    all_products = Product.objects.all()

    context = {'all_products': all_products}

    return render(request, "storeapp/products.html", context)

def orders(request):
    all_orders = Order.objects.all()

    context = {'all_orders': all_orders}

    return render(request, "storeapp/orders.html", context)



def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

    period = request.GET.get('period')

    today = datetime.today().date()
    if period == '7':
        start_date = today - timedelta(days=7)
    elif period == '30':
        start_date = today - timedelta(days=30)
    elif period == '365':
        start_date = today - timedelta(days=365)
    else:
        start_date = None

    if start_date:
        client_orders = Order.objects.filter(client_id=client_id, date_ordered__gte=start_date).order_by('date_ordered')
    else:
        client_orders = Order.objects.filter(client_id=client_id).order_by('date_ordered')

    context = {'client': client, 'client_orders': client_orders}
    return render(request, 'storeapp/client_orders.html', context)


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            foto = form.cleaned_data['foto']
            fs = FileSystemStorage()
            fs.save(foto.name, foto)
            form.save()

    else:
        form = ProductForm(instance=product)

    return render(request, 'storeapp/update_product.html', {'form': form})


