from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Thanks
from .forms import forms
from django.template import loader
import datetime



def thanksgivings(request):
	#Load completed and current as separate lists
	thanks_list = Thanks.objects.all().order_by('thanks_date')
	template = loader.get_template('thanksgivings.html')
	context = {
		'thanks_list' : thanks_list,
	}
	return HttpResponse(template.render(context,request))

def thanksgiving(request):
	if request.method == 'GET':
		form = forms.Thanksgiving()
		context = {
			'form': form,
			'reqGet': True
		}
		template = loader.get_template('thanksgiving.html')
	elif request.method == 'POST':
		form = forms.Thanksgiving(request.POST)
		if form.is_valid():
			tgd = datetime.datetime.now()
			tgt = form.cleaned_data['thanks_title']
			tgde = form.cleaned_data['thanks_description']
			tc = '1'
			try:
				t = Thanks(thanks_title=tgt,thanks_date=tgd,thanks_description=tgde,thanks_count=tc)
				t.save()
				return redirect('/thanksgivings/')
			except Exception as e:
				template = loader.get_template('error.html')
				context = {
					'error' : str(e)
				}
		else:
			context = {		
				'error' : 'Form Validation Error',
			}
			template = loader.get_template('error.html')
	else:
		template = loader.get_template('error.html')
		context = {
			'error' : '501 Invalid Request Protocol',
		}
	return HttpResponse(template.render(context,request))

def thanks(request,thanks_id):
	#View an individual prayer to pray for it
	if request.method == 'GET':
		try:
			thanks = Thanks.objects.get(pk=thanks_id)
			template = loader.get_template('thanks.html')
			context = {
				'thanks' : thanks
			}
		except Exception as e:
			template = loader.get_template('error.html')
			context = {
				'error' : str(e)
			}
	else:
		context = {
			'error' : '501 Invalid Request Protocol'
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def givethanks(request, thanks_id):
	if request.method == 'GET':
		try:
			thanks = Thanks.objects.get(pk=thanks_id)
			form = forms.GiveThanks()
			template = loader.get_template('givethanks.html')
			context = {
				'thanks_id' : thanks_id,
				'thanks_title' : thanks.thanks_title,
				'thanks_description' : thanks.thanks_description,
				'thanks_count' : thanks.givethanks_count
			}
		except Exception:
			context = {
				'error' : str(Exception)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))

def increasethanks(request, thanks_id, givethanks_count):
	if request.method == 'POST':
		try:
			thanks = Thanks.objects.get(pk=thanks_id)
			#potentially reference other fields in prayer object to populate the rest of the form
			#increment prayer count
			count = givethanks_count
			count = count + 1
			thanks.givethanks_count = count
			thanks.save()
			return redirect('/thanksgivings/')
		except Exception as e:
			context = {
				'error' : str(e)
			}
			template = loader.get_template('error.html')
	else:
		context = {
			'error' : '501 Invalid Request Protocol' #protocol error
		}
		template = loader.get_template('error.html')
	return HttpResponse(template.render(context,request))
