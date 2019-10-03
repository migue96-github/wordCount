from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def formcountWord_view(request):
    return render(request, 'formcountWord.html')

def countWord_view(request):
    text = request.GET['text']
    splitted = text.split()

    countByWords = {}

    for word in splitted:
        if word in countByWords:
            countByWords[word] += 1
        else:
            countByWords[word] = 1

    return render(request, 'countWord.html', {'text': text,'count': len(splitted), "countByWords": countByWords.items(), 'difwords': len(countByWords.items())})