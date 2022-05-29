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

def login_user(request):
        if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
    if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect('index')
        else:
        messages.error(request, f'Invalid Username or password')
    else:
        messages.error(request, f'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {"login_form": form})

def logout_user(request):
    logout(request)
    messages.info(request, f'You have successfully logged out.')
    return redirect('index')

