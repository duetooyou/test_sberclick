from django.forms import ModelForm
from .models import Claim


class ClaimCreateForm(ModelForm):
    class Meta:
        model = Claim
        fields = ('name', 'category')
