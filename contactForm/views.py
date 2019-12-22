from rest_framework.response import Response
from rest_framework.views import APIView


class VacancyView(APIView):
    def post(self, request):
        name = request.data['name']
        email = request.data['email']
        tel = request.data['tel']
        birth_date = request.data['birth_date']
        sex = request.data['sex']
        experience = request.data['experience']
        driver_license = request.data['driver_license']
        passenger_transport_license = request.data['passenger_transport_license']
        additional_qualification = request.data['additional_qualification']
        contact_info = request.data['contact_info']
        comment = request.data['comment']
        resume = request.data['resume']
        return Response({'success': 1})


class ContactView(APIView):
    def post(self, request):
        title = request.data['title']
        name = request.data['name']
        email = request.data['email']
        message = request.data['message']
        return Response[{'success': 1}]
