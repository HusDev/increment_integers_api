from django.db import models

class Sequence(models.Model):
    value = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.value}'

    def get_incerement(self):
        return f'{self.value + 1}'
    