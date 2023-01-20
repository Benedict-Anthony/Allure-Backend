from rest_framework import serializers

from users.models import CustomUser

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta(object):
       model = CustomUser
       fields = [
           "first_name", 
           "last_name",
           "email",
           "password",
           "phone",
        #    "gender"
        ]
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        name = validated_data.pop("name")
        if not password:
            raise ValueError("This field is required") 
        
        if password in name or password in [1,2,3]:
            raise ValueError("password is too common")
        
        if len(password) <= 5:
            raise ValueError("password shouldf be at least 6 character")        
        
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user