from django import forms

from core.models import UserProfile, Project, Participation
from core.choices import ROLE


class ProjectUsernameForm(forms.Form):
    title = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Project name'}))
    username = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username__exact=username).exists():
            raise forms.ValidationError(
                "This username is occupied, please enter a different name")
        else:
            return self.cleaned_data['username']

    def save(self):
        username = self.cleaned_data['username']
        project_title = self.cleaned_data['title']
        password = UserProfile.objects.make_random_password(length=10)
        user = UserProfile.objects.create_user(username=username,
            password=password)
        user.temporary_password = password
        user.save()
        project = Project.objects.create(title=project_title)
        Participation.objects.create(user=user, project=project, role=ROLE.OWNER)
        return (project, user)


class UsernameForm(forms.Form):
    username = forms.CharField(max_length=255, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username__exact=username).exists():
            raise forms.ValidationError(
                "This username is occupied, please enter a different name")
        else:
            return self.cleaned_data['username']

    def save(self):
        username = self.cleaned_data['username']
        password = UserProfile.objects.make_random_password(length=10)
        user = UserProfile.objects.create_user(username=username,
            password=password)
        user.temporary_password = password
        user.save()
        return user
