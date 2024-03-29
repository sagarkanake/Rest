# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


from rest_framework.generics import RetrieveUpdateDestroyAPIView,  RetrieveDestroyAPIView, RetrieveUpdateAPIView , ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView


class StudentList(ListAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer
      
class StudentCreate(CreateAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer
      
class StudentRetrieve(RetrieveAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer   

class StudentUpdate(UpdateAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer
           
class StudentDestroy(DestroyAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer   
              
class StudentListCreate(ListCreateAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer 
           
class RetrieveUpdateAPIView(RetrieveUpdateAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer  
                     
class StudentRetrieveDestroy(RetrieveDestroyAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
           queryset = Student.objects.all()
           serializer_class = StudentSerializer


# # List and Create - PK Not Required
# class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
#  queryset = Student.objects.all()
#  serializer_class = StudentSerializer

#  def get(self, request, *args, **kwargs):
#   return self.list(request, *args, **kwargs)

#  def post(self, request, *args, **kwargs):
#   return self.create(request, *args, **kwargs)

# # Retrieve Update and Destroy - PK Required
# class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#  queryset = Student.objects.all()
#  serializer_class = StudentSerializer

#  def get(self, request, *args, **kwargs):
#   return self.retrieve(request, *args, **kwargs)

#  def put(self, request, *args, **kwargs):
#   return self.update(request, *args, **kwargs)

#  def delete(self, request, *args, **kwargs):
#   return self.destroy(request, *args, **kwargs)