from .models import VacDrive
from .serializers import VacDriveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse, HttpResponse
import datetime, pika

# Create your views here.
class DrivesList(APIView):

    def get(self, request):
        drives = VacDrive.objects.all()
        open = request.query_params.get('open', None)
        if open:
            drives = drives.filter(date__gte=datetime.date.today())
        serializer = VacDriveSerializer(drives, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacDriveSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()

            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('user', 'password')))
            channel = connection.channel()
            channel.basic_publish(exchange='vmss_ex', routing_key='test', body=f'New Vaccination Drive request received: {request.data}')
            connection.close()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DriveDetail(APIView):

    def get_object(self, pk):
        try:
            return VacDrive.objects.get(pk=pk)
        except VacDrive.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        drive = self.get_object(pk)
        serializer = VacDriveSerializer(drive)
        return Response(serializer.data)

    def put(self, request, pk):
        drive = self.get_object(pk)
        serializer = VacDriveSerializer(drive, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        drive = self.get_object(pk)
        drive.delete()
        return Response(status=status.HTTP_200_OK)



