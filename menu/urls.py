from django.urls import path

from menu.views import MenuTemplateView

app_name = 'menu'

urlpatterns = [
    path('', MenuTemplateView.as_view(), name='index')
]