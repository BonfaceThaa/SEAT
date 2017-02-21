from django.shortcuts import render
from analysis.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.serializers import serialize
from analysis.models import County, Incidents
from django.views.generic import TemplateView


def index(request):
	return render(request, 'index.html')

def default(request):
	return render(request, 'default.html')

def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered}, context)
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('home')
			else:
				return HttpResponse("Your SEAT account is disabled.")
		else:
			print ("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('login.html', {}, context)