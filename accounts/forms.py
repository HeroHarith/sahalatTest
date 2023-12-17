from django import forms
from django.core.validators import RegexValidator

class Login(forms.Form):
	username = forms.CharField(label="اسم المستخدم")
	password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput())
	remember = forms.BooleanField(label="تذكرني", initial=True, required=False, label_suffix="")



class NewCustomer(forms.Form):
	first_name = forms.CharField(label="الاسم الأول")
	last_name = forms.CharField(label="القبيلة")
	phone = forms.CharField(label="رقم الهاتف +968", max_length=8, min_length=8, widget=forms.TextInput(attrs={"type": "tel"}), validators=[RegexValidator("^(([97]{7})|(2[2-6]\d{6}))$")])
	address = forms.CharField(label="عنوان السكن")
	username = forms.CharField(label="اسم المستخدم")
	password = forms.CharField(label="كلمة المرور", widget=forms.PasswordInput())
	conferm_password = forms.CharField(label="تأكيد كلمة المرور", widget=forms.PasswordInput())
	email = forms.EmailField(label="البريد الالكتروني")
	accept = forms.BooleanField(label="الموافقة على شروط وأحكام سهالات", initial=False)

class CarDetails(forms.Form):
	name = forms.CharField(label="اسم السيارة بالكامل", help_text="مثال: lexus ES350")
	number = forms.CharField(label="رقم اللوحة")
	
