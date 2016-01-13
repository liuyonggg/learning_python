from django.test import TestCase
from django.core.urlresolvers import reverse
from booklog.models import *
from django.utils.timezone import utc
import datetime

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

class BookModelTests(TestCase):
    def setUp(self):
        u1 = User.objects.create(first_name="fn1", last_name="ln1", email="fn1_ln1@example.com")
        u1.save()
        a1 = Author.objects.create(first_name="fn2", last_name="ln2", email="fn2_ln2@example.com")
        a1.save()
        b1 = Book.objects.create(name="b1", pub_date=datetime.datetime(2016, 01, 12, 8, 55, tzinfo=utc))
        b1.authors.add(a1)
        b1.save()
        r1 = Review.objects.create(user=u1, book=b1, date=datetime.datetime(2016, 01, 12, 8, 55, tzinfo=utc), score=5, comment="good book")
        r1.save()

    def test_user(self):
        user = User.objects.get(email="fn1_ln1@example.com")
        self.assertEqual(str(user), 'fn1_ln1@example.com')

    def test_author(self):
        author = Author.objects.get(email='fn2_ln2@example.com')
        self.assertEqual(str(author), 'fn2_ln2@example.com')

    def test_book(self):
        book = Book.objects.get(name='b1')
        self.assertEqual(str(book), 'b1')

    def test_review(self):
        b1 = Book.objects.get(name='b1')
        r1 = Review.objects.get(book=b1)
        u1 = User.objects.get(email='fn1_ln1@example.com')
        self.assertEqual(str(r1), '5')
        self.assertEqual(r1.user, u1)
