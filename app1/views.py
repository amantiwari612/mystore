from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import *
# Create your views here.

def data(request):
    return HttpResponse("<h1>This is my first webpage</h1>")


def index(request):
    a=Category.objects.all()

    return render(request,"index.html",{'data':a})

def productall(request):
    a=Product.objects.all()
    return render(request,"product.html",{'data':a})

def productfilter(request,id):
    a=Product.objects.filter(Category=id)
    return render(request,"product.html",{'data':a})

def productget(request,id):
    if 'email' in request.session:
        a=Product.objects.get(id=id)
        return render(request,'product_details.html',{'data':a})
    else:
        return redirect('login')

def contact(request):
        if request.method=="POST":
            name1=request.POST.get('name')
            email1=request.POST.get('email')
            message1=request.POST.get('message')
            data=Contactus(name=name1,email=email1,message=message1)
            data.save()

        return render(request,"contact.html")

def register(request):
    if request.method=="POST":
        name1=request.POST['name']
        email1=request.POST['email']
        number1=request.POST['number']
        address1=request.POST['address']
        password1=request.POST['password']
        user=Userregister(name=name1,email=email1,number=number1,address=address1,password=password1)
        data=Userregister.objects.filter(email=email1)
        if  len(data)==0:
            user.save()
            return redirect('login')
        else:
            return render(request,"register.html",{'m':'user alredy exist'})
    return render(request,"register.html")

def login(request):
    if request.method=="POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            user=Userregister.objects.get(email=email1,password=password1)
            if user:
                request.session['email']=user.email
                request.session['id']=user.pk
                return redirect('index1')
            else:
                return render(request,"login.html",{'m':'invalid data enter'})
        except:
            return render(request,"login.html",{'m':'invalid data enter'})
    return render(request,"login.html")

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        del request.session['id']
        return redirect('login')
    else:
        return redirect('login')
    
def profile(request):
    if 'email' in request.session:
        user=Userregister.objects.get(email=request.session['email'])
        if request.method=="POST":

            name1=request.POST['name']
            email1=request.POST['email']
            number1=request.POST['number']
            address1=request.POST['address']
            oldpass=request.POST['oldpassword']
            newpass=request.POST['newpassword']
            user.name=name1
            user.number=number1
            user.address=address1
            user.password=newpass
            if user.password==oldpass:
                user.save()
                return render(request,'profile.html',{'user':user,'m':'profileupdated succesfull'})
            else:
                return render(request,'profile.html',{'user':user,'m':'invalid old password'})
        return render(request,'profile.html',{'user':user})
    else:
        return redirect('login')
    

def buynow(request):
    if 'email' in request.session:
        if request.method=="POST":
            model=Order()
            model.userid=str(request.session['id'])
            model.productid=request.POST['productid']
            productdata=Product.objects.get(id=request.POST['productid'])
            model.quantity="1"
            model.price=str(int(model.quantity)*productdata.price)
            model.paymentmethod="razorpay"
            model.transactionid="adbcib432"
            productdata.quantity-=1
            productdata.save()
            model.save()
            return redirect('ordersuccesview')  
    else:
        return redirect('login')

def ordertable(request):
    if 'email' in request.session:
        orderdata=Order.objects.filter(userid=request.session['id'])
        productlist=[]
        for i in orderdata:
            productdict={}
            productdata=Product.objects.get(id=i.productid)
            productdict['image']=productdata.image
            productdict['name']=productdata.name
            productdict['quantity']=i.quantity
            productdict['price']=i.price
            productdict['date']=i.datetime
            productdict['transactionid']=i.transactionid
            productlist.append(productdict)
        return render(request,'ordertable.html',{'productlist':productlist})
    else:
        return redirect('login')
    
def ordersucess(request):
    if 'email' in request.session:
        return render(request,'order_sucess.html')
    else:
        return redirect('login')