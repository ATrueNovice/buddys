from rest_framework import serializers

from buddysapp.models import Dispensary

class DispensarySerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()


    def get_logo(self, dispensary):
        request = self.context.get('request')
        logo_url = dispensary.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Dispensary
        fields = ("id", "name", "phone", "address", "logo")
