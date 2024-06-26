from django.contrib import messages
from django.shortcuts import render,redirect
from .models import user_details,Login_user,registration



# Create your views here.


def User_registration(request):
    registertable=registration()
    login_user=Login_user()



    if request.method=='POST':

       registertable.username=request.POST['username']
       registertable.password=request.POST['password']
       registertable.cpassword=request.POST['cpassword']

       login_user.username = request.POST['username']
       login_user.password = request.POST['password']
       login_user.cpassword = request.POST['cpassword']
       login_user.type='user'


       if request.POST['password']==request.POST['cpassword']:
           registertable.save()
           login_user.save()
           messages.success(request, "Registration completed successfully")
           return redirect('login')

       else:
            messages.error(request,"password is incorrect")
            return redirect('register')
    return render(request,'registration.html')



def login(request):

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']

        user=Login_user.objects.filter(username=username,password=password)
        try:
            if user is not None:

                user_details = Login_user.objects.get(username=username, password=password)
                user_name = user_details.username
                type = user_details.type

                if type == 'user':
                    request.session['username'] = user_name
                    return redirect('home')
                elif type == 'admin':
                    request.session['username'] = user_name
                    return redirect('dash')
            else:
                messages.error(request, "Invalid username or password")
        except:
            messages.error(request, 'invalid role')
    return render(request, 'login.html')



def User_home(request):
    user=user_details.objects.all()
    user_name = request.session['username']
    return render(request, 'User_home.html', {'user_name': user_name,'user':user})



def user_reg(request):


    if request.method=='POST':

       User = user_details()
       User.username=request.POST.get('username')
       User.age=request.POST.get('age')
       User.Address=request.POST.get('Address')
       User.Gender=request.POST.get('Gender')
       User.Mobile_number=request.POST.get('Mobile_number')
       User.Email=request.POST.get('Email')
       User.Skills=request.POST.get('Skills')
       User.company = request.POST.get('company')
       User.experience = request.POST.get('experience')
       User.position = request.POST.get('position')
       User.projects = request.POST.get('projects')
       User.certificates = request.POST.get('certificates')
       User.profile_pic = request.FILES.get('profile_pic')

       User.save()
       messages.success(request,"Inserted successfully")

    return render(request, 'user_profile.html')



def user_detail(request,userid):

    user=user_details.objects.get(id=userid)
    return render(request,'user_detail.html',{'user':user})




def update_profile(request,userid):
    User=user_details.objects.get(id=userid)

    if request.method=="POST":

        username = request.POST.get('username')
        age = request.POST.get('age')
        Address = request.POST.get('Address')
        Gender = request.POST.get('Gender')
        Mobile_number = request.POST.get('Mobile_number')
        Email = request.POST.get('Email')
        Skills = request.POST.get('Skills')
        company = request.POST.get('company')
        experience = request.POST.get('experience')
        position = request.POST.get('position')
        projects = request.POST.get('projects')
        certificates = request.POST.get('certificates')
        profile_pic = request.FILES.get('profile_pic')

        User.username =username
        User.age = age
        User.Address = Address
        User.Gender = Gender
        User.Mobile_number = Mobile_number
        User.Email = Email
        User.Skills = Skills
        User.company = company
        User.experience = experience
        User.position = position
        User.projects = projects
        User.certificates = certificates
        User.profile_pic = profile_pic
        User.save()
        return redirect('/')


    return render(request, 'updateview.html', {'User': User})



















