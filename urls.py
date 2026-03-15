from django.contrib import admin
from django.urls import path
from onlinecourseapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # submit exam
    path('submit/', views.submit, name='submit'),

    # show exam result
    path('show_exam_result/', views.show_exam_result, name='show_exam_result'),
]