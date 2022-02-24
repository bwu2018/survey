from django.shortcuts import render
from django.http import HttpResponse
import random
import string

from .forms import GameForm

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Brandon', 'secret_code': random_code()})

def random_code():
    length = 4
    return ''.join(random.choice(string.ascii_uppercase) for x in range(length))

def welcome(request):
    return render(request, 'welcome.html')

def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            num_players = form.cleaned_data['num_players']
            print(num_players)
            secret_code = random_code()
            return render(request, 'game_main.html', {'num_players': num_players, 'secret_code': secret_code})
    return render(request, 'hello.html')


def query(request):
    return

def result(request):
    return