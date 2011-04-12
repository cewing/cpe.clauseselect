from datetime import date
from django.db import models


this_year = date.today().year
MODEL_YEARS = [(y, str(y)) for y in range(this_year-15, this_year+1)]


class Vehicle(models.Model):

    vehicle_type = models.CharField(max_length=8)
    vehicle_color = models.CharField(max_length=8)
    model_year = models.IntegerField(choices=MODEL_YEARS)

    def __unicode__(self):
        template = u"%s %s %s"
        return template % (self.vehicle_color,
                           self.model_year,
                           self.vehicle_type)

    @classmethod
    def get_choices_for(cls, fieldname, add_all=False):
        if fieldname not in [f.name for f in cls._meta.fields]:
            raise ValueError("%s is not a valid fieldname" % fieldname)

        if add_all:
            yield (unicode('all'), unicode(add_all))
        allvals = cls.objects.all().values_list(fieldname, flat=True)\
            .order_by(fieldname).distinct()
        for val in allvals:
            yield (unicode(val), unicode(val))
