from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # Admin Auth
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/change-password/', views.admin_change_password, name='admin_change_password'),

    # Admin Dashboard & Profile
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/profile/', views.admin_profile, name='admin_profile'),
    path('admin-panel/settings/', views.admin_settings, name='admin_settings'),

    # Skills
    path('admin-panel/skills/', views.admin_skills, name='admin_skills'),
    path('admin-panel/skills/add/', views.admin_skill_add, name='admin_skill_add'),
    path('admin-panel/skills/<int:pk>/edit/', views.admin_skill_edit, name='admin_skill_edit'),
    path('admin-panel/skills/<int:pk>/delete/', views.admin_skill_delete, name='admin_skill_delete'),

    # Projects
    path('admin-panel/projects/', views.admin_projects, name='admin_projects'),
    path('admin-panel/projects/add/', views.admin_project_add, name='admin_project_add'),
    path('admin-panel/projects/<int:pk>/edit/', views.admin_project_edit, name='admin_project_edit'),
    path('admin-panel/projects/<int:pk>/delete/', views.admin_project_delete, name='admin_project_delete'),

    # Experience
    path('admin-panel/experiences/', views.admin_experiences, name='admin_experiences'),
    path('admin-panel/experiences/add/', views.admin_experience_add, name='admin_experience_add'),
    path('admin-panel/experiences/<int:pk>/edit/', views.admin_experience_edit, name='admin_experience_edit'),
    path('admin-panel/experiences/<int:pk>/delete/', views.admin_experience_delete, name='admin_experience_delete'),

    # Education
    path('admin-panel/educations/', views.admin_educations, name='admin_educations'),
    path('admin-panel/educations/add/', views.admin_education_add, name='admin_education_add'),
    path('admin-panel/educations/<int:pk>/edit/', views.admin_education_edit, name='admin_education_edit'),
    path('admin-panel/educations/<int:pk>/delete/', views.admin_education_delete, name='admin_education_delete'),

    # Social Links
    path('admin-panel/social-links/', views.admin_social_links, name='admin_social_links'),
    path('admin-panel/social-links/add/', views.admin_social_add, name='admin_social_add'),
    path('admin-panel/social-links/<int:pk>/edit/', views.admin_social_edit, name='admin_social_edit'),
    path('admin-panel/social-links/<int:pk>/delete/', views.admin_social_delete, name='admin_social_delete'),

    # Blog
    path('admin-panel/blogs/', views.admin_blogs, name='admin_blogs'),
    path('admin-panel/blogs/add/', views.admin_blog_add, name='admin_blog_add'),
    path('admin-panel/blogs/<int:pk>/edit/', views.admin_blog_edit, name='admin_blog_edit'),
    path('admin-panel/blogs/<int:pk>/delete/', views.admin_blog_delete, name='admin_blog_delete'),

    # Certifications
    path('admin-panel/certifications/', views.admin_certifications, name='admin_certifications'),
    path('admin-panel/certifications/add/', views.admin_certification_add, name='admin_certification_add'),
    path('admin-panel/certifications/<int:pk>/edit/', views.admin_certification_edit, name='admin_certification_edit'),
    path('admin-panel/certifications/<int:pk>/delete/', views.admin_certification_delete, name='admin_certification_delete'),

    # Messages
    path('admin-panel/messages/', views.admin_messages, name='admin_messages'),
    path('admin-panel/messages/<int:pk>/', views.admin_message_view, name='admin_message_view'),
    path('admin-panel/messages/<int:pk>/delete/', views.admin_message_delete, name='admin_message_delete'),
]