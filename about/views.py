from django.shortcuts import render


def about(request):
    """ Display the About Us page """

    template = 'about/about.html'
    context = {}

    return render(request, template, context)