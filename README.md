# BojJobs Job board with Django


This project is created by Django and django from CWS youtube channel. And this is an enhaced version of the project. I have code it from scratch.


Continue the course at:
https://www.youtube.com/watch?v=C8pYT1R8yo4&list=PLpyspNLjzwBkV1Lo2CSKLFtzG3PUNTG8q&index=8

- Video 8 min  18:25 / 24:27



Notes:

meaing of the double underscore on userprofile.views.vie_application view:


@CodeWithStein
2 years ago
The double underscore means that you're using a field on a foreignkey.
The first one:
application = get_object_or_404(ApllayJob,pk=application_id,job__created_by = request.user)
Here you are getting an object (ApllayJob where the ID/Primary key is the application_id and that the job is created by the authenticated user. 

The second one:
application = get_object_or_404(ApllayJob,pk=application_id,created_by = request.user)
Here you are getting an object (ApllayJob where the ID/Primary key is the application_id and  the application is created by the authenticated user.