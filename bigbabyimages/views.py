from django.shortcuts import render

# Create your views here.
@login_required(login_url='/login')
def index(request):
    images = Image.objects.all()
    # comments = image.comments.filter(active=True)
    # new_comment = None
    # if request.method == 'POST':
    #   comment_form = CommentForm(data=request.POST)
    #   if comment_form.is_valid():

    #     #Create Comment object but fail to save to the database yet
    #     new_comment = comment_form.save(commit=False)

    #     #Assign current post to comment
    #     new_comment.image = image

    #     #Save comment to database
    #     new_comment.save()
    #   else:
    #     comment_form = CommentForm
    return render(request, 'index.html', {"images":images})

def register_new_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration Successful.')
            return redirect('index')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    return render(request, 'registration/registration_form.html', {"registration_form": form} )

