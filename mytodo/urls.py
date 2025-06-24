from django.urls import path
from mytodo import views as mytodo
from mytodo.views import UpdateView
from mytodo.views import DeleteView

urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"),
    path("update_task_complete/", mytodo.Update_task_complete.as_view(), name="update_task_complete"),
    path("update/<int:pk>/", UpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete"),
]
