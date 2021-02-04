from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from account.forms import AccountUpdateForm
from account.models import SampleModel


def hello(request):
    if request.method == "POST":
        temp = request.POST.get('helloworldinput')
        new_model = SampleModel()
        new_model.text = temp
        new_model.save()

        return HttpResponseRedirect(reverse('account:hello'))
    else:
        hello_world_list = SampleModel.objects.all()
        return render(request, 'accountapp/helloword.html', context={'hello_world_list':hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('account:hello')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('account:login')
    template_name = 'accountapp/delete.html'