from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return render(request, 'home.html')

def countPage(request):
    fulltext = request.GET['fulltext']
    list = fulltext.split()

    occurance = {}
    for word in list:
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1

    sortedWords = sorted(occurance.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', { 'fulltext':fulltext, 'size' : len(list), 'occurance' : sortedWords })

def aboutPage(request):
    return render(request, 'about.html', {'name':"Brandon"})
