Elokenz Twote App
=================

This should exists in two versions. A standalone one and an integrated one inside elokenz.


Install
-------

Create your virtualenv with python3.
Python dev:
`sudo apt-get install python-dev`

lxml requirements:
`sudo apt-get install libxml2-dev libxslt-dev`

For PIL to recognize .jpg images:
`sudo apt-get install libjpeg-dev zlib1g-dev libpng12-dev`

`pip install -r requirements.txt`


Download NLP related corpora:
`curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3`




- for nltk libraries:
```
sudo python -m nltk.downloader -d /usr/local/share/nltk_data all.
```

- In your `INSTALLED_APPS`, add:

```python
    'modeltranslation',  # translation within models
    ...
    'elokenz_twote',
```

`modeltranslation` should be placed on top of the installed apps.

There is an automatic check which makes sure all of these apps are in INSTALLED_APPS.

- Add url(r'^', include('elokenz_twote.urls')) in your urls.py


TEST
----

Run tests with the following command:
`pytest`

To create a new db while running tests: `pytest --create-db`
The default behavior reuse the same db for performance reasons
