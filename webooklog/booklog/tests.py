from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class BookViewTests(TestCase):
    def test_index_view_with_books(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('booklog:index'))
        self.assertEqual(response.status_code, 200)
        print response
        '''
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        '''

