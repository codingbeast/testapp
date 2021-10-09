from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views import View

class hello(View):
    def get(self, request):
    	return HttpResponse("Hello world")
