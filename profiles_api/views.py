from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self,request,format=None):
        """Return a list of apiview"""
        an_apiview=['uses Http method as functions (get,post,patch,put,delete)',
        'is similiar to traditional djnago view',
        'gives most control over application logic',
        'is mapped manualy in URLs',

        ]

        return Response({'message':'hello','an_apiview':an_apiview})
