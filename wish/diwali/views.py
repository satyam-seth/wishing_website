from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'diwali/home.html')
    
def wish(request):
    name=request.GET.get('name')
    share_url=f"Whatsapp://send?text=*{name}* ने आपके लिए कुछ खास संदेश भेजा है।%0a🪔 🪔 🪔 🪔 🪔 🪔 🪔 🪔%0aइस *नीली लाइन* को टच करके देखो।%0a👇 👇 👇 👇 👇 👇 👇 👇%0awishing.pythonanywhere.com/diwali/wish/?name={name.replace(' ','%2B')}%0a👆 👆 👆 👆 👆 👆 👆 👆"
    return render(request, 'diwali/wish.html', {'name':name,'share_url':share_url})