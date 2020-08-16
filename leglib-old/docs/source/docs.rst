Documentation
=============

There are two sets of documentation:

1. leglib docs at ``leglib/docs/build/html/index.html``.

#. Coverage report at ``leglib/docs/coverage/html/index.html``.

Building Documentation
----------------------

To build leglib html documentation:

.. code-block:: bash

   $ cd PATH-TO/leglib/docs
   $ make html

Alternate way to build leglib html documentation:

.. code-block:: bash

   $ cd PATH-TO/leglib
   $ make html

To build Coverage report:

.. code-block:: bash

   $ cd PATH-TO/leglib
   $ make test

Docs Makefile Listing
---------------------

Listing of ``leglib/docs/Makefile``:

.. literalinclude:: ../Makefile
   :language: make

