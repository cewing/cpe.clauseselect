.. contents::

Introduction
============

This package provides two classes for the Django framework which allow for the
generation of sentence-based forms. For examples of this type of form, see the
`California Energy Efficiency Program Data map`_ at the `OpenEMV website`_.

.. _California Energy Efficiency Program Data map: http://open-emv.com/data
.. _OpenEMV website: http://open-emv.com

Testing out the project
=======================

This package comes with a built-in buildout and demo project and app. To test
out the whole thing, simply clone the repo to your local machine::

    git clone git@github.com:cewing/cpe.clauseselect.git ./clauseselect

Then, you can run the buildout to get everything ready::

    cd clauseselect
    /usr/bin/python bootstrap.py
    bin/buildout

When buildout completes, you'll have a ready-to-go demo site all set up.
Simply run syncdb to get started::

    bin/django syncdb

You'll need to add an admin user at the prompt. Once the db is synced, you can
start the django development server::

    bin/django runserver

Surf to http://localhost:8000/admin to log in and start by adding a few
vehicles. Once you've added a dozen or so, go ahead and check out the listing
view at http://localhost:8000/cars/list

Using the Sentence Form
=======================

The sentence form presents you with a simple sentence which initially displays
the selected value for any required fields in your form. In the demo app, the
only required field is 'vehicle_type', so when you first load the form, that's
the only choice you get. In addition, the form shows a 'refine further' link
at the end of the sentence. If you click on this link, you'll open up a drawer
containing additional, optional fields. Click on a field to see a list of the
available selections for that field. When you select something other than the
default for that field, the field will be shown in the sentence after
submitting. If you return to the default value, then the field will disappear
from the sentence and return to the 'refine further' drawer on submitting.

Building Your Own Forms
-----------------------

The javascript functionality of the form is dependent on the `jQuery Tools`_
package. You'll need to include that in any pages on which a SentenceForm is
built. You can see how it's done by looking at the test_form.html template in
the demo app from this package. It's based on the tooltip functionality from
that package, so at the least you need to have that present in whatever subset
of the full toolset you choose to use.

.. _jQuery Tools: http://flowplayer.org/tools/index.html

Credits
=======

This package would not be possible without a few folks, here's a quick list:

* The `OpenEMV Team`_, who provided the original impetus to develop the tool 
* The outstanding UI folks at `Fog Creek Software`_, whose filter interface for
  the outstanding issue tracking system `FogBugz`_ was the inspiration for this
  project. This is but a pale imitation of the original.

.. _OpenEMV Team: http://open-emv.com/about/our-team
.. _Fog Creek Software: http://www.fogcreek.com/
.. _FogBugz: http://www.fogcreek.com/fogbugz/
