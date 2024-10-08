# Generated by Django 5.1.1 on 2024-09-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realtor', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('home_type', models.CharField(max_length=50)),
                ('sale_type', models.CharField(max_length=10)),
                ('main_picture', models.ImageField(upload_to='uploads')),
                ('picture', models.ImageField(upload_to='uploads')),
                ('picture2', models.ImageField(upload_to='uploads')),
                ('picture3', models.ImageField(upload_to='uploads')),
                ('picture4', models.ImageField(upload_to='uploads')),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
