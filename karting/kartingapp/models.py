from django.db import models

# Create your models here.
class Name(models.Model):
    mdl_name = models.CharField(max_length=264, unique=False)

    def __str__(self):
        return self.mdl_name


class Email(models.Model):
    mdl_email = models.EmailField(max_length=264, unique=True)


    def __str__(self):
        return self.mdl_email


class Contact(models.Model):
    mdl_contact = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.mdl_contact)


class Message(models.Model):
    mdl_message = models.TextField(max_length=300, unique=False)

    def __str__(self):
        return str(self.mdl_message)

# class Search(models.Model):
#     mdl_search = models.CharField(max_length=300)

#     def __str__(self):
#         return str(self.mdl_search)

global Search
Search = ''