from django.shortcuts import render, redirect
import requests
from django.contrib import messages

# Create your views here.

# Home view
def index(request):
    context={}
    messages.success(request, " SDictionary is more than a dictionary. We believe in simple, easy-to-understand definitions with lots of tools to help you choose your words precisely.")
    return render(request, 'dictionaryApp/index.html', context) 

def results(request):

    if request.method=="GET":
        word= request.GET.get('word','')
        url= "https://api.dictionaryapi.dev/api/v2/entries/en_US/"
        url=url+word
        r= requests.get(url).json()
        # No Definitions Found 
        try:
            if r["title"]=="No Definitions Found":
                messages.error(request, "Sorry pal, we couldn't find definitions for the word you were looking for.")
                return redirect('home')
        except:
            pass

        fWord=r[0]
        name=fWord["word"]

        try:
            partOfSpeech= fWord["meanings"][0]["partOfSpeech"]
        except:
            partOfSpeech='Not Available'

        try:
            definition= fWord["meanings"][0]['definitions'][0]['definition']
        except:
            definition= 'Not Available'

        try:
            example= fWord["meanings"][0]['definitions'][0]['example']
        except:
            example='No example available'

        try:
            audio= fWord["phonetics"][0]['audio']    
        except:
            audio=""


            
            
            
            
        try:
            synonyms= fWord["meanings"][0]['definitions'][0]['synonyms'][0:5]
        except:
            synonyms=['No Synonyms Available']
        context={'word':name, 'pOS':partOfSpeech, 'definition': definition, 'example': example, 'synonyms': synonyms, 'audio': audio }

        return render(request, 'dictionaryApp/searchresults.html', context) 
    return redirect('home')