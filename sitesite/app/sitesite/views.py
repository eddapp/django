from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import pyrebase

config = {

'apiKey': "AIzaSyBzS6cYXT6bW3rsX59PCOE104U2j92iG8s",
    'authDomain': "django-framework-48359.firebaseapp.com",
    'databaseURL': "https://django-framework-48359.firebaseio.com",
    'projectId': "django-framework-48359",
    'storageBucket': "django-framework-48359.appspot.com",
    'messagingSenderId': "1035375680898"
  }

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, "signIn.html")


def postsign(request):
    return render(request, "welcome.html")