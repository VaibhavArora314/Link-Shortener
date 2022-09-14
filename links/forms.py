from django import forms
from django.core.validators import MinLengthValidator
from .models import Link

def tag_validator(value):
    if Link.objects.filter(tag = value).exists():
        return forms.ValidationError('Link with this tag already exists')


class CreateLinkform(forms.ModelForm):
    original_link= forms.URLField(widget= forms.URLInput(attrs ={'class':'form-control'}))
    tag = forms.CharField(validators=[tag_validator,MinLengthValidator(2,'Tag should have min length 2')], widget=forms.TextInput(attrs ={'class':'form-control'}))

    class Meta:
        model = Link
        fields = ('original_link','tag')


    