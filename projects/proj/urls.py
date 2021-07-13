from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomeView, name="home"),
    path("add_project/",views.AddProjView, name="add project"),
    path("delete_project/",views.DeleteProjView, name="delete project"),
    path("<int:proj_id>/",views.ProjView, name="project"),
    path("<int:proj_id>/add_chore/",views.AddChoreView, name="add chore"),
    path("<int:proj_id>/delete_chore/",views.DeleteChoreView, name="delete chore"),
    path("<int:proj_id>/done_chore/",views.DoneChoreView, name="done chore"),
]