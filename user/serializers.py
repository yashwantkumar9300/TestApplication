from rest_framework import serializers
from .models import SmsModel


class SmsSerializes(serializers.ModelSerializer):
    fromm = serializers.CharField(min_length=6)
    to = serializers.CharField(min_length=6)
    text = serializers.CharField(min_length=1)

    class Meta:
        model = SmsModel
        fields = "__all__"