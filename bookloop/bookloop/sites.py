from django.shortcuts import render
from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.utils.translation import ugettext as _, ugettext_lazy
from django.urls import NoReverseMatch, reverse
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.cache import never_cache
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.template.response import TemplateResponse

# Create your views here.
class SiteView(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Book Loop')
    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('Reader')
    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Reader')
    # URL for the "View site" link at the top of each admin page.
    site_url = '/'
    _empty_value_display = '-'
    login_template = 'site/login.html'
    logout_template = 'site/logged_out.html'
    index_template = 'reader/index.html'
    password_change_template = 'site/password_change.html'
    password_change_done_template = 'site/password_change_done.html'

    @never_cache
    def index(self, request, extra_context=None):
        """
        Displays the main admin index page
        """
        app_list = self.get_app_list(request)

        context = dict(
            self.each_context(request),
            title=self.index_title,
            app_list=app_list,
        )
        context.update(extra_context or {})

        request.current_app = self.name

        return TemplateResponse(request, self.index_template or
                                'index.html', context)


    @never_cache
    def login(self, request, extra_context=None):
        """
        Displays the login form for the given HttpRequest.
        """
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('index', current_app=self.name)
            return HttpResponseRedirect(index_path)

        from django.contrib.auth.views import login
        # Since this module gets imported in the application's root package,
        # it cannot import models from other applications at the module level,
        # and django.contrib.admin.forms eventually imports User.
        from django.contrib.admin.forms import AdminAuthenticationForm
        context = dict(self.each_context(request),
            title=_('Log in'),
            app_path=request.get_full_path(),
        )
        if (REDIRECT_FIELD_NAME not in request.GET and
                REDIRECT_FIELD_NAME not in request.POST):
            context[REDIRECT_FIELD_NAME] = reverse('index', current_app=self.name)
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'login.html',
        }
        request.current_app = self.name
        return login(request, **defaults)


    def password_change(self, request, extra_context=None):
        """
        Handles the "change password" task -- both form display and validation.
        """
        from django.contrib.admin.forms import AdminPasswordChangeForm
        from django.contrib.auth.views import password_change
        url = reverse('password_change_done', current_app=self.name)
        defaults = {
            'password_change_form': AdminPasswordChangeForm,
            'post_change_redirect': url,
            'extra_context': dict(self.each_context(request), **(extra_context or {})),
        }
        if self.password_change_template is not None:
            defaults['template_name'] = self.password_change_template
        request.current_app = self.name
        return password_change(request, **defaults)

    def password_reset(self, request, extra_context=None):
        """
        Handles the password reset task
        """
        return password_reset(request, 
                       template_name='site/password_reset.html',
                       email_template_name='site/password_reset_email.html',
                       subject_template_name='site/password_reset_subject.txt',
                       extra_context=extra_context,
                      )

    def password_reset_done(self, request, extra_context=None):
        """
        Handles the password reset done task
        """
        return password_reset_done(request, 
                                   template_name='site/password_reset_done.html',
                                   extra_context=extra_context,
                                  )
    
    def password_reset_confirm(self, request, uidb64, token, extra_context=None):
        return password_reset_confirm(request, uidb64, token, 
                                      template_name='site/password_reset_confirm.html',
                                     )

    def password_reset_complete(self, request, extra_context=None):
        return password_reset_complete(request, 
                                       template_name='site/password_reset_complete.html', 
                                       extra_context=extra_context
                                      )

site = SiteView()
