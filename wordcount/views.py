from django.shortcuts import render
from django.http import HttpResponse
import operator

def home(request):
    return render(request,'home.html')

def wordcount(request):
    x = request.GET["x"]
    y = x.split()
    worddictionary = {}
    for word in y:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedword = sorted(worddictionary.items(), key=operator.itemgetter(1) , reverse=True)
    return render (request, 'wordcount.html',{'x' : x , "count" : len(y), "sortedword" : sortedword })
