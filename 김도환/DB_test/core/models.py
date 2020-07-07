from django.db import models

# Create your models here.
class TempDate(models.Model):
    created = models.DateField(auto_now_add=True, null=True)
    updated = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = "core"
        abstract = True
