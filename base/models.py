from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # dar asl ye ertebat 1:n taeen kardim ke miyad chand ta chiz to be yek user nesbat mide
    # cascade dar asl be ma mige ke age user pak shod data hasham pak misham
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # baees mishe be jay namayesh esm object az esm yeki az row hash estefade beshe ke aghlab hamon title


class Meta:
    ordering = ['complete']
    # mige tartib ro bar asas complete shode ha bechin
