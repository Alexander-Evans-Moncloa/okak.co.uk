from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
import json
from .models import UserData
from django.shortcuts import render

def my_form_view(request):
    return render(request, 'checkout.html')

@csrf_protect  # Protects the view from CSRF attacks
def submit_form(request):
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request
            data = json.loads(request.body)

            # Create a new record in the database
            UserData.objects.create(
                first_name=data['first-name'],
                last_name=data['last-name'],
                email=data['email'],
                address_line1=data['address-line1'],
                address_line2=data.get('address-line2'),  # Optional field
                city=data['city'],
                postal_code=data['postal-code']
            )

            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except KeyError:
            return JsonResponse({'error': 'Missing data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
