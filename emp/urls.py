from django.contrib import admin
from django.urls import path
from emp import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.registration,name="registration"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout,name="logout"),
    path('empdetail/',views.empdetail,name="empdetail"),
    path('employdata/',views.empdata,name="employdata"),
     path('employdata1/<id>',views.empdata1,name="employdata1"),

    path('deletemployee/<id>/',views.deletemployee,name="delete-mployee"),
    # path('search/',views.search,name='search'),
    path('update/<id>/',views.update,name='update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)