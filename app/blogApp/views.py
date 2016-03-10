from django.contrib.auth import authenticate, login as auth_login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from app.blogApp.serializers import LoginSerializer
from .models import Post, Comment


# Create your views here.

def index(request):
    post_list = Post.objects.all()
    return render(request,'blogApp/index.html',{
        'post_list':post_list,
        'error_message':"No posts there",
    })


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogApp/post.html', {
        'post': post,
        'request': request,
        'error_message': "You didn't select a choice.",
    })


def comment(request, pk):
    new_comment = Comment(comment_user=request.POST['user'], comment_content=request.POST['content'],
                          comment_date=timezone.now(), post_id=pk)
    new_comment.save();
    return HttpResponseRedirect(reverse('blogApp:post', args=(pk,)))


class JSONResponse(object):
    pass


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    if request.method == 'POST':
        # data = JSONParser().parse(request)
        pwd=request.data.get('pwd', None)
        usr=request.data.get('usr', None)
        account=authenticate(username=usr, password=pwd)
        if account is not None:
            auth_login(request, account)
            serialized = LoginSerializer(account)
            print 'credentials found'
            return Response(serialized.data, status=status.HTTP_200_OK)
            # return Response({'token':serialized.data,'request':request}, status=status.HTTP_200_OK)
        else:
            print 'credentials are not found'
            return Response({
                    'status': 'Unauthorized',
                    'message': 'Username/password combination invalid.'
                }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def delete_comment(request):
    if request.method == 'POST':
        comment_id=request.data.get('comment_id',None)
        Comment.objects.filter(id=comment_id).delete()
        print comment_id
        return HttpResponse('Successful')
    else:
        return HttpResponse('Not successful')