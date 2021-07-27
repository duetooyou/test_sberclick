from django.forms import ModelForm
from .models import Claim, Client


class ClaimCreateForm(ModelForm):
    class Meta:
        model = Claim
        fields = '__all__'


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
