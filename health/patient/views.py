# -*- coding=utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect

def home(request):
    output = u'欢迎使用'
    return HttpResponse(output)

@csrf_protect
def register(request):
    '''注册'''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/edit_profile/")
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {
        'form': form,
    })

def login(request):
    '''登录'''

    # If we submitted the form...
    if request.method == 'POST':

        # Check that the test cookie worked (we set it below):
        if request.session.test_cookie_worked():

            # The test cookie worked, so delete it.
            request.session.delete_test_cookie()

            try:
                m = Member.objects.get(username=request.POST['username'])
                if m.password == request.POST['password']:
                    request.session['member_id'] = m.id
                    return HttpResponseRedirect('/')
            except Member.DoesNotExist:
                return HttpResponse("Your username and password didn't match.")

        # The test cookie failed, so display an error message. If this
        # were a real site, we'd want to display a friendlier message.
        else:
            return HttpResponse("Please enable cookies and try again.")

    # If we didn't post, send the test cookie along with the login form.
    request.session.set_test_cookie()
    return render(request, 'login.html')

def logout(request):
    '''登出'''
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def list(request):
    output = u'列出'
    return HttpResponse(output)

def edit_profile(request):
    output = u'编辑个人信息'
    return HttpResponse(output)

def auth_logout(request):
    output = u'认证登出'
    return HttpResponse(output)

def auth_password_change(request):
    output = u'修改密码'
    return HttpResponse(output)

def auth_login(request):
    output = u'认证登录'
    return HttpResponse(output)
