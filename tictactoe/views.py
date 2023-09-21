# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import  csrf_exempt

from .Board.tictactoe import Board_Game



new_game_dict = {}

def index(request):


    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits']= num_visits+1
    new_game_dict[str((num_visits+1)%100)] = Board_Game()

    context ={'user_id':str((num_visits+1)%100)}
    return render(request, 'tictactoe/index.html', context)




@csrf_exempt

def myajaxtestview(request):
    row = request.POST['row']
    col = request.POST['col']
    user_id = request.POST['user_id']
    new_game = new_game_dict[user_id]
    #new_game=request.session.get('board')
    new_game.x_play(int(row), int(col))
    return JsonResponse({'board':new_game.stringBoardArray(),'x_score':new_game.x_wins,
        'o_score':new_game.o_wins})
