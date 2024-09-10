import os

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase

from app.models import Profile


class ProfileTestCase(TestCase):

    def setUp(self):
        self._create_test_user()
        self._create_test_image()
        self.client = Client()

    def tearDown(self):
        os.remove(self.profile_pic_path)

    def _create_test_user(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def _create_test_image(self):
        self.profile_pic_path = "./my_profile_pic.png"
        self.profile_pic = Image.new('RGBA', size=(50, 50), color=(256, 0, 0))
        self.profile_pic.save(self.profile_pic_path)

    def test_profile_creation(self):
        Profile.objects.create(user=self.user, address="test address", profile_pic=self.profile_pic_path)
        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(Profile.objects.get(user=self.user).address, "test address")

    def test_profile_pic(self):
        with open(self.profile_pic_path, 'rb') as img:
            file_obj = SimpleUploadedFile('my_profile_pic.png', img.read(), content_type='image/png')
            profile = Profile.objects.create(user=self.user, address="test address", profile_pic=file_obj)
            profile.save()
        self.assertIsNotNone(profile.profile_pic.path)
        self.assertTrue(os.path.exists(profile.profile_pic.path))

    def test_profile_deletion(self):
        profile = Profile.objects.create(user=self.user, address="test address", profile_pic=self.profile_pic_path)
        user_id = profile.user.id
        profile.user.delete()
        self.assertFalse(Profile.objects.filter(user_id=user_id).exists())
