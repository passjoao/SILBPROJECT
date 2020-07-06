from rest_framework import serializers
from core.models import *


class AuthoritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Authority
        fields = '__all__'


class CaptaincySerializer(serializers.ModelSerializer):
    class Meta:
        model = Captaincy
        fields = ['name', 'initials']


class ConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confirmation
        fields = '__all__'


class DefermentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deferment
        fields = '__all__'


class DemandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demands
        fields = '__all__'


class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class JustificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justification
        fields = '__all__'


class LandrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandRecord
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'


class ReligiousOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligiousOrder
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class TramitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tramitations
        fields = '__all__'
