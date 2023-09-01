
from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

    def validate_difficulty(self, data):
        if data < 1 or data > 10:
            raise serializers.ValidationError("Difficulty should be between 1 and 10")
        return data
    

# Sample Request to try out
# {
#     "front" : "Orange",
#     "back" : "नारंगी",
#     "source_language" : "English",
#     "target_language" : "Hindi",
#     "difficulty" : 8,
# }