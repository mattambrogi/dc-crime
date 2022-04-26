# dc-crime
A dashboard that displays a count of violent crimes in Washington, DC as reported by the Metropolitan Police Department on Twitter. Vist the live site [here](http://www.crimeindc.com/). 

## What it is
This project is a dashboard, designed to provide transparency into the number of violent crimes in DC.

The app displays a count of the total reported shooting and robberies in DC year to date. These counts are lower bound estimates. The DC Police deparment sends out alets via Twitter whena violent crime occurs. The numbers on this dashboard are derived by aggregating these Tweets. Tweets are then parsed for key words, categorized, and counted accordingly. 

This is a Django app which relies on Tweepy for Twitter API access and Django-Celery-Beat for the execution of daily tasks. 


## Why I built it
Violent crime has risen dramatically over the last five years in Washington, D.C. Shooting are commonplace in the neighborhood I live in. At the beginning of 2022, I was walking to get pizza when a drive by happened a few hundred feet away. I've noticed that the data on the DC police department's website far under-reports the incidence of crime. Strangely, the department does do a pretty good job of consistently sending out alerts via Twitter when crimes occur. 

Many residents are upset by the crime in the city. As a small contribution to transparency, I built this dashboard to keep tabs on how many alerts the police have sent out year to date. 

## Features
- Dashboard displaying count of shootings and robberies year to date
- Automated daily updates

## Technologies
- Python
- Django
- Tweepy
- Django Celery Beat
- Redis Message Broker
- PostgreSQL Database
- HTML, CSS, Bootstrap frontend
- Heroku deployment


## Future work
Features
- Add error handling to alert me when if data pull is unsucccessful
- Once data has built up, add charts for seasonal trends

Other ideas
- The key word parsing is very primitive, but fairly good at capturing the intended tweets. I would like to explore variations of this parsing and programmatically compare their performance.
- At the end of the year I would like to compare this data to DC's offical reported data. My theory is that the department is under-reporting violent crime by a significant margin. 


## Reflections and learnings
This project taught me how to set up and deploy recurring tasks. In this case, a daily job runs which pulls data from an API, parses it, and creates a database entry. I used django-celery-beat and Redis as a message broker to accomplish this. 

This was a useful learning experience for me. First, it allowed me to practice figuring out something completely new: comparing technologies I could utilize, diving into new documentation, and designing a way to integrate a solution into my app. It wasn't immediately obvious how I should aggregate and store data. I enjoyed talking over my logic with more experience engineers. Second, this project opens up the door to building other apps which depend on recurring tasks such as batch data processing or user communications.
