from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def indexDynamic(request):
    quotes = ['The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson '
              'Mandela', 'The way to get started is to quit talking and begin doing. - Walt Disney',
              'If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt',
              'If you set your goals ridiculously high and it\'s a failure, you will fail above everyone '
              'else \'s success. -JamesCameron']
    quote = random.choice(quotes)
    context = {"quote": quote}

    return render(request, "quotes.html", context)

