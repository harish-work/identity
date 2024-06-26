from rest_framework.serializers import ModelSerializer
from .models import Identity


class IdentitySerializer(ModelSerializer):
    class Meta:
        model = Identity
        fields = '__all__'