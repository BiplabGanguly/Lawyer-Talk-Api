from User import models
from User import serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# View Functions......................................................

@api_view(['POST'])
def sign_in(req):
    if req.method == 'POST':
        dict = {'status':200}
        auth_data = req.data.get('auth_id')
        query = models.User_data.objects.filter(auth_id = auth_data)
        if query.exists():
            return Response({'status': 208, 'payload' : 'already signin'})
        else:
            user_serializer = serializer.UserSerializer(data = req.data)
            if user_serializer.is_valid():
                user_serializer.save()
                dict['payload'] = user_serializer.instance.id
                return Response(dict)


@api_view(['GET'])
def get_data(req):
    if req.method == "GET":
        query = models.User_data.objects.all()
        user_serializer = serializer.UserSerializer(query,many = True)
        return Response({'data':user_serializer.data})

