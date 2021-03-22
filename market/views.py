from django.shortcuts import render, redirect
from .models import Team
import numpy as np
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .system import mela


def home(request):
    return render(request, 'index.html')


@login_required(login_url="/accounts/login")
def predict(request):
    if request.method == 'POST':
        Quater = request.POST['firm']
        Area = request.POST['area']
        Frequency = request.POST['frequency']
        Investment = request.POST['investment']

        input_variables = [[Area, Quater, Frequency, Investment]]
        input_variables = np.array(input_variables)

        prediction, maxprofit = mela(input_variables)

        original_input = {'Firm': Quater,
                          'Area': Area,
                          'Frequency': Frequency,
                          'Investment': Investment}
        return render(request, 'predicted.html',
                      {'original': original_input,
                          'results': prediction, 'profit': maxprofit}
                      )
    else:
        return render(request, 'predict.html')


def survey(request):
    return render(request, 'survey.html')


def team(request):
    teams = Team.objects.all()

    return render(request, 'team.html', {"Teams": teams})

# def login(request):


# def user(request, username):
#     user = User.objects.get(username=username)
#     return render(request, "user.html", {"user": user})
