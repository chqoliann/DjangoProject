from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    rate = models.FloatField(verbose_name="Ставка", default=0)
    count = models.IntegerField(verbose_name="Количество", default=0)

    def update_rating(self, new_rating):
        self.rate = (self.rate * self.count + new_rating) / (self.count + 1)
        self.count += 1
        self.save()

    def __str__(self):
        return self.title