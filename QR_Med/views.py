from django.views.generic import TemplateView, View
from django.http import HttpResponse
from QR_Med.models import *
from QR_Med.service import *
import qrcode


class GenerateDoctorQRView(TemplateView):
    template_name = "doctor_qr.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        qr = qrcode.QRCode(
            version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_M   ,
            box_size=10,
            border=4,
        )
        qr.add_data(self.request.META['HTTP_HOST'] + "/positive_feedback/" + str(kwargs['doctor_id']))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        context['qr_positive'] = convert_to_base64(img)

        qr = qrcode.QRCode(
            version=6,
            error_correction=qrcode.constants.ERROR_CORRECT_M   ,
            box_size=10,
            border=4,
        )
        qr.add_data(self.request.META['HTTP_HOST'] + "/negative_feedback/" + str(kwargs['doctor_id']))
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        context['qr_negative'] = convert_to_base64(img)

        context['doctor'] = Doctor.objects.get(id=kwargs['doctor_id'])
        return context


class PositiveFeedbackView(View):
    def get(self, request, *args, **kwargs):
        Feedback.objects.create(score=5, doctor=Doctor.objects.get(id=self.kwargs['doctor_id']))
        return HttpResponse("Ваш отзыв успешно сохранён")


class NegativeFeedbackView(View):
    def get(self, request, *args, **kwargs):
        Feedback.objects.create(score=0, doctor=Doctor.objects.get(id=self.kwargs['doctor_id']))
        return HttpResponse("Ваш отзыв успешно сохранён")

