from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.password_validation import validate_password

UserModel = get_user_model()


class MyHolidayUserCreationForm(auth_forms.UserCreationForm):
    user = None

    def clean_password2(self):
        password2 = super().clean_password2()
        validate_password(password2)
        return password2

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class MyHolidayUserChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
