import os
from celery import Celery
import datetime as dt
import tweepy




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

app = Celery('django_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

#app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@app.task(bind=True)
def hello_world(self):
    print('Hello world!')

@app.task(bind=True)
def get_alerts(self):
    from crime.models import DailyAlert
    from .settings import BEARER_TOKEN
    print('Getting alerts...')
    bearer = BEARER_TOKEN
    client = tweepy.Client(bearer_token=bearer)

    id = 285198536

    today = dt.datetime.now(dt.timezone.utc)
    yesterday = today - dt.timedelta(days=1)
    yesterday_date = yesterday.date()
    yesterday = yesterday.replace(microsecond=0).isoformat()

    alert_tweets = []
    shooting_tweets = []
    robbery_tweets = []

    for response in tweepy.Paginator(client.get_users_tweets, id, tweet_fields='id,created_at,text',     
        max_results=10, limit=30):
        for i in range(len(response.data)):
            text = response.data[i].text.lower()
            if 'alert' in text and response.data[i].created_at.date() == yesterday_date:
                alert_tweets.append([response.data[i].text, response.data[i].created_at])
                if 'shooting' in text or 'shot' in text:
                    shooting_tweets.append([response.data[i].text, response.data[i].created_at])
                if 'robbery' in text:
                    robbery_tweets.append([response.data[i].text, response.data[i].created_at])
    
    num_alerts = len(alert_tweets)
    num_shootings = len(shooting_tweets)
    num_robberies = len(robbery_tweets)
    previous_data = DailyAlert.objects.latest('date')
    sum_alerts = previous_data.sum_all_alerts + num_alerts
    sum_shootings = previous_data.sum_shooting_alerts + num_shootings
    sum_robberies = previous_data.sum_robbery_alerts + num_robberies

    daily_alert = DailyAlert(
        all_alerts = num_alerts,
        sum_all_alerts = sum_alerts,
        shooting_alerts = num_shootings,
        sum_shooting_alerts = sum_shootings,
        robbery_alerts = num_robberies,
        sum_robbery_alerts = sum_robberies
    )

    daily_alert.save()
    print('New alerts added')
