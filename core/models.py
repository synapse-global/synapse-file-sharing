from django.db import models

class Files(models.Model):
    file = models.FileField(verbose_name="Файл", upload_to="files/")
    key = models.CharField(max_length=255, default="", verbose_name="Ключ", unique=True)
    name = models.CharField(max_length=1025, verbose_name="Наименование")

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f"{self.key}"