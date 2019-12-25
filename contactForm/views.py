from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage

from .forms import ContactForm


class VacancyView(APIView):
    def post(self, request):
        data = ContactForm(request.data)
        if data.is_valid():
            return Response(request.data)
        else:
            return Response(data.errors)


class ContactView(APIView):
    def post(self, request):
        data = ContactForm(request.data)
        if data.is_valid():
            return Response(request.data)
        else:
            return Response(data.errors)


def email(subject, from_email, to, html_content):
    # subject, from_email, to = 'hello', 'from@example.com', 'to@example.com'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.send()
