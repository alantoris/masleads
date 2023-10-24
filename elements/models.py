from django.db import models

class ElementsToProcess(models.Model):
    """
    Class to represent a Element
    """
    idBulk = models.IntegerField()
    retries = models.IntegerField(null=True, default=None) 
    status = models.IntegerField()
    name = models.CharField(max_length=100)


    class Meta:
        indexes = [
            models.Index(fields=['idBulk', 'status'], name='ElementsToProcess_idBulk_IDX'),
            models.Index(fields=['status'], name='ElementsToProcess_status_IDX'),
        ]

    def __str__(self):
        return f'Element: {self.pk} - {self.name}'
