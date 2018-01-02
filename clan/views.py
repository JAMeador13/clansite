from django.shortcuts import  render
from django.shortcuts import render_to_response
from django.template import RequestContext
import requests


def index(request):
    return render(request, 'clan/index.html')


def multi_stream(request, s1=None, s2=None, s3=None, s4=None):
    context = {
        'streamers': {
            'FNB': ['afirstnamebasis', '', False, '', ''],
            'K4RL': ['DR_K4RL', '', False, 'https://cdn.discordapp.com/attachments/350285037519765504/352488342010462209/unknown.png', 'height:22px'],
            'Cephas': ['Cephas___', '', False, '', ''],
            'jam': ['thejamtime', '', False, 'https://cdn.discordapp.com/attachments/350285037519765504/352502390831710219/C--fakepath-jam_2.png', 'height:22px'],
            'Feen': ['Feendog29', '', False, '', ''],
            'GrandmasSugar': ['GrandmasSugar', '', False, '', ''],
            'pedro': ['pedr0theli0n', '', False, '', ''],
            'Jmoe': ['Jmoe80', '', False, 'https://cdn.discordapp.com/attachments/352475028056440833/352475381351055372/image.jpg', 'height:22px'],
            'Xeno': ['The_Xenocide', '', False, '', ''],
            'Metriq': ['Metriq', '', False, '', ''],
            'Strykr': ['strykr009', '', False, '', ''],
            'Merf': ['merfmi', '', False, '', ''],
            'GDub': ['GDub5307', '', False, 'https://cdn.discordapp.com/attachments/339282207673679872/353806151483129856/Wallpaper.png', 'height:22px'],
            'scorcho': ['ellscorcho', '', False, 'https://cdn.discordapp.com/attachments/332916773315805184/390994654927126549/S-Logo.png', 'height:22px'],
            },
        'current_view': [[s1, False, ''], [s2, False, ''], [s3, False, ''], [s4, False, '']]
        }

    HEADERS = {'Client-ID': 'xlmo2mau29ow7fp73kayj751eftrhh', 'Accept': 'application/vnd.twitchtv.v5+json'}
    payload = {'login': ''}

    for item in range(len(context['current_view'])):
        try:
            context['current_view'][item][1] = context['streamers'][context['current_view'][item][0]][2]
            context['current_view'][item][2] = context['streamers'][context['current_view'][item][0]][0]
        except KeyError:
            continue

    for k, v in context['streamers'].items():
        payload['login'] += v[0]+','
    else:
        payload['login'] = payload['login'][:-1]

    r = requests.get('https://api.twitch.tv/kraken/users', headers=HEADERS, params=payload)
    req = r.json()

    for i in req['users']:
        for key, value in context['streamers'].items():
            if i['display_name'] == value[0]:
                value[1] = i['_id']

    payload = {'channel': ''}

    for k, v in context['streamers'].items():
        payload['channel'] = v[1]
        r = requests.get('https://api.twitch.tv/kraken/streams/', headers=HEADERS, params=payload)
        req = r.json()

        if req['streams'] != []:
            v[2] = True

    return render(request, 'clan/multistream.html', context)



def streams(request, streamer):
    context = {
        'streamers': {
            'FNB': ['afirstnamebasis', '', False, '', ''],
            'K4RL': ['DR_K4RL', '', False, 'https://cdn.discordapp.com/attachments/350285037519765504/352488342010462209/unknown.png', 'height:22px'],
            'Cephas': ['Cephas___', '', False, '', ''],
            'jam': ['thejamtime', '', False, 'https://cdn.discordapp.com/attachments/350285037519765504/352502390831710219/C--fakepath-jam_2.png', 'height:22px'],
            'Feen': ['Feendog29', '', False, '', ''],
            'GrandmasSugar': ['GrandmasSugar', '', False, '', ''],
            'pedro': ['pedr0theli0n', '', False, '', ''],
            'Jmoe': ['Jmoe80', '', False, 'https://cdn.discordapp.com/attachments/352475028056440833/352475381351055372/image.jpg', 'height:22px'],
            'Xeno': ['The_Xenocide', '', False, '', ''],
            'Metriq': ['Metriq', '', False, '', ''],
            'Strykr': ['strykr009', '', False, '', ''],
            'Merf': ['merfmi', '', False, '', ''],
            'GDub': ['GDub5307', '', False, 'https://cdn.discordapp.com/attachments/339282207673679872/353806151483129856/Wallpaper.png', 'height:22px'],
            'scorcho': ['ellscorcho', '', False, 'https://cdn.discordapp.com/attachments/332916773315805184/390994654927126549/S-Logo.png', 'height:22px']
            },
        'streamer': streamer
        }

    HEADERS = {'Client-ID': 'xlmo2mau29ow7fp73kayj751eftrhh', 'Accept': 'application/vnd.twitchtv.v5+json'}
    payload = {'login': ''}

    for k, v in context['streamers'].items():
        if k == streamer:
            context['username'] = v[0]
        payload['login'] += v[0]+','
    else:
        payload['login'] = payload['login'][:-1]

    r = requests.get('https://api.twitch.tv/kraken/users', headers=HEADERS, params=payload)
    req = r.json()

    for i in req['users']:
        for key, value in context['streamers'].items():
            if i['display_name'] == value[0]:
                value[1] = i['_id']

    payload = {'channel': ''}

    for k, v in context['streamers'].items():
        payload['channel'] = v[1]
        r = requests.get('https://api.twitch.tv/kraken/streams/', headers=HEADERS, params=payload)
        req = r.json()

        if req['streams'] != []:
            v[2] = True

    return render(request, 'clan/streams.html', context)


def league(request, num=None):
    context = {
        'season': num,
        'seasonOps': [1]
        }
    return render(request, 'clan/league.html', context)


def season(request, num, tab=None):
    context = {}

    if tab == None:
        return render(request, 'clan/season.html', context)

    elif tab == 'teams':
        return render(request, 'clan/teams.html', context)

    elif tab == 'record':
        return render(request, 'clan/record.html', context)

    elif tab == 'schedule':
        return render(request, 'clan/schedule.html', context)

    elif tab == 'compare':
        return render(request, 'clan/compare.html', context)


def stats(request):
    return render(request, 'clan/stats.html')


def about(request):
    return render(request, 'clan/about.html')


def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response