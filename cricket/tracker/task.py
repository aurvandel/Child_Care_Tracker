from django.core.mail import send_mail
from background_task import background
from .models import Contact, Todo

# @background(schedule=60)
def notify_users():
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
        
        