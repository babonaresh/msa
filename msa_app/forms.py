from django import forms
from .models import Team,Player

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_logo', 'school','active_status','coach')

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name','email','phone','team','eligibility_status','team_role', 'squad_position', 'street', 'city','state','zipcode')
