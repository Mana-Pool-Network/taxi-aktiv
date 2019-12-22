from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage


class VacancyView(APIView):
    def post(self, request):
        try:
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
        except KeyError:
            return Response({'error': 'is not specified'})
        return Response({'success': 1})


class ContactView(APIView):
    def post(self, request):
        try:
            title = request.data['title']
            name = request.data['name']
            email = request.data['email']
            message = request.data['message']
        except KeyError:
            return Response({'error': 'is not specified'})
        return Response({'success': 1})


def email(subject, from_email, to, html_content):
    # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.send()
