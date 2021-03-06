from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    #this will run before all functions
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
        email = 'admin@gmail.com',
        password = 'password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
        email = 'user@gmail.com',
        password = 'password123',
        name = 'Test user Full name'
        )

    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)
        #assertion here checks whether the response contains certain items and looks into the res for content

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        #status code :200 is for OK
        #/admin/core/user/1 format of  the URL

    def test_create_user_page(self):
        """Testing that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
