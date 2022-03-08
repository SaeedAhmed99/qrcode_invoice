from django.db import models
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class image(models.Model):
    photo = models.ImageField(upload_to='photos')


class Website(models.Model):
    value = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='photos', blank=True)

    # def __str__(self):
    #     return str(self.name)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.value)
        canvas = Image.new('RGB', (500, 500), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-01.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)