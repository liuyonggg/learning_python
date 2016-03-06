from django.test import TestCase
from reader.models import *
from reader.models import Book
from django.db import models
from django.utils import timezone
import datetime

class OldModelTests(TestCase):                                                                      
    def test_book(self):                                                                            
        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b1.save()

        self.assertEqual(b1.name, 'b1')
        self.assertEqual(b1.isbn, 'RENNOC-IS-HERE')
        self.assertEqual(b1.authors, 'Bob')
        self.assertEqual(str(b1.pub_date), '2016-01-01')

    def test_user_sort_friend(self):                                                                
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('tom', 'tom@example.com', 'tompassword')
        u3 = User.objects.create_user('peter', 'peter@example.com', 'peterpassword')
        u4 = User.objects.create_user('sean', 'sean@example.com', 'seanpassword')

        fs1 = FriendShip.objects.create(from_user=u2, to_user=u1, date=datetime.date(2016, 1, 31), status=FRIEND_STATUS[0][0])
        fs2 = FriendShip.objects.create(from_user=u3, to_user=u1, date=datetime.date(2016, 1, 29), status=FRIEND_STATUS[1][0])
        fs3 = FriendShip.objects.create(from_user=u4, to_user=u1, date=datetime.date(2016, 2, 1), status=FRIEND_STATUS[2][0])

        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 2, 1))

        comment = 'abcdefghijklmnopqrstuvwxyznowinomyABCnexttimewillusinwithme'
        today = timezone.now().date()

        recommendation = Recommendation.objects.create(book=b1, comment=comment, date=today, from_user=u2)
        recommendation2 = Recommendation.objects.create(book=b2, comment=comment, date=today, from_user=u4)

        recommendship = RecommendShip.objects.create(recommendation=recommendation, to_user=u1)
        recommendship1 = RecommendShip.objects.create(recommendation=recommendation2, to_user=u1)
        recommendship2 = RecommendShip.objects.create(recommendation=recommendation2, to_user=u1)

        recommendship3 = RecommendShip.objects.filter(recommendation=recommendation2, to_user=u1)

        self.assertEqual(fs1.status, 1)
        self.assertEqual(fs2.status, 2)
        self.assertEqual(fs3.status, 3)

        self.assertEqual(fs1.get_status_display(), 'Created')
        self.assertEqual(fs2.get_status_display(), 'Sent')
        self.assertEqual(fs3.get_status_display(), 'Failed')

        self.assertEqual(recommendation.book, b1)
        self.assertEqual(recommendation.comment, comment)
        self.assertEqual(recommendation.date, today)
        self.assertEqual(recommendation2.book, b2)

    def test_to_user_books(self):                                                                   
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')

        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))

        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1), from_user=u1)
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2), from_user=u1)

        rs1 = RecommendShip(recommendation=r1, to_user=u2)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_user=u2)
        rs2.save()

        for rs in RecommendShip.objects.filter(to_user=u2):
            self.assertEqual(rs, rs1) if rs == rs1 else self.assertEqual(rs, rs2)
            self.assertEqual(rs.recommendation.book, r1.book) if rs == rs1 else self.assertEqual(rs.recommendation.book, r2.book)

    def test_from_user_books(self):                                                                 
        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u3 = User.objects.create_user('u3', 'u3@example.com', 'u3password')

        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))

        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1), from_user=u1)
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2), from_user=u1)

        rs1 = RecommendShip(recommendation=r1, to_user=u2)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_user=u2)
        rs2.save()
        rs3 = RecommendShip(recommendation=r1, to_user=u3)
        rs3.save()

        books = set()
        for rs in Recommendation.objects.filter(from_user=u1):
            books.add(rs.book)
        self.assertEqual(books, set([b1, b2]))

    def test_popular_books(self):                                                                   
        u1 = User.objects.create_user('u1', 'u1@example.com', 'u1password')
        u2 = User.objects.create_user('u2', 'u2@example.com', 'u2password')
        u3 = User.objects.create_user('u3', 'u3@example.com', 'u3password')

        b1 = Book.objects.create(name='b1', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))
        b2 = Book.objects.create(name='b2', isbn='RENNOC-IS-HERE', authors='Bob', pub_date=datetime.date(2016, 1, 1))

        r1 = Recommendation.objects.create(book=b1, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 1), from_user=u1)
        r2 = Recommendation.objects.create(book=b2, comment='abcdefghijklmnopqrstuvwxyz ', date=datetime.date(2016, 1, 2), from_user=u1)

        rs1 = RecommendShip(recommendation=r1, to_user=u2)
        rs1.save()
        rs2 = RecommendShip(recommendation=r2, to_user=u2)
        rs2.save()
        rs3 = RecommendShip(recommendation=r1, to_user=u3)
        rs3.save()
    
        books = sorted(Book.objects.all(), key=number_of_recommendation_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])

        books = sorted(Book.objects.all(), key=number_of_from_user_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])

        books = sorted(Book.objects.all(), key=number_of_to_user_for_a_book, reverse=True)
        self.assertEqual(books, [b1, b2])

