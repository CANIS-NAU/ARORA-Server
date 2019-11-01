from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class ButterflyList(generics.ListAPIView):
    queryset = Butterfly.objects.all()
    serializer_class = ButterflySerializer


class ButterflyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Butterfly.objects.all()
    serializer_class = ButterflySerializer


class UserButterflyEndPoint(APIView):

    def get(self, request, user_butterfly_id):
        try:
            query = UserButterfly.objects.get(user_butterfly_id=user_butterfly_id)
            serializer = UserButterflySerializer(query)
            return Response(serializer.data)
        except UserButterfly.DoesNotExist:
            return Response({"error": "User butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = UserButterflySerializer(data=request.data)
        if serializer.is_valid():
            new_user_butterfly = serializer.save()
            return Response({"user_butterfly_id": new_user_butterfly.user_butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_butterfly_id):
        try:
            update_user_butterfly = UserButterfly.objects.get(user_butterfly_id=user_butterfly_id)
        except UserButterfly.DoesNotExist:
            return Response({"error": "User_butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        '''This code chunk uses to check if the request is form the user who creates this item'''
        # if update_user_butterfly.UserId != request.user:
        #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        '''code chunk ends'''

        serializer = UserButterflySerializer(update_user_butterfly, data=request.data)
        if serializer.is_valid():
            update_user_butterfly = serializer.save()
            return Response({"user_butterfly_id": update_user_butterfly.user_butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_butterfly_id):
        try:
            update_user_butterfly = UserButterfly.objects.get(user_butterfly_id=user_butterfly_id)
        except UserButterfly.DoesNotExist:
            return Response({"error": "User_butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        '''This code chunk uses to check if the request is form the user who creates this item'''
        # if update_user_butterfly.UserId != request.user:
        #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
        '''code chunk ends'''

        serializer = UserButterflySerializer(update_user_butterfly, data=request.data, partial=True)
        if serializer.is_valid():
            update_user_butterfly = serializer.save()
            return Response({"user_butterfly_id": update_user_butterfly.user_butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_butterfly_id):
        try:
            delete_user_butterfly = UserButterfly.objects.get(user_butterfly_id=user_butterfly_id)
            # if delete_user_butterfly.UserId.UserId != request.user.UserId:
            #     return Response({"error": "Permission denied"}, status=status.HTTP_401_UNAUTHORIZED)
            delete_user_butterfly.delete()
            return Response({}, status=status.HTTP_200_OK)
        except UserButterfly.DoesNotExist:
            return Response({"error": "User_butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserButterfliesEndPoint(APIView):

    def get(self, request, user_id):
        try:
            queryset = UserButterfly.objects.get(user_id=user_id)
            serializer = UserButterflySerializer(queryset, many=True)
            return Response(serializer.data)
        except UserButterfly.DoesNotExist:
            return Response({"error": "All User_butterfly do not exist"}, status=status.HTTP_404_NOT_FOUND)


'''Butterfly Type End Point starts here'''


class ButterflyTypeEndPoint(APIView):

    def get(self, request, butterfly_type_id):
        try:
            query = ButterflyType.objects.get(butterfly_type_id=butterfly_type_id)
            serializer = ButterflyTypeSerializer(query)
            return Response(serializer.data)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ButterflyTypeSerializer(data=request.data)
        if serializer.is_valid():
            new_butterfly_type = serializer.save()
            return Response({"butterfly_type_id": new_butterfly_type.butterfly_type_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, butterfly_type_id):
        try:
            updated_butterfly_type = ButterflyType.objects.get(butterfly_type_id=butterfly_type_id)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyTypeSerializer(updated_butterfly_type, data=request.data)
        if serializer.is_valid():
            updated_butterfly_type = serializer.save()
            return Response({"butterfly_type_id": updated_butterfly_type.butterfly_type_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, butterfly_type_id):
        try:
            updated_butterfly_type = ButterflyType.objects.get(butterfly_type_id=butterfly_type_id)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_type does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyTypeSerializer(updated_butterfly_type, data=request.data, partial=True)
        if serializer.is_valid():
            updated_butterfly_type = serializer.save()
            return Response({"butterfly_type_id": updated_butterfly_type.butterfly_type_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ButterflyTypesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = ButterflyType.objects.all()
            serializer = ButterflyTypeSerializer(queryset, many=True)
            return Response(serializer.data)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_type does not exist"}, status=status.HTTP_404_NOT_FOUND)


'''Butterfly Type End Point ends here'''

'''Butterfly End Point starts here'''


class ButterflyEndPoint(APIView):

    def get(self, request, butterfly_id):
        try:
            query = Butterfly.objects.get(butterfly_id=butterfly_id)
            serializer = ButterflySerializer(query)
            return Response(serializer.data)
        except Butterfly.DoesNotExist:
            return Response({"error": "Butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ButterflySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            new_butterfly = serializer.save()
            return Response({"butterfly_id": new_butterfly.butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, butterfly_id):
        try:
            updated_butterfly = Butterfly.objects.get(butterfly_id=butterfly_id)
        except Butterfly.DoesNotExist:
            return Response({"error": "Butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflySerializer(updated_butterfly, data=request.data)
        if serializer.is_valid():
            updated_butterfly = serializer.save()
            return Response({"butterfly_id": updated_butterfly.butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, butterfly_id):
        try:
            updated_butterfly = Butterfly.objects.get(butterfly_id=butterfly_id)
        except Butterfly.DoesNotExist:
            return Response({"error": "Butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflySerializer(updated_butterfly, data=request.data, partial=True)
        if serializer.is_valid():
            updated_butterfly = serializer.save()
            return Response({"butterfly_id": updated_butterfly.butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ButterfliesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = Butterfly.objects.all()
            serializer = ButterflySerializer(queryset, many=True)
            return Response(serializer.data)
        except Butterfly.DoesNotExist:
            return Response({"error": "Butterfly does not exist"}, status=status.HTTP_404_NOT_FOUND)


'''Butterfly End Point ends here'''

'''Superfly End Point starts here'''
class SuperflyEndPoint(APIView):

    def get(self, request, superfly_id):
        try:
            query = Superfly.objects.get(superfly_id=superfly_id)
            serializer = SuperflySerializer(query)
            return Response(serializer.data)
        except Superfly.DoesNotExist:
            return Response({"error": "Superfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = SuperflySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            new_superfly = serializer.save()
            return Response({"butterfly_id": new_superfly.superfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, superfly_id):
        try:
            updated_superfly = Superfly.objects.get(superfly_id=superfly_id)
        except Superfly.DoesNotExist:
            return Response({"error": "Superfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SuperflySerializer(updated_superfly, data=request.data)
        if serializer.is_valid():
            updated_superfly = serializer.save()
            return Response({"superfly_id": updated_superfly.butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, superfly_id):
        try:
            updated_superfly = Superfly.objects.get(superfly_id=superfly_id)
        except Superfly.DoesNotExist:
            return Response({"error": "Superfly does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SuperflySerializer(updated_superfly, data=request.data, partial=True)
        if serializer.is_valid():
            updated_superfly = serializer.save()
            return Response({"superfly_id": updated_superfly.butterfly_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class SuperfliesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = Superfly.objects.all()
            serializer = SuperflySerializer(queryset, many=True)
            return Response(serializer.data)
        except Superfly.DoesNotExist:
            return Response({"error": "Superfly does not exist"}, status=status.HTTP_404_NOT_FOUND)


class SuperfliesEndPointByButterflyAtriumId(APIView):

    def get(self, request, butterfly_atrium_id):
        try:
            queryset = Superfly.objects.filter(butterfly_atrium_id=butterfly_atrium_id)
            serializer = SuperflySerializer(queryset, many=True)
            return Response(serializer.data)
        except Superfly.DoesNotExist:
            return Response({"error": "Superfly does not exist"}, status=status.HTTP_404_NOT_FOUND)


'''Superfly End Point ends here'''


class ButterflyLikeEndPoint(APIView):

    def get(self, request, butterfly_like_id):
        try:
            query = ButterflyLike.objects.get(butterfly_like_id=butterfly_like_id)
            serializer = ButterflyLikeSerializer(query)
            return Response(serializer.data)
        except ButterflyLike.DoesNotExist:
            return Response({"error": "Butterfly_like does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ButterflyLikeSerializer(data=request.data)
        if serializer.is_valid():
            new_butterfly_like = serializer.save()
            return Response({"butterfly_like_id": new_butterfly_like.butterfly_like_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, butterfly_like_id):
        try:
            updated_butterfly_like = ButterflyLike.objects.get(butterfly_like_id=butterfly_like_id)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_like does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyLikeSerializer(updated_butterfly_like, data=request.data)
        if serializer.is_valid():
            updated_butterfly_like = serializer.save()
            return Response({"butterfly_like_id": updated_butterfly_like.butterfly_like_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, butterfly_like_id):
        try:
            updated_butterfly_like = ButterflyLike.objects.get(butterfly_like_id=butterfly_like_id)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_like does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyLikeSerializer(updated_butterfly_like, data=request.data, partial=True)
        if serializer.is_valid():
            updated_butterfly_like = serializer.save()
            return Response({"butterfly_like_id": updated_butterfly_like.butterfly_like_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ButterflyLikesEndPoint(APIView):

    def get(self, request):
        try:
            queryset = ButterflyLike.objects.all()
            serializer = ButterflyLikeSerializer(queryset, many=True)
            return Response(serializer.data)
        except ButterflyLike.DoesNotExist:
            return Response({"error": "All Butterfly_like do not exist"}, status=status.HTTP_404_NOT_FOUND)


class ButterflyCommentEndPoint(APIView):

    def get(self, request, butterfly_comment_id):
        try:
            query = ButterflyComment.objects.get(butterfly_comment_id=butterfly_comment_id)
            serializer = ButterflyCommentSerializer(query)
            return Response(serializer.data)
        except ButterflyType.DoesNotExist:
            return Response({"error": "Butterfly_comment does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ButterflyCommentSerializer(data=request.data)
        if serializer.is_valid():
            new_butterfly_comment = serializer.save()
            return Response({"butterfly_comment_id": new_butterfly_comment.butterfly_comment_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, butterfly_comment_id):
        try:
            updated_butterfly_comment = ButterflyComment.objects.get(butterfly_comment_id=butterfly_comment_id)
        except ButterflyComment.DoesNotExist:
            return Response({"error": "Butterfly_comment does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyCommentSerializer(updated_butterfly_comment, data=request.data)
        if serializer.is_valid():
            updated_butterfly_comment = serializer.save()
            return Response({"butterfly_comment_id": updated_butterfly_comment.butterfly_comment_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, butterfly_comment_id):
        try:
            updated_butterfly_comment = ButterflyComment.objects.get(butterfly_comment_id=butterfly_comment_id)
        except ButterflyComment.DoesNotExist:
            return Response({"error": "Butterfly_comment does not exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ButterflyCommentSerializer(updated_butterfly_comment, data=request.data, partial=True)
        if serializer.is_valid():
            updated_butterfly_comment = serializer.save()
            return Response({"butterfly_comment_id": updated_butterfly_comment.butterfly_comment_id},
                            status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ButterflyCommentsEndPoint(APIView):

    def get(self, request):
        try:
            queryset = ButterflyComment.objects.all()
            serializer = ButterflyCommentSerializer(queryset, many=True)
            return Response(serializer.data)
        except ButterflyComment.DoesNotExist:
            return Response({"error": "All Butterfly_comment do not exist"}, status=status.HTTP_404_NOT_FOUND)
