from django.shortcuts import render
from django.utils import timezone
from .models import RspsMember

# Create your views here.
def members_list(request):
    members = RspsMember.objects.order_by('created_date')
    return render(request, 'members/members_list.html', {'members': members})