from django.core.mail import send_mail
from background_task import background
from .models import Contact, Todo
from django.utils import timezone
import datetime

@background(schedule=0)
def notify_users():
    # get tasks that are due soon
    now = timezone.now()
    within5 = now - datetime.timedelta(minutes=5)
    tasks = Todo.objects.filter(todoTime__gt=)
    #TODO: figure out the correct operator when I'm more awake

    # get users addresses
    fromEmail = 'parkergw@gmail.com'
    user = Contact.objects.get(pk=2)
    print(user.getEmail())
    # tasks = Todo.objects.all()

    # addresses = ()
    # users = Contact.objects.all()
    # for user in user:

    send_mail(
    'Subject here',
    'Here is the message.',
    fromEmail,
    [user.getEmail()],
    fail_silently=False,
)
        
        