from django.db import models

class Files(models.Model):
    file = models.FileField(verbose_name="File", upload_to="files/")
    key = models.CharField(max_length=255, default="", verbose_name="Key", unique=True)
    name = models.CharField(max_length=1025, verbose_name="Name")

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return f"{self.key}"