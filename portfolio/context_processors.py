from .models import SiteSettings, Profile, SocialLink

def site_settings(request):
    settings_obj = SiteSettings.objects.first()
    
    if not settings_obj:
        settings_obj = SiteSettings(
            show_skills=True,
            show_projects=True,
            show_experience=True,
            show_education=True
        )

    return {
        'site_settings': settings_obj,
        'profile_global': Profile.objects.first(),
        'social_links_global': SocialLink.objects.all(),
    }