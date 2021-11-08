from django.shortcuts import render


# Create your views here.
def index(request):
    context = {"name": "d4x1"}
    return render(request, "hybrid_react/index.html", context)