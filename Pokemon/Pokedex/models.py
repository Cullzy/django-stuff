from django.db import models

# Create your models here.
diff_types = (
	('Normal','NORMAL'),
	('Fire','FIRE'),
	('Water','WATER'),
	('Grass','GRASS'),
	('Psychic','PSYCHIC'),
	('Fighting','FIGHTING'),
	('Lightning','LIGHTNING'),
	)


class Pokemon(models.Model):

	name = models.CharField(max_length=168)
	the_type = models.CharField(max_length=168, choices = diff_types, default='normal')
	hp = models.IntegerField()
