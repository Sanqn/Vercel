from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import NewPersonViewsets, AllUsersViewsets, RegisterView, TagDetailView, ContactsUsersView, \
    DashboardUserView, NewQueryView, ContactsGoogleFacebook, UsersView, ContactsGoogleFacebookNew, \
    NewsAboutView, NewLoaderView, GetTokenFaceBook, ContactFaceBookViews, ContactGoogleViews, CalendarUserViews, \
    GetEventCalendarView, CalendarUserEventViews
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from . import views

router = routers.DefaultRouter()
router.register('person', NewPersonViewsets, basename='person')
router.register('allusers', AllUsersViewsets, basename='allusers')
router.register('contact', ContactsUsersView, basename='contact')
router.register('dashboarduser', DashboardUserView, basename='dashboarduser')
router.register('testfacebook', ContactsGoogleFacebook, basename='testfacebook')
router.register('news', NewsAboutView, basename='news')
router.register('newcontactfacebook', ContactFaceBookViews, basename='newcontactfacebook')
router.register('newcontactgoogle', ContactGoogleViews, basename='newcontactgoogle')
router.register('calendar', CalendarUserViews, basename='calendar')
router.register('event', CalendarUserEventViews, basename='event')
# router.register('testfacebooknew', ContactsGoogleFacebookNew, basename='testfacebooknew')


urlpatterns = [
                  path('', include(router.urls)),
                  path("contact/tags/<slug:tag_slug>/", TagDetailView.as_view()),
                  path('auth/', include('djoser.urls')),
                  path('auth/', include('djoser.urls.jwt')),
                  path('auth/', include('rest_framework.urls')),
                  path('', views.main, name='main'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
                  path('register/', RegisterView.as_view()),
                  path('test/', NewQueryView.as_view()),
                  path('gettokenfb/', GetTokenFaceBook.as_view()),
                  path('users_in_reg/', UsersView.as_view()),
                  path('check', views.check_bd, name='check_bd'),
                  path('news_loader', NewLoaderView.as_view(), name='news_loader'),
                  path('getcalendarevent', GetEventCalendarView.as_view(), name='getcalendarevent'),
                  path('testfacebooknew/', ContactsGoogleFacebookNew.as_view()),
                  path("ckeditor/", include('ckeditor_uploader.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ----------------------- django rest swagger ----------------------
schema_view2 = get_swagger_view(title='Pastebin API')

url_django_swagger = [
    path('swagger/', schema_view2),
]
# -------------------- end django rest swagger ----------------------

# urlpatterns += url_swagger
urlpatterns += url_django_swagger
