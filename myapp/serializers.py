from rest_framework import serializers

class CountryInfoSerializer(serializers.Serializer):
    # name = serializers.CharField()
    flag_link=serializers.CharField()
    capital = serializers.CharField()
    largest_city=serializers.CharField()
    official_languages=serializers.CharField()
    area_total=serializers.FloatField()
    population = serializers.FloatField()
    GDP_nominal=serializers.IntegerField()
   # area = serializers.FloatField()
