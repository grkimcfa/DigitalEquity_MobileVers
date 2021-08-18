from django.shortcuts import render, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist

# Grace User Authentication
from django.contrib.auth.backends import ModelBackend, UserModel
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.hashers import check_password

from .models import User

def authenticate(username=None, password=None):
    User = get_user_model()
    try: #to allow authentication through phone number or any other field, modify the below statement
        user = User.objects.get(email=username)
        print(user)
        print(password)
        print(user.password)
        print(user.check_password(password))
        if user.check_password(password):
            return user 
        return None
    except User.DoesNotExist:
        return None

def get_user(self, user_id):
    try:
        return UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return None

def files_to_string(file_list):
    list_string = ""
    counter = 0

    # Get File_List into easy to read list to print out in template
    for key, value in file_list.items():
        # only add things to the list_string if its true
        if value == True:
            # Also add commas based on counter
            if counter == 1:
                list_string += ", "
                counter = 0
            else:
                counter = 1
            list_string += key
    if list_string == "":
        list_string = "1040 Form"
    #TODO 10/24 Incorporate ID card here somewhere...
    #list_string ="ID Card"
    return list_string

# redirect user to whatever page they need to go to every time by checking which steps they've
# completed in the application process
def what_page(user):
    if user.is_authenticated:
        try:
            value = user.addresses
        except AttributeError:
            return "application:address"

        try:
            value = user.eligibility
        except AttributeError:
            return "application:finances"
        
        try:
            value = user.programs
        except AttributeError or ObjectDoesNotExist:
            return "application:programs"
        
        try:
            value = user.forms
        except AttributeError:
            return "dashboard:files"
        
        return "dashboard:index"

    else:
        return "application:account"
