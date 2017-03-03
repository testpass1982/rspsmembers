from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import RspsMember
from .forms import MemberForm
from django.shortcuts import redirect

# Create your views here.
def members_list(request):
    members = RspsMember.objects.order_by('created_date')
    return render(request, 'members/members_list.html', {'members': members})

def member_detail(request, pk):
    member = get_object_or_404(RspsMember, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.first_name = request.first_name
            member.last_name = request.last_name
            member.middle_name = request.middle_name
            member.created_date = timezone.now()
            member.save()
            return redirect('members.views.member_detail', pk=member.pk)
    else:
        form = MemberForm()
    return render(request, 'members/member_edit.html', {'form': form})
