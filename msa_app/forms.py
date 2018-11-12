from django import forms
from .models import Team, Goal

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'team_logo', 'school','active_status','coach')

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ('match', 'team', 'player', 'goal_minute')