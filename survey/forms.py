from django import forms

class GameForm(forms.Form):
    num_players = forms.CharField(label='num_players', max_length=3)