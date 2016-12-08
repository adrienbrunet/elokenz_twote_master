# coding: utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        r'^get_tweetable_sentences/$',
        views.TwittableSentencesView.as_view(),
        name='get_tweetable_sentences'
    ),
]
