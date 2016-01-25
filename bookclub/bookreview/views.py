from django.shortcuts import render

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'booklog/index.html'
    context_object_name = 'book_list'
     
    def get_queryset(self):
        #return ["book1", "book2"]
        return None
