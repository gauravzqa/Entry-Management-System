from django.db import models


class HostEventDetail(models.Model):
    """
    Model to store host details
    """

    event_name = models.CharField(
        max_length=127,
    )

    host_name = models.CharField(
        max_length=127,
    )

    host_address = models.CharField(
        max_length=127,
        blank=False,
        null=False,
    )

    phone_number = models.CharField(
        max_length=15,
        unique=False,
        blank=True,
        null=True,
    )

    email_address = models.EmailField(
        unique=False,
        blank=True,
        null=True,
    )

    class Meta:
        """
        Meta class for host details
        """

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f'{self.event_name} organised by {self.host_name}'


class VisitorDetail(models.Model):
    """
    Model to store visitor details
    """

    host = models.ForeignKey(
        to='HostEventDetail',
        on_delete=models.CASCADE,
    )

    visitor_name = models.CharField(
        max_length=127,
    )

    phone_number = models.CharField(
        max_length=15,
        unique=False,
        blank=True,
        null=True,
    )

    email_address = models.EmailField(
        unique=False,
        blank=True,
        null=True,
    )

    check_in_time = models.DateTimeField(
        null=False,
        blank=False,
    )

    check_out_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        """
        Meta class for visitor details
        """

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        return f'{self.visitor_name} invited by {self.host}'
