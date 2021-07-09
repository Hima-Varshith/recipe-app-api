from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_withsuccessemail(self):
        """Test creating a new user with email is succcessful"""
        email = 'test@londonappdev.com'
        password = 'hima2908'
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

#docker-compose run app sh -c "python manage.py test"

    def test_create_user_normalised(self):
       """Test the email for new user is normalised """
       email = 'test@LONDONAPPDEV.COM'
       user = get_user_model().objects.create_user(email,'hima2908')
       self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'hima2908')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
        'test@londonappdev.com','hima2908'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
