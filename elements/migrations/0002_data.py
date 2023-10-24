
from django.db import migrations, models
from elements.models import ElementsToProcess

DATA = [
    (1, 0, 20, 'Element 1'),
    (1, 1, 20, 'Element 2'),
    (2, 2, 20, 'Element 3'),
    (2, 0, 20, 'Element 4'),
    (3, 0, 60, 'Element 5'),
    (3, 1, 60, 'Element 6'),
    (4, 2, 60, 'Element 7'),
    (5, 0, 80, 'Element 8'),
    (5, 1, 80, 'Element 9'),
    (6, 0, 100, 'Element 10')  
]

def load_data(*args):
    for element in DATA:
        ElementsToProcess.objects.create(
            idBulk = element[0],
            retries = element[1],
            status = element[2],
            name = element[3]
        )

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('elements', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_data, migrations.RunPython.noop)
    ]
