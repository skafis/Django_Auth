import random
import string
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
import haikunator
from .models import Room
from django.db import transaction
from django.utils.text import slugify

from django.db.models import Q

from profiles.models import Create_opportunity
# def view_rooms(request):
#     rooms = Room.objects.all()
#     context = {
#         "rooms": rooms,
#     }
#     return render(request, "all_rooms.html", context)

def view_rooms(request):	
    show_items = Create_opportunity.objects.filter(
		Q(user__exact=request.user.id)
		)
    context = {
        'show_items': show_items
    }
    return render(request, 'chat/browse.html', context)

def new_room(request, id=None):
    """
    create a new room(if does not exist), and redirect to it.
    """
    opportunity = get_object_or_404(Create_opportunity, id=id)
    new_room = None
    label = slugify(opportunity.title)
    print label
    while not new_room:
        with transaction.atomic():
            if Room.objects.filter(label=label).exists():
                continue
            else:
                new_room = Room.objects.create(label=label)
    return redirect('/chat/' + label, label=label)

def chat_room(request, label):
    if request.user.is_authenticated:
        """
        Room view - show the room, with latest messages.
        The template for this view has the WebSocket business to send and stream
        messages, so see the template for where the magic happens.
        """
        # If the room with the given label doesn't exist, automatically create it
        # upon first visit (a la etherpad).
        room, created = Room.objects.get_or_create(label=label)

        # We want to show the last 50 messages, ordered most-recent-last
        messages = reversed(room.messages.order_by('-timestamp')[:50])

        return render(request, "chat/room.html", {
            'room': room,
            'messages': messages,
        })
    else:
        return redirect("/")