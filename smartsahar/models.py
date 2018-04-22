from django.db import models

# Create your models here.
 
CITY=(
 	('Kathmandu','Kathmandu'),
 	('Pokhara','Pokhara'),
 	('Chitawan','Chitawan'),
 	('Bhairahawa','Bhairahawa'),
 	('Nuwakot','Nuwakot'),
	)


STATE=(
 	('state1','state1'),
 	('state2','state2'),
 	('state3','state3'),
 	('state4','state4'),
 	('state5','state5'),
 	('state6','state6'),
 	('state7','state7'),
 	)
EVENT_ON=(
	('Health','Health'),
	('Education','Education'),
	('Transport','Transport'),
	)

class City (models.Model):
	name= models.CharField(max_length= 20, choices= CITY)
 	state=models.CharField(max_length=20, unique= True, choices= STATE)
 	governor=models.CharField(max_length=30)


 	def __str__(self):
 		return'{},{},{}'.format(self.name, self.state, self.governor)


class Events(models.Model):
	event=models.CharField(max_length=20,choices=EVENT_ON,blank=True)
	Description=models.CharField(max_length=200)
	posted_by=models.CharField(max_length=200,blank=True)
	citizensip_no=models.CharField(max_length=20)
	District=models.CharField(max_length=100,choices=CITY,blank=True)
	Location=models.CharField(max_length=100,blank=True)
	posted_on = models.DateTimeField(auto_now_add=True)
	#image = models.ImageField(upload_to='image', blank=True)
	#is_considered=models.BooleanField(default=False)

	def __str__(self):
		return '{}:{}'.format(self.event,self.posted_by)