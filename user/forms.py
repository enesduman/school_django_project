from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import Account, UserTypes


class RegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields=['name','username','user_type','okul','sinif']

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')
        okul = cleaned_data.get('okul')
        classes = cleaned_data.get('sinif')
        if user_type == UserTypes.DIRECTOR and okul.accounts.filter(user_type=UserTypes.DIRECTOR).exists():
            msg = "Okula ait müdür bulunmaktadır."
            self.add_error('user_type', msg)
            self.add_error('okul', msg)

        elif user_type == UserTypes.TEACHER and okul.accounts.filter(user_type=UserTypes.TEACHER).count()>5:
            msg = "Okula ait 4 adet öğretmen bulunmaktadır."
            self.add_error('user_type', msg)
            self.add_error('okul', msg)

        elif user_type == UserTypes.TEACHER and classes.accounts.filter(user_type=UserTypes.TEACHER).count():
            msg = "Sınıfa ait 1 adet öğretmen bulunmaktadır."
            self.add_error('user_type', msg)
            self.add_error('sinif', msg)
        
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput,required=True)