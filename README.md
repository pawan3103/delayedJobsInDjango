celery -A sample worker -l debug

celery -A sample beat -l debug # for periodic tasks



Celery is used for distribution of tasks which dont need to be done under normal request response cycle(asynchronous).
for example sending mail, uploading images and many more, for that we just need to start celery server.

pip install celery


It requires messaging agent to handling requests from external sources, which is reffered to as broker.

pip install celery[redis] -other then redis we can use rebbitmq

now we will add these brokerurl in settings

BROKER_URL = 'redis//127.0.0.1:6379/0' -o for first database.
BROKER_TRANSPORT = 'redis'

Here we are storing our tasks which need to be executed in queue.


Now, we will create our celery.py file where first we will export default settings

`os.environ.setdefault('DJANGO_SETTINGS_MODULE','sample.settings')`

app = Celery('sample') #sample is project name
#instantiate our celery object, so that we have app running on celer,#celery is actually dependent upon its own application
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) #looks for tasks.py file in all apps

once these is done we can run celery in different terminal(worker) which will execute tasks from queue

`celery -A <project_name> worker -l debug`

here we are setting -l(log level to debug to get extra info to debug)



To deal with periodic tasks   celery has celery beat
so we need to install
`pip install django-celery`

add `djcelery` to installed apps


CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

now need to migrate since we have djcelery installed

celery -A sample beat -l debug --max-interval=10
- beat will look for periodic tasks