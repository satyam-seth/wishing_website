from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'chhath/home.html')
    
def wish(request):
    name=request.GET.get('name')
    share_url=f"Whatsapp://send?text=*{name.upper()}* ने आपके लिए कुछ खास संदेश भेजा है।%0a%0a🪔 🪔 🪔 🪔 🪔 🪔 🪔 🪔%0a%0aइस *नीली लाइन* को टच करके देखो।%0a%0a👇 👇 👇 👇 👇 👇 👇 👇%0awishing.pythonanywhere.com/chhath/wish/?name={name.replace(' ','%2B')}%0a👆 👆 👆 👆 👆 👆 👆 👆"
    return render(request, 'chhath/wish.html', {'name':name,'share_url':share_url})