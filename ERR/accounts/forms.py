from django import forms
from django.utils.translation import gettext_lazy
from .models import ReviewLaptop
from django.contrib.auth.models import User

class ReviewLaptopForm(forms.ModelForm):
    class Meta:
        model = ReviewLaptop
        fields = ['rate','comment']
        labels = {
            'comment': gettext_lazy('Review'),
            'rate':gettext_lazy('Rate')
        }
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 40, 'rows': 7}),
        }

class  UserSignUpForm(forms.Form):
    
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def clean_content(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Password doesn't match")
        return username, email, password

    def saveUser(self): 
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = User.objects.create_user(username = username, email = email, password = password)
        user_group = user.save()
        # group_main = Group.objects.get(name="client")
        # user_group.groups.add(group_main)
<<<<<<< HEAD
        return user
=======
        return user
>>>>>>> ERR/master
