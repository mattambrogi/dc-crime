from django.db import models

# Create your models here.


class DailyAlert(models.Model):
    date = models.DateField(auto_now_add=True)
    all_alerts = models.IntegerField()
    sum_all_alerts = models.IntegerField()
    shooting_alerts = models.IntegerField()
    sum_shooting_alerts = models.IntegerField()
    robbery_alerts = models.IntegerField(default=1)
    sum_robbery_alerts = models.IntegerField(default=1)

    def __str__(self):
        return "Alerts for: " + str(self.date)