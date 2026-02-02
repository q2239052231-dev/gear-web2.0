from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'product_type', 'demand', 'created_at', 'is_handled']
        read_only_fields = ['id', 'created_at', 'is_handled']