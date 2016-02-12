from django.shortcuts import render
from django.contrib import admin
from django.utils.translation import ugettext as _, ugettext_lazy
from django.views.generic import TemplateView
from django.db.models import Q
from reader.models import FriendShip, FRIEND_STATUS, Book, ReadBook
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import NoReverseMatch, reverse

# Create your views here.

class IndexView(TemplateView):
    template_name = "reader/index.html"

    def get_context_data(self, **kwargs):
        friends = FriendShip.objects.filter(Q(from_user=self.request.user) | Q(to_user=self.request.user))
        confirmed_friends = []
        to_be_confirmed_friends = []
        for f in friends:
            if f.status == FRIEND_STATUS[4][0]:
                tf = f.from_user if f.from_user != self.request.user else f.to_user
                confirmed_friends.append(tf)
            elif f.status == FRIEND_STATUS[1][0] and f.to_user == self.request.user:
                to_be_confirmed_friends.append(f.from_user)
        users = User.objects.all()
        books = ReadBook.objects.filter(user=self.request.user)
        return {'user': self.request.user, 
                'confirmed_friends':confirmed_friends,
                'to_be_confirmed_friends':to_be_confirmed_friends,
                'users': users, 
                'books': books,
                }

def dummy_url_handler(request, pk=None):
    return None


