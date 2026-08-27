from django.db import models

class Ticket(models.Model):
    title = models.CharField(max_length=150)
    email = models.EmailField()
    priority = models.CharField(max_length=20, choices=[('LOW','Low'), ('MED','Medium'), ('HIGH','High')], default='MED')
    status = models.CharField(max_length=20, choices=[('OPEN','Open'), ('RESOLVED','Resolved')], default='OPEN')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.priority}] {self.title}"
