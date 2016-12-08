# coding: utf-8

import json

from django.http import JsonResponse

from newspaper import Article, nlp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TwittableSentencesView(APIView):
    def get(self, request, format=None):
        return JsonResponse({"msg": "Wrong request"}, status=200)

    def post(self, request, format=None):
        data = json.loads(request.body.decode('utf-8'))
        url = data.get('url', None)
        if not url:
            return JsonResponse(
                {"msg": "No url provided"}, status=status.HTTP_400_BAD_REQUEST)

        twittable_sentences = get_twittable_sentences_from_url(url)
        return Response(json.dumps(twittable_sentences))


def get_twittable_sentences_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    best_sentences = nlp.summarize(title=article.title, text=article.text)
    return [s for s in best_sentences if len(s) < 140]
