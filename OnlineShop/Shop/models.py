from django.db import models
from django.contrib.auth.models import User


class Figure(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    price_usd = models.DecimalField(max_digits=10, decimal_places=2) 
    availability = models.BooleanField(default=True) 
    RACE_CHOICES =[
    ('human', 'Human'),
    ('skaven', 'Skaven'),
    ('greenskins', 'Greenskins'),
    ('high_elves', 'High Elves'),
    ('chaos_undivided', 'Chaos Undivided'),
    # add more races as needed
    ]
    race = models.CharField(max_length=100, choices=RACE_CHOICES)
    # factions are depended of chosen race
    FACTION_CHOICES = {
        'human': [
            ('empire','Empire'),
            ('brettonia','Brettonia'),
            ('golden_order','Golden Order'),
            ('huntsmarshal','The Huntsmarshal\'s Expedition'),
        ],
        'skaven': [
            ('clan_skryre','Clan Skryre'),
            ('clan_eshin','Clan Eshin'),
        ],
        'greenskins':[
            ('grimgor','Grimgor\'s Ardboyz'),
            ('broken_axe','Broken Axe'),
        ],
        'high_elves':[
            ('eataine','Eataine'),
            ('avelorn','Avelorn'),
            ('yvresse','Yvresse'),
        ],
        'chaos_undivided': [
            ('legion_of_chaos','Legion of Chaos'),
            ('shadow_legion','Shadow Legion'),
        ],
        # add more factions as needed
    }
    faction = models.CharField(max_length=100, choices=FACTION_CHOICES)
    height_cm = models.FloatField() # heigh of figure
    image = models.ImageField(upload_to='figurines', blank=True)