class NewModelTests(TestCase):                                                                      
    def test_user(self):                                                                            
        u1 = User.objects.create_user(username='Bob', email='bob123@example.com', password='bobpassword')
        u1.username = 'Joe'
        u1.email = 'joe123@example.com'
        u1.password = 'joepassword'
        u1.save()

        user = User.objects.get(pk=1)
        self.assertEqual(user.username, 'Joe')
        self.assertEqual(user.email, 'joe123@example.com')
        self.assertEqual(user.password, 'joepassword')

        u2 = User.objects.create_user(username='Kevin', email='kevin123@example.com', password='kevinpassword')
        u3 = User.objects.create_user(username='Cindy', email='cindy123@example.com', password='cindypassword')
        u4 = User.objects.create_user(username='Barbara', email='barbara123@example.com', password='barbarapassword')

        user = User.objects.get(username='Kevin')
        self.assertEqual(user.email, 'kevin123@example.com')

    def test_book(self):
        b1 = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 17))
        b2 = Book.objects.create(name='The Example Textbook', isbn='the-example-textbook', authors='Examp leson', pub_date = datetime.date(2016, 2, 17))
        b3 = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 17))

        self.assertEqual(b1.name, 'The Example Handbook')
        self.assertEqual(b1.isbn, 'the-example-handbook')
        self.assertEqual(b1.authors, 'Ex Ample')
        self.assertEqual(str(b1.pub_date), '2016-02-17')

        self.assertEqual(b2.name, 'The Example Textbook')
        self.assertEqual(b2.isbn, 'the-example-textbook')
        self.assertEqual(b2.authors, 'Examp leson')
        self.assertEqual(str(b2.pub_date), '2016-02-17')

        self.assertEqual(b3.name, 'The Not-So-Example Handbook')
        self.assertEqual(b3.isbn, 'the-not--so--example-handbook')
        self.assertEqual(b3.authors, 'Ample Exson')
        self.assertEqual(str(b3.pub_date), '2016-02-17')

        b3.name = '**********'
        b3.save()
        self.assertEqual(Book.objects.get(name='**********').authors, 'Ample Exson')

        b3.delete()

        try:
            Book.objects.get(name='**********')
            b3_existence = True
        except:
            b3_existence = False

        self.assertFalse(b3_existence)

    def test_recommendation(self):                                                                  
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('tom', 'tom@example.com', 'tompassword')
        u3 = User.objects.create_user('peter', 'peter@example.com', 'peterpassword')

        b1 = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 17))
        b2 = Book.objects.create(name='The Example Textbook', isbn='the-example-textbook', authors='Examp leson', pub_date = datetime.date(2016, 2, 17))
        b3 = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 17))

        r1 = Recommendation.objects.create(book=b1, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Example Handbook for 2016!!!', from_user=u1)
        r2 = Recommendation.objects.create(book=b2, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Example Textbook for 2016!!!', from_user=u2)
        r3 = Recommendation.objects.create(book=b3, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Not-So-Example Handbook for 2016!!!', from_user=u3)

        r1 = Recommendation.objects.get(book=b3)
        r2 = Recommendation.objects.get(from_user=u2)
        r3 = Recommendation.objects.get(book=b1)

        self.assertEqual(r1.book, b3)
        self.assertEqual(r1.date, datetime.date(2016, 2, 18))
        self.assertEqual(r1.comment, 'Well, this is the offical comment for The Not-So-Example Handbook for 2016!!!')
        self.assertEqual(r1.from_user, u3)

        self.assertEqual(r2.book, b2)
        self.assertEqual(r2.date, datetime.date(2016, 2, 18))
        self.assertEqual(r2.comment, 'Well, this is the offical comment for The Example Textbook for 2016!!!')
        self.assertEqual(r2.from_user, u2)

        self.assertEqual(r3.book, b1)
        self.assertEqual(r3.date, datetime.date(2016, 2, 18))
        self.assertEqual(r3.comment, 'Well, this is the offical comment for The Example Handbook for 2016!!!')
        self.assertEqual(r3.from_user, u1)

        self.assertEqual(list(Recommendation.objects.filter(date=datetime.date(2016, 2, 18))), [r3, r2, r1])
    def test_recommendship(self):                                                                   
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('tom', 'tom@example.com', 'tompassword')
        u3 = User.objects.create_user('peter', 'peter@example.com', 'peterpassword')

        b1 = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 17))
        b2 = Book.objects.create(name='The Example Textbook', isbn='the-example-textbook', authors='Examp leson', pub_date = datetime.date(2016, 2, 17))
        b3 = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 17))

        r1 = Recommendation.objects.create(book=b1, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Example Handbook for 2016!!!', from_user=u1)
        r2 = Recommendation.objects.create(book=b2, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Example Textbook for 2016!!!', from_user=u2)
        r3 = Recommendation.objects.create(book=b3, date=datetime.date(2016, 2, 18), comment='Well, this is the offical comment for The Not-So-Example Handbook for 2016!!!', from_user=u3)

        rs1 = RecommendShip.objects.create(recommendation=r1, to_user=u2)
        rs2 = RecommendShip.objects.create(recommendation=r2, to_user=u3)
        rs3 = RecommendShip.objects.create(recommendation=r3, to_user=u1)

        rs1 = RecommendShip.objects.get(to_user=u1)
        rs2 = RecommendShip.objects.get(to_user=u3)
        rs3 = RecommendShip.objects.get(to_user=u2)

        self.assertEqual(rs1.recommendation, r3)
        self.assertEqual(rs1.to_user, u1)
        self.assertEqual(rs2.recommendation, r2)
        self.assertEqual(rs2.to_user, u3)
        self.assertEqual(rs1.recommendation, r3)
        self.assertEqual(rs1.to_user, u1)

    def FriendShip(self):                                                                           
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('tom', 'tom@example.com', 'tompassword')
        u3 = User.objects.create_user('peter', 'peter@example.com', 'peterpassword')

        fs1 = FriendShip.objects.create(from_user=u1, to_user=u2, date=datetime.date(2016, 2, 20), status=0)
        fs2 = FriendShip.objects.create(from_user=u1, to_user=u3, date=datetime.date(2016, 2, 20), status=1)
        fs3 = FriendShip.objects.create(from_user=u2, to_user=u3, date=datetime.date(2016, 2, 20), status=0)

        fs1 = FriendShip.objects.filter(status=1)
        fs2 = FriendShip.objects.filter(from_user=u2)
        fs3 = FriendShip.objects.filter(to_user=u2)

        fs1[0].status = 3
        fs2[0].status = 5
        fs3[0].status = 4

        fs1[0].save()
        fs2[0].save()
        fs3[0].save()

        self.assertEqual(fs1[0].from_user, u1)
        self.assertEqual(fs1[0].to_user, u2)
        self.assertEqual(fs1[0].date, datetime.date(2016, 2, 20))
        self.assertEqual(fs1[0].get_status_display, 'Failed')

        self.assertEqual(fs2[0].from_user, u2)
        self.assertEqual(fs2[0].to_user, u3)
        self.assertEqual(fs2[0].date, datetime.date(2016, 2, 20))
        self.assertEqual(fs2[0].get_status_display, 'Expired')

        self.assertEqual(fs3[0].from_user, u1)
        self.assertEqual(fs3[0].to_user, u3)
        self.assertEqual(fs3[0].date, datetime.date(2016, 2, 20))
        self.assertEqual(fs3[0].get_status_display, 'Accepted')

        fs1[0].delete()
        fs2[0].delete()
        fs3[0].delete()

        try:
            FriendShip.objects.get(status=3)
            fs1_existence = True
        except:
            fs1_existence = False

        try:
            FriendShip.objects.get(status=4)
            fs3_existence = True
        except:
            fs3_existence = False

        try:
            FriendShip.objects.get(status=5)
            fs2_existence = True
        except:
            fs2_existence = False

        self.assertFalse(fs1_existence)
        self.assertFalse(fs2_existence)
        self.assertFalse(fs3_existence)

    def test_read_book(self):                                                                       
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('tom', 'tom@example.com', 'tompassword')
        u3 = User.objects.create_user('peter', 'peter@example.com', 'peterpassword')
                                                                                                    
        b1 = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 17))
        b2 = Book.objects.create(name='The Example Textbook', isbn='the-example-textbook', authors='Examp leson', pub_date = datetime.date(2016, 2, 17))
        b3 = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 17))
                                                                                                    
        rb1 = ReadBook.objects.create(user=u1, book=b1, date=datetime.date(2016, 2, 21))
        rb2 = ReadBook.objects.create(user=u2, book=b2, date=datetime.date(2016, 2, 20))
        rb3 = ReadBook.objects.create(user=u3, book=b3, date=datetime.date(2016, 2, 21))
                                                                                                    
        date = datetime.date(2016, 2,20)
                                                                                                   
        rb3 = ReadBook.objects.get(user=u1)
        rb2 = ReadBook.objects.get(book=b3)
        rb1 = ReadBook.objects.filter(date=date)
                                                                                                    
        self.assertEqual(list(rb1)[0].user, u2)
        self.assertEqual(list(rb1)[0].book, b2)
        self.assertEqual(list(rb1)[0].date, datetime.date(2016, 2, 20))
                                                                                                    
        self.assertEqual(rb2.user, u3)
        self.assertEqual(rb2.book, b3)
        self.assertEqual(rb2.date, datetime.date(2016, 2, 21))
                                                                                                   
        self.assertEqual(rb3.user, u1)
        self.assertEqual(rb3.book, b1)
        self.assertEqual(rb3.date, datetime.date(2016, 2, 21))

