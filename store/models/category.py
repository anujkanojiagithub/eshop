from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

    @staticmethod
    def getAllCategory():
        # no need to this function your are just increasing a function call.
        return Category.objects.all()
