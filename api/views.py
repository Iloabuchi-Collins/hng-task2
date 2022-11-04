from rest_framework import generics, status
from django.http import JsonResponse
from . import serializers
from rest_framework.response import Response

class BioView(generics.GenericAPIView):
    def get(self, request):
        return JsonResponse(
            data = {
            "slackUsername": "Collins Iloabuchi", 
            "backend": True, "age": 19, 
            "bio": "I am a medical student enthusiastic about tech. Let's see how far i go in HNG. Hopefully, i become a finalist."
            }
        )

class Calculate():
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y

class OutputView(generics.GenericAPIView):
    serializer_class = serializers.InputSerializer

    def get(self, request):
        return JsonResponse(
            data = {
            "slackUsername": "Collins Iloabuchi", 
            "backend": True, "age": 19, 
            "bio": "I am a medical student enthusiastic about tech. Let's see how far i go in HNG. Hopefully, i become a finalist."
            }
        )


    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        operation_type = str(data['operation_type'])

        if serializer.is_valid():
            
            if operation_type.strip().lower() == 'addition' or operation_type.strip().lower().__contains__('+') or operation_type.strip().lower().__contains__('add') or operation_type.strip().lower().__contains__('adding') or operation_type.strip().lower().__contains__('plus') or operation_type.strip().lower().__contains__('total') or operation_type.strip().lower().__contains__('sum'):
                serializer.data['operation_type'] == 'ADDITION'
                return JsonResponse(
                data = {
                "slackUsername": "Collins Iloabuchi", 
                "result": Calculate.add(serializer.data['x'], serializer.data['y']),
                "operation_type": 'addition'
                    }
                )

            elif operation_type.strip() == 'subtraction' or operation_type.strip().lower().__contains__('subtraction') or operation_type.strip().lower().__contains__('subtract') or operation_type.strip().lower().__contains__('minus') or operation_type.strip().lower().__contains__('subtracting') or operation_type.strip().lower().__contains__('deduct'):
                serializer.data['operation_type'] == 'SUBTRACTION'
                return JsonResponse(
                data = {
                "slackUsername": "Collins Iloabuchi", 
                "result": Calculate.subtract(serializer.data['x'], serializer.data['y']),
                "operation_type": 'addition'
                    }
                )

            elif operation_type.strip() == 'multiplication' or operation_type.strip().lower().__contains__('multiplication') or operation_type.strip().lower().__contains__('multiply') or operation_type.strip().lower().__contains__('multiplying') or operation_type.strip().lower().__contains__('times') or operation_type.strip().lower().__contains__('product'):
                serializer.data['operation_type'] == 'MULTIPLICATION'
                return JsonResponse(
                data = {
                "slackUsername": "Collins Iloabuchi", 
                "result": Calculate.multiply(serializer.data['x'], serializer.data['y']),
                "operation_type": 'addition'
                    }
                )

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)