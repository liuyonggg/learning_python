from django.test import TestCase
from django.core.urlresolvers import reverse
from booklog.models import *
from django.utils.timezone import utc
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.models import Permission, Group
from django.contrib.auth import get_permission_codename
from django.http import HttpRequest, HttpResponse

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
        self.assertEqual(response.status_code, 302)

    def test_add_view(self):
        response = self.client.get(reverse('booklog:add'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "add")

    def test_login_view_succ(self):
        user = 'john'
        password = 'johnpassword'
        u1 = AuthUser.objects.create_user(user, 'john@example.com', password)
        u1.save()
        response = self.client.post('/login/', {'username': user, 'password': password, 'next':'/dummynextpage/'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/dummynextpage/', target_status_code=404)

    def test_login_view_fail(self):
        user = 'john'
        password = 'johnpassword'
        u1 = AuthUser.objects.create_user(user, 'john@example.com', password)
        u1.save()
        response = self.client.post('/login/', {'username': user, 'password': password+"123", 'next':'/dummynextpage/'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Your username and/or password were incorrect')


    def test_logout_view_succ(self):
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_password_change_succ(self):
        user = 'john'
        password = 'johnpassword'
        u1 = AuthUser.objects.create_user(user, 'john@example.com', password)
        u1.save()
        self.client.post('/login/', {'username':user, 'password':password})
        response = self.client.post('/password_change/', {'oldpassword':password, 'newpassword':password + '1', 'newpassword2':password + '1'})
        self.assertRedirects(response, '/password_change_done/')

    def test_password_change_wrong_old_password(self):
        user = 'john'
        password = 'johnpassword'
        u1 = AuthUser.objects.create_user(user, 'john@example.com', password)
        u1.save()
        self.client.post('/login/', {'username':user, 'password':password})
        response = self.client.post('/password_change/', {'oldpassword':password+'123', 'newpassword':password + '1', 'newpassword2':password + '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'old password is not correct')

    def test_password_change_wrong_diff_new_password(self):
        user = 'john'
        password = 'johnpassword'
        u1 = AuthUser.objects.create_user(user, 'john@example.com', password)
        u1.save()
        self.client.post('/login/', {'username':user, 'password':password})
        response = self.client.post('/password_change/', {'oldpassword':password, 'newpassword':password + '123', 'newpassword2':password + '1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'new password is not same as new password confirmation')

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

def get_perm(Model, perm):
    """Return the permission object, for the Model"""
    ct = ContentType.objects.get_for_model(Model)
    return Permission.objects.get(content_type=ct, codename=perm)

class UserTests(TestCase):
    def setUp(self):
        u1 = AuthUser.objects.create_user('john', 'john@example.com', 'johnpassword')
        u1.save()


        add_perm = get_perm(Book, get_permission_codename('add', Book._meta))
        change_perm = get_perm(Book, get_permission_codename('change', Book._meta))
        delete_perm = get_perm(Book, get_permission_codename('delete', Book._meta))

        username = 'adduser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.user_permissions.add(add_perm)
        u1.save()

        username = 'changeuser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.user_permissions.add(change_perm)
        u1.save()


        username = 'deleteuser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.user_permissions.add(delete_perm)
        u1.save()

        add_group = Group.objects.create(name="add_group")
        add_group.permissions.add(add_perm)
        
        change_group = Group.objects.create(name="change_group")
        change_group.permissions.add(add_perm, change_perm)

        delete_group = Group.objects.create(name="delete_group")
        delete_group.permissions.add(add_perm, change_perm, delete_perm)

        username = 'addgroupuser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.groups.add(add_group)
        u1.save()

        username = 'changegroupuser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.groups.add(change_group)
        u1.save()

        username = 'deletegroupuser'
        u1 = AuthUser.objects.create_user(username, username + '@example.com', username + 'password')
        u1.groups.add(delete_group)
        u1.save()


    def test_user(self):
        u1 = authenticate(username='john', password='johnpassword')
        self.assertIsNotNone(u1)
        u1 = authenticate(username='john', password='wrongpassword')
        self.assertIsNone(u1)
        u1 = authenticate(username='wronguser', password='johnpassword')
        self.assertIsNone(u1)

    def test_perm(self):
        u1 = authenticate(username='john', password='johnpassword')
        self.assertIsNotNone(u1)
        self.assertFalse(u1.has_perm('booklog.add_book'))
        self.assertFalse(u1.has_perm('booklog.change_book'))
        self.assertFalse(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='adduser', password='adduserpassword')
        self.assertIsNotNone(u1)
        self.assertTrue(u1.has_perm('booklog.add_book'))
        self.assertFalse(u1.has_perm('booklog.change_book'))
        self.assertFalse(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='changeuser', password='changeuserpassword')
        self.assertIsNotNone(u1)
        self.assertFalse(u1.has_perm('booklog.add_book'))
        self.assertTrue(u1.has_perm('booklog.change_book'))
        self.assertFalse(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='deleteuser', password='deleteuserpassword')
        self.assertIsNotNone(u1)
        self.assertFalse(u1.has_perm('booklog.add_book'))
        self.assertFalse(u1.has_perm('booklog.change_book'))
        self.assertTrue(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='addgroupuser', password='addgroupuserpassword')
        self.assertIsNotNone(u1)
        self.assertTrue(u1.has_perm('booklog.add_book'))
        self.assertFalse(u1.has_perm('booklog.change_book'))
        self.assertFalse(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='changegroupuser', password='changegroupuserpassword')
        self.assertIsNotNone(u1)
        self.assertTrue(u1.has_perm('booklog.add_book'))
        self.assertTrue(u1.has_perm('booklog.change_book'))
        self.assertFalse(u1.has_perm('booklog.delete_book'))

        u1 = authenticate(username='deletegroupuser', password='deletegroupuserpassword')
        self.assertIsNotNone(u1)
        self.assertTrue(u1.has_perm('booklog.add_book'))
        self.assertTrue(u1.has_perm('booklog.change_book'))
        self.assertTrue(u1.has_perm('booklog.delete_book'))

    def test_session_perm(self):
        res = self.client.login(username='changegroupuser', password='changegroupuserpassword')
        self.assertTrue(res)
        pk=3
        response = self.client.get(reverse('booklog:delete', args=(pk,)))
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        res = self.client.login(username='deletegroupuser', password='deletegroupuserpassword')
        self.assertTrue(res)
        pk=3
        response = self.client.get(reverse('booklog:delete', args=(pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "delete %d" % pk)
        self.client.logout()


        res = self.client.login(username='changegroupuser', password='wrongpassword')
        self.assertFalse(res)

        res = self.client.login(username='wronguser', password='changegroupuserpassword')
        self.assertFalse(res)


'''
<Item> 
  <ASIN>B004HO6I4M</ASIN> 
  <SmallImage> 
    <URL> 
      http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL75_.jpg 
    </URL> 
    <Height Units="pixels">75</Height> 
    <Width Units="pixels">56</Width> 
  </SmallImage> 
  <MediumImage> 
    <URL> 
      http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL160_.jpg 
    </URL> 
    <Height Units="pixels">160</Height> 
    <Width Units="pixels">120</Width> 
  </MediumImage> 
  <LargeImage> 
    <URL> 
      http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL500_.jpg 
    </URL> 
    <Height Units="pixels">500</Height> 
    <Width Units="pixels">375</Width> 
  </LargeImage> 
  <ImageSets> 
    <ImageSet Category="primary"> 
      <SwatchImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL30_.jpg 
        </URL> 
        <Height Units="pixels">30</Height> 
        <Width Units="pixels">22</Width> 
      </SwatchImage> 
      <SmallImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL75_.jpg 
        </URL> 
        <Height Units="pixels">75</Height> 
        <Width Units="pixels">56</Width> 
      </SmallImage> 
      <ThumbnailImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL75_.jpg 
        </URL> 
        <Height Units="pixels">75</Height> 
        <Width Units="pixels">56</Width> 
      </ThumbnailImage> 
      <TinyImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL110_.jpg 
        </URL> 
        <Height Units="pixels">110</Height> 
        <Width Units="pixels">82</Width> 
      </TinyImage> 
      <MediumImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL160_.jpg 
        </URL> 
        <Height Units="pixels">160</Height> 
        <Width Units="pixels">120</Width> 
      </MediumImage> 
      <LargeImage> 
        <URL>  
          http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL500_.jpg 
        </URL> 
        <Height Units="pixels">500</Height> 
        <Width Units="pixels">375</Width> 
      </LargeImage> 
    </ImageSet> 
  </ImageSets>
</Item>
http://docs.aws.amazon.com/AWSECommerceService/latest/DG/ItemSearch.html
http://docs.aws.amazon.com/AWSECommerceService/latest/DG/prod-adv-api-dg.pdf
http://docs.aws.amazon.com/AWSECommerceService/latest/DG/EX_RetrievingImages.html
'''
