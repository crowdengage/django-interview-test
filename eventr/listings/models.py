from django.db import models

class Source(models.Model):
    spektrix_client_name = models.TextField(unique=True)
    friendly_name = models.TextField()

class Event(models.Model):
    source = models.ForeignKey(Source, related_name="events", on_delete=models.CASCADE)
    name = models.TextField()
    # TODO Which other fields should we store for an Event?

class EventInstance(models.Model):
    event = models.ForeignKey(Event, related_name="instances", on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    # TODO Which other fields should we store for an EventInstance?