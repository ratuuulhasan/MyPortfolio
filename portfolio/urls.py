from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),

    # Admin auth
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),

    # Admin dashboard
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/profile/', views.admin_profile, name='admin_profile'),

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

    # Messages
    path('admin-panel/messages/', views.admin_messages, name='admin_messages'),
    path('admin-panel/messages/<int:pk>/', views.admin_message_view, name='admin_message_view'),
    path('admin-panel/messages/<int:pk>/delete/', views.admin_message_delete, name='admin_message_delete'),

    # Settings
    path('admin-panel/settings/', views.admin_settings, name='admin_settings'),
]