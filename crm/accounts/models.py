from django.db import models


class Customer(models.Model):
    # Have to register models in the admin.py file as well
    name = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # in admin, if we don't declare this we just get a Customer object
        return self.name


class Product(models.Model):
    """
    Product item many-to-many
    """

    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    """

    """

    STATUS = (
        ("Pending", "Pending"),
        ("Out for delivery", "Out for deliver"),
        ("Delivered", "Delivered"),
    )
    # customer
    # product
    status = models.CharField(max_length=255, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
