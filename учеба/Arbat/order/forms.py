from .models import Article_order
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Article_order
        fields = ['title', 'email', 'name', 'company', 'description', 'link', 'date', 'username']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заказа'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта для обратной связи',
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Как к вам обращаться?',
            }),
            "company": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название вашей компании',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите ваш заказ:',
            }),
            "link": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка на диск с материалами',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выполнения заказа',
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
            }),
        }
