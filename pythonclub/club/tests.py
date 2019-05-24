from django.test import TestCase
from .models import Meeting, MeetingMinute, Resource, Event
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

