from rest_framework import serializers
from courts.models import Court


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ('id', 'name', 'type', 'time_on_court', 'court_end_time', 'wait_list')
