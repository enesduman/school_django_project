from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .models import Account,UserTypes

def register(request):
    form= RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        
        messages.success(request,"Başarıyla Kayıt Oldunuz.")
        return redirect('index')
    cx = {
        "form":form
    }
    return render(request,"register.html",cx)


def register_detail(request,username):
    user = get_object_or_404(Account, username=username)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,"Başarıyla Güncelleme Yapıldı.")
            return redirect('index')
    else:
        form = RegisterForm(instance=user)
    cx = {
        "form":form
    }
    return render(request,"register.html",cx)

def loginUser(request):
    form= LoginForm(request.POST or None)
    cx={
        "form":form
    }
    if form.is_valid():
        cx={}
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",cx)
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        login(request,user)
        return redirect('index')
    cx={
        "form":form
    }
    return render(request,"login.html",cx)


def logoutUser(request):
    logout(request)
    messages.success(request,"Çıkış Yapıldı.")
    return redirect('index')

def dashboard(request):
    cx={}
    cx['ogrenci']=[]
    cx['ogretmen']=[]
    user= Account.objects.all()
    for o in user:
        if o.user_type ==3:
            cx['ogrenci'].append(o)
        elif o.user_type==2:
            cx['ogretmen'].append(o)

    return render(request,"dashboard.html",cx)

def user_delete(request,username):
    user = Account.objects.get(username=username)
    user.delete()
    return redirect("user:dashboard")