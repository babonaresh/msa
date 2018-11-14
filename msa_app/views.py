from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

now = timezone.now()

# Homepage Views
#################
def home(request):
    matches_sch = Match.objects.filter(match_status='scheduled')
    matches_full = Match.objects.filter(match_status='full_time')
    matches_live = Match.objects.filter(match_status='in_progress')
    team_live = Team.objects.filter(id=1)
    return render(request, 'base/home.html', {'matches_sch': matches_sch,
                                              'matches_full': matches_full,
                                              'matches_live': matches_live,
                                              'team_logo_live': team_live})

# Match Views
#############
def match_list(request):
    matches_sch = Match.objects.filter(match_status='scheduled')
    matches_full = Match.objects.filter(match_status='full_time')
    matches_all = Match.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/match_list.html', {'matches_sch': matches_sch,
                                                   'matches_full': matches_full,
                                                   'matches_all': matches_all})

@login_required
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    home_team = match.home_team
    guest_team = match.guest_team
    home_goals = Goal.objects.filter(match=match, team=home_team)
    guest_goals = Goal.objects.filter(match=match, team=guest_team)
    return render(request, 'custom/match_detail.html', {'match': match,
                                                'home_team': home_team,
                                                'guest_team': guest_team,
                                                'home_goals': home_goals,
                                                'guest_goals': guest_goals})

# Team Views
#############
@login_required
def team_edit(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == "POST":
        #update
        form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            team = form.save(commit=False)
            team.updated_date = timezone.now()
            team.save()
            teams = Team.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/team_list.html', {'team_list': teams})
    else:
        # edit
        form = TeamForm(instance = team)
    return render(request, 'custom/team_edit.html', {'form': form})

@login_required
def team_new(request):
    if request.method == "POST":
        #update
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.created_date = timezone.now()
            team.save()
            teams = Team.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/team_list.html', {'team_list': teams})
    else:
        # edit
        form = TeamForm()
    return render(request, 'custom/team_edit.html', {'form': form})

def team_list(request):
    team_list = Team.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/team_list.html',
                 {'team_list': team_list})


@login_required
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('msa_app:team_list')


# Player Views
##############
def player_list(request):
    player_list = Player.objects.filter(created_date__lte=timezone.now())
    return render(request, 'custom/player_list.html',
                 {'player_list': player_list})

@login_required
def myteamplayer_list(request, pk):
    coach_id = get_object_or_404(User, pk=pk)
    teamid = get_object_or_404(Team, coach_id=pk)
    myPlayer = Player.objects.filter(team=teamid.id)
    return render(request, 'custom/myteamplayer_list.html',
                            {'myplayer': myPlayer})


@login_required
def player_new(request):
    if request.method == "POST":
        #update
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.created_date = timezone.now()
            player.save()
            players = Player.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/player_list.html', {'player_list': players})
    else:
        # edit
        form = PlayerForm()
    return render(request, 'custom/player_edit.html', {'form': form})

@login_required
def player_edit(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == "POST":
        #update
        form = PlayerForm(request.POST,instance=player)
        if form.is_valid():
            player = form.save(commit=False)
            player.updated_date = timezone.now()
            player.save()
            players = Player.objects.filter(created_date__lte=timezone.now())
            return render(request, 'custom/player_list.html', {'player_list': players})
    else:
        # edit
        form = PlayerForm(instance = player)
    return render(request, 'custom/player_edit.html', {'form': form})



@login_required
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('msa_app:player_list')


#Role Views
###########
@login_required
def role_list(request):
    user_list = User.objects.all()
    role_list = Msarole.objects.filter(registered='No')
    return render(request, 'custom/roles.html', {'roles_list': role_list, 'user_list': user_list,
                                                 'sent': 'False', 'Emailid': 'None'})


@login_required
def assign_role(request):
    form = AssignRoleForm(request.POST or None)
    user_list = User.objects.all()
    role_list = Msarole.objects.filter(registered='No')
    if request.method == "POST":
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            assignrole = form.save(commit=False)
            assignrole.save()
            cd = form.cleaned_data
            host_name = request.get_host()
            print('host_name--', host_name)
            host_url = request.get_full_path()
            print('host_url--', host_url)
            final_url = 'http://' + host_name + "/register"
            print('final_url--', final_url)
           # post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = 'Activate your MSA account as ' + cd['role']
            message = "Hi!\n You are selected as '" + cd['role'] +"' from MSA administration." \
                    "\nPlease register at MSA using below link \n " +final_url + "\n Thanks ! MSA"
            #message = 'Please register at MSA as  ' + cd['role'] + 'using below url.'+ final_url + 'Thanks ! MSA'

            send_mail(subject, message, 'mavstaruno@gmail.com', [cd['receiver_email']])
            return render(request, 'custom/roles.html', {'roles_list': role_list, 'user_list': user_list,
                                                         'sent': 'True', 'emailid': cd['receiver_email']})
    else:
        form = AssignRoleForm()
    return render(request, 'custom/assign_roles.html', {'form': form})


@login_required
def delete_role(request, pk):
    msarole = get_object_or_404(Msarole, pk=pk)
    msarole.delete()
    return redirect('msa_app:role_list')


#Session Views
##############
def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('msa_app:home')
    return render(request, 'registration/login_form.html', {'form': form, 'title': title})


def register_view(request):
    title = 'Register'
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user.set_password(password)
        user.is_staff = True
        user.save()

        msarole = Msarole.objects.get(receiver_email=email)
        group_name = msarole.role
        print('group_name---', group_name)
        my_group = Group.objects.get(name=group_name)
        print('my_group--', my_group)
        my_group.user_set.add(user)

        msarole.registered = 'Yes'
        msarole.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('msa_app:home')


    context = {
        "form": form,
        "title": title
    }
    return render(request, "registration/login_form.html", context)


def register_success(request):
    return render(request, 'registration/success.html')


def logout_view(request):
    logout(request)
    return redirect('msa_app:home')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        print('form--', form)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            print('form-valid-', form)
            #return redirect('msa_app:home')
            return HttpResponseRedirect('/password/success/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        print('form-new-', form)
    return render(request, 'registration/change_password.html', {'form': form })


def password_success(request):
    return render(request, 'registration/change_password_success.html')


