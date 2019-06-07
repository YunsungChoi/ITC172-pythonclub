from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event
from django.contrib.auth.models import User
import datetime
from .forms import MeetingForm
# Create your tests here.

class MeetingTest(TestCase):
    def test_string(self):
       type=Meeting(meetingTitle="Generalmeeting")
       self.assertEqual(str(type), type.meetingTitle)
    
    def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'Meeting')

class MeetingMuniteTest(TestCase):
    
    def test_table(self):
       self.assertEqual(str(MeetingMinute._meta.db_table), 'MeetingMinute')


class ResourceTest(TestCase):
    def test_string(self):
       type=Resource(resourceName="Resource1")
       self.assertEqual(str(type), type.resourceName)
    
    def test_table(self):
       self.assertEqual(str(Resource._meta.db_table), 'Resource')

class EventTest(TestCase):
    def test_string(self):
       type=Event(eventTitle="Event1")
       self.assertEqual(str(type), type.eventTitle)
    
    def test_table(self):
       self.assertEqual(str(Event._meta.db_table), 'Event')

class MeetingFormTest(TestCase):
   def setUp(self):
      self.meetingDate = datetime.date.today()
      self.meetingTime = datetime.time(12,00)

   def test_meetingForm(self):
      data={
         'meetingTitle' : 'testMeeting',
         'meetingDate' : self.meetingDate,
         'meetingTime' : self.meetingTime,
         'meetingLocation' : 'testLocation',
         'meetingAgenda' : 'testAgenda',
      }
      form = MeetingForm(data=data)
      self.assertTrue(form.is_valid)

   def test_meetingFormInvalid(self):
      data={
         'meetingTitle' : 'testMeeting',
         'meetingDate' : 'NULL',
         'meetingTime' : 'NULL',
         'meetingLocation' : 'testLocation',
         'meetingAgenda' : 'testAgenda',
      }
      form = MeetingForm(data=data)
      self.assertFalse(form.is_valid())
