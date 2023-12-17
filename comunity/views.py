from django.shortcuts import render, redirect
from .models import Trip, Announcement, Order
from .forms import AnnouncementForm, NewTripForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Trip

# Create your views here.

def index(r):
	return render(r, 'comunity/index.html')

def trips(r):
	user = r.user
	if user.profile.ac_type == 0:
		trips = Trip.objects.all().order_by("-id")
		return render(r, "comunity/trips.html", {"trips": trips})
	else:
		trips = Trip.objects.filter(user=user).order_by("-id")
		return render(r, "comunity/driver_trips.html", {"trips": trips})


def trip(r, pk):
	t = Trip.objects.get(pk=pk)
	if r.method == "POST":
		form = AnnouncementForm(r.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			n = Announcement(trip=t, content=content)
			n.save()
			messages.success(r, "تم إرسال الإعلام")
			return redirect("trip", pk=t.id)
	if r.user != t.user:
		announcement = Announcement.objects.filter(trip=t)
		orders = t.order_set.get_queryset()
		ordered = False
		for order in orders:
			if order.user == r.user:
				ordered = True
				break
		return render(r, 'comunity/trip.html', {"trip": t, "announcements": announcement, "ordered": ordered})
	
	orders = t.order_set.get_queryset()
	cost = 0.4*len(orders)
	service_cost = 0.1*len(orders)
	total_cost = round(cost-service_cost, 2)
	form = AnnouncementForm()
	return render(r, "comunity/driver_trip.html", {"trip": t, "orders": orders, "cost": cost, "service_cost": service_cost, "total_cost": total_cost, "form": form})


@login_required
def new_trip(r):
	if r.method == "POST":
		form = NewTripForm(r.POST)
		if form.is_valid():
			direction = form.cleaned_data['direction']
			direction = int(direction)
			time =  form.cleaned_data['time']
			address = form.cleaned_data['address']
			notes = form.cleaned_data['notes']
			user = r.user
			trip = Trip(user=user, direction=direction, time=time, address=address, notes=notes)
			trip.save()
			return redirect("trips")
		
	form = NewTripForm({"address": r.user.profile.address})

	return render(r, "comunity/new_trip.html", {"form": form})

@login_required
def order(r, pk):
	t = Trip.objects.get(pk=pk)
	orders = t.order_set.values()
	if len(orders) <=3:
		user = r.user
		order = Order(user=user, trip=t)
		order.save()
		messages.success(r, "تم تسجيلك في الرحلة بنجاح")
		return trip(r, pk)
