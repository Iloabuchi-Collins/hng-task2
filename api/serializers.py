from rest_framework import serializers
import enum
from rest_enumfield import EnumField

class Operation(enum.Enum):
    ADDITION = "addition"
    SUBTRACTION = "subtraction"
    MULTIPLICATION = "multiplication"


class InputSerializer(serializers.Serializer):
    operation_type = EnumField(choices=Operation)
    x = serializers.IntegerField()
    y = serializers.IntegerField()