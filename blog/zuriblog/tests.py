from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post


class BlogPostTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin',
            email='admin@gmail.com',
            password='admin'
        )

        self.post = Post.objects.create(
            title='My test Post',
            author=self.user,
            body='This is a test post!'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.post), self.post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "My test Post")
        self.assertEqual(f"{self.post.author}", "admin")
        self.assertEqual(f"{self.post.body}", 'This is a test post!')

    def test_post_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'zuriblog/index.html')

    def test_post_detail_view(self):
        response = self.client.get(reverse('detail', args=(1,)))
        no_response = self.client.get(reverse('detail', args=(5,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'This is a test post!')
        self.assertTemplateUsed(response, 'zuriblog/detail.html')
