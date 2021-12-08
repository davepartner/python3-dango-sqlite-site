from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dating
from .models import Facilitator
from .forms import RegistrationForm
# Create your views here.

def index(request):
    return HttpResponse('Hello Dworld')


def home(request):
    friendss = Dating.objects.all()

    should_display = False

    return render(request, 'dating/index.html', {
        'friendss' : friendss,
        'should_display': should_display
    })


def dating_detail(request, friend_slug):
    # connect to database, search db for the user with friend_slug, return the info
    try:
        friend = Dating.objects.get(friend_slug=friend_slug)

        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                facilitator, _ = Facilitator.objects.get_or_create(email=user_email)
                friend.facilitator.add(facilitator)
                return redirect('confirm-registration')

        return render(request, 'dating/dating-details.html', {
                'friend': friend,
                'dating_found' : True,
                'form' : registration_form
            })
    except Exception as err:
        print(err)
        return render(request, 'dating/dating-details.html', {
        'dating_found': False,
        'error_message': err
         })

def confirm_registration(request):
    return render(request, 'dating/registration-successful.html')
