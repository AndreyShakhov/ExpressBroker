from django import forms
from .models import *

class AddDecl(forms.Form):
    decl_company_name = forms.ModelChoiceField(queryset=Firm.objects.all())
    decl_number = forms.IntegerField()
    decl_tipe = forms.ModelChoiceField(queryset=Decl_type.objects.all())#models.ForeignKey('Decl_type', on_delete=models.PROTECT, null=True)
    decl_code_quantity = forms.IntegerField()
    decl_car_number = forms.CharField(max_length=100, required=False)
    decl_car_quantity = forms.IntegerField(required=False)
    decl_comment = forms.CharField(required=False)
    decl_status = forms.ModelChoiceField(queryset=Decl_status.objects.all())


