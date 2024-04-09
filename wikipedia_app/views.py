from django.http import HttpResponse
from django.shortcuts import render
import wikipedia

def home(request):
    res = ""
    if request.method == 'POST':
        search = request.POST.get('search')
        if search:
            try:
                res = wikipedia.summary(search, sentences=5)
            except wikipedia.exceptions.DisambiguationError as e:
                res = "Ambiguous search term. Please provide more specific query."
            except wikipedia.exceptions.PageError as e:
                res = "No Wikipedia page found for the provided query."
            except Exception as e:
                res = "An error occurred while fetching the Wikipedia page."
        else:
            return render(request, "index.html", {"error": True})
    return render(request, "index.html", {"res": res})
