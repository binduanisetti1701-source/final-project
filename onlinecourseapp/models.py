from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=200)

    def _str_(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def _str_(self):
        return self.text


class Submission(models.Model):
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def _str_(self):
        return f"Submission {self.id}"