"""litreview_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
#from review import views
#from accounts import views


urlpatterns = [
	#path('accounts/', include('accounts.urls')),
	path('', include('accounts.urls')),
	path('', include('ticket.urls')),
	path('', include('review.urls')),
	#path(' ', views.index, name='index'),
	#path(' ', views.inscriptionPage, name='inscriptionPage'),
	#path('review/', include('review.urls')), # ajoute toutes les routes de review.urls aux routes du projet en les préfixant par review/.
	path('admin/', admin.site.urls),
]


if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),
	] + urlpatterns