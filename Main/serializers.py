from rest_framework import serializers

from Main.models import ItemTable


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTable
        fields = "__all__"