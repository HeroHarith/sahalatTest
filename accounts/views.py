from django.shortcuts import render, redirect
from .forms import Login, NewCustomer, CarDetails
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Car
from django.contrib import auth
# Create your views here.

def login(r):
	if r.method == "POST":
		form = Login(r.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = auth.authenticate(username=username, password=password)
			if user:
				auth.login(r, user)
				if "remember" not in r.POST:
					r.session.set_expiry(0)
				return redirect('home')
			else:
				messages.error(r, "لقد أدخلت اسم مستخدم أو كلمة مرور غير صحيحة")
	form = Login()
	return render(r, 'accounts/login.html', {"form": form})

def new_customer(r):
	if r.method == "POST":
		form = NewCustomer(r.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			phone = form.cleaned_data["phone"]
			email = form.cleaned_data["email"]
			address = form.cleaned_data['address']
			password = form.cleaned_data["password"]
			conferm_password = form.cleaned_data["conferm_password"]
			accept = form.cleaned_data["accept"]
			if User.objects.filter(username=username).exists():
				messages.error(r, "اسم المستخدم الذي قمت بإدخاله موجود بالفعل")
			else:
				
				if not accept:
					messages.error(r, "يجب الموافقة على شروط الاستخدام للمتابعة")
				else:
					if password != conferm_password:
						messages.error(r, "لا يتطابق حقل تأكيد كلمة المرور مع كلمة المرور المدخلة")
					else:
						user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
						profile = Profile(user=user, phone=phone, ac_type=0, address=address)
						profile.save()
						auth.login(r, user)
						
						messages.success(r, "تم إنشاء حسابك بنجاح")
						return redirect("home")
	

	form = NewCustomer()
	return render(r, "accounts/new_customer.html", {"form": form})

def new_driver(r):
	if r.method == "POST":
		form1 = NewCustomer(r.POST, prefix="form1")
		form2 = CarDetails(r.POST, prefix="form2")
		if form1.is_valid() and form2.is_valid():
			print("@sdcvsdvsdvsdv")
			username = form1.cleaned_data['username']
			first_name = form1.cleaned_data["first_name"]
			last_name = form1.cleaned_data["last_name"]
			phone = form1.cleaned_data["phone"]
			email = form1.cleaned_data["email"]
			address = form1.cleaned_data['address']
			password = form1.cleaned_data["password"]
			conferm_password = form1.cleaned_data["conferm_password"]
			accept = form1.cleaned_data["accept"]
			car_name = form2.cleaned_data['name']
			car_number = form2.cleaned_data['number']
			if User.objects.filter(username=username).exists():
				messages.error(r, "اسم المستخدم الذي قمت بإدخاله موجود بالفعل")
			else:
				if not accept:
					messages.error(r, "يجب الموافقة على شروط الاستخدام للمتابعة")
				else:
					if password != conferm_password:
						messages.error(r, "لا يتطابق حقل تأكيد كلمة المرور مع كلمة المرور المدخلة")
					else:
						user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name)
						user.is_active = False
						profile = Profile(user=user, phone=phone, ac_type=1, address=address)
						profile.save()
						car = Car(user=user, name=car_name, number=car_number)
						car.save()
						auth.login(r, user)
						messages.success(r, "تم إنشاء حسابك بنجاح, وسيتم تفعيله فور الانتهاء من مراجعة البيانات")
						return redirect("home")
	form1 = NewCustomer(prefix="form1")
	form2 = CarDetails(prefix="form2")
	return render(r, "accounts/new_driver.html", {"form1": form1, "form2": form2})


def logout(r):
	if r.user.is_authenticated:
		auth.logout(r)
	return redirect("home")