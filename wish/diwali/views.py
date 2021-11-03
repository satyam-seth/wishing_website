from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method=='GET':
        return render(request, 'diwali/diwali.html')
    elif request.method=='POST':
        name=request.POST.get('name')
        return render(request, 'diwali/diwali.html', {'name':name})
        