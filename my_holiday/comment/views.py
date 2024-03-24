
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from my_holiday.comment.forms import CommentForm
from my_holiday.comment.models import Like, Comment
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



def like_logic(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    # Check if the user has already liked the place
    liked_place = Like.objects.filter(to_place_id=place_id, user=request.user).first()

    if liked_place:
        # If the user has already liked the place, remove the like
        liked_place.delete()
        action = 'unliked'
    else:
        # If the user hasn't liked the place yet, create a new like
        like = Like(to_place=place, user=request.user)
        like.save()
        action = 'liked'

    # Redirect back to the previous page with an anchor to the place
    return redirect(request.META['HTTP_REFERER'] + f'#{place_id}', action=action)
# def get_places_with_email():
#     # Retrieve all places from the database
#     places = Place.objects.all()
#
#     # Create a list to store place objects along with associated user emails
#     places_with_email = []
#
#     # Iterate over each place and fetch the associated user email
#     for place in places:
#         user_email = place.user.email if place.user else None
#         places_with_email.append({
#             'place': place,
#             'user_email': user_email
#         })
#
#     return places_with_email
#
# def show_comments_for_place(request, pk):
#     place = get_object_or_404(Place, pk=pk)
#     comments = Comment.objects.filter(to_place=place)
#
#     # Assuming you have logic to get places_with_email
#     # You might need to adjust this based on your actual implementation
#     places_with_email = get_places_with_email()
#
#     context = {
#         'place': place,
#         'comments': comments,
#         'places_with_email': places_with_email,
#     }
#
#     return render(request, 'destination/travelogue.html', context=context)






