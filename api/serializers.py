from rest_framework import serializers
from api.models import Location
from django.contrib.auth.models import User

'''Example of Regular Serializer
class LocationSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    address = serializers.CharField(required=False, allow_blank=True, max_length=60)
    zip_code = serializers.CharField(required=True, allow_blank=False, max_length=20)
    notes = serializers.CharField()
    
    def create(self, validated_data):
        """
        Create and return a new location instance, given validated data.
        """
        
        return Location.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        """
        Update and return an existing Location instance, given validated data.
        """
        
        instance.name = validated_data.get('name',instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.zip_code = validated_data.get('zip_code',instance.zip_code)
        instance.notes = validated_data.get('notes',instance.notes)
        
        instance.save()
        return instance
        '''
        
class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Location
        fields = ('id','name','address','zip_code','notes','owner')
        
class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())
    
    class Meta:
        model = User
        fields = ('id','username','locations')