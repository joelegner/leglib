.. _usage:

Using :mod:`leglib.structural` for Projects
===========================================

To use leglib for a project, create an input file like this:[#f1]_

.. literalinclude:: _static/usage.py

If the filename of the input file is ``input.py``, we can run it by:

.. code-block:: bash

   $ python input.py > output.txt

This will create a text file called ``output.txt`` containing the report:

.. literalinclude:: _static/usage.txt

.. rubric:: Footnotes

.. [#f1] This assumes that ``leglib`` is in Python's search path.
