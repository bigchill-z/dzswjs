from django.db import models


# Create your models here.
class Douyin(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=20)
    hotvalue = models.CharField(max_length=20)
    label = models.IntegerField()
    position = models.IntegerField()
    sentenceid = models.CharField(max_length=20)
    word = models.CharField(max_length=50)

    class Meta:
        db_table = 'douyin'
        managed = True

    def __str__(self):
        return self.word
