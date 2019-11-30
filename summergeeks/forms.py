from django import forms

from summergeeks.models import HostEventDetail, VisitorDetail


class HostForm(forms.ModelForm):
    """
    Form for host details
    """

    class Meta:
        """
        Meta class for host form
        """

        model = HostEventDetail
        fields = '__all__'


class VisitorForm(forms.ModelForm):
    """
    Form for visitor details
    """

    class Meta:
        """
        Meta class for visitor form
        """

        model = VisitorDetail
        fields = ['host', 'visitor_name', 'phone_number', 'email_address']


class CheckoutForm(forms.ModelForm):
    """
    Form for checkout
    """

    class Meta:
        """
        Meta class for checkout form
        """

        model = VisitorDetail
        fields = ['host', 'phone_number']
