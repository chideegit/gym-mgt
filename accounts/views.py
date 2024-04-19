from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse

User = get_user_model()

# Only admins can do this
def register_user(request):
    pass 