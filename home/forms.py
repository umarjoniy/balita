from django import forms
from .models import Comments


class FormComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'website', 'message']

    def __init(self, *args, **kwargs):
        super(FormComment, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
