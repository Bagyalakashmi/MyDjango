from django import forms
from LMSApp.models import Register, Book
from django.utils import timezone


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ("Name", "Roll", "Dob", "Class", "Department", "Email", "Phone")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('Book_Name', 'Author', 'Volume', 'Update')


# class MembershipForm(forms.ModelForm):
#     class Meta:
#         model = Membership
#         fields = ('Member_Id', 'Membership_Date')
