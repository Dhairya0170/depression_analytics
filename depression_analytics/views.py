from rest_framework import viewsets
from .models import Assessment
from .serializers import AssessmentSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all().order_by('-taken_at')
    serializer_class = AssessmentSerializer

    # This is a special DRF function that lets us intercept the data 
    # right before it gets saved to the database.
    def perform_create(self, serializer):
        answers = serializer.validated_data
        
        total = (
            answers.get('q1', 0) + answers.get('q2', 0) + answers.get('q3', 0) +
            answers.get('q4', 0) + answers.get('q5', 0) + answers.get('q6', 0) +
            answers.get('q7', 0) + answers.get('q8', 0) + answers.get('q9', 0)
        )

        if total <= 4:
            severity = "Minimal"
        elif total <= 9:
            severity = "Mild"
        elif total <= 14:
            severity = "Moderate"
        elif total <= 19:
            severity = "Moderately Severe"
        else:
            severity = "Severe"

        # Check if the user is a logged-in account or anonymous!
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user, total_score=total, severity=severity)
        else:
            # Save it completely anonymously
            serializer.save(total_score=total, severity=severity)