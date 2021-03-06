import random
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .forms import TweetFrom
from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    form = TweetFrom(request.POST or None)
    if form.is_valid():
        obj = form.save(commt=False)
        # do other form related logic
        obj.save()
        form = TweetFrom()
    return render(request, 'components/form.html', context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    """ REST API VIEW
        consume by Javascripts or Swift/Java/IOS/Andriod
        return json data
    """
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content,
                   "likes": random.randint(0, 100)} for x in qs]
    data = {
        "isUser": False,
        "response": tweet_list,
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """ REST API VIEW
        consume by Javascripts or Swift/Java/IOS/Andriod
        return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    # json.dumps content_type='application/json';
    return JsonResponse(data, status=status)
