from django.db import models

class FlowData(models.Model):
    Prec_Zone_0 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_1 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_2 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_3 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_4 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_5 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_6 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_7 = models.DecimalField(decimal_places=4,max_digits=24)
    Prec_Zone_8 = models.DecimalField(decimal_places=4,max_digits=24)

    Temp_Zone_0 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_1 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_2 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_3 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_4 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_5 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_6 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_7 = models.DecimalField(decimal_places=4,max_digits=24)
    Temp_Zone_8 = models.DecimalField(decimal_places=4,max_digits=24)

    Flow = models.DecimalField(decimal_places=4,max_digits=24)

    Date = models.DateTimeField()

class PredictedValues(models.Model):
    PredictedValue = models.DecimalField(decimal_places=4,max_digits=24)
    
