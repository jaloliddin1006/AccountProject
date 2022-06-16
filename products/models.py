from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
# Create your models here.
class Products(models.Model):
    Product_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='image/', blank=True)
    price = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=255)
    desc = RichTextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    quenty = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pk} - {self.Product_name} - {self.price}"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])



class Comment(models.Model):
    product_id = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    comment = models.CharField(max_length=150)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.pk)])