class UseModelTest(TestCase):                                                                       
    def test_book_to_read_for_a_user(self):                                                         
        user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        user_friend = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')

        book = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 21))

        recommendation = Recommendation.objects.create(book=book, date=datetime.date(2016, 2, 21), comment='Well, this is the offical test comment for book to read function!!!', from_user=user_friend)

        recommendship = RecommendShip.objects.create(recommendation=recommendation, to_user=user)

        self.assertEqual(book, book_to_read_for_a_user(user))

    def test_book_finished_for_a_user(self):                                                        
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        u3 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        u4 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')

        b1 = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 21))
        b2 = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 21))

        rb1 = ReadBook.objects.create(user=u1, book=b1, date=datetime.date(2016, 2, 22))
        rb2 = ReadBook.objects.create(user=u1, book=b2, date=datetime.date(2016, 2, 22))

        rb3 = ReadBook.objects.create(user=u2, book=b1, date=datetime.date(2016, 2, 22))
        rb4 = ReadBook.objects.create(user=u2, book=b2, date=datetime.date(2016, 2, 22))

        rb5 = ReadBook.objects.create(user=u3, book=b1, date=datetime.date(2016, 2, 22))
        rb6 = ReadBook.objects.create(user=u3, book=b2, date=datetime.date(2016, 2, 22))

        rb7 = ReadBook.objects.create(user=u4, book=b1, date=datetime.date(2016, 2, 22))
        rb8 = ReadBook.objects.create(user=u4, book=b2, date=datetime.date(2016, 2, 22))

        date = datetime.date(2016, 2, 22)
        u1f = list(ReadBook.objects.filter(user=u1))
        u2f = list(ReadBook.objects.filter(user=u2))
        u3f = list(ReadBook.objects.filter(user=u3))
        u4f = list(ReadBook.objects.filter(user=u4))

        self.assertEqual(u1f[0].book, b1)
        self.assertEqual(u1f[0].date, date)
        self.assertEqual(u1f[1].book, b2)
        self.assertEqual(u1f[1].date, date)

        self.assertEqual(u2f[0].book, b1)
        self.assertEqual(u2f[0].date, date)
        self.assertEqual(u2f[1].book, b2)
        self.assertEqual(u2f[1].date, date)

        self.assertEqual(u3f[0].book, b1)
        self.assertEqual(u3f[0].date, date)
        self.assertEqual(u3f[1].book, b2)
        self.assertEqual(u3f[1].date, date)

        self.assertEqual(u4f[0].book, b1)
        self.assertEqual(u4f[0].date, date)
        self.assertEqual(u4f[1].book, b2)
        self.assertEqual(u4f[1].date, date)

    def test_friends_for_a_user(self):
        user = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        userf1 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        userf2 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        userf3 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')
        no_friend_user = User.objects.create_user('kevin', 'kevin@example.com', 'kevinpassword')

        fs1 = FriendShip.objects.create(from_user=user, to_user=userf1, date=datetime.date(2016, 2, 23), status=5)
        fs2 = FriendShip.objects.create(from_user=user, to_user=userf2, date=datetime.date(2016, 2, 23), status=5)
        fs3 = FriendShip.objects.create(from_user=userf3, to_user=user, date=datetime.date(2016, 2, 23), status=5)

        user_friends = friends_for_a_user(user)
        no_friend_user = friends_for_a_user(no_friend_user)

        self.assertEqual(user_friends[0], userf1)
        self.assertEqual(user_friends[1], userf2)
        self.assertEqual(user_friends[2], user)

        self.assertEqual(len(no_friend_user), 0)

    def test_readers_for_a_book(self):
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        u3 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        u4 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')

        pb = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 21))
        npb = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 21))

        r1 = ReadBook.objects.create(user=u1, book=pb, date = datetime.date(2016, 2, 23))
        r2 = ReadBook.objects.create(user=u2, book=pb, date = datetime.date(2016, 2, 23))
        r3 = ReadBook.objects.create(user=u3, book=pb, date = datetime.date(2016, 2, 23))
        r4 = ReadBook.objects.create(user=u4, book=pb, date = datetime.date(2016, 2, 23))

        self.assertEqual(number_of_readers_for_a_book(pb), 4)
        self.assertEqual(number_of_readers_for_a_book(npb), 0)

    def test_friend_readers_for_a_book(self):
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        u3 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        u4 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')

        f1 = FriendShip.objects.create(from_user=u1, to_user=u2, date=datetime.date(2016, 2, 24), status=5)
        f2 = FriendShip.objects.create(from_user=u1, to_user=u3, date=datetime.date(2016, 2, 24), status=2)

        pb = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 21))
        npb = Book.objects.create(name='The Not-So-Example Handbook', isbn='the-not--so--example-handbook', authors='Ample Exson', pub_date = datetime.date(2016, 2, 21))

        r1 = ReadBook.objects.create(user=u1, book=pb, date = datetime.date(2016, 2, 23))
        r2 = ReadBook.objects.create(user=u2, book=pb, date = datetime.date(2016, 2, 23))
        r3 = ReadBook.objects.create(user=u3, book=pb, date = datetime.date(2016, 2, 23))
        r4 = ReadBook.objects.create(user=u4, book=pb, date = datetime.date(2016, 2, 23))

        self.assertEqual(friend_reader_of_a_book(pb, u1)[0], u2)
        self.assertEqual(friend_reader_of_a_book(pb, u1)[1], u3)

    def test_other_readers_for_a_book(self):
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        u3 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        u4 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')

        f1 = FriendShip.objects.create(from_user=u1, to_user=u2, date=datetime.date(2016, 2, 24), status=5)
        f2 = FriendShip.objects.create(from_user=u1, to_user=u3, date=datetime.date(2016, 2, 24), status=5)

        pb = Book.objects.create(name='The Example Handbook', isbn='the-example-handbook', authors='Ex Ample', pub_date = datetime.date(2016, 2, 21))

        r1 = ReadBook.objects.create(user=u1, book=pb, date = datetime.date(2016, 2, 23))
        r2 = ReadBook.objects.create(user=u2, book=pb, date = datetime.date(2016, 2, 23))
        r3 = ReadBook.objects.create(user=u3, book=pb, date = datetime.date(2016, 2, 23))
        r4 = ReadBook.objects.create(user=u4, book=pb, date = datetime.date(2016, 2, 23))

        self.assertEqual(other_readers_for_a_book(u1, pb), [u4])

    def test_pending_invitation_for_a_user(self):
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('babara', 'babara@example.com', 'babarapassword')
        u3 = User.objects.create_user('robert', 'robert@example.com', 'robertpassword')
        u4 = User.objects.create_user('emily', 'emily@example.com', 'emilypassword')

        f1 = FriendShip.objects.create(from_user=u1, to_user=u2, date=datetime.date(2016, 2, 24), status=5)
        f2 = FriendShip.objects.create(from_user=u1, to_user=u3, date=datetime.date(2016, 2, 24), status=2)
        f3 = FriendShip.objects.create(from_user=u1, to_user=u4, date=datetime.date(2016, 2, 24), status=1)

        self.assertEqual(pending_invitation_for_a_user(u1), [f3, f2])

    def test_worm_score(self):
        u1 = User.objects.create_user('john', 'john@example.com', 'johnpassword')
        u2 = User.objects.create_user('jake', 'jake@example.com', 'jakepassword')

        b = Book.objects.create(name="The John Jake Mix'o Book", isbn='nhoj-ekaj-xim-o-koob', authors='The John Jake Series Author', pub_date=datetime.date(2016, 2, 28))

        ReadBook.objects.create(user=u1, book=b, date=datetime.date(2016, 2, 28))
        RecommendShip.objects.create(recommendation=Recommendation.objects.create(book=b, date=datetime.date(2016, 2, 28), comment="Well, this is the offical comment for The John Jake Mix'o book for 2016!!!", from_user=u1), to_user=u2)

        self.assertEqual(worm_score(u1), 2)
        self.assertEqual(worm_score(u2), 0)
