from django.shortcuts import redirect, render
from .models import Store
from .forms import StoreForm
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

def store_list(request):
	stores = Store.objects.all()
	return render(request, 'stores/store_list.html', {'stores':stores})

def store_detail(request, pk):
	try:
		store = Store.objects.get(pk=pk)
	except Store.DoesNotExist:
		raise Http404
	return render(request, 'stores/store_detail.html', {'store':store})

def store_create(request):
	if request.method == 'POST':
		form = StoreForm(request.POST, submit_title='create')
		if form.is_valid():
			store = form.save(commit=False)
			if request.user.is_authenticated():
				store.owner = request.user
			store.save()
			# return redirect(store.get_absolute_url())
			return HttpResponseRedirect('/store')
	else:
		form = StoreForm(submit_title="create")
	return render(request, 'stores/store_create.html', {'form':form})

def store_update(request, pk):
	try:
		store = Store.objects.get(pk=pk)
	except:
		raise Http404
	if request.method =='POST':
		form = StoreForm(request.POST, instance=store, submit_title='update')
		if form.is_valid():
			store = form.save()
			return redirect(store.get_absolute_url())
	else:
		form = StoreForm(instance=store, submit_title='update')
	return render(request, 'stores/store_update.html', {'form':form, 'store':store})

@login_required
@require_http_methods(['POST'])
def store_delete(request, pk):
	try:
		store = Store.objects.get(pk=pk)
	except Store.DoesNotExist:
		raise Http404
	if store.can_user_delete(request.user):
		store.delete()
		return redirect('store_list')
	return HttpResponseForbidden()

