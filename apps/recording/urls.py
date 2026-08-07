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
    path(
        "recording/<uuid:record_id>/submit/",
        views.submit_confirm,
        name="submit_confirm",
    ),
    path(
        "recording/<uuid:record_id>/submitted/",
        views.record_submitted,
        name="record_submitted",
    ),
]
