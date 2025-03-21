# chat/views.py
from django.shortcuts import render, redirect
from .models import Room
import uuid

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    mode = request.GET.get('mode', 'video')  # Default to video if mode is not provided
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'mode': mode,  # Pass the mode to the template
    })

def create_room(request):
    mode = request.GET.get('mode', 'video')  # Get the mode from the query parameter
    available_room = Room.objects.filter(user2__isnull=True).first()

    if available_room:
        # Add the current user to the room
        available_room.user2 = str(request.session.session_key)
        available_room.save()
        room_name = available_room.name
    else:
        # Create a new room
        room_name = str(uuid.uuid4())
        Room.objects.create(name=room_name, user1=str(request.session.session_key))

    return redirect(f'/chat/{room_name}/?mode={mode}')