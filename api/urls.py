from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

router = DefaultRouter()
router.register('profile', views.ProfileViewSet)
router.register('site-settings', views.SiteSettingsViewSet)
router.register('skills', views.SkillViewSet)
router.register('projects', views.ProjectViewSet)
router.register('experience', views.ExperienceViewSet)
router.register('education', views.EducationViewSet)
router.register('social-links', views.SocialLinkViewSet)
router.register('messages', views.MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]