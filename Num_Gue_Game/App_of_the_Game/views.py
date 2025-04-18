from django.shortcuts import render, redirect
import random



def Home(request):
    return render(request, 'App_of_the_Game/home.html')




def level(request):
    return render(request, 'App_of_the_Game/level.html')





def easy(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1,100)
        request.session['attempts'] = 10
    
    rand_num = request.session['rand_num']
    attempts = request.session['attempts']
    
    message = None
    win_message = None
    Low_message = None
    High_message = None
    Over_message = None

    if 'guessed_number' in request.GET:
        guess = request.GET.get('guessed_number')
        if guess is not None and guess.isdigit():
            guess = int(guess)
            if guess == rand_num:
                win_message = f"The Number Was {rand_num}."
                del request.session['rand_num']
                del request.session['attempts']
            
            elif guess < rand_num:
                attempts -= 1
                Low_message = f"📉 {guess} is Too Low!"
            
            elif guess > rand_num:
                attempts -= 1
                High_message = f"📈 {guess} is Too High!"
            request.session['attempts'] = attempts

    
    
    if attempts != 0:
        message = "Guess Again..."
    elif attempts == 0:
        Over_message = f"Game Over 🔚! The Number Was {rand_num}."
        del request.session['rand_num']
        del request.session['attempts']
    
    context = {
        "attempts": attempts,
        "Over_message": Over_message,
        "High_message": High_message,
        "Low_message": Low_message,
        "win_message": win_message,
        "message": message,
        "rand_num": rand_num
    }

    return render(request, 'App_of_the_Game/easy.html', context)











def hard(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1,100)
        request.session['attempts'] = 5
    

    rand_num = request.session['rand_num']
    attempts = request.session['attempts']
    
    message = None
    win_message = None
    Low_message = None
    High_message = None
    Over_message = None

    if 'guessed_number' in request.GET:
        guess = request.GET.get('guessed_number')
        if guess is not None and guess.isdigit():
            guess = int(guess)
            if guess == rand_num:
                win_message = f"The Number Was {rand_num}."
                del request.session['rand_num']
                del request.session['attempts']
            
            elif guess < rand_num:
                attempts -= 1
                Low_message = f"📉 {guess} is Too Low!"
            
            elif guess > rand_num:
                attempts -= 1
                High_message = f"📈 {guess} is Too High!"
            request.session['attempts'] = attempts

    
    
    if attempts != 0:
        message = "Guess Again..."
    elif attempts == 0:
        Over_message = f"Game Over 🔚! The Number Was {rand_num}."
        del request.session['rand_num']
        del request.session['attempts']
    
    context = {
        "attempts": attempts,
        "Over_message": Over_message,
        "High_message": High_message,
        "Low_message": Low_message,
        "win_message": win_message,
        "message": message,
        "rand_num": rand_num
    }

    return render(request, 'App_of_the_Game/hard.html', context)









def reset_game(request):
    if 'rand_num' in request.session:
        del request.session['rand_num']
    if 'attempts' in request.session:
        del request.session['attempts']
    return redirect('Level')