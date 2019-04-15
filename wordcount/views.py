from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['Fulltext']

    worldlist = fulltext.split()

    worldDictionary = {}

    for word in worldlist:
        if word in worldDictionary:
            #Increase
            worldDictionary[word] += 1
        else:
            #add to the dictionary
            worldDictionary[word] = 1

    sortedWords = sorted(worldDictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(worldlist), 'sortedWords': sortedWords})
    
def about(request):
    return render(request, 'aboutus.html')
