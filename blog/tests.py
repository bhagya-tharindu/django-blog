from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.user
        )

    # 🟢 Test login required redirect
    def test_home_redirect_if_not_logged_in(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    # 🟢 Test login success
    def test_login(self):
        login = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login)

    # 🟢 Test homepage loads after login
    def test_home_page_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    # 🟢 Test create post page
    def test_create_post(self):
        self.client.login(username='testuser', password='testpass123')

        response = self.client.post('/create/', {
            'title': 'New Post',
            'content': 'New Content'
        })

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())