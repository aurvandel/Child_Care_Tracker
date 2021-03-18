from django.core.mail import send_mail
from background_task import background
from tracker.models import Contact, Todo
from django.utils import timezone
import datetime

# timezone.make_naive to get time in timezone

@background(schedule=0)
def notify_users():
    print("task ran at ", timezone.make_naive(timezone.now()))

    # get tasks that are due soon and put in list
    msgs = []
    now = (timezone.now())
    withinTime = now + timezone.timedelta(minutes=1)
    tasks = Todo.objects.filter(todoTime__range=(now, withinTime))
    if tasks.exists():
        for task in tasks:
            if not task.messageSent:
                print(task)
                msgs.append(task + " is due at " + task.getTime)



    # get users addresses
    fromEmail = 'parkergw@gmail.com'

    user = Contact.objects.get(pk=2)

    addresses = []
    # users = Contact.objects.all()
    # for user in user:

    # send_mail(
    # '',
    # 'Here is the message.',
    # fromEmail,
    # [user.getEmail()],
    # fail_silently=False,
# )
        
        