from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from api.models import Note
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': 'api/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/api/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/api/notify/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates a new note with data sent in the post request'
        },
        {
            'Endpoint': '/api/notify/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates a note with data sent in the put request'
        },
        {
            'Endpoint': '/api/notify/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes a note'
        }
    ]

    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    try:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)
    except Note.DoesNotExist:
        return Response({'detail': 'Note does not exist'}, status=404)
    
@api_view(['PUT'])   
def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response('Note was deleted')


@api_view(['POST'])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        title=data['title'],
        content=data['content']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)