from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ResourceManger(models.Model):

    class ManagerTypes(models.TextChoices):

        Seller = 'Seller', 'Seller'
        PHARMACIST = 'pharmacist', 'Pharmacist'

    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField()
    email = models.EmailField(max_length=254)
    resource_type = models.CharField(
        max_length=50,
        choices=ManagerTypes.choices,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("resourcemanger_detail", kwargs={"pk": self.pk})


class Resource(models.Model):

    class ResourceTypes(models.TextChoices):

        PHARMACY = 'PHARMACY', 'Pharmacy'
        STORE = 'STORE', 'Store'
        MARKET = 'MARKET', 'Market'

    class ResourceStatus(models.TextChoices):

        OPEN = 'OPEN', 'Open'
        CLOSED = 'CLOSED', 'Closed'
        UNKNOWN = 'UNKNOWN', 'Unknown'

    name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(verbose_name="phone number")
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=254)
    state = models.CharField(max_length=100)
    lga = models.CharField(max_length=100)

    resource_type = models.CharField(
        max_length=15,
        choices=ResourceTypes.choices,
        default=ResourceTypes.STORE,
    )

    resource_status = models.CharField(
        max_length=15,
        choices=ResourceStatus.choices,
        default=ResourceStatus.UNKNOWN
    )

    resource_manager = models.ForeignKey(
        ResourceManger, on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Resource Center"
        verbose_name_plural = "Resource Centers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basemodel_detail", kwargs={"pk": self.pk})
