# Generated by Django 4.1.5 on 2023-06-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_package_coupon_alter_package_additionalcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='product',
            field=models.CharField(max_length=255),
        ),
    ]
