from django.contrib import admin
from .models import (Profile, SiteSettings, Skill, Project, Experience,
                     Education, SocialLink, Message, Blog, Certification)

admin.site.register([Profile, SiteSettings, Skill, Project,
                     Experience, Education, SocialLink, Message,
                     Blog, Certification])