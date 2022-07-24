from rest_framework import serializers
from .models import VacDrive

class VacDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacDrive
        fields = ['date', 'numDosesC', 'numDosesCS', 'status']

