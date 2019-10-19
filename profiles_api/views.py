from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list od APIView featurese"""
        an_apiview = [
            'Uses Http method as function (get, post, patch, put, dlete)',
            'Is similar to a traditional django View',
            'Gives you the most control over youre application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
