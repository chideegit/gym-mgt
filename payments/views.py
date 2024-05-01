from django.shortcuts import render, redirect
from .models import Payment
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from accounts.models import GymMembership
from datetime import datetime, timedelta

User = get_user_model()

def initiate_payment(request):
	if request.method == "POST":
		amount = request.POST.get('amount')
		email = request.POST.get('email')

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(amount=amount, email=email, user=request.user)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'payments/make_payment.html', context)

	return render(request, 'payments/initiate_payment.html')


def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		gm = GymMembership.objects.get(user=request.user)

		# Get the current date and time
		current_datetime = datetime.now()
		# Extract the date from the datetime object
		current_date = current_datetime.date()
		gm.last_sub_date = current_date
		gm.next_sub_date = current_date + timedelta(days=31)
		gm.save()
		messages.success(request, 'Payment completed! Your Gym Member has is now renewed for a month.')
		return redirect('dashboard')
	