from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Categories
from .serializers import CategoriesSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from docxtpl import DocxTemplate 
from main.settings import BASE_DIR
import io
from django.core.files.base import ContentFile
import datetime

# Create your views here.

class CategoriesrViewsSet(ModelViewSet):
   queryset = Categories.objects.all()
   serializer_class = CategoriesSerializers

   @action(methods=['post'] , detail=False)
   def create_file(self , request , *args, **kwargs):
      serializers = CategoriesSerializers(data=request.data)
      serializers.is_valid(raise_exception=True)
      data = serializers.validated_data
      doc = DocxTemplate(f'{BASE_DIR}/doc1.docx')
      doc.render(data)
      file_stream = io.BytesIO()
      doc.save(file_stream)
      file_stream.seek(0)
      docs = ContentFile(file_stream.getvalue(),f'Жалоба сотрудника{datetime.datetime.now()}.docx')
      serializers.save(file=docs)

      return Response(data=serializers.data)
