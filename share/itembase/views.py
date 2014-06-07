from django.contrib.auth import authenticate, login, logout
from itembase.forms import LoginForm
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from models import Location, Membership, Items, ShareEvents


def login_page(request):
    data = {}
    template = 'itembase/login.djhtml'
    data['message'] = None
    if request.method == "POST":

        data['form'] = LoginForm(request.POST)
        if data['form'].is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username= username, password=password)
            if user is not None:
                login(request, user)
                message = "Your user is active now"
                return redirect('itembase/home')
            else:
                message = "Invalid username and /or password"
    else:
        data['form'] = LoginForm()

    return render(request, template ,data)


def logout_view(request):
    logout(request)
    return redirect('itembase/home')



def home(request):
    data = {}
    template = 'itembase/home.djhtml'
    return render(request, template, data)


@login_required
def locations(request):
    """
    Show the Locationlist
    """
    data = {}
    data['locations'] = Location.objects.all()
    template = 'itembase/locations.djhtml'
    return render(request, template, data)


@login_required
def location_detail(request, location_id):
    """
    Shows the Items for a Location and some Location Infos
    :param request:
    :param location_id:
    :return:
    """
    data = {}
    template = 'itembase/detail_location.djhtml'
    data['location'] = get_object_or_404(Location, pk=location_id)
    data['members'] = Membership.objects.filter(me_location = data['location'])

    return render(request, template, data)


@login_required
def membership(request, user_id):
    """
    Show the Users Memberships
    """
    data = {}
    data['memberships'] = Membership.objects.filter(me_user = user_id)
    template = 'itembase/membership.djhtml'
    return render(request, template, data)


@login_required
def user_items(request, user_id):
    """
    Show the users Items
    """
    data = {}
    data['items'] = Items.objects.filter(it_user = user_id)
    template = 'itembase/user_items.djhtml'
    return render(request, template, data)