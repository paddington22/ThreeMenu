from django.urls import path

from menu.views import MenuTemplateView

urlpatterns = [
    path('', MenuTemplateView.as_view(), name='menu')
]