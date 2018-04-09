from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from bus.models import Bus
from .models import bookAticket
import pickle
import os.path as pp

# Create your views here.
@login_required
def book_ticket(request,bus_id,template_name='bus/book_ticket_form.html'):
    page_title = 'Book a ticket'
    # bus_info = get_object_or_404(Bus,id=bus_id)
    #get all post data in postdata variable
    print "HH"
    routes = []
    my_path = pp.abspath(pp.dirname(__file__))
    pat = pp.join(my_path, "dat.txt")
    with open(pat,"rb") as f:
        temp_lis = []
        for line in f.readlines():
            temp_lis.append(line.split())
            temp_lis = []
            routes.append(temp_lis)
    print "YAY"
    for lis in routes:
        for i in lis:
            print i
        print "\n"
    pat = pp.join(my_path, "dat.pkl")
    f = open(pat,"rb")
    final_global_path = pickle.load(f)
    print "Dump Opened"
    f.close()

    postdata=request.POST.copy()
    if request.method == 'POST':
        if postdata['bookticket'] == 'Book Ticket':
            #create a object for save
            for path in final_global_path[int(bus_id)]:
                # for xx in bus_number:
                bookTicket = bookAticket()
                bookTicket.email=postdata.get('email',0)
                bookTicket.phone = postdata.get('phone',0)
                bookTicket.booking_seats_num = postdata.get('noofseats',0)
                bookTicket.fare = postdata.get('fare_bus',0)
                if request.user.is_authenticated():
                    bookTicket.user = request.user
                bookTicket.booking_date = postdata.get('book_date',0)
                print path.arriving_from
                print path.depature_at
                bookTicket.bus_number = path.bus_number
                bookTicket.A_from = path.arriving_from
                bookTicket.D_at = path.depature_at
                bookTicket.A_time = path.arriving_time
                bookTicket.D_time = path.depature_time
                # print bookTicket.bus.arriving_from
                # print bookTicket.bus.depature_at
                bookTicket.fare = path.fare
                bookTicket.ip_address = request.META.get('REMOTE_ADDR')
                #save details in the table
                bookTicket.save()
                receipt_url = urlresolvers.reverse('account:my_account')
            return HttpResponseRedirect(receipt_url)

    return render(request,template_name, locals())
