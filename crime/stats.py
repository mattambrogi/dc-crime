from .models import DailyAlert
import datetime as dt


def get_monthly(num):
    today = dt.datetime.now(dt.timezone.utc)
    start_of_year = dt.datetime.now(dt.timezone.utc).replace(month=1, day=1)
    days = (today - start_of_year).days 
    monthly = int((num/days)*31)  
    return monthly  


    pass
    # Get current date. Get number of days since start of year. Divide by that x by 31


def get_stats():
    most_recent_data = DailyAlert.objects.latest('date')
    stats = {}
    stats['num_shootings'] = most_recent_data.sum_shooting_alerts
    stats['monthly_shootings'] = get_monthly(most_recent_data.sum_shooting_alerts)
    stats['num_robberies'] = most_recent_data.sum_robbery_alerts
    stats['monthly_robberies'] = get_monthly(most_recent_data.sum_robbery_alerts)
    stats['most_recent_date'] = most_recent_data.date
    return stats

