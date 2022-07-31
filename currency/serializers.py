from rest_framework import serializers

from .models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ('cur_id', 'charcode', 'name', 'rate', 'nominal')
