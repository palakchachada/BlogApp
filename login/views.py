from django.shortcuts import render
from .models import Post
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout


def home(request):
    blg = AdminBlogs.objects.all()
    context = {
        'blg':blg,
    }
    return render(request,'home.html',context)


def user_login(request):
    error_message=""
    if request.method == 'POST':
        #username = request.POST['email']
        #password = request.POST['password']
        #username = User.objects.get(email=email.lower()).username
        user_id = request.POST.get('user_id')  
        print("code",user_id)
        password = request.POST.get('password')
        print("ps",password)
        # user_id = request.POST.get('vendor_code')  
        user = authenticate(user_id = user_id , password=password)
        print("user",user)
        if user is not None:
            login(request,user)
            return redirect('/profile/')
        else:
            error_message = 'Invalid user ID or password'
    return render(request,'login.html' , {'error_message': error_message})


def user_logout(request):
    if request.user.is_authenticated:        
        logout(request)
    return redirect('/login/')


from django.contrib.auth.hashers import make_password
from django.contrib import messages
def signup_view(request):
    message = ""
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        # password = request.POST.get('password')
        password = make_password(request.POST['password'])
        # confirm_password = make_password(request.POST['confirm_password'])
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        vendor_user = Post( user_id =user_id, address = address, mobile_number=mobile_number, name=name, password=password,is_user=True,is_active=True,is_staff=True,is_superuser=False)
        vendor_user.save()
        messages.success(request,"Updated Successfully")  
        return redirect('/login/')
    else:
        message = 'Please fill up all the details correctly'

    context={
        'message':message,
        'generated_user_id': generate_random_code(),
    }    

    return render(request, 'signup.html',context)


import secrets
import string   
def generate_random_code(prefix="USER",length=2):
    alphabet = string.digits
    return prefix + ''.join(secrets.choice(alphabet) for _ in range(length))



def profile(request):
    q = Post.objects.get(user_id=request.user.user_id)
    print("vendors",q.user_id)
    if request.method=='POST':
        q.user_id = request.POST.get('user_id')
        print(q.user_id,"codeeee")
        q.name = request.POST.get('name')
        print('namee',q.name)
        q.address = request.POST.get('address')
        print('ojjjjjjj',q.address)
        q.mobile_number = request.POST.get('mobile_number')
        q.save()
        # serializer_class = VendorSerializer
    context = {
        'q' : q,

    }
    return render(request,'profile.html',context)


from .models import AdminBlogs
def add_blog(request):
    q = AdminBlogs.objects.all()
    print("blog",q)
    if request.method=='POST':
        title = request.POST.get('title')
        print(title,"title")
        content = request.POST.get('content')
        print('content',content)
        date  = request.POST.get('date')
        print('date',date)
        blg = AdminBlogs(title=title, content=content , date = date) 
        blg.save()
        messages.success(request,"Uploaded Successfully")
        
        
    context = {
        'q':q,
    }
    return render(request,'blog.html',context)


def delete_blog(request,id):
    cus = AdminBlogs.objects.get(id=id)
    cus.delete()
    return redirect('/blog/')


def blogs_1(request):
    return render(request,"blogs_1.html")


def blogs_2(request):
    return render(request,"blogs_2.html")

def blogs_3(request):
    return render(request,"blogs_3.html")

def blogs_4(request):
    return render(request,"blogs_4.html")

# def blogs_5(request):
#     return render(request,"blogs_5.html")

# def blogs_6(request):
#     return render(request,"blogs_6.html")