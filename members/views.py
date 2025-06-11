from django.shortcuts import render
from .models import MembersModel, Category
from django.http import JsonResponse
from .forms import MemberForm, LoginForm
from django.http import HttpResponse 
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

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
    data = MembersModel.objects.all()  # Fetch all members from the database
    categories = Category.objects.all()  # Fetch all categories from the database
    # Handle search functionality
    query = request.GET.get('query', '')  # Get the search query from the request
    category_id = request.GET.get('category', 0)  # Get the category ID from the request
    sort_by = request.GET.get('sort_by', 'name_asc')  # Get the sort field from the request
    
    # Sort the data based on the selected sort field
    if sort_by == 'name_desc':
        data = data.order_by('-name')
    else:
        data = data.order_by('name')    
    # Filter members based on the category and query
    #     
    if category_id:
        # Filter members based on the selected category
        data = data.filter(category_id=category_id)
    if query:
        # Filter members based on the search query
        data = data.filter(
            Q(name__icontains=query) | Q(surname__icontains=query) | Q(id_number__icontains=query)
        )
    return render(request, 'members.html', 
                  {'form': form,
                   'members': data, 
                   'query': query, 
                   'categories': categories, 
                   'category_id': int(category_id), 
                   'sort_by': sort_by})  

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
