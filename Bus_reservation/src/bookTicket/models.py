from django.db import models
from django.contrib.auth.models import User
from bus.models import Stop
# Create your models here.
class bookAticket(models.Model):
    #each indivitual status
    Cancelled = "CNL"
    CONFIRMED = "CNF"

    TICKET_STATUSES = ((Cancelled,'Cancelled'),
                      (CONFIRMED,'Confirmed'),)

    #booking Info
    booking_date = models.DateTimeField()
    status = models.CharField(choices=TICKET_STATUSES,default=CONFIRMED,max_length=2)
    ip_address = models.GenericIPAddressField()
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    # bus = models.ForeignKey(Bus)
    A_time = models.TimeField()
    D_time = models.TimeField()
    A_from = models.CharField(max_length=100,default = 'A')
    D_at = models.CharField(max_length=100,default = 'A')
    date=models.DateTimeField(auto_now_add=True)
    bus_number = models.IntegerField(default=1)
    #contact Info
    email=models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

    #no. of ppl
    booking_seats_num =models.IntegerField(default=1)
    fare = models.DecimalField(max_digits=9,decimal_places=2)

    class Meta:
        verbose_name_plural = 'Booked Tickets'
    def __str__(self):
        return 'BUSBK#00'+str(self.id)

    @property
    def total(self):
        total = self.fare*self.booking_seats_num
        return total
