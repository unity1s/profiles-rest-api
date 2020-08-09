from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers




class HelloApiView(APIView):
    """test api view"""

    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Return a list of apiview"""
        an_apiview=['uses Http method as functions (get,post,patch,put,delete)',
        'is similiar to traditional djnago view',
        'gives most control over application logic',
        'is mapped manualy in URLs',

        ]

        return Response({'message':'hello','an_apiview':an_apiview})


    def post(self,request):
        """create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello {name}'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """handle partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """test API ViewSet"""
    serializer_class=serializers.HelloSerializer


    def list(self,request):
        """return a hello message"""

        a_viewset=[
        'uses action like list,retrive,update,partial_update,create',
        'automatically maps to URL using Routers',
        'provide more functionality with less code',
        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        """create a new hello message"""

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """handle getting an object by its id"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(Self,request,pk=None):
        """handle partial update of the object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handle removing an object"""
        return Response({'http_method':'DELETE'})
