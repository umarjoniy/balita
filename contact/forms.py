from django.forms import ModelForm
from .models import Contact


class FormContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super(FormContact, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'