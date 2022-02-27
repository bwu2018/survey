from email.policy import HTTP
from re import template
from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
import string

from .models import Room
from .forms import GameForm, CodeForm

# Create your views here.
def random_code():
    length = 4
    return ''.join(random.choice(string.ascii_uppercase) for x in range(length))

def welcome(request):
    return render(request, 'welcome.html')

def add_answer(response, code):
    answers = Room.objects.get(code=code)

    if response.method == "POST":
        if response.POST.get("newAnswer"):
            answer = response.POST.get('new')
            answers.answer_set.create(user = 'temp', text = answer)
    return render(response, 'game_main.html', {'answers': answers})

def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            num_players = form.cleaned_data['num_players']
            code = random_code()
            room = Room(code = code, num_players = num_players)
            room.save()
        return HttpResponseRedirect(f'/survey/{room.code}')
    else:
        form = CodeForm(request.GET)
        if form.is_valid():
            code = form.cleaned_data['code']
            room = Room.objects.get(code=code)
        return HttpResponseRedirect(f'/survey/{room.code}')
