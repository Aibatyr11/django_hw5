from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Children(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(Human, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class IceCream(models.Model):
    size = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    kiosk = models.ForeignKey('Kiosk', related_name='ice_creams', on_delete=models.CASCADE)  # связь с киоском

    def __str__(self):
        return f'Ice Cream size {self.size}, price {self.price}'



class Kiosk(models.Model):
    quantity_of_icecream = models.IntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name = "Kiosk"
        verbose_name_plural = "Kiosks"
        ordering = ['size']

    def __str__(self):
        return f'Kiosk size {self.size}'
