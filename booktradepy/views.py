from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

from changebook import Book, Message

def listBook(request):
    """
    List all books which is avaliable.
    """
    response['books'] = [ _.id for _ in Book.objects.all().filter(status=True) ]
    return JsonResponse(response)

def getBook(request, id=0):
    """
    Return detail information about specific book.
    """
    if id is not 0:
        try:
            book = Book.objects.get(id=id)
            return JsonResponse(book)
        except DoNotExist:
            return JsonResponse({"message":"do not exist"})
    return JsonResponse({"message":"invalid code"})

def sendMessage(request):
    if request.method == 'POST':
        if requests.user.is_authenticated():
            message = request.POST.get('message', 'null message')
            try:
                book_id = request.POST.get('book_id', 0)
                book = Book.objects.get(id=book_id)
            except:
                return JsonResponse({"message":"invalid book"})
            m = Message(receiver=book.owner, sender=request.user, message=message )
            m.save()
            return JsonResponse({"message":"success"})
        else:
            return JsonResponse("message":"user not login")

