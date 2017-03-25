from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from chkbal.forms import RegistrationForm,Editform,AccountForm,DepositeForm,Transaction,OtherAccountForm
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from  .models import UserProfile,account
from django.views.generic.edit import UpdateView,CreateView
from django.views import generic
from django.views.generic import View

y=''

@login_required
def fund(request,y) :
	if request.method=="POST":
		x=UserProfile.objects.get(user=request.user)
		form=Transaction(request.POST)
		if form.is_valid():
			amt=int(form.cleaned_data['amt'])
			if amt > int(x.balance):
				return render(request,'chkbal/insufficient.html',{'bal':x.balance})
			else:
				return render(request,'chkbal/mpin.html',{'amt':amt})
	else:
		form =Transaction()
		x=UserProfile.objects.get(user=request.user)
		print y
		otheracc=UserProfile.objects.get(user__first_name=y)
		args={
			'form':form,
			'x':x,
			'y':otheracc
			  }
		return render(request,'chkbal/amount.html',args)

@login_required
def deposite(request):
	if request.method=="POST":
		x=UserProfile.objects.get(user=request.user)
		form=DepositeForm(request.POST)
		if form.is_valid():
			c1= int(form.cleaned_data['Text1'])
			c2 = int(form.cleaned_data['Text2'])
			c3 = int(form.cleaned_data['Text3'])
			c4 = int(form.cleaned_data['Text4'])
			print c1,c2,c3,c4
			c1=c1+c3
			c2=c2-c4
			if c1*c2%50 == 0:
				x.balance= int(x.balance)+c1*c2/100

				x.save()
				print x.balance
				return redirect('/chkbal/profile')
			else:
				print "Invalid Serial Key"
				return render(request,'chkbal/Invalid.html')

		return redirect('/chkbal/deposite')
	else:
		form=DepositeForm()
		return render(request,'chkbal/deposite.html',{'form':form})


@login_required
def updateAccount(request):

	if request.method=="POST":
		print "Hello"
		form = AccountForm(request.POST)
		x = UserProfile.objects.get(user=request.user)
		if form.is_valid():
			print 'World'
			account=form.cleaned_data['accountno']
			ifsc=form.cleaned_data['IFSC_Code']
			name=form.cleaned_data['name']
			city=form.cleaned_data['city']
			phone=form.cleaned_data['phone']
			description=form.cleaned_data['description']
			balance=form.cleaned_data['balance']
			address=form.cleaned_data['address']
			x.accountno=account
			x.IFSC_Code=ifsc
			x.city=city
			x.phone=phone
			x.description=description
			x.balance=balance
			x.address=address
			x.name=name
			x.save()
			return redirect('/chkbal/profile')
		else:
			return render(request,'chkbal/data.html',{'x':x})
	else:
		form=AccountForm()
		args={'form':form}
		return render(request,'chkbal/update_account.html',args)



def data(request,acc):
	y=UserProfile.objects.get(user__first_name=acc)
	x=UserProfile.objects.get(user=request.user)
	print x.accountno
	return render(request,'chkbal/data.html',{'x':x,'y':y})

def help(request):
	return render(request,'chkbal/help.html')

def Aboutus(request):
	return render(request,'chkbal/about.html')

def index(request):
	if request.user.id :
		return render(request,'chkbal/home.html',{'user':request.user})
	else:
		return render(request,'chkbal/user_home.html')

@login_required()
def profile(request):
	x=UserProfile.objects.get(user=request.user)
	args={
		'user':request.user,
		'x':x
		  }
	return render(request,'chkbal/profile.html',args)

def register(request):
	if request.user.id:
		return redirect('/chkbal')
	print 'Hello World'
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/chkbal/login')
		else:
			return redirect('/chkbal/register')
	else :
		form=RegistrationForm()
		args={'form':form}
		return render(request,'chkbal/register.html',args)

@login_required
def account(request):
	if request.method=='POST':
		print "Hello"
		form=AccountForm(request.POST,request.UserProfile(instance=request.user))

		if form.is_valid():

			form.save()
			print "World"


			return redirect('/chkbal/profile')
		else:
			return redirect('/chkbal/profile/account-details')
	else :
		form=AccountForm()
		args={'form':form}
		return render(request,'chkbal/update_account.html',args)


@login_required()
def update(request):
	if request.method=='POST':
		form=Editform(request.POST,instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/chkbal/profile')
	else:
		form=Editform(instance=request.user)
		args={'form':form}
		return render(request,'chkbal/update.html',args)

@login_required()
def password(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/chkbal/profile')
		else:
			return redirect('/chkbal/change-password')
	else:
		form=PasswordChangeForm(user=request.user)
		args={'form':form}
		return render(request,'chkbal/change.html',args)

@login_required()
def enquiry(request):
	return render(request,'chkbal/enquiry.html')

@login_required()
def transaction(request):
	x=UserProfile.objects.get(user=request.user)

	if int(x.balance) > 0 :
		return redirect('/chkbal/checkAccount')
	else:
		return render(request,'chkbal/insufficient.html',{'bal':0})

@login_required()
def mini(request):
	return render(request,'chkbal/mini.html')

@login_required()
def details(request):
	return render(request,'chkbal/update_account.html')

@login_required
def checkAccount(request):
	if request.method == "POST":
		form=OtherAccountForm(request.POST)
		if form.is_valid():
			y=form.cleaned_data['name']
			print y
			x=UserProfile.objects.get(user__first_name=y)
			print x.accountno,form.cleaned_data['account']
			if x.accountno == form.cleaned_data['account'] and x.IFSC_Code==form.cleaned_data['ifsc']:
				print "Valid"
				return redirect('/chkbal/fund/'+x.name)
			else:
				print "invalid"
				return redirect('/chkbal/checkAccount')
	else:
		form=OtherAccountForm()
		args={'form':form}
		return render(request,'chkbal/transaction.html',args)

