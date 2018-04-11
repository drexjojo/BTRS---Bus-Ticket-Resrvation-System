from django.db import models
# from .models import Bus

# Create your models here.
# class Stop(models.Model):
#     area_name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=255,unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table='busrv_Stop'
#         ordering=['-created_at']
#     def __str__(self):
#         return self.area_name
#
# class Stop(models.Model):
#     area_name = models.CharField(max_length=50)
#     slug = models.SlugField(max_length=255,unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table='busrv_Stop'
#         ordering=['-created_at']
#     def __str__(self):
#         return self.area_name

class Route(models.Model):
    route_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255,unique=True)
    # start_stop_id = models.ForeignKey(Stop,unique=False)
    # end_stop_id = models.ForeignKey(Stop,unique=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='Route'
        ordering=['-created_at']
        def __str__(self):
            return self.route_name

class Stop(models.Model):
    area_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    route = models.ForeignKey(Route,unique=False)
    class Meta:
        db_table='Stop'
        ordering=['-created_at']
    def __str__(self):
        return self.area_name


class Bus(models.Model):
    #Bus type
    AC = 'AC'
    NON_AC = 'NAC'

    BUS_TYPES = ((AC,'AC Bus'),
                      (NON_AC,'Non AC bus'),)

    bus_number = models.IntegerField(default=50, primary_key = True)
    slug = models.SlugField(max_length=255,unique=True)
    # bus_description = models.TextField()
    type = models.CharField(choices=BUS_TYPES,default=AC,max_length=10)    
    no_of_seats = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/bus/main/')
    class Meta:
        db_table='Bus'
        ordering=['-created_at']
    def __str__(self):
        return str(self.bus_number)


class Bus_trip(models.Model):
    bus_number = models.ForeignKey(Bus,on_delete=models.CASCADE)
    arriving_time = models.TimeField()
    depature_time = models.TimeField()
    arriving_from = models.ForeignKey(Stop,unique=False,related_name="pickuparea")
    depature_at = models.ForeignKey(Stop,unique=False,related_name="droparea")
    fare = models.DecimalField(max_digits=9,decimal_places=2)
    class Meta:
        db_table='Bus_trip'
 #       ordering=['-created_at']
    def __str__(self):
        return str(self.id)
#
# class RouteTable(model.Model):
#     route_id = models.CharField(max_length=50)
#     route_name = models.CharField(max_length=50)
#     starting_time =
#     stop_id =
