from django.db import models
from django.urls import reverse 
from django.utils import timezone 
from django.contrib.auth.models import User 
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='post_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    user_post = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     imgs = Image.open(self.img.path)

    #     if imgs.height > 300 or imgs.width > 300:
    #         output_size = (300, 300)
    #         imgs.thumbnail(output_size)
    #         imgs.save(self.img.path)



