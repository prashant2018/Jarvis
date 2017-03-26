from django.shortcuts import render
from django.shortcuts import redirect
from modules.youtube import youtube
from modules.song import play_song
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from TextProcessing import ProcessText as pt
from speak import tts
import signal
import os
from modules.news import news_fetch
from modules.weather import weather_fetch

process_stack = []


@csrf_exempt
def textProcessing(request):
    query = request.GET['query']
    id = pt.getCommandId(query)
    print "------------------------------" + str(id)
    if id==1:
        context = {'status' : True,
                   'val'    : 'Which one would you like to listen ?!',
                   'url'    : 'video/?name=',}
    elif id==2:
        return redirect('song')

    elif id == 3:
        return redirect('news')

    elif id == 6:
        return redirect('weather')

    elif id == 7:
        context = {'status': True,
                   'val': 'Hi, Have a good day.',
                   'url': 'home/?query=',}
    elif id == 8:
        context = {'status': True,
                   'val': 'A very good morning to you .',
                   'url': 'home/?query=',}
    elif id == 9:
        context = {'status': True,
                   'val': 'I am Jarvis. I was developed by Neural Mind team. I will try my best to serve you. ',
                   'url': 'home/?query=',}

    elif id==100:
        return redirect('exitProcess')

    else:
        context = {'status': True,
                   'val'   : 'I am still learning. Thankyou',
                   'url'   : 'home/?query=',}

    tts.main(context['val'])
    return JsonResponse(context)



@csrf_exempt
def weather(request):
    try:
        d = weather_fetch.main()
        temp = d['Temp']
        humid = d['Humidity']
        disc = d['Description']

        s = "Weather is "+disc+", temperature "+str(temp)+" degree , humidity "+str(humid)
        context = {'status': True,
                   'val': s,
                   'url': 'home/?query=',}
    except Exception as e:
        print e
        context = {'status': True,
                   'val': 'Sorry, Unable to fetch wether report',
                   'url': 'home/?query=',}

    tts.main(context['val'])
    return JsonResponse(context)

@csrf_exempt
def news(request):
    print "Fetching News"
    headlines = news_fetch.main()
    print headlines
    context = {'status': True,
               'val': 'Todays Headline. '+headlines,
               'url': 'home/?query='}

    tts.main(context['val'])
    return JsonResponse(context)


@csrf_exempt
def video(request):
    name = request.GET['name']
    status  = youtube.main(name)
    if status['pid']!=-1:
        process_stack.append(status['pid'])
        context = {'status': True,
                   'val': 'Started playing, Enjoy!',
                   'url': 'home/?query='}
    else:
        context = {'status': True,
                   'val': 'Something went wrong!',
                   'url': 'home/?query='}



    tts.main(context['val'])
    return JsonResponse(context)

@csrf_exempt
def song(request):
    statusJson = play_song.play()
    if statusJson['status'] == True:
        process_stack.append(statusJson['pid'])
        print '-------------------------'+str(statusJson['pid'])
        context = {'status': True,
                   'val': 'Enjoy Your Song!',
                   'url': 'home/?query='}
    else:
        context = {'status': False,
                   'val': 'Oh snap! Something went wrong',
                   'url': 'home/?query='}

    tts.main(context['val'])
    return JsonResponse(context)

@csrf_exempt
def exitProcess(request):
    print process_stack
    try:
        pid = process_stack[len(process_stack)-1]
        os.kill(pid,signal.SIGKILL)
        context = {'status': True,
                   'val': 'Sure. Closing it.',
                   'url': 'home/?query=',}
    except Exception as e:
        print e
        context = {'status': False,
                   'val': 'Unable to terminate',
                   'url': 'home/?query=',}

    return JsonResponse(context)