from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/',views.registerpage, name="register"),
    path('login/', views.login_page, name='login'),
path('addpersons/', views.admin_add_persons, name='addpersons'),
    path('uploadcsv_file/',views.upload_csv_file,name='uploadcsv_file'),
    path('show_file_list/',views.show_all_files_list,name='show_file_list'),
path('view_contact_list/',views.show_view_contact_list,name='view_contact_list')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)