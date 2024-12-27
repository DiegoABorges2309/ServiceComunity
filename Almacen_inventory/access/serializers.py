from rest_framework import serializers
from .models import Users, Questions


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        
        
class QuestionsSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    class Meta:
        model = Questions
        fields = '__all__'
        

class LoginSerializers(serializers.Serializer):
    user = serializers.CharField(max_length=60)
    password = serializers.CharField(write_only=True, max_length=50)

    def validate(self, attrs):
        user = attrs.get('user')
        password = attrs.get('password')

        try:
            user_instance = Users.objects.get(user=user)
        except Users.DoesNotExist:
            raise serializers.ValidationError("El usuario no existe")

    
        if user_instance.password != password:
            raise serializers.ValidationError("Contraseña incorrecta")

        attrs['user_instance'] = user_instance
        return attrs

