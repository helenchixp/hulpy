import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class DataBaseInfo(models.Model):
    info_type = models.CharField(max_length=15)
    db_filename = models.CharField(max_length=50)
    user_name = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        results = []
        results.append(self.info_type)
        results.append(self.db_filename)
        return " ".join(results)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class TableInfo(models.Model):
    info_type = models.ForeignKey(DataBaseInfo, on_delete=models.CASCADE)
    table_name = models.CharField(max_length=50)

    def __str__(self):
        return self.table_name
