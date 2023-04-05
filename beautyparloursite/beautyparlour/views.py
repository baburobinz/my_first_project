from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def home(request):

    data1 = gallery.objects.all()
    data2 = offers.objects.all().last()

    dispuname = user_details.objects.get(user_name=request.session['id'])

    return render(request, 'home.html',{'data':data1,'offer':data2,'dispuname':dispuname})








def registered(request):
    if request.method=='POST':
        a = request.POST['fname']
        b = request.POST['lname']
        c = request.POST['uname']
        d = request.POST['email']
        e = request.POST['gend']
        f = request.POST['password']
        f=make_password(f)

        try:


            data=user_details.objects.get(user_name=c)

        except:

            data = user_details.objects.create(first_name=a, last_name=b, user_name=c, email=d, gender=e, password=f)

            data.save()

            return render(request, 'login.html')

        if data :
            error={'error':'Username Already in use..!'}
            return render(request,'register.html',error)

        else:

            data=user_details.objects.create(first_name=a,last_name=b,user_name=c,email=d,gender=e,password=f)

            data.save()

            return render(request,'login.html')


def user_login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']

        error_message = 'Invalid Username or Password...!!'


        try:

            data = user_details.objects.get(user_name=uname)

            check = check_password(pword, data.password)

            if data:

                if uname == data.user_name and check == True:
                    request.session['id'] = uname

                    return redirect(profile)





        except:

            try:

                data2 = admin_details.objects.get(user_name=uname)

                if data2:

                    if uname == data2.user_name and data2.password == pword:

                        request.session['id'] = uname

                        return redirect(profile)

                    else:
                        return render(request, 'login.html', {'error': error_message})



            except:

                return render(request,'login.html',{'error':error_message})




def profile(request):


    if 'id' in request.session:

        data1 = gallery.objects.all()
        data2 = offers.objects.all().last()

        try:

            dispuname = user_details.objects.get(user_name=request.session['id'])

            if dispuname:

                return render(request,'home.html',{'dispuname':dispuname,'data':data1,'offer':data2})

        except:

            return render(request, 'admin_home.html')
    else:
        return render(request,'login.html')


def logout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'login.html')

def user_profile(request):

    return render(request,'user_profile.html')

def change_username(request):
    if request.method=='POST':
        a=request.POST['current']
        b=request.POST['new']

        try:

            data=user_details.objects.get(user_name=a)
            data1=data.user_name

            if data1==a:

                user_details.objects.filter(user_name=a).update(user_name=b)

                request.session['id'] = b

                return render(request,'user_profile.html',{'data':'Username successfully updated'})
        except:

            return render(request, 'user_profile.html', {'data': 'Invalid Username...!!'})



def change_password(request):
    if request.method=='POST':
        uname=request.POST['current_uname']
        a=request.POST['current']
        b=request.POST['new']

        data = user_details.objects.get(user_name=uname)

        check=check_password(a,data.password)
        print(check)
        b=make_password(b)

        if uname==data.user_name and check==True:

            print('check true')

            fil=user_details.objects.filter(user_name=uname).update(password=b)
            print(fil)

            return render(request,'user_profile.html',{'data':'Password successfully updated'})

        else:
            return render(request, 'user_profile.html', {'data': 'Invalid Password..!!'})


def booking_haircut(request):

    quote = quotes.objects.all()
    return render(request,'booking_hair_cut.html',{'quote':quote})

def booked_haircut(request):
    if request.method == 'POST':
        N=request.POST['name']
        P=request.POST['phone']
        T=request.POST['time']
        D=request.POST['date']
        S = request.POST['sel']

        quote = quotes.objects.all()


        booking=booking_details.objects.create(User_name=request.session['id'],Name=N,Phone_Number=P,Time=T,Date=D,Service=S)
        booking.save()

        return render(request,'booking_hair_cut.html',{'message':'Your booking successfully completed','quote': quote})




