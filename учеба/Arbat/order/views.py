from django.shortcuts import render, redirect
from .models import Article_order
from .forms import ArticlesForm
from django.views.generic import DetailView


def order_home(request):
    order = Article_order.objects.all()
    return render(request, 'order/order.html', {'order': order})


class OrderDetailView(DetailView):
    model = Article_order
    template_name = 'order/order_view.html'
    context_object_name = 'article'


def order_create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'В форме допущены ошибки!'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'order/create.html', data)