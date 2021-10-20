django-blockchain
=================

Wrap the Blockchain API in Django.


Installation
------------

    pip install django-blockchain

Add app in your ``settings.py``

    INSTALLED_APPS = [
        "django_blockchain",
    ]

And something in your ``urls.py``

    urlpatterns = patterns('',
        url(r'^blockchain$', 'django_blockchain.urls', name='blockchain_urls'),
    )
