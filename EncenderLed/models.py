from django.db import models

class iluminacion(models.Model):
	led = models.IntegerField(blank=True, null=True, default=0)

	def __unicode__(self):
		return self.led
