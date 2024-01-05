from django.shortcuts import render
from .models import Parcel, Address, EmailVerification
from django.http import JsonResponse

def check_address(request):
    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        recipient_address = request.POST.get('recipient_address')
        address_exists = Address.objects.filter(address=recipient_address).exists()
        if address_exists:
            address_obj = Address.objects.get(address=recipient_address)
            new_parcel = Parcel.objects.create(sender_name=sender_name, recipient_address=address_obj)
            return JsonResponse({'status': 'Parcel created'})
        else:
            return JsonResponse({'status': 'Invalid recipient address'})

def change_parcel_status(request, parcel_id):
    if request.method == 'PUT':
        new_status = request.POST.get('new_status')
        try:
            parcel = Parcel.objects.get(id=parcel_id)
            parcel.status = new_status
            parcel.save()
            return JsonResponse({'status': 'Parcel status updated'})
        except Parcel.DoesNotExist:
            return JsonResponse({'status': 'Parcel not found'})

def check_parcel_status(request, parcel_id):
    try:
        parcel = Parcel.objects.get(id=parcel_id)
        return JsonResponse({'status': parcel.status})
    except Parcel.DoesNotExist:
        return JsonResponse({'status': 'Parcel not found'})


def verify_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        verification_result = True
        email_result, created = EmailVerification.objects.get_or_create(email=email)
        email_result.verified = verification_result
        email_result.save()

    return JsonResponse({'email': email, 'verified': verification_result})


def get_all_results(request):
    results = EmailVerification.objects.all().values('email', 'verified')
    return JsonResponse(list(results))

def get_result(request, email):
    try:
        result = EmailVerification.objects.get(email=email)
        return JsonResponse({'email': result.email, 'verified': result.verified})
    except EmailVerification.DoesNotExists:
        return JsonResponse({'error': 'Result not found'})

def delete_result(request, email):
    try:
        result = EmailVerification.objects.get(email=email)
        result.delete()
        return JsonResponse({'message': 'Result deleted'})
    except EmailVerification.DoesNotExist:
        return JsonResponse({'error': 'Result not found'})





