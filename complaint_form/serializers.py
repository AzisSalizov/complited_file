from .models import Categories
from rest_framework import serializers

class CategoriesSerializers(serializers.ModelSerializer):
   class Meta:
      model = Categories
      fields = ('id' ,'fio' , 'age' , 'directions' , 'sex' , 'bthd', 'date_out' , 'file')