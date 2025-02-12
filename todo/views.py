from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos , many = True)
    return Response(serializer.data)


@api_view(['POST' , 'GET'])
def todo_create(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@api_view(['GET'])
def todo_detail(request , pk):
    todos = Todo.objects.get(id = pk)
    serializer = TodoSerializer(todos , many = False)
    return Response(serializer.data)


@api_view(['POST'])
def todo_update(request,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance = todos , data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def todo_delete(request, pk):
    todos = Todo.objects.get(id=pk)
    todos.delete()
    return Response()

