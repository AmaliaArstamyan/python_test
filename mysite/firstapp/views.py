#
import json
# 
from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from .models import Choice, Question, FirstappUser, Userlog
from django.contrib.auth import authenticate, login as _login
from django.contrib.auth import authenticate, logout as _logout
import datetime


def index(request):
    if request.user.is_authenticated: ## should this add in all classes
        """Return the last five published questions."""
        latest_question_list = Question.objects.order_by("-pub_date")[:5]
        context = {
            "latest_question_list": latest_question_list,
            "user": request.user
        }
        return render(request, "firstapp/index.html", context)
    else:
        # Redirect unauthenticated users to the login page
        return HttpResponseRedirect("/firstapp/login")

# class IndexView(generic.ListView):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template_name = "firstapp/index.html"
#     context_object_name = "latest_question_list"

#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "firstapp/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "firstapp/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "firstapp/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("firstapp:results", args=(question.id,)))
    

####################################### For Registration ########################################################
    
def register(request):
    if request.method == "GET":
        return render(request, "firstapp/register.html", {})
    else:
        try:
            first_name = request.POST["firstname"]
            last_name = request.POST["lastname"]
            email = request.POST["email"]
            country = request.POST["country"]
            password = request.POST["password"]
            repeat_password = request.POST["repeat_password"]
        except:
            return render(request, "firstapp/register.html", {"error_message": "dfgsg"})
        
        if password != repeat_password:
             return render(request, "firstapp/register.html", {"error_message": "Password not match"}) 
        
    user = User.objects.create_user(username=email, email=email, password=password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()

    firstapp_user = FirstappUser(user=user, country=country)
    firstapp_user.save()

    return HttpResponseRedirect("/firstapp/login")


############################################# Login ###############################################################
def login(request):
    if request.method == "GET":
        return render(request, "firstapp/login.html", {})
    else:
        try:
            email = request.POST["email"]
            password = request.POST["password"]
        except:
            return render(request, "firstapp/login.html", {"error_message": "dfgsg"})
        
    user = authenticate(username=email, password=password)
    print("USER", user)
    if user:
        _login(request, user)
        usr=FirstappUser.objects.get(user=request.user)
        log = Userlog(user=usr, action_time = datetime.now(), action = 'question')
        log.save()
        return HttpResponseRedirect("/firstapp")
    else:
        return render(request, "firstapp/login.html", {"error message" :"Email or password is incorect"})
    
def logout(request):
    _logout(request)
    return HttpResponseRedirect("/firstapp/login")


        

