from django.db import models
from recipe.models import Recipe
from django.utils.translation import ugettext_lazy as _

class Ingredient(models.Model):
     title = models.CharField(_('title'), max_length=250)
     quantity =  models.CharField(_('quantity'), max_length=10)
     measurement = models.CharField(_('measurement'),max_length=200, blank=True, null=True)
     preparation = models.CharField(_('preparation'),max_length=100, blank=True, null=True)
     recipe    = models.ForeignKey(Recipe, verbose_name=_('recipe'), related_name='ingredients')
 
     class Meta:
         ordering = ['title']

     def __unicode__(self):
        return self.title
