from django import forms

class GameForm(forms.Form):
    num_players = forms.IntegerField(label='num_players')

class CodeForm(forms.Form):
    code = forms.CharField(label='code')

# class UserForm(forms.Form):
#     username = forms.CharField(label='username')