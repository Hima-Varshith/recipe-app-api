from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email = 'hima29@gmail.com', password = 'testpass'):
    """create a sample user"""
    return get_user_model().objects.create_user(email,password)

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

    def test_tag_str(self):
        """Test tag string representation"""
        tag=models.Tag.objects.create(
        user=sample_user(),
        name='Vegan'
        )
        self.assertEqual(str(tag),tag.name)

    def test_ingredient_str(self):
        """Test ingredient string representation"""
        ingredient=models.Ingredient.objects.create(
        user=sample_user(),
        name='Cucumber'
        )
        self.assertEqual(str(ingredient),ingredient.name)

    def test_recipe_str(self):
        """Test the recioe string representation"""
        recipe=models.Recipe.objects.create(
        user=sample_user(),
        title='Palak Paneer',
        time_minutes=20,
        price=180.0
        )
        self.assertEqual(str(recipe),recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'myimage.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
