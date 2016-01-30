from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.template import loader
from .models import Book, Review
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User as AuthUser

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'booklog/index.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        #return ["book1", "book2"]
        return None

#def index(request):
#    bookname = ""
#    booklist = ""
#    if request.GET:
#        bookname= request.GET.get('search')
#        try:
#            booklist = Book.objects.filter(name=bookname)
#        except:
#            booklist = ""
#    return render(request, 'booklog/index.html', {'booklist': booklist, 'bookname':bookname, 'user':request.user})
site_title = "Book Log"
def index(request):
    bookname = ""
    booklist = ""
    if request.GET:
        bookname= request.GET.get('search')
        try:
            booklist = Book.objects.filter(name=bookname)
        except:
            booklist = ""
    return render(request, 'booklog/index.html', {'booklist': booklist, 'bookname':bookname, 'user':request.user, 'site_title':site_title, 'title':''})



def detail(request, pk):
    reviews = None
    book = None
    try:
        book = Book.objects.get(pk=pk)
    except:
        book = None
    if book:
        reviews = Review.objects.filter(book=book)
    return render(request, 'booklog/detail.html', {'book':book, 'reviews':reviews, 'book_cover_url':'http://ecx.images-amazon.com/images/I/519SgX2wwDL._SL500_.jpg'})

@permission_required('booklog.add_book')
@login_required
@permission_required('booklog.delete_book')
def delete(request, pk):
    return HttpResponse("delete %s" % pk)

#@login_required(login_url=reverse('login'))
@permission_required('booklog.add_book')
@login_required
def add(request, name):
    if request.POST:
        name = request.POST.get('name')
        pub_date = datetime.strptime(request.POST.get('pub_date'), '%b %d %Y')
        b1 = Book.objects.create(name=name, pub_date=pub_date)
        b1.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'booklog/add.html', {'name':name})

@permission_required('booklog.change_book')
@login_required
def change(request, pk):
    book = Book.objects.get(pk=pk)
    if request.POST:
        name = request.POST.get('name')
        #pub_date = datetime.strptime(request.POST.get('pub_date'), '%b %d %Y')
        #book.pub_date = pub_date
        book.name = name
        book.save()

        score = request.POST.get('review_score')
        comment = request.POST.get('comment')
        u1 = AuthUser.objects.get(pk=request.user.pk)
        review = Review.objects.create(user=u1, book=book, date=timezone.now(), score=score, comment=comment)
        review.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, 'booklog/change.html', {'book':book})
