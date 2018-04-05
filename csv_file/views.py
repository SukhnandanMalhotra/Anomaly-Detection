from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_csv.parsers import CSVParser
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer


class FileView(APIView):
    parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                    data=file_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
            )