from django.db import models

class TimestampUseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract= True

class MemberRequest(TimestampUseModel):

    lastname = models.CharField(max_length=150)
    firstname = models.CharField(max_length=255)
    job = models.CharField(max_length=250)
    enterprise= models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    #join_way=models.charField(max_lenght=)

    def __str__(self):
        return '{} {} <{}>'.format(self.firstname, self.lastname, self.email)
