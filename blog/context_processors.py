from profiles.models import Profile


def extras(request):
    profile = Profile.objects.all()

    return {'profile': profile}
