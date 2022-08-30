from django.db import models

# Create your models here.
type_choice = (
    ('kindergarten', "Bog'cha"),
    ('school', "Maktab"),
)


class Document(models.Model):
    title = models.CharField(max_length=128)
    cover_photo = models.ImageField(upload_to='document/cover/')
    file = models.FileField(upload_to='document/file/')
    type = models.CharField(max_length=32, choices=type_choice)
    content = models.TextField()

    def __str__(self):
        return self.title
