from rest_framework import serializers
from .models import Assessment

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        # We include 'user' here so the API knows whose test this is
        fields = ['id', 'user', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10_difficulty', 'total_score', 'severity', 'taken_at']
        
        # We make these read-only because our backend logic will calculate them later!
        read_only_fields = ['total_score', 'severity', 'taken_at']