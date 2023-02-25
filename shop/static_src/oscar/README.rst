=======
Statics
=======

Shop ships with a set of static files (js/css/scss/images).  These are used on
the sandbox site.

When building your own project, it is not recommended to use these files
straight from the package.  Rather, you should take a static copy of the
``shop/static/shop`` folder and commit it into your project.


Compiling assets
----------------

You can compile the static assets from the root of the project using a make target::

    make assets


Assets in development
---------------------

If you make changes to Shop's assets in development, you can run
``npm run watch`` to automatically watch and compile changes to them.
