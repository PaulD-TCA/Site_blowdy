# Generated by Django 3.1.5 on 2021-03-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_code', models.CharField(max_length=50)),
                ('p_name', models.CharField(max_length=200)),
                ('p_description', models.CharField(max_length=1000)),
                ('p_image', models.FileField(upload_to='product_image')),
                ('p_category', models.CharField(max_length=50)),
            ],
        ),
    ]