def clear_booking_user(request):
    data=booking_details.objects.filter(User_name=request.session['id'])
    data.delete()
    return render(request, 'user_profile.html', {'notbooking': 'No Booking History'})


def show_booking_details(request):
    try:
        # data=booking_details.objects.filter(User_name=request.session['id'])
        data=booking_details.objects.all()



        if data:
            return render(request,'user_profile.html',{'booking':data})
        else:
            return render(request, 'user_profile.html', {'notbooking': 'No Booking History'})

    except:

        return render(request, 'user_profile.html', {'notbooking': 'No Booking History'})



def admin_reg(request):
    return render(request,'admin_reg.html')

def admin_show_booking(request):

    data=booking_details.objects.all()


    if data:
        return render(request,'admin_home.html',{'booking':data})
    else:
        return render(request,'admin_home.html',{'nobooking':'No Booking Details'})


def latest(request):

    data=booking_details.objects.all().order_by('-Date','-Time')
    if data:
        return render(request,'admin_home.html',{'booking':data})
    else:
        return render(request,'admin_home.html',{'nobooking':'No Booking Details'})

def older(request):

    data=booking_details.objects.all().order_by('Date','Time')
    if data:
        return render(request,'admin_home.html',{'booking':data})
    else:
        return render(request,'admin_home.html',{'nobooking':'No Booking Details'})

def filter_by_date(request):

    if request.method=="POST":
        a=request.POST['date']
        data=booking_details.objects.filter(Date=a)
        if data:
            return render(request, 'admin_home.html', {'booking': data})
        else:
            return render(request, 'admin_home.html', {'nobooking': 'No Booking Details'})


def clear_booking(request):
    data = booking_details.objects.all().delete()

    return render(request, 'admin_home.html', {'nobooking': 'No Booking Details'})


def change_admin_username(request):
    if request.method == 'POST':
        a = request.POST['current']
        b = request.POST['new']

        try:

            data = admin_details.objects.get(user_name=a)
            data1 = data.user_name

            if data1 == a:
                admin_details.objects.filter(user_name=a).update(user_name=b)
                request.session['id']=b
                return render(request,'admin_home.html',{'msg':'Username successfully updated'})


        except:

            return render(request, 'admin_home.html', {'msg': 'Invalid Username...!!'})


def change_admin_password(request):

    if request.method=="POST":

        a = request.POST['username']
        b = request.POST['cur_pass']
        c = request.POST['new_pass']


        try:

            data = admin_details.objects.get(user_name=a)


            if data.user_name == a and data.password== b:

                admin_details.objects.filter(user_name=a).update(password=c)

                return render(request,'admin_home.html',{'msg2':'Password successfully updated'})


        except:

            return render(request,'admin_home.html',{'msg2':'Invalid Username or Password'})


def upload_gallery(request):

    try:

        if request.method=="POST":

            a = request.FILES['upload_img']

            if a:

                data = gallery.objects.create(image=a)
                data.save()



                return render(request,'admin_home.html',{'img_upload':'Uploaded successfully'})

            else:
                return render(request, 'admin_home.html', {'img_upload': 'Please choose an image'})

    except:

        return render(request,'admin_home.html',{'img_upload':'Please choose an image'})


def upload_quotes(request):

    try:

        if request.method=="POST":

            a=request.POST['upload_quotes']

            if a:

                data = quotes.objects.create(quote=a)
                data.save()
                return render(request, 'admin_home.html', {'quote_msg':'Uploaded successfully'})

            else:
                return render(request, 'admin_home.html', {'quote_msg': 'Please write Quote...!'})

    except:

        return render (request,'admin_home.html',{'quote_msg':'Please write Quote...!'})


def offer(request):

    if request.method=="POST":

        a = request.POST['haircut']
        b = request.POST['makeup']
        c = request.POST['massage']
        data = offers.objects.create(hair=a,massage=b,makeup=c)
        data.save()


def clear_quotes(request):

    data = quotes.objects.all()

    data.delete()



