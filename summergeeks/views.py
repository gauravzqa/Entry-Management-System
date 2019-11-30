from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from summergeeks.forms import HostForm, VisitorForm, CheckoutForm
from summergeeks.models import HostEventDetail, VisitorDetail

from summergeeks.utils.send_email import send_host_email, send_visitor_details_email
from summergeeks.utils.send_text import send_host_sms, send_visitor_details_sms


def create_host(request):
    """
    :param request: request method
    :return:
    """

    if request.method == "GET":
        host_form = HostForm()
    elif request.method == "POST":
        host_form = HostForm(request.POST)
        if host_form.is_valid():
            data = host_form.cleaned_data

            for host in HostEventDetail.objects.all():
                if host.phone_number == data['phone_number'] or host.email_address == data['email_address']:
                    return HttpResponse('A event has already been registered with these details')

            try:
                host = HostEventDetail(
                    event_name=data['event_name'],
                    host_name=data['host_name'],
                    host_address=data['host_address'],
                    phone_number=data['phone_number'],
                    email_address=data['email_address'],
                )
            except:
                return HttpResponse('Please provide correct details')
            host.save()
            return HttpResponse(
                'Host has been created successfully',
                status=200
            )
    return render(request, 'summergeeks/host_form.html', {'form': host_form})


def create_visitor(request):
    """
    :param request: request method
    :return:
    """

    if request.method == "GET":
        visitor_form = VisitorForm()
    elif request.method == "POST":
        visitor_form = VisitorForm(request.POST)
        if visitor_form.is_valid():
            data = visitor_form.cleaned_data
            for visitor in data['host'].visitordetail_set.all():
                if visitor.phone_number == data['phone_number'] or visitor.email_address == data['email_address']:
                    return HttpResponse('Visitor already registered')

            try:
                visitor = VisitorDetail(
                    host=data['host'],
                    visitor_name=data['visitor_name'],
                    email_address=data['email_address'],
                    phone_number=data['phone_number'],
                    check_in_time=datetime.now(),
                )
            except:
                return HttpResponse('Please provide correct details')
            visitor.save()
            send_host_email(
                visitor.visitor_name,
                visitor.check_in_time,
                visitor.phone_number,
                visitor.email_address,
            )
            send_host_sms(
                visitor.visitor_name,
                visitor.check_in_time,
                visitor.phone_number,
                visitor.email_address,
            )
            return HttpResponse(
                f'You have successfully checked in on {visitor.check_in_time}',
                status=200
            )
    return render(request, 'summergeeks/visitor_form.html', {'form': visitor_form})


def checkout_visitor(request):
    """
    :param request:
    :return: visitor searched by mobile number
    """

    if request.method == "GET":
        checkout_form = CheckoutForm()
    elif request.method == "POST":
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            data = checkout_form.cleaned_data
            try:
                get_visitor = VisitorDetail.objects.get(host=data['host'], phone_number=data['phone_number'])
            except:
                return HttpResponse('Invalid Record. Please provide the same phone number as per check in')
            if get_visitor.check_out_time is None:
                get_visitor.check_out_time = datetime.now()
                get_visitor.save()
                send_visitor_details_email(
                    get_visitor.visitor_name,
                    get_visitor.host.host_name,
                    get_visitor.phone_number,
                    get_visitor.email_address,
                    get_visitor.check_in_time,
                    get_visitor.check_out_time,
                )
                send_visitor_details_sms(
                    get_visitor.visitor_name,
                    get_visitor.host.host_name,
                    get_visitor.phone_number,
                    get_visitor.email_address,
                    get_visitor.check_in_time,
                    get_visitor.check_out_time,
                )
                return HttpResponse(
                    f'{get_visitor.visitor_name} has successfully checked out on {get_visitor.check_out_time}',
                    status=200
                )
            else:
                return HttpResponse('Already checked out, register as another visitor')
    return render(request, 'summergeeks/checkout_form.html', {'form': checkout_form})
