from celery.decorators import task


@task
def save_email(form):
    obj = form.save(commit=False)
    try:
        obj.save()
        log.info(u'Email został zapisany')
    except:
        log.info(u'Błąd')
