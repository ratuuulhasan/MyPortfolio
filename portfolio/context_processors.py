from .models import SiteSettings, Profile, SocialLink

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'profile_global': Profile.objects.first(),
        'social_links_global': SocialLink.objects.all(),
    }