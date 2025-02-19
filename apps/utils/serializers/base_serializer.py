from rest_framework import serializers

class BaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)
    updated_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)
    
    class Meta:
        abstract = True


    def create(self, validated_data):
        request = self.context.get("request")  
        if request and request.user.is_authenticated:
            validated_data["created_by"] = request.user
            validated_data["updated_by"] = request.user 
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["updated_by"] = request.user 
        return super().update(instance, validated_data)
