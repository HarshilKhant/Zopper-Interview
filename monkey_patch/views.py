from django.views.decorators.csrf import csrf_exempt
from monkey_patch.models import User_Details
from django.http import HttpResponse
import json
import logging

logger = logging.getLogger('api_call')

@csrf_exempt
def get_user_details(request):
    """

    Args:
        request: Request object that contains user information such as

    Returns:

    """
    username = request.POST.get('username')
    contact = int(request.POST.get('contact'))

    user_details = User_Details.objects.filter(username=username, contact=contact).first()

    if user_details:
        response_object = {
            "username": user_details.username,
            "contact": user_details.contact,
            'address_1': user_details.address_line1,
            'address_2': user_details.address_line1,
            'address_3': user_details.address_line1,
            "state": user_details.state,
            "pincode": user_details.pincode,
            "city": user_details.city
        }

        return HttpResponse(json.dumps(response_object))
    else:
        return HttpResponse("User does not exists")



@csrf_exempt
def save_user_details(request):
    try:
        username = request.POST.get('username')
        contact = int(request.POST.get('contact'))
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        address_3 = request.POST.get('address_3')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')

        if validate_max_length(address_1, 30) and validate_max_length(address_2, 30) and validate_max_length(address_3, 22):
            user_exists = User_Details.objects.filter(username=username, contact=contact).count()

            if user_exists == 0:
                User_Details.objects.create(username=username, contact=contact, address_line1=address_1,
                                            address_line2=address_2, address_line3=address_3, state=state, city=city,
                                            pincode=pincode)
                return HttpResponse("User created successfully.")
            else:
                return HttpResponse("User Already Exists.")
        else:
            return HttpResponse("Address length too long.")

    except Exception as e:
        logging.error("error in user creation " + str(e))
        return HttpResponse("Error in creating user.")





def validate_max_length(s, l):
    if len(s) > l:
        return False
    return True