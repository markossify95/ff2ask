from django.db import models


class AudienceQuestion(models.Model):
    aq_text = models.CharField(max_length=500)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.aq_text + ' - ' + str(self.score)
