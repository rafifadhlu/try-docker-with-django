
from supabase import create_client
from django.conf import settings

supabase = create_client(settings.SUPABASE_URL,settings.SUPABASE_KEY)

def get_avatar_url(file_path: str,bucket_name: str):
    return supabase.storage.from_(bucket_name).get_public_url(file_path)
