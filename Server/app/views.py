from django.shortcuts import render
from django.shortcuts import redirect
from modules.youtube import youtube
from modules.song import play_song
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from TextProcessing import ProcessText as pt
import os
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
        context = {'status': True,
                   'val': 'Which one would you like to listen ?!',
                   'url': 'song/?name=',}

        return redirect('song')

    elif id==100:
        return redirect('exitProcess')
    else:
        context = {'status': True,
                   'val'   : 'I am not that smart! Still learning :-)',
                   'url'   : 'home/?query=',}

    return JsonResponse(context)


@csrf_exempt
def video(request):
    name = request.GET['name']
    status  = youtube.main(name)
    if status['pid']!=-1:
        process_stack.append(status['pid'])

    context = {'status' :True,
               'val'    :'Started playing, Enjoy!',
               'url'    :'home/?query='}
    return JsonResponse(context)

@csrf_exempt
def song(request):
    statusJson = play_song.play()
    if statusJson['status'] == True:
        process_stack.append(statusJson['pid'])
        context = {'status': True,
                   'val': 'Enjoy Your Song!',
                   'url': 'home/?query='}
    else:
        context = {'status': False,
                   'val': 'Oh snap! Something went wrong',
                   'url': 'home/?query='}

    return JsonResponse(context)

@csrf_exempt
def exitProcess(request):
    try:
        pid = process_stack[len(process_stack)-1]
        os.system(pid.kill)
        context = {'status': True,
                   'val': 'Yo killed the process!',
                   'url': 'home/?query=',}
    except:
        context = {'status': False,
                   'val': 'Unable to terminate',
                   'url': 'home/?query=',}
    return context