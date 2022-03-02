"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from book.views import homepage,show_all_books,edit_data   # in  this case we dont need to write views.pagename
## OR
from book import views      # call each page as views.pagename
# from book.views import book_list
urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name="homepage"),
    # path('book_list/',book_list)
    path('show-all-books/',views.show_all_books, name="show_all_books"),
    path('edit/<int:id>/', views.edit_data, name="edit"),
    path('delete/<int:id>/', views.delete_data, name="delete"),
    path('show-book-bootstrap/',views.show_book_bootstrap, name="show_book_bootstrap"),
    path('login/',views.login,name="login"),
    path('delete-all-books/',views.delete_all_books,name="delete_all_books"),
    path('soft_delete/<int:id>/', views.soft_delete, name="soft_delete"),
    path('soft_delete_all/',views.soft_delete_all,name="soft_delete_all"),
    path('soft_delete_pg/',views.soft_delete_pg,name="soft_delete_pg"),
]
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
"""