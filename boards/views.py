from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board
def home(request): #shfaqja e te dhenave nga databasa, tabela Board
    boards = Board.objects.all()
    boards_names = list()

    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
	
def home1(request): #i shfaqim ne HTML file home te gjitha objektet e tabeles Boards
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
	
	
def home2(request): #i shfaqim ne HTML file home te gjitha objektet e tabeles Boards
    boards = Board.objects.all()
    return render(request, 'home2.html', {'boards': boards})
	
def home3(request): #i shfaqim ne HTML file home te gjitha objektet e tabeles Boards
    boards = Board.objects.all()
    return render(request, 'home3.html', {'boards': boards})