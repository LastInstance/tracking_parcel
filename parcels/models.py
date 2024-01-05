from django.db import models

class Address(models.Model):
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address


class Parcel(models.Model):
    sender_name = models.CharField(max_length=100)
    recipient_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending')



class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email
