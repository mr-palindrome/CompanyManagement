from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class TeamByCompanyIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id','team_lead_name']