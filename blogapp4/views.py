from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Validation, Movies

def Signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        
        if Validation.objects.filter(Email=email).exists():
            messages.error(request,"User Already Exists!")
            return redirect('signup')
        
        obj = Validation()
        obj.Email = email
        obj.Password = make_password(password)
        obj.save()

        messages.success(request,"Signup Sucessful!")
        return redirect('login')
    return render(request,'signup.html') 


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Validation.objects.get(Email=email)
            if check_password(password, user.Password):
                messages.success(request,"Login Sucessful!")
                return redirect('home')
            
            else:
                messages.error(request,"Invalid Password!")
        
        except Validation.DoesNotExist:
            messages.error(request,"User does not Exist. Signup First")

    return render(request,'login.html')


def Home(request):
    pics=Movies.objects.all()
    return render(request,"home.html",{'movie':pics})

def Moviedetails(request,id):
    moviedetail =  get_object_or_404(Movies, id=id)
    return render(request, 'Moviedetails.html', {'moviedetail': moviedetail})

def Movielist(request):
    pics=Movies.objects.all()
    return render(request,"Movielist.html",{'movie':pics})

def AddtoFavourite(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    movie.favourite = True
    movie.save()
    return redirect('moviedetail', id=movie.id)

def ToggleFavourite(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    movie.favourite = not movie.favourite 
    movie.save()
    return redirect('favouritelist')

def FavouriteList(request):
    favourites = Movies.objects.filter(favourite=True)
    return render(request, 'Favourites.html', {'favourites': favourites})

def Subscription(request):
    return render(request,"Subscribe.html")

def Payment(request):
    return render(request,"payment.html")
    
def root_redirect(request):
    referer = request.META.get('HTTP_REFERER', '')
    if '/admin/' in referer:
        return redirect('home')
    return redirect('signup')


def Forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Validation.objects.filter(Password=make_password(password)).exists():
            messages.error(request, "This Password is already Used. Use Different Password!")
            return redirect('forget')

        try:
            mypass = Validation.objects.get(Email=email)
        except Validation.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect('forget')

        mypass.Password = make_password(password) 
        mypass.save()

        messages.success(request, "Password reset successful! Please login.")
        return redirect('login')

    return render(request, 'fogetpass.html')


def Delete(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            mypass = Validation.objects.get(Email=email)
        except Validation.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('delete')

        if not check_password(password, mypass.Password):
            messages.error(request, "Invalid Password!")
            return redirect('delete')

        mypass.delete()
        messages.success(request, "Account Deleted Successfully!")
        return redirect('signup')
    
    return render(request, 'deleteacc.html')


def Logout(request):
    return redirect('login')