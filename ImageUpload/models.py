import os.path

from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    img_file = models.ImageField(upload_to='')
    created_at = models.DateTimeField(auto_now_add=True)
    to_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.img_file:
            if os.path.exists(self.img_file.path):
                os.remove(self.img_file.path)
        super().delete(*args, **kwargs)
