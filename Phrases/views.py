from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Phrase
from .serializers import PhraseSerializer


class PhraseList(generics.ListAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer


class PhraseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer


class PhraseEndPoint(APIView):

    def get(self, request, phrase_id):
        try:
            query = Phrase.objects.get(phrase_id=phrase_id)
            serializer = PhraseSerializer(query)
            return Response(serializer.data)
        except Phrase.DoesNotExist:
            return Response({"error": "Phrase does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = PhraseSerializer(data=request.data)
        if serializer.is_valid():
            new_mood_type = serializer.save()
            return Response({"phrase_id": new_mood_type.phrase_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, phrase_id):
        try:
            updated_phrase = Phrase.objects.get(phrase_id=phrase_id)
        except Phrase.DoesNotExist:
            return Response({"error": "Phrase does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhraseSerializer(updated_phrase, data=request.data)
        if serializer.is_valid():
            updated_phrase = serializer.save()
            return Response({"phrase_id": updated_phrase.phrase_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, phrase_id):
        try:
            updated_phrase = Phrase.objects.get(phrase_id=phrase_id)
        except Phrase.DoesNotExist:
            return Response({"error": "Phrase does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PhraseSerializer(updated_phrase, data=request.data, partial=True)
        if serializer.is_valid():
            updated_phrase = serializer.save()
            return Response({"phrase_id": updated_phrase.phrase_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PhrasesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = Phrase.objects.all()
            serializer = PhraseSerializer(queryset, many=True)
            return Response(serializer.data)
        except Phrase.DoesNotExist:
            return Response({"error": "Phrase does not exist"}, status=status.HTTP_404_NOT_FOUND)
