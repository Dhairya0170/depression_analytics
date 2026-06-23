from django.db import models
from django.contrib.auth.models import User

class Assessment(models.Model):
    # Links this assessment to a specific registered user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessments',null=True, blank=True)
    
    # Store the date and time they took the test
    taken_at = models.DateTimeField(auto_now_add=True)
    
    # Store individual answers as integers (0 = Not at all, 3 = Nearly every day)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    
    # Question 10 is about difficulty, scored slightly differently or stored as text/int
    q10_difficulty = models.IntegerField()
    
    # Store the calculated final score (we will calculate this automatically in Phase 2)
    total_score = models.IntegerField(blank=True, null=True)
    severity = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Assessment for {self.user.username} on {self.taken_at.date()}"