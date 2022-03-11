from django.shortcuts import render

def index(request):
    return render(request,'entries/index.html')
def add(request):
    return render(request,'entries')