from django.db import models

class Sequence(models.Model):
    current = models.IntegerField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.current}'

    def get_incerement(self):
        return f'{self.current + 1}'
    