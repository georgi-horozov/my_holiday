from django.shortcuts import render, redirect
from django.contrib import messages

from my_holiday.comment.forms import CommentForm
from my_holiday.destination.models import Place

def add_comment(request, pk):
    if request.method == "POST":
        place = Place.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_place = place
            comment.save()
            messages.success(request, "Comment added successfully.")  # Add success message
        else:
            messages.error(request, "Failed to add comment. Please check your input.")  # Add error message

        return redirect(request.META['HTTP_REFERER'] + f'#{pk}')
    else:
        return redirect('travelogue_view')  # Redirect to travelogue view if not a POST request

