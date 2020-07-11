from rest_framework.views import APIView
from rest_framework.response import Response

from.models import Word
from .serializers import WordSerializer


class WordList(APIView):
    """View to list all words in database"""

    def get(self, request):
        words = Word.objects.all()
        data = WordSerializer(words, many=True).data
        return Response(data)