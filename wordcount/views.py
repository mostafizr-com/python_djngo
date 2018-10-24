from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html', {'title':'Word Counter - Python Website'})

def count(request):
    data = request.POST['text']
    word_list = data.split()
    word_count = len(word_list)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            #increas word
            word_dict[word] += 1
        else:
            #add to dictionary and set value to  1
            word_dict[word] = 1

        
    return render(request, 'count.html', {'data':data, 'word_count':word_count, 'word_dict':word_dict.items()})