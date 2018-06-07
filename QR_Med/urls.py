"""QR_Med URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, ListView
from QR_Med.models import *
from QR_Med.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('doctors_list', ListView.as_view(model=Doctor, template_name='doctors_list.html'), name='doctors_list'),
    path('doctors_qr/<int:doctor_id>', GenerateDoctorQRView.as_view(), name='doctors_qr'),
    path('positive_feedback/<int:doctor_id>', PositiveFeedbackView.as_view(), name='positive_feedback'),
    path('negative_feedback/<int:doctor_id>', NegativeFeedbackView.as_view(), name='negative_feedback'),
    path('admin/', admin.site.urls),
]
