from django.db import models
from django.db.models.deletion import CASCADE
# create models for a quiz app

class Question(models.Model):
    question = models.TextField(null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    hint = models.TextField(null=True)

    # def __str__(self):
    #     return self.question
    
class Prompted(models.Model):
    question_number = models.AutoField(primary_key=True)
    option_click_time = models.DurationField()
    help_button_click_time = models.DurationField()
    continue_button_click_time = models.DurationField()
    time_spent_on_question = models.DurationField()
    option_chosen = models.JSONField(default=list)

    # def __str__(self):
    #     return self.question_number

class Unprompted(models.Model):
    question_number = models.AutoField(primary_key=True)
    option_click_time = models.DurationField()
    help_button_click_time = models.DurationField()
    continue_button_click_time = models.DurationField()
    time_spent_on_question = models.DurationField()
    option_chosen = models.JSONField(default=list)
    
class NoAssistance(models.Model):
    question_number = models.AutoField(primary_key=True)
    option_click_time = models.DurationField()
    help_button_click_time = models.DurationField()
    continue_button_click_time = models.DurationField()
    time_spent_on_question = models.DurationField()
    option_chosen = models.JSONField(default=list)

# class Misleading(models.Model):
#     question_number = models.AutoField(primary_key=True)
#     option_click_time = models.DurationField()
#     help_button_click_time = models.DurationField()
#     continue_button_click_time = models.DurationField()
#     time_spent_on_question = models.DurationField()
#     option_chosen = models.JSONField(default=list)