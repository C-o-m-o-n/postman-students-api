from rest_framework import serializers
from .models import Student, Event, Registration, Speaker

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    social_links = serializers.ListField(child=serializers.DictField())

    class Meta:
        model = Speaker
        fields = '__all__'

    def create(self, validated_data):
        social_links_data = validated_data.pop('social_links', [])  # Get social links data or empty list if not provided
        speaker = Speaker.objects.create(**validated_data)
        return speaker
