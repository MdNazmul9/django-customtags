from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'home.html', context={'data':'amaer deshe hobe sei cele kobe j kothai na boro hoye kaje boro hobe.', 't':20,})