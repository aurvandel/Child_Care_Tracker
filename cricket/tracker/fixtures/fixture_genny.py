import yaml
from datetime import date, timedelta, datetime, timezone
from random import randint, randrange


'''
- model: tracker.todo
  pk: 1
  fields:
    todoTime: John
    todoDate: Lennon
    task: asdf
    lastDone: 
    recurring:
    completed: 
    messageSent:
'''

def saveYAML(items, filename):
    with open(filename, 'w') as file:
        documents = yaml.dump(items, file)

def todoGen():
    today = date.today()
    startTime = datetime.combine(today, datetime.min.time())
    items = []
    tasks = ['Breathing Treatment', 'Medications', 'Feeding']
    
    for i in range(1, 24, 2):
        template = {'model': 'tracker.todo', 'pk': i, 
        'fields': {'todoTime': (startTime + timedelta(hours=i-1)).strftime('%X'), 'todoDate': today, 
            'task': tasks[i%3], 'lastDone': today, 'recurring': True, 'completed': False, 'messageSent': False}}
        items.append(template)
    
    saveYAML(items, r'todo.yaml')


# todoGen()

'''
- model: tracker.supply
  pk: 1
  fields:
    description: John
    orderNumber: Lennon
    category: asdf
    amount: 
    supplier_id:
    lastDelivery: 
    nextDelivery:
    deliveryFrequency:
    '''

def getRandomDate(back=True):
    
    if back:
        start = datetime.now() - timedelta(days=60)
        end = datetime.now()
        
    else:
        end = datetime.now() + timedelta(days=60)
        start = datetime.now()

    timeBetween = end - start
    daysBetween = timeBetween.days
    randomNumDays = randrange(daysBetween)
    return start + timedelta(days=randomNumDays)

def getRandomTime():
    startTime = datetime.combine(date.today(), datetime.min.time())
    return (startTime + timedelta(hours=randint(7,19))).strftime('%X')

def supplyGen():
    items = []
    
    resp = ['Circuts', 'suction cathaters', 'whisper swivle', 'inhalation water']
    feed = ['formula', 'feed bags', 'button']
    meds = ['albuteral', 'saline', 'sildenafil', 'phenobarbital']
    wound = ['gauze']
    cats = {'RESP': resp, 'FEED': feed, 'MEDS': meds, 'WOUND': wound}
    catMap = {0: 'RESP', 1:'FEED', 2:'MEDS', 3:'WOUND'}
    supplierID = ['IHC', 'Alpine']
    for i in range(1, 24):
        itemList = cats[catMap[i % 4]]
        last = getRandomDate()
        freq = randint(30, 90)
        nextD = last + timedelta(days=freq)
        template = {'model': 'tracker.supply', 'pk': i, 
        'fields': {'description': itemList[i % len(itemList)], 'orderNumber': randint(100, 99999), 
            'category': catMap[i%4], 'amount': randint(1, 200), 'supplier_id': randint(1,2),
            'lastDelivery': last, 'deliveryFrequency': freq, 'nextDelivery': nextD}}
        items.append(template)
    
    saveYAML(items, r'supplies.yaml')


'''
- model: tracker.appointment
  pk: 1
  fields:
    apptTime: John
    apptDate: Lennon
    description: asdf
    address: 
    phone:
'''
def apptGen():
    today = date.today()
    startTime = datetime.combine(today, datetime.min.time())
    items = []
    
    tasks = ['Pulmonogist', 'Dr. Smith', 'Dr. Jones', 'Physical Therapy', 'Trach Team', 
        'Cardiologist', 'Neurologist', 'Gastroenterologist']
    
    addresses = ['368 N Mall Dr, Saint George, Utah', 
        '324 N 1680th E, Saint George, Utah',
        '394 S 1660 West, Saint George, Utah',
        '2259 Santa Maria Ct, Saint George, Utah']

    phone = ['435-215-1326', '435-218-2299', '435-229-2104', '435-251-0946', '435-256-4441']

    for i in range(1, 24):
        template = {'model': 'tracker.appointment', 'pk': i, 
        'fields': {'apptTime': getRandomTime(), 'apptDate': getRandomDate(False), 
            'description': tasks[i % len(tasks)], 'address': addresses[i % len(addresses)], 
            'phone': phone[i % len(phone)]}}
        items.append(template)
    
    saveYAML(items, r'appts.yaml')

apptGen()