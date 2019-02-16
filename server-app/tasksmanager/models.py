from django.db import models

STATUSES = (
    ('created', 'creada'),
    ('revised', 'revisada'),
    ('marked', 'marcada'),
    ('deleted', 'deleted'),
)

class Task(models.Model):
    title = models.CharField(max_length=128)
    status = models.CharField(max_length=32, choices=STATUSES, default=STATUSES[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
