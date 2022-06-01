from django.db import models


class LabelState(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Label(models.Model):
    number = models.PositiveSmallIntegerField("Номер", default=0, unique=True)
    state = models.ForeignKey(LabelState, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)
