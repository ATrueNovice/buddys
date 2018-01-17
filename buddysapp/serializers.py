from rest_framework import serializers

from buddysapp.models import Dispensary, Product

#From Here we create the API that allows the app to see data from the webapp

class DispensarySerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

#shows these fields from each dispensary signed up
    def get_logo(self, dispensary):
        request = self.context.get('request')
        logo_url = dispensary.logo.url
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = Dispensary
        fields = ("id", "name", "phone", "address", "logo")

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, product):
        request = self.context.get('request')
        image_url = product.image.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Product
        fields = ("id", "name", "short_description", "primary_usage", "secondary_usage", "sizes", "image", "price")
