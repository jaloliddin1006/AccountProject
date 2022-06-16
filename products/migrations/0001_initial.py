# Generated by Django 4.0.4 on 2022-05-31 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, upload_to='image/')),
                ('price', models.CharField(max_length=20)),
                ('subtitle', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('quenty', models.CharField(max_length=255)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
