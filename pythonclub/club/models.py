from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meeting(models.Model):
    meetingTitle=models.CharField(max_length=255)
    meetingDate=models.DateField()
    meetingTime=models.TimeField()
    meetingLocation=models.TextField(null=True, blank=True)
    meetingAgenda=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.meetingTitle

    class Meta():
        db_table='Meeting'
        verbose_name_plural='Meetings'

class MeetingMinute(models.Model):
    meetingAttendance=models.ManyToManyField(User)
    meetingID=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.meetingAttendance

    class Meta:
        db_table='MeetingMinute'
        verbose_name_plural='MeetingMinutes'

class Resource(models.Model):
    resourceName=models.CharField(max_length=255)
    resourceType=models.CharField(max_length=255)
    resourceURL=models.URLField(null=True, blank=True)
    dateEntered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourceDescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.resourceName

    class Meta:
        db_table='Resource'
        verbose_name_plural='Resources'

class Event(models.Model):
    eventTitle=models.CharField(max_length=255)
    eventLocation=models.TextField(null=True, blank=True)
    eventwdate=models.DateField()
    eventTime=models.TimeField()
    eventDescription=models.TextField()
    userID=models.ManyToManyField(User)

    def __str__(self):
        return self.eventTitle

    class Meta:
        db_table='Event'
        verbose_name_plural='Events'
        
