from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class User(AbstractUser):
    profile = models.ImageField(upload_to='profile')
    profile_image = ProcessedImageField(
        processors=[ResizeToFill(50, 50)],
        format='JPEG',  # JPEG로 포맷 설정
        options={'quality': 60},
        upload_to='profile_image',
    )

    # post_set (FK)
    # comment_set
    # post_set => like_postes (MMF)

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # related_name='followers'하는 순간 `follwers = `가 생김