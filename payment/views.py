from django.shortcuts import render

# Create your views here.
def payment_success(req):
    return render(req, "payment/payment_success.html", {})