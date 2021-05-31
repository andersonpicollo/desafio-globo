"""desafio URL Configuration

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
from desafio.planner.api.views.planner import PlannerView, PlannerViewDetail
from desafio.planner.api.views.planner_task import TaskPlannerViewDetail, TaskPlannerView
from rest_framework.authtoken.views import obtain_auth_token
from desafio.planner.api.views.client_registry import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('planner', PlannerView.as_view(), name="planner"),
    path('planner/<int:pk>', PlannerViewDetail.as_view()),
    path('task', TaskPlannerView.as_view(), name="task"),
    path('task/<int:pk>', TaskPlannerViewDetail.as_view()),
    path('token', obtain_auth_token, name='token'),
    path('register', RegisterView.as_view(), name='register')
]
