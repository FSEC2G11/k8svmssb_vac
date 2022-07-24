from django.db import models

# Create your models here.

# Enumerations
class VacDriveStatus(models.IntegerChoices):
    PENDING = 0
    APPROVED = 1
    COMPLETED = 2

class VacName(models.IntegerChoices):
    NONE = 0
    COVAXIN = 1
    COVISHIELD = 2


class VacDrive(models.Model):
    date = models.DateField(primary_key=True)
    numDosesC = models.IntegerField(default=0)
    numDosesCS = models.IntegerField(default=0)
    status = models.IntegerField(choices=VacDriveStatus.choices, default=0)

    def __str__(self):
        return str(self.date)


