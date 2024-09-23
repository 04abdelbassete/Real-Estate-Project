from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserAccountForm(UserCreationForm):
    
    class Meta:
        model = User
        exclude = ('is_active', 'is_staff',)

    def __init__(self, *args, **kwargs):
        super().__init__(self,*args, **kwargs)
        self.fields['is_realtor'].widget.attrs.update({'label':'Are you a realtor?'})
