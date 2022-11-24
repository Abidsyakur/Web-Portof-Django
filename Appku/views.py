from cgitb import text
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Future

# Create your views here.
def index(request):
    # future 1
    future1 = Future()
    future1.id = 0
    future1.skill = 'HTML'
    future1.percent = '90%'
    # future 2
    future2 = Future()
    future2.id = 1
    future2.skill = 'CSS3'
    future2.percent = '85%'
    # future 3
    future3 = Future()
    future3.id = 2
    future3.skill = 'Javascript'
    future3.percent = '25%'
    # future 4
    future4 = Future()
    future4.id = 3
    future4.skill = 'C++'
    future4.percent = '40%'
    # future 5
    future5 = Future()
    future5.id = 4
    future5.skill = 'Python'
    future5.percent = '25%'
    # future 6
    future6 = Future()
    future6.id = 5
    future6.skill = 'Editing'
    future6.percent = '70%'
    # future 7
    future7 = Future()
    future7.id = 6
    future7.skill = 'Blender'
    future7.percent = '35%'
    # future 8
    future8 = Future()
    future8.id = 7
    future8.skill = 'Game Development'
    future8.percent = '65%'
    
    
    return render(request, 'index.html',{'future1':future1,'future2': future2,'future3':future3,'future4':future4,'future5':future5,'future6':future6,'future7':future7,'future8':future8})
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{'amount' : amount_of_words})
