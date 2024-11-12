from django.shortcuts import render

# Create your views here.

def elastic_search(request):
    return render(request,'search.html')