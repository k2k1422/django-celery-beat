# Celery Scheduler


### start celery by default
```
celery -A schedule worker --loglevel=INFO
```

### start celery by name(1@%host)
```
celery -A schedule worker --loglevel=INFO -n worker1@%h
```

### start beat celery
```
celery -A schedule beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```



