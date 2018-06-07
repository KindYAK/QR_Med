from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Hospital(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(User):
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return "Доктор {} {} из {}".format(self.first_name, self.last_name, self.hospital)


class Feedback(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.CharField(max_length=333, null=True, blank=True)

    def __str__(self):
        return "{} баллов - {}".format(self.score, self.doctor)
