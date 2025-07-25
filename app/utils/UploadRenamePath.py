import os
from datetime import datetime
from django.conf import settings
import uuid

from supabase import create_client

supabase = create_client(settings.SUPABASE_URL,settings.SUPABASE_KEY)

def user_ava_upload_path(instance,filename):
    base,ext = os.path.splitext(filename)
    uploadedTime = datetime.now().strftime('%Y_%m_%d')
    unique_id = uuid.uuid4()
    username = instance.id_user.username
    full_format_name = f'avatars/{unique_id}_{username}_{uploadedTime}{ext}'
    return full_format_name


def upload_media_to_supabase(file_obj, supabase_path):
    try:
        response = supabase.storage.from_(settings.SUPABASE_BUCKET).upload(supabase_path, file_obj)
        return print("Succes :",response)
    except Exception as e:
        print("Upload Failed, Caused : ",e)
        return None
    

