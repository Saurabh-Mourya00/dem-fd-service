from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     img=Image.open(self.image.path)
       

    #     if img.height>300 or img.width>300:
    #         output_size=(300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Remove default local file; allow blank/NULL
#     image = models.ImageField(
#         upload_to='profile_pics/',  # Folder inside Supabase bucket
#         blank=True,
#         null=True
#     )

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     @property
#     def image_url(self):
#         """
#         Returns the uploaded image URL if exists; otherwise, return the Supabase default.
#         """
#         if self.image and hasattr(self.image, 'url'):
#             return self.image.url
#         # Build default public object URL from settings to avoid hard-coded bucket or project
#         supabase_url = getattr(settings, 'MEDIA_URL', '').rstrip('/')
#         bucket_name = getattr(settings, 'AWS_STORAGE_BUCKET_NAME', 'profile-images')
#         # MEDIA_URL is configured to the public object base in settings when using Supabase
#         # e.g. https://<project>.supabase.co/storage/v1/object/public/
#         if supabase_url:
#             return f"{supabase_url}/{bucket_name}/default.jpg"
#         # Fallback: construct from SUPABASE_URL if MEDIA_URL isn't set
#         base_url = getattr(settings, 'SUPABASE_URL', '').rstrip('/')
#         if base_url:
#             return f"{base_url}/storage/v1/object/public/{bucket_name}/default.jpg"
#         # Last resort: local placeholder path
#         return "/static/image/sitelogo.png"


     

# AWS S3 settings
