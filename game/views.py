from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import User,History
import time
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return render(request, "game/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "game/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "game/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "game/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "game/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "game/register.html")

def guessgame(request,id):
    return render(request, "game/guessgame.html",{
        "player": id
    })

# save user gameplay history
@login_required(login_url=reverse_lazy("index"))
def end_game(request):
    if request.method == "POST":
        playerid =  request.POST["playerid"]
        difficulitylevel =  request.POST["difficulitylevel"]
        guessnumber=  request.POST["guessnumber"]
        status =  request.POST["status"]
        try:
            user = History.objects.create(playerid=User.objects.get(id=playerid),playeridnumber=playerid,difficulitylevel=difficulitylevel,guessnumber=guessnumber,status=status)
            user.save()
        except IntegrityError:
            return render(request, "game/index.html")

        time.sleep(2)
        return HttpResponseRedirect("/guessgame/"+playerid)

# load player all gameplay history and display in page
@login_required(login_url=reverse_lazy("login"))
def showhistory(request,id):
    userhistory=History.objects.filter(playerid=id).order_by('-date')
    paginator = Paginator(userhistory, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    wincount = 0
    losecount = 0
    counter=len(userhistory)

    if userhistory:
        for data in userhistory:
            if data.status == "Win":
                wincount = wincount + 1
            elif data.status == "lose":
                losecount = losecount + 1


    return render(request, "game/playerhistory.html",{
        'page_obj': page_obj,"wincount":wincount, "gamerid":id, "losecount":losecount, 'num_pages': counter,
    })
