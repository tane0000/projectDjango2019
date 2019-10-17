from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Trouble
from .models import Product, Bruser, Brmachine
from .models import Acceptedmethod, Actioncategory, Suspendcategory, Disposalcategory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name',)
        widgets = {'name': forms.TextInput(),}

class BruserForm(forms.ModelForm):
    class Meta:
        model = Bruser
        fields = (
            'product_name',
            'name',
        )
        widgets = {
            'product_name': forms.Select(),
            'name': forms.TextInput(),
        }

class BrmachineForm(forms.ModelForm):
    class Meta:
        model = Brmachine
        fields = ('name',)
        widgets = {'name': forms.TextInput(),}

class TroubleForm(forms.ModelForm):
#            'restoration_datetime': forms.DateTimeInput(attrs={"type":"datetime"}),
    class Meta:
        model = Trouble
        fields = (
#            'product_name',
            'user_name',
            'staff_name',
            'accepted_method',
            'occurrence_datetime',
            'restoration_datetime',
            'action_category',
            'suspend_category',
            'trouble_machine',
            'trouble_location',
            'error_code',
            'error_name',
            'trouble_name',
            'situation',
            'cause',
            'measure',
            'restoration_procedure',
            'special_note',
            'complete_date',
            'disposal_category',
            'field_worker',
            'office_worker',
            'first_contact',
            'first_contact_datetime',
            'input_date',
            'inputter',
        )
        widgets = {
#            'product_name': forms.Select(),
            'user_name': forms.Select(),
            'staff_name': forms.TextInput(),
            'accepted_method': forms.Select(),
            'occurrence_datetime': forms.DateTimeInput(attrs={"type":"datetime"}),
            'restoration_datetime': forms.DateTimeInput(attrs={"type":"datetime"}),
            'action_category': forms.Select(),
            'suspend_category': forms.Select(),
            'trouble_machine': forms.Select(),
            'trouble_location': forms.TextInput(attrs={'placeholder':'記入例：1号機1列1連1段前'}),
            'error_code': forms.TextInput(),
            'error_name': forms.TextInput(),
            'trouble_name': forms.TextInput(),
            'situation': forms.Textarea(attrs={'rows':4}),
            'cause': forms.Textarea(attrs={'rows':4}),
            'measure': forms.Textarea(attrs={'rows':4}),
            'restoration_procedure': forms.Textarea(attrs={'rows':4}),
            'special_note': forms.Textarea(attrs={'rows':4}),
            'complete_date': forms.DateInput(attrs={"type":"date"}),
            'disposal_category': forms.Select(),
            'field_worker': forms.TextInput(),
            'office_worker': forms.TextInput(),
            'first_contact': forms.TextInput(),
            'first_contact_datetime': forms.DateTimeInput(attrs={"type":"datetime"}),
#            'first_contact_date': forms.DateInput(attrs={"type":"date"}),
#            'first_contact_time': forms.TimeInput(attrs={"type":"time"}),
            'input_date': forms.DateInput(attrs={"type":"date"}),
            'inputter': forms.TextInput(),
        }

class CSVUploadForm(forms.Form):
    file = forms.FileField(label='CSVファイル', help_text='※拡張子csvのファイルをアップロードしてください。')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.name.endswith('.csv'):
            return file
        else:
            raise forms.ValidationError('拡張子がcsvのファイルをアップロードしてください')

class AcceptedmethodForm(forms.ModelForm):
    class Meta:
        model = Acceptedmethod
        fields = ('method',)
        widgets = {'method': forms.TextInput(),}

class ActioncategoryForm(forms.ModelForm):
    class Meta:
        model = Actioncategory
        fields = ('category',)
        widgets = {'category': forms.TextInput(),}

class SuspendcategoryForm(forms.ModelForm):
    class Meta:
        model = Suspendcategory
        fields = ('category',)
        widgets = {'category': forms.TextInput(),}

class DisposalcategoryForm(forms.ModelForm):
    class Meta:
        model = Suspendcategory
        fields = ('category',)
        widgets = {'category': forms.TextInput(),}
