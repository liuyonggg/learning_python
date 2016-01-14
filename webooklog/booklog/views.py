from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'booklog/index.html'
    context_object_name = 'book_list'
    
    def get_queryset(self):
        #return ["book1", "book2"]
        return None


from django.http import HttpResponse
from django.template import loader

def index(request):
    #template = loader.get_template('booklog/index.html')
    return HttpResponse("index")

def detail(request, pk):
    return HttpResponse("detail %s" % pk)

@login_required        
@permission_required('booklog.delete_book')
def delete(request, pk):
    return HttpResponse("delete %s" % pk)

def add(request):
    return HttpResponse("add")
