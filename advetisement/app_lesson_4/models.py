from django.db import models
class Advetisement(models.Model):
    title=models.CharField(verbose_name="название",max_length=128)
    desc=models.TextField('описание')
    price=models.DecimalField('цена',max_digits=10,decimal_places=2)
    torg=models.BooleanField('торг',help_text='возможен ли торг')
    ca=models.DateField(auto_now_add=True)
    ua=models.DateField(auto_now=True)
    class Meta:
        db_table="Advertisements"
    def __str__(self):
        return f'Advertisements(id={self.id},title={self.title},price={self.price})'