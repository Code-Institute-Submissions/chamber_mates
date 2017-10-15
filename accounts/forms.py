from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.gis import forms
from mapwidgets.widgets import GooglePointFieldWidget
from .models import Profile, UserInstrument

class UserRegistrationForm(UserCreationForm):
    """
    We make just one tiny alteration to the Django default User Creation Form: we make the e-mail
    field required
    """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    """
    The form for a user to fill out their basic profile information (location,
    and maximum distance they are willing to travel)
    """
    
    # make the max_distance ForeignKey field have no "blank" option in the form:
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["max_distance"].empty_label = None
        self.fields["max_distance"].widget.choices = self.fields["max_distance"].choices

    class Meta:
        model = Profile
        fields = ["location", "max_distance"]
        widgets = {"location": GooglePointFieldWidget,
                   "max_distance": forms.RadioSelect}


class UserInstrumentForm(forms.ModelForm):
    """
    This form allows a user to select an instrument that they play, their rough
    standard on it - and what other instruments they are looking fo form a group with,
    and what standard they require the other players to be at.

    Copies of this form will be inserted into the profile form, with buttons the user
    can click to add or remove instruments
    """
    def __init__(self, *args, **kwargs):
        super(UserInstrumentForm, self).__init__(*args, **kwargs)
        fields = ["instrument", "standard", "desired_instruments", "accepted_standards"]
        for field in fields:
            self.fields[field].empty_label = None
            self.fields[field].widget.choices = self.fields[field].choices


    class Meta:
        model = UserInstrument
        fields = ["instrument", "standard", "desired_instruments", "accepted_standards"]
        widgets = {"instrument": forms.RadioSelect, "standard": forms.RadioSelect,
                   "desired_instruments": forms.CheckboxSelectMultiple,
                   "accepted_standards": forms.CheckboxSelectMultiple}
