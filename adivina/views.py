from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'adivina/home.html')

def guess(request):
    random_number=random.randint(1,100)
    user_guess = int(request.POST['guess'])

    if user_guess == random_number:
        message='Congratulations'
    else:
        message='You failed'
    
    return render(request, 'adivina/guess.html',{'message':message})
