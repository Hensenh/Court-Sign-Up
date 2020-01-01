from django.db import models
from datetime import datetime, timedelta
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Court(models.Model):
    DEFAULT_TIME = timedelta(minutes=30)
    CHALLENGE = 'CH'
    TRAINING = 'TR'
    TIME = 'TI'
    COURT_TYPES = (
        (CHALLENGE, 'Challenge Court'),
        (TRAINING, 'Training Court'),
        (TIME, 'Timebase Court'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=2,
        choices=COURT_TYPES,
        default=TIME,
    )
    time_on_court = models.DurationField(default=DEFAULT_TIME)
    court_end_time = models.DateTimeField()
    # WaitList uses player id
    on_court = ArrayField(
            models.IntegerField(),
            null=True
        )
    wait_list = ArrayField(
        ArrayField(
            models.IntegerField()
        ),
        null=True
    )

    def update_time(self):
        self.court_end_time = datetime.now() + timedelta(days=self.time_on_court)

    def save(self, *args, **kwargs):
        self.update_time()
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def court_update(self):
        now = datetime.now()
        if now > self.court_end_time:
            self.on_court = self.wait_list[0]
            self.wait_list = self.wait_list[1:]
            self.update_time()
