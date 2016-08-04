from django.db import models


# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class TeacherQuestion(models.Model):
    QUESTION_TYPE_CHOICES = (
        (1, 'One answer'),
        (2, 'N answers'),
        (3, 'Rate on scale'),
    )
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    tq_text = models.CharField(max_length=500)
    tq_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES)

    def __str__(self):
        return str(self.teacher_id) + ' ' + self.tq_text


class TQAnswer(models.Model):
    question_id = models.ForeignKey(TeacherQuestion, on_delete=models.CASCADE)
    tq_answer_text = models.CharField(max_length=500)  # the text of an answer
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.question_id) + ' ' + self.tq_answer_text + ' ' + str(self.score)
