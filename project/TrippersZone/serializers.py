from rest_framework import serializers
from .models import owner, renter, OwnerPost


class ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner

        fields = '__all__'


class renterSerializer(serializers.ModelSerializer):
    class Meta:
        model = renter

        fields = '__all__'


class OwnerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerPost

        fields = '__all__'
