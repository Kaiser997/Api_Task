from django.urls import path

from api_task.views import PersonListAPIView
from api_task.views import TaskListAPIView
from api_task.views import TaskUpdateDestroyAPIView
from api_task.views import PersonUpdateDestroyAPIView
from api_task.views import PersonCountAPIView
from api_task.views import PersonsNameAPIView

urlpatterns =[
    path("personcreatelist/", PersonListAPIView.as_view(), name = "personcreatelist"),
    path("personupdate/<int:pk>", PersonUpdateDestroyAPIView.as_view(), name = "personupdatedestroy"),
    path("taskcreatelist/", TaskListAPIView.as_view(), name = "taskcreatelist"),
    path("taskupdatedestroy/<int:pk>", TaskUpdateDestroyAPIView.as_view(), name="taskupdatedestroy"),
    path("persons/task-count/", PersonCountAPIView.as_view(), name = "personscounttask"),
    path("persons/names/", PersonsNameAPIView.as_view(), name = "personsname")
    
]