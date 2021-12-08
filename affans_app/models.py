from django.db import models

# Create your models here.

#ideally this is how the files are stored[model names]
class FileName(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "file_names"