# A dashboard showing the number of reported violent crimes this year in DC


This project is designed to be a dashboard which provides greater transparency into the number of violent crimes in DC.

The app displays a count of the total reported shooting and robberies in DC year to date. These counts are lower bound estimates. They are derived by collecting alert Tweets from the Metropolitan Police Department via a daily task. These tweets are then parsed for key words, categorized, and counted accordingly. 

This is a Django app which relies on Tweepy for Twitter API access and Django-Celery-Beat for the execution of daily tasks. 