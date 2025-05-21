from django.shortcuts import render
from .models import MembersModel
from django.http import JsonResponse
from .forms import MemberForm, LoginForm
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def homepage(request):
    form = LoginForm()
    try:
        if request.user.is_authenticated:
            return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'home.html', {'form': form})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}")


def members_list(request):
    form = MemberForm()
    members = MembersModel.objects.all()
    return render(request, 'members.html',  {'form': form, 'members': members})

# Function to handle the form submission
# and save the data to the database
@csrf_protect
def add_member(request):
    # Check if the request method is POST
    # and process the form data
    try:
        if request.method == 'POST':
            form = MemberForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'errors': form.errors})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
    # If the request method is not POST, return an error
    # response
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
