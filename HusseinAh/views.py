from django.shortcuts import render

def home(request):
    return render(request, 'HusseinAh/home.html')
def glass(request):
    return render(request, 'HusseinAh/glass.html')
def example(request):
    return render(request, 'HusseinAh/ex.html')