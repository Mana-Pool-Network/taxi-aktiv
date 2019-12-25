from django import forms
from phonenumber_field.formfields import PhoneNumberField


class VacancyForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    tel = PhoneNumberField()
    birth_date = forms.DateField()
    sex = forms.CharField(max_length=10)
    experience = forms.CharField()
    driver_license_id = forms.CharField()
    passenger_transport_license = forms.CharField()
    additional_qualification = forms.CharField()
    contact_info = forms.CharField()
    comment = forms.CharField()
    resume = forms.FileField()


class ContactForm(forms.Form):
    title = forms.CharField()
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
