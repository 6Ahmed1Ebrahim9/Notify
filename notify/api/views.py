from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


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

    return JsonResponse(routes, safe=False)