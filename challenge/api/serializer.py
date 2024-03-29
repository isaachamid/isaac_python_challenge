from rest_framework import serializers
from rest_framework.serializers import Serializer


class DeviceSerializer(Serializer):
    id = serializers.CharField(max_length=50, allow_null=False)
    deviceModel = serializers.CharField(max_length=50, allow_null=False)
    name = serializers.CharField(max_length=100, allow_null=False)
    note = serializers.CharField(max_length=1000, allow_null=False)
    serial = serializers.CharField(max_length=50, allow_null=False)

    def validate_id(self, value):
        tmp_value = value
        id = value.replace("/devices/id", "")

        if value.isdigit():
            raise serializers.ValidationError(
                "id field can't be number"
            )
        if not id.isdigit() or id == tmp_value:
            raise serializers.ValidationError(
                "id field must be in this format: /devices/id<pk>"
            )

        return value

    def validate_deviceModel(self, value):
        device_model = value.replace("/devicemodels/id", "")

        if value.isdigit():
            raise serializers.ValidationError(
                "deviceModel field can't be number"
            )
        if not device_model.isdigit():
            raise serializers.ValidationError(
                "2deviceModel field must be in this format /devicemodels/id1"
            )

        return value

    def validate_name(self, value):
        if value.isdigit():
            raise serializers.ValidationError("name field can't be number")
        return value

    def validate_note(self, value):
        if value.isdigit():
            raise serializers.ValidationError("note field can't be number")
        return value

    def validate_serial(self, value):
        if value.isdigit():
            raise serializers.ValidationError("serial field can't be number")
        return value
