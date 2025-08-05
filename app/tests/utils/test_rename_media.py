from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import UserAva
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest.mock import patch



class RenameMediaPathTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.img = SimpleUploadedFile("testimg.jpg", b"dummycontent", content_type="image/jpeg")


    def test_rename_media_path(self):
        from utils.UploadRenamePath import user_ava_upload_path
        # logged_user = self.client.login(username='testuser', password='testpass')
        ava_instance = UserAva.objects.create(id_user=self.user, ava=self.img)
        
        if ava_instance:
            test_method = user_ava_upload_path(ava_instance, self.img.name)
            split_name = test_method.split('_')
            self.assertEqual(split_name[1], self.user.username)

    @patch('accounts.models.upload_media_to_supabase')
    def test_upload_media_to_supabase(self,mock_upload):
        mock_upload.return_value = "Mocked upload success"
        ava_instance = UserAva.objects.create(id_user=self.user, ava=self.img)
        
        mock_upload.assert_called_once()

        split_name = ava_instance.ava.name.split('_')
        
        self.assertEqual(split_name[1], self.user.username)
        


