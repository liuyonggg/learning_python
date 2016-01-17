from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    redirect_to = request.POST.get('next',
                                   request.GET.get('next', '/'))
    username = ''
    password = ''
    state = 'Please log in ...'
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user and user.is_active:
                auth_login(request, user)
                state = "You're successfully logged in!"
                return HttpResponseRedirect(redirect_to)
        else:
            state = "Your username and/or password were incorrect"
    return render(request, 'registration/login.html', {'state':state, 'username':username})


def logout(request):
    auth_logout(request)

    return render(request, 'registration/logged_out.html')

def password_change(request):
    status = ""
    if request.POST:
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        newpassword2 = request.POST.get('newpassword2')
        if newpassword != newpassword2:
            status = "new password is not same as new password confirmation"
        else:
            if request.user.check_password(oldpassword):
                request.user.set_password(newpassword)
                request.user.save()
                return HttpResponseRedirect(reverse('password_change_done'))
            else:
                status = "old password is not correct"
    return render(request, 'registration/password_change.html', {'status':status})

def password_change_done(request):
    return HttpResponse("password change done")


def password_reset(request):
    status = ""
    if request.POST:
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user and user.username == username:
            token = default_token_generator.make_token(user)
            url = "http://127.0.0.1:8000/password_reset_confirm/%s/%s/" %  (user.pk, token)
            return HttpResponse("<a href=%s>please click to set new password</a>" % url)
            #return HttpResponseRedirect(reverse('password_reset_done', args=[url]))
        else:
            status = "username and email are not matched"
    return render(request, 'registration/password_reset.html', {'status': status})

def password_reset_done(request, url):
    return HttpResponse("<a href=%s>please click to set new password</a>" % url)

def password_reset_confirm(request, pk, token):
    status = "input new password"
    try:
        user = User.objects.get(pk=pk)
    except:
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        if request.POST:
            newpassword = request.POST.get('newpassword')
            newpassword2 = request.POST.get('newpassword2')
            if newpassword != newpassword2:
                status = "new password is not same as new password confirmation"
            else:
                user.set_password(newpassword)
                user.save()
                return HttpResponseRedirect(reverse('password_reset_complete'))
        return render(request, 'registration/password_reset_confirm.html', {'status': status, 'pk':pk, 'token':token})
    return HttpResponse("password reset confirm fail %s %s" % (pk, token))

def password_reset_complete(request):
    return HttpResponse("password reset complete")

@login_required(login_url='/login/')
def user_profile(request):
    if request.POST:
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        request.user.email = email
        request.user.first_name = firstname
        request.user.last_name = lastname
        request.user.save()
    return render(request, 'registration/user_profile.html', 
                 {'username': request.user.username, 
                  'firstname': request.user.first_name,
                  'lastname': request.user.last_name,
                  'email': request.user.email,
                 }
                 )
