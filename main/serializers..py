from rest_framework import serializers
from main.models import PopularIndex,IndexInfluence,Index

class PopularIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularIndex
        fields = ('id','')