from django.urls import path


from .views import *

app_name = "jobs"
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('create-job/', CreateJobView.as_view(), name="create_job"),
    path('search-job/', SearchJobView.as_view(), name="search_job"),
    path('detail/<slug>/<int:pk>', SingleJobView.as_view(), name="job_detail"),
    path('category-detail/<slug>/<int:pk>', CategoryDetailView.as_view(), name="category_detail"),
]
