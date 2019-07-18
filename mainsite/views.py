from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Board
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    #게시판 만들기 위해서는 
    #제목, 사용자, 내용, 컨텐츠
    return render(request, 'mainsite/index.html')

def newBoard(request):
    content ={}
    try:
        if request.method == 'POST':
            title = request.POST.get('title')
            userName = request.POST.get('userName')
            contents = request.POST.get('contents')
            image= request.FILES['image']

            board = Board(
                title = title,
                userName = userName,
                contents = contents,
                image= image
            )
            board.save()
            content ={'board':board}
        else: #일반 새로고침은 get 방식이라서 중복을 제거 할 수 있음
            errMsg='잘못된 접근입니다.'
    except:
        errMsg = 'server error'
        content={'errMsg':errMg}
    return redirect(reverse('listBoard'))
    #새로 고침을 했을때 계속 정보가 같이 넘어가 버렸음 
    #redirect 데이터 없이 다시 그 경로로 보내버림 

def listBoard(request):
    content ={}
    try:
        boards = Board.objects.all()
        paginator = Paginator(boards, 5)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        
        content={'boards':boards, 'posts':posts}
    except:
        errMsg = 'server error'
        content={'errMsg':errMg}

    return render(request, 'mainsite/boardList.html',content)

def viewBoard(request,id):
    content ={}
    try:
        board = Board.objects.get(id = id)
        board.lookup += 1
        board.save()
        content = {'board':board}
    except:
        errMsg = 'server error'
        content={'errMsg':errMg}
    return render(request, 'mainsite/boardView.html',content)

def updateDelete(request, id):
    content = {}
    if request.POST.get('updateordelete'):
        board = Board.objects.get(id = id)

        title = request.POST.get('title')
        userName = request.POST.get('userName')
        contents = request.POST.get('contents')

        board.title = title
        board.userName = userName
        board.contents = contents
        board.save()

        content = {'board': board}
        return render(request, 'mainsite/boardView.html', content)
    
    else:
        board = Board.objects.get(id = id)
        board.delete()

        return redirect('listBoard')

def updatepage(request, id):
    board = Board.objects.get(id = id)
    content = {'board':board}
    return render(request, 'mainsite/update.html', content)