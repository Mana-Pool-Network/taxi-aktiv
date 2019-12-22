from django.urls import path, include

from . import views

urlpatterns = [
    path('vacancy/', views.VacancyView.as_view()),
    path('contact/', views.ContactView.as_view()),
    # re_path('.*', TemplateView.as_view(template_name='index.html'), name="app"),
]
