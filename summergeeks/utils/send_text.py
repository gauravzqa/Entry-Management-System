from sendsms import api


def send_host_sms(visitor_name, check_in_time, phone_number, email_address):
    """
    :param visitor_name:
    :param check_in_time:
    :param phone_number:
    :param email_address:
    :return: mail sent to the visitor
    """

    api.send_sms(
        body=f"Host Event Details: "
             f"Event Name: {visitor_name}"
             f"Phone Number: {phone_number}"
             f"Email Address: {email_address}"
             f"Check in Time: {check_in_time}",
        from_phone='+41791111111',
        to=[phone_number],
    )


def send_visitor_details_sms(visitor_name, host_name, phone_number, email_address, check_in_time, check_out_time):
    """
    :param visitor_name:
    :param host_name:
    :param phone_number:
    :param email_address:
    :param check_in_time:
    :param check_out_time:
    :return: mail to visitor
    """

    api.send_sms(
        body=f"Host Event Details: "
             f"Visitor Name: {visitor_name}"
             f"Host Name: {host_name}"
             f"Phone Number: {phone_number}"
             f"Email Address: {email_address}"
             f"Check in time: {check_in_time}"
             f"Check out time: {check_out_time}",
        from_phone='+41791111111',
        to=[phone_number],
    )
