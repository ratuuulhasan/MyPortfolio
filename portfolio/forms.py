from django import forms
from .models import (Profile, SiteSettings, Skill, Project,
                     Experience, Education, SocialLink, Message,
                     Blog, Certification, Comment)

class BootstrapMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            w = field.widget
            if isinstance(w, forms.CheckboxInput):
                w.attrs.setdefault('class', 'form-check-input')
            elif isinstance(w, forms.Select):
                w.attrs.setdefault('class', 'form-select')
            else:
                w.attrs.setdefault('class', 'form-control')

class ProfileForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'title', 'short_bio', 'bio', 'profile_image',
                  'email', 'phone', 'location', 'cv']
        widgets = {'bio': forms.Textarea(attrs={'rows': 4})}

class SiteSettingsForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['site_title', 'meta_description', 'logo', 'favicon',
                  'theme_color', 'show_skills', 'show_projects',
                  'show_experience', 'show_education']
        widgets = {
            'meta_description': forms.Textarea(attrs={'rows': 3}),
            'theme_color': forms.TextInput(attrs={'type': 'color'}),
        }

class SkillForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category', 'level', 'icon', 'order']

class ProjectForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'tech_stack',
                  'live_url', 'github_url', 'featured', 'order']
        widgets = {'description': forms.Textarea(attrs={'rows': 4})}

class ExperienceForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'role', 'start_date', 'end_date', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EducationForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institute', 'degree', 'year', 'description']
        widgets = {'description': forms.Textarea(attrs={'rows': 4})}

class SocialLinkForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url', 'icon', 'order']

class ContactForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
        widgets = {'message': forms.Textarea(attrs={'rows': 5})}

class BlogForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'excerpt', 'content', 'cover_image',
                  'tags', 'is_published']
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 14}),
        }

class CertificationForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['title', 'issuer', 'issue_date', 'expiry_date',
                  'image', 'credential_url', 'credential_id', 'order']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CommentForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment...'}),
        }