from rest_framework import serializers
from core.models import *

class AuthoritySerializer(serializers.MdeSerializer):

    class Meta:
        model = Authority
        fields = '__all__'