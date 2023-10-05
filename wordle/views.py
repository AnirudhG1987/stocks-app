
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from wordle.worldesolver import wordlesolver

def index(request):
    return render(request, 'wordle/index.html')

@csrf_exempt
def next_guess(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        guess = body_data['guessString']
        #words_array = json.loads(body_data['wordsArray'])
        words_array = json.loads(body_data['wordsArray'])
        if len(words_array)>2:
            words_array = eval(words_array)
        #print(guess)
        #print(words_array)
        #print(len(words_array))
        colorsBox = body_data['colorsBox']
        #print(colorsBox)
        green_string=""
        yellow_string = ""
        grey_string = ""
        for i,c in enumerate(colorsBox):
            if c=="g":
                green_string+=str(i)+":"+guess[i]+","
            elif c=="y":
                yellow_string += guess[i] +":"+ str(i) + ","
            else:
                grey_string += guess[i]+","
        #print(green_string,grey_string,yellow_string)
        guess,  words_array = wordlesolver(words_array,green_string[:-1],yellow_string[:-1],grey_string[:-1])
        #print("output")
        #print(guess,words_array)
        #solution=solve_puzzle(data)
        #print(solution)
        status = "success"
        if guess is  None:
            status = "fail"
        response = {
            'status': status,
            'message': 'guess received',
            'next_guess': guess,
            'words':json.dumps(words_array.tolist())
        }
        return JsonResponse(response)


