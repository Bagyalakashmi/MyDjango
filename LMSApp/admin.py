from django.contrib import admin
from LMSApp.models import Register, Book


class RegisterAdmin(admin.ModelAdmin):
    list = ['Id', "Name", "Roll", "Dob", "Class", "Department", "Email", "Phone", "Created", 'is_member']


class BookRegister(admin.ModelAdmin):
    list = ['Book_Name', 'Author', 'Volume', 'Update']


# class MembershipAdmin(admin.ModelAdmin):
#     list = ["Member_Id", "Membership_Date"]


# Register your models here.
admin.site.register(Register, RegisterAdmin)
admin.site.register(Book, BookRegister)
# admin.site.register(Membership, MembershipAdmin)
