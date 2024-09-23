from django.db import models


class House(models.Model):

    class HomeType(models.TextChoices):
        house = 'House'
        condo = 'Condo'
        townhouse = 'Townhouse'

    class SaleType(models.TextChoices):
        for_sale = 'For sale'
        for_rent = 'For rent'

    realtor = models.EmailField(max_length=254)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20)
    area = models.FloatField(default=1)
    description = models.TextField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length=10, choices=HomeType.choices, default=HomeType.house)
    sale_type = models.CharField(max_length=10, choices=SaleType.choices, default=SaleType.for_sale)
    main_picture = models.ImageField(upload_to='uploads')
    picture1 = models.ImageField(upload_to='uploads')
    picture2 = models.ImageField(upload_to='uploads')
    picture3 = models.ImageField(upload_to='uploads')
    picture4 = models.ImageField(upload_to='uploads')
    slug = models.SlugField(unique=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(max_length=20)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        ''' Automatically saves this model to the 'secondary' database'''
        kwargs['using'] = 'listings'
        super().save(*args, **kwargs)


class PlotOfLand(models.Model):

    realtor = models.EmailField(max_length=254)
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=20)
    description = models.TextField()
    zoning_type = models.CharField(max_length=50)
    sale_type = models.CharField(max_length=10, choices=House.SaleType.choices, 
                                 default=House.SaleType.for_sale)
    main_picture = models.ImageField(upload_to='uploads')
    picture1 = models.ImageField(upload_to='uploads', null=True)
    picture2 = models.ImageField(upload_to='uploads', null=True)
    picture3 = models.ImageField(upload_to='uploads', null=True)
    picture4 = models.ImageField(upload_to='uploads', null=True)
    slug = models.SlugField(unique=True, null=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(max_length=20)
    area = models.FloatField(default=0)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        ''' Automatically saves this model to the 'secondary' database'''
        kwargs['using'] = 'listings'
        super().save(*args, **kwargs)
