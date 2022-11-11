# Generated by Django 4.1.2 on 2022-11-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_category',
            field=models.CharField(default=3, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
