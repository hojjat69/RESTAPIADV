from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creation a new user with an email is successful"""
        email ="hoj.borhany@gmail.com"
        password="1234"
        user =get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):


        """Test whether the email for new user is normalized"""

        email = "Test@yahoo.com"
        user = get_user_model().objects.create_user(email,"test")
        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"test")

    def test_create_new_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@yahoo.com", "1234"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)