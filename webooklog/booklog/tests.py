from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class BookViewTests(TestCase):
    def test_index_view_with_books(self):
        response = self.client.get(reverse('booklog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "index")

    def test_detail_view(self):
        pk = 3
        response = self.client.get(reverse('booklog:detail', args=(pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "detail %d" % pk)


    def test_delete_view(self):
        pk = 3
        response = self.client.get(reverse('booklog:delete', args=(pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "delete %d" % pk)

    def test_add_view(self):
        response = self.client.get(reverse('booklog:add'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "add")


