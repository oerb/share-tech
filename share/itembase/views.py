from django.contrib.auth import authenticate, login, logout
from itembase.forms import LoginForm, ItemForm, UserForm, LocationForm
from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from models import Location, Membership, Items, ShareEvents
from django.contrib.auth.models import User


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
def membership(request, location_id):
    """
    Show the Users Memberships
    """
    data = {}
    data['memberships'] = Membership.objects.filter(me_location = location_id)
    template = 'itembase/membership.djhtml'
    return render(request, template, data)


@login_required
def user_membership(request):
    """
    Show the Users Memberships
    """
    data = {}
    data['memberships'] = Membership.objects.filter(me_user=request.user.id)
    print data['memberships']
    template = 'itembase/user_membership.djhtml'
    return render(request, template, data)


@login_required
def user_items(request):
    """
    Show the users Items
    """
    data = {}
    data['items'] = Items.objects.filter(it_owner = request.user)
    template = 'itembase/user_items.djhtml'
    return render(request, template, data)


@login_required
def item_events(request, item_id):
    """
    Show the Item events
    """
    data = {}
    template = 'itembase/item_events.djhtml'
    data['events'] = ShareEvents.objects.filter(se_item = item_id)
    data['item'] = get_object_or_404(Items, pk=item_id)
    return render(request, template, data)



def new_user(request):
    """
    New User
    """
    data = {}
    template = 'itembase/new_user.djhtml'
    message = None
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['user_password'] == form.cleaned_data['user_password2']:
                user = User(username=form.cleaned_data['user_name'],
                            email=form.cleaned_data['user_email'],
                            password=form.cleaned_data['user_password'])
                user.save()
                return redirect('itembase/home')
            else:
                return redirect('itembase/home') # TODO: use next for Redirect
    else:
        data['form'] = UserForm()
    return render(request, template, data)


def new_item(request):
    """
    New item
    """
    data = {}
    template = 'itembase/simpleform.djhtml'
    data['message'] = None
    data['headstring']='New Item'
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = Items(it_name=form.cleaned_data['it_name'],
                         it_info=form.cleaned_data['it_info'],
                         it_storageinfo=form.cleaned_data['it_storageinfo'],
                         it_back_to_owner=form.cleaned_data['it_back_to_owner'],
                         it_personal_handover=form.cleaned_data['it_personal_handover'],
                         it_owner=request.user,
                         )
            item.save()
            return redirect('itembase/home')
        return redirect('itembase/home')
    else:
        data['form'] = ItemForm()
    return render(request, template, data)

def new_location(request):
    """
    New Location
    """
    data = {}
    template = 'itembase/simpleform.djhtml'
    data['message'] = None
    data['headstring'] = 'New Location'
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            location = Location(lc_name=form.cleaned_data['lc_name'],
                                lc_geo=form.cleaned_data['lc_geo'],
                                lc_adr=form.cleaned_data['lc_adr'],
                                lc_city=form.cleaned_data['lc_city'],
                                lc_www=form.cleaned_data['lc_www'],
                                lc_mail=form.cleaned_data['lc_mail'],
                                lc_info=form.cleaned_data['lc_info'],
                                )
            location.save()
            print(location)
            membership = Membership(me_user = request.user,
                                    me_location = location,
                                    me_trust1 = request.user,
                                    me_trust2 = request.user,
            )
            membership.save()
            print membership
            return redirect('itembase/home')
        return redirect('itembase/home')
    else:
        data['form'] = LocationForm()
    return render(request, template, data)


@login_required
def join_location(request, location_id):
    """
    Join a Location
    """
    data = {}
    location = get_object_or_404(Location, pk=location_id)
    membership = Membership(me_user = request.user,
                            me_location = location,
    )
    membership.save()
    print membership
    return redirect('itembase/home')