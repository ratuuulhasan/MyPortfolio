from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('portfolio.urls')),
]

# ডেভেলপমেন্টের সময় (লোকালহোস্টে) মিডিয়া ফাইল সার্ভ করার জন্য
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # স্ট্যাটিক ফাইলের জন্য আলাদা লাইন দেওয়ার দরকার নেই, django.contrib.staticfiles এটি হ্যান্ডেল করে