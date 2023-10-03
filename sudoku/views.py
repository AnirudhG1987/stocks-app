from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sudoku.pySudoku import solve_puzzle, generate_sudoku


@csrf_exempt
def solve_sudoku(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        data = body_data['data']

        # Your code to solve Sudoku goes here.
        # For now, just sending back the received data.
        #print(data)
        solution=solve_puzzle(data)
        #print(solution)
        response = {
            'status': 'success',
            'message': 'Sudoku received!',
            'data': solution
        }
        return JsonResponse(response)


@csrf_exempt
def sudoku_gen(request):
    if request.method == 'GET':
        puzzle=generate_sudoku()
        response = {
            'status': 'success',
            'message': 'Puzzle generated!',
            'data': puzzle
        }
        return JsonResponse(response)


def index(request):
    return render(request, 'sudoku/index.html')


