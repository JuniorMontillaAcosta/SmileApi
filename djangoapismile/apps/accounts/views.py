from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfModel
# Create your views here.
class UserProfileView(ListView, LoginRequiredMixin):
	template_name = 'accounts/profile.html'
	model = UserProfModel
	filds = [
			'id',
			'username_prof',
			'prof'
		]

	def doctor_function(self, request, *args, **kwargs):
		if get_object_or_404(UserProfModel, pk=request.user.id)  == 'doctor':
			ctx = {'msgdoctor': 'Prueba doctor'}
			return render(request, 'accounts/doctor.html', ctx)
	def father_function(self, request, *args, **kwargs):
		if get_object_or_404(UserProfModel, pk=request.user.id)  == 'fathers':
			ctx = {'msgfathers': ' Prueba fathers'}
			return render(request, 'accounts/father.html', ctx)
	def teacher_function(self, request, *args, **kwargs):
		if get_object_or_404(UserProfModel, pk=request.user.id)  == 'teachers':
			ctx = {'msgteachers': 'Prueba teachers'}
			return render(request, 'accounts/teacher.html', ctx)