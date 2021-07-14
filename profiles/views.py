from django.shortcuts import render


def profile(request):
    """ Display a users profile """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)