from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'front_page/home.html')

def dont_do_that(request):
    return render(request, 'front_page/dont_do_that.html')