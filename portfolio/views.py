from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages as msg
from .models import *
from .forms import *


# ==================== PUBLIC VIEWS ====================
def home(request):
    context = {
        'profile': Profile.objects.first(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all()[:6],
        'recent_posts': Blog.objects.filter(is_published=True)[:3],
    }
    return render(request, 'public/home.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'public/project_detail.html', {'project': project})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            admin = User.objects.filter(is_superuser=True).first()
            if admin:
                obj.user = admin
                obj.save()
                msg.success(request, 'Your message has been sent!')
                return redirect('contact')
            msg.error(request, 'Admin not configured yet.')
    else:
        form = ContactForm()
    return render(request, 'public/contact.html', {'form': form})


# ==================== AUTH ====================
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        msg.error(request, 'Invalid credentials or not authorized.')
    return render(request, 'admin_panel/login.html')


@login_required
def admin_logout(request):
    logout(request)
    return redirect('admin_login')


# ==================== DASHBOARD ====================
@login_required
def admin_dashboard(request):
    context = {
        'total_skills': Skill.objects.count(),
        'total_projects': Project.objects.count(),
        'total_blogs': Blog.objects.count(),
        'total_certifications': Certification.objects.count(),
        'total_messages': Message.objects.count(),
        'unread_messages': Message.objects.filter(is_read=False).count(),
        'recent_messages': Message.objects.all()[:5],
    }
    return render(request, 'admin_panel/dashboard.html', context)


# ==================== GENERIC CRUD HELPERS ====================
def _generic_form(request, FormClass, instance=None, redirect_to='admin_dashboard',
                  file_upload=False, action='Add'):
    if request.method == 'POST':
        form = FormClass(request.POST,
                         request.FILES if file_upload else None,
                         instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            if instance is None:      # creating new
                obj.user = request.user
            obj.save()
            msg.success(request, f'{action}ed successfully!')
            return redirect(redirect_to)
    else:
        form = FormClass(instance=instance)
    return form


# ==================== PROFILE ====================
@login_required
def admin_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            msg.success(request, 'Profile updated!')
            return redirect('admin_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'admin_panel/profile.html', {'form': form})


# ==================== SKILLS ====================
@login_required
def admin_skills(request):
    return render(request, 'admin_panel/skills.html',
                  {'skills': Skill.objects.all()})


@login_required
def admin_skill_add(request):
    form = _generic_form(request, SkillForm, redirect_to='admin_skills', action='Add')
    if hasattr(form, 'is_valid'):   # still rendering form
        return render(request, 'admin_panel/skill_form.html',
                      {'form': form, 'action': 'Add Skill'})
    return form


@login_required
def admin_skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    form = _generic_form(request, SkillForm, instance=skill,
                         redirect_to='admin_skills', action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/skill_form.html',
                      {'form': form, 'action': 'Edit Skill'})
    return form


@login_required
def admin_skill_delete(request, pk):
    get_object_or_404(Skill, pk=pk).delete()
    msg.success(request, 'Skill deleted!')
    return redirect('admin_skills')


# ==================== PROJECTS ====================
@login_required
def admin_projects(request):
    return render(request, 'admin_panel/projects.html',
                  {'projects': Project.objects.all()})


@login_required
def admin_project_add(request):
    form = _generic_form(request, ProjectForm, redirect_to='admin_projects',
                         file_upload=True, action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/project_form.html',
                      {'form': form, 'action': 'Add Project'})
    return form


@login_required
def admin_project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = _generic_form(request, ProjectForm, instance=project,
                         redirect_to='admin_projects', file_upload=True, action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/project_form.html',
                      {'form': form, 'action': 'Edit Project'})
    return form


@login_required
def admin_project_delete(request, pk):
    get_object_or_404(Project, pk=pk).delete()
    msg.success(request, 'Project deleted!')
    return redirect('admin_projects')


# ==================== EXPERIENCE ====================
@login_required
def admin_experiences(request):
    return render(request, 'admin_panel/experiences.html',
                  {'experiences': Experience.objects.all()})


@login_required
def admin_experience_add(request):
    form = _generic_form(request, ExperienceForm,
                         redirect_to='admin_experiences', action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/experience_form.html',
                      {'form': form, 'action': 'Add Experience'})
    return form


@login_required
def admin_experience_edit(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    form = _generic_form(request, ExperienceForm, instance=exp,
                         redirect_to='admin_experiences', action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/experience_form.html',
                      {'form': form, 'action': 'Edit Experience'})
    return form


@login_required
def admin_experience_delete(request, pk):
    get_object_or_404(Experience, pk=pk).delete()
    msg.success(request, 'Experience deleted!')
    return redirect('admin_experiences')


# ==================== EDUCATION ====================
@login_required
def admin_educations(request):
    return render(request, 'admin_panel/educations.html',
                  {'educations': Education.objects.all()})


@login_required
def admin_education_add(request):
    form = _generic_form(request, EducationForm,
                         redirect_to='admin_educations', action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/education_form.html',
                      {'form': form, 'action': 'Add Education'})
    return form


@login_required
def admin_education_edit(request, pk):
    edu = get_object_or_404(Education, pk=pk)
    form = _generic_form(request, EducationForm, instance=edu,
                         redirect_to='admin_educations', action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/education_form.html',
                      {'form': form, 'action': 'Edit Education'})
    return form


@login_required
def admin_education_delete(request, pk):
    get_object_or_404(Education, pk=pk).delete()
    msg.success(request, 'Education deleted!')
    return redirect('admin_educations')


# ==================== SOCIAL LINKS ====================
@login_required
def admin_social_links(request):
    return render(request, 'admin_panel/social_links.html',
                  {'links': SocialLink.objects.all()})


@login_required
def admin_social_add(request):
    form = _generic_form(request, SocialLinkForm,
                         redirect_to='admin_social_links', action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/social_form.html',
                      {'form': form, 'action': 'Add Social Link'})
    return form


@login_required
def admin_social_edit(request, pk):
    link = get_object_or_404(SocialLink, pk=pk)
    form = _generic_form(request, SocialLinkForm, instance=link,
                         redirect_to='admin_social_links', action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/social_form.html',
                      {'form': form, 'action': 'Edit Social Link'})
    return form


@login_required
def admin_social_delete(request, pk):
    get_object_or_404(SocialLink, pk=pk).delete()
    msg.success(request, 'Social link deleted!')
    return redirect('admin_social_links')


# ==================== MESSAGES ====================
@login_required
def admin_messages(request):
    return render(request, 'admin_panel/messages.html',
                  {'messages_list': Message.objects.all()})


@login_required
def admin_message_view(request, pk):
    m = get_object_or_404(Message, pk=pk)
    if not m.is_read:
        m.is_read = True
        m.save()
    return render(request, 'admin_panel/message_view.html', {'message': m})


@login_required
def admin_message_delete(request, pk):
    get_object_or_404(Message, pk=pk).delete()
    msg.success(request, 'Message deleted!')
    return redirect('admin_messages')


# ==================== SETTINGS ====================
@login_required
def admin_settings(request):
    obj, _ = SiteSettings.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            msg.success(request, 'Settings updated!')
            return redirect('admin_settings')
    else:
        form = SiteSettingsForm(instance=obj)
    return render(request, 'admin_panel/settings.html', {'form': form})

# ==================== PUBLIC BLOG ====================
def blog_list(request):
    posts = Blog.objects.filter(is_published=True)
    return render(request, 'public/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, is_published=True)
    related = Blog.objects.filter(is_published=True).exclude(pk=post.pk)[:3]
    return render(request, 'public/blog_detail.html',
                  {'post': post, 'related': related})


# ==================== ADMIN: BLOG ====================
@login_required
def admin_blogs(request):
    return render(request, 'admin_panel/blogs.html',
                  {'blogs': Blog.objects.all()})


@login_required
def admin_blog_add(request):
    form = _generic_form(request, BlogForm, redirect_to='admin_blogs',
                         file_upload=True, action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/blog_form.html',
                      {'form': form, 'action': 'Add Blog Post'})
    return form


@login_required
def admin_blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = _generic_form(request, BlogForm, instance=blog,
                         redirect_to='admin_blogs', file_upload=True, action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/blog_form.html',
                      {'form': form, 'action': 'Edit Blog Post'})
    return form


@login_required
def admin_blog_delete(request, pk):
    get_object_or_404(Blog, pk=pk).delete()
    msg.success(request, 'Blog post deleted!')
    return redirect('admin_blogs')


# ==================== ADMIN: CERTIFICATION ====================
@login_required
def admin_certifications(request):
    return render(request, 'admin_panel/certifications.html',
                  {'certifications': Certification.objects.all()})


@login_required
def admin_certification_add(request):
    form = _generic_form(request, CertificationForm,
                         redirect_to='admin_certifications',
                         file_upload=True, action='Add')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/certification_form.html',
                      {'form': form, 'action': 'Add Certification'})
    return form


@login_required
def admin_certification_edit(request, pk):
    cert = get_object_or_404(Certification, pk=pk)
    form = _generic_form(request, CertificationForm, instance=cert,
                         redirect_to='admin_certifications',
                         file_upload=True, action='Edit')
    if hasattr(form, 'is_valid'):
        return render(request, 'admin_panel/certification_form.html',
                      {'form': form, 'action': 'Edit Certification'})
    return form


@login_required
def admin_certification_delete(request, pk):
    get_object_or_404(Certification, pk=pk).delete()
    msg.success(request, 'Certification deleted!')
    return redirect('admin_certifications')