from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Record

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Email Address')})
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('First Name')})
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': _('Last Name')})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = _('User Name')
        self.fields['username'].label = ''
        self.fields['username'].help_text = _(
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = _('Password')
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = _(
            '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = _('Confirm Password')
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = _(
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('First Name'), "class":"form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('Last Name'), "class":"form-control"}),
        label=""
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('Email'), "class":"form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('Phone'), "class":"form-control"}),
        label=""
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('Address'), "class":"form-control"}),
        label=""
    )
    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('City'), "class":"form-control"}),
        label=""
    )
    state = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('State'), "class":"form-control"}),
        label=""
    )
    zipcode = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _('Zipcode'), "class":"form-control"}),
        label=""
    )

    class Meta:
        model = Record
        exclude = ("user",)