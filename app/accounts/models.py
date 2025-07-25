from django.db import models
from django.contrib.auth.models import User 
from utils import user_ava_upload_path, upload_media_to_supabase

# Create your models here.
class UserAva(models.Model):
    id_user =  models.ForeignKey(User,models.CASCADE)
    ava = models.ImageField()
    updated_at = models.DateField(null=True)

    def save(self,*args, **kwargs):
        file_path_in_supabase = user_ava_upload_path(self,self.ava.name)

        if self.ava:
            file_data = self.ava.read()
            print(f'change ori name {self.ava.name} to the {file_path_in_supabase}')
            upload_media_to_supabase(file_data ,file_path_in_supabase)
            self.ava.name = file_path_in_supabase

        super().save(self,*args, **kwargs)

