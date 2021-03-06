Quick Start
===========

Nap has two methods of use, you can use the: Serialisers/Publisher or the
DataMapper/Views combinations.

DataMapper/Views Quick Start
----------------------------

1. Create a DataMapper for your Model in mappers.py

.. code-block:: python

    from nap import datamapper
    from myapp.models import MyModel

    class MyModelMapper(datamapper.ModelDataMapper):
        class Meta:
            model = MyModel
            exclude = ['user',]

2. Create some views in rest_views.py

.. code-block:: python

    from nap.rest import views

    class MyModelListView(views.ListPostMixin,
                           views.BaseListView):
        pass


    class MyModelObjectView(views.ObjectGetMixin,
                            views.BaseObjectView):
        pass

3. Add your APIs to your URLs:

.. code-block:: python

    urlpatterns = [
        url(r'^mymodel/$',
            MyModelListView.as_view(),
            name='mymodel-list'),

        url(r'^mymodel/(?P<pk>\d+)/$',
            MyModelObjectView.as_view(),
            name='mymodel-detail'),
    ]



Serialiser/Publisher Quick Start
--------------------------------

1. Create a Serialiser for your Model in serialisers.py

.. code-block:: python

    from nap import serialiser
    from myapp.models import MyModel

    class MyModelSerialiser(serialiser.ModelSerialiser):
        class Meta:
            model = MyModel
            exclude = ['user',]

2. Create a Publisher in publishers.py, and register it.

.. code-block:: python

    from nap import rest
    from myapp.serialisers import MyModelSerialiser

    class MyModelPublisher(rest.ModelPublisher):
        serialiser = MyModelSerialiser()

    rest.api.register('api', MyModelPublisher)

3. Auto-discover publishers:

.. code-block:: python

    from nap import rest

    rest.api.autodiscover()

or if you're using Django 1.7, use the AppConfig:

.. code-block:: python

   INSTALLED_APPS = [
       ...
       'nap',
   ]


4. Add your APIs to your URLs:

.. code-block:: python

    urlpatterns('',
        (r'', include(rest.api.patterns())),
        ...
    )
