from django.urls import path
from django.views.generic import TemplateView
from hybrid_react.views import index

urlpatterns = [
    path("", index),
    path('react/', TemplateView.as_view(template_name="hybrid_react/spa-home.html")),
]
