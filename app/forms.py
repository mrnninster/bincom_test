from django import forms
from .models import Party
from .models import PollingUnitsModel


class AddResultForm(forms.Form):
    CHOICES = list(Party.objects.all().values_list("partyid","partyname"))

    polling_unit_uniqueid = forms.IntegerField(
        label="Polling Unit Unique ID",
    )

    party_abbreviation = forms.ChoiceField(
        label="Party Abbreviation",
        choices=CHOICES,
    )

    party_score = forms.IntegerField(
        label="Party Score"
    )

    entered_by_user = forms.CharField(
        label="Agents Name"
    )


