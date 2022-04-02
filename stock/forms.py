from django import forms

from stock.models import UserPhone


class ProfileCreateForm(forms.ModelForm):

    class Meta:
        model = UserPhone
        fields = ['mobile', ]

