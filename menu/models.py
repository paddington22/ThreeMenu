from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


#@receiver(post_save, sender=Item)
#def update_stock(sender, instance, **kwargs):
#    print(instance)
#    Menu.objects.create(title=instance)