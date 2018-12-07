.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.smartlink
==============================================================================


Features
--------

- Adds an output filter that changes all the internal link in a page (the ones
  with `resolveuid`) to the absolute url of that plone object.
- Adds the `ILeadImage` behavior to the Link content type so you can add an
  image to a link object.


Notes on upgrading this add-on
------------------------------

If you come from a `0.1.x` version, make sure to upgrade to the `2.0` and run
the upgrade step before upgrading further to avoid issues.


Installation
------------

Install collective.smartlink by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.smartlink


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/RedTurtle/collective.smartlink/issues
- Source Code: https://github.com/RedTurtle/collective.smartlink


Support
-------

If you are having issues, please let us know.


License
-------

The project is licensed under the GPLv2.
