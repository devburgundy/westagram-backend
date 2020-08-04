import json

from django.views import View
from django.http import JsonResponse

from .models import User

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        if data['email'] != '' and data['password'] != '':
            if User.objects.filter(email = data['email']).exists():
                return JsonResponse({"message" : "email already exists"}, status = 400)
            elif not '@' in data['email'] or not '.' in data['email']:
                return JsonResponse({"message" : "email form is mismatched"}, status = 400)
            elif len(data['password']) < 8:
                return JsonResponse({"message" : "password form is mismatched"}, status = 400)
            else:
                User(
                    email    = data['email'],
                    password = data['password'],
                ).save()
                return JsonResponse({"message" : "SUCCESS"}, status = 200)
        else:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)
        
class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)
        if data['email'] != '' and data['password'] != '':
            if User.objects.filter(email = data['email']).exists():
                signin_user = User.objects.get(email = data['email'])
                if signin_user.password == data['password']:
                    return JsonResponse({"message" : "SUCCESS"}, status = 200)
                else:
                    return JsonResponse({"message" : "INVALID_USER"}, status = 401)
            else:
                return JsonResponse({"message" : "INVALID_USER"}, status = 401)
        else:
            return JsonResponse({"message" : "KEY_ERROR"}, status = 400)