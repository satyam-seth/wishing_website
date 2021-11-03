from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'diwali/home.html')
    
def wish(request):
    name=request.GET.get('name')
    return render(request, 'diwali/wish.html', {'name':name})