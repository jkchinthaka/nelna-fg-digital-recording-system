from django.urls import path

from apps.recording import views

app_name = "recording"

urlpatterns = [
    path("recording/", views.recordable_task_list, name="task_list"),
    path(
        "recording/tasks/<uuid:task_id>/start/",
        views.start_recording,
        name="start_recording",
    ),
    path(
        "recording/<uuid:record_id>/",
        views.record_detail,
        name="record_detail",
    ),
]
