:class:`DriftCalc` - Prototype Calculation
==========================================

.. index::
   single: calculations; driftcalc
   single: calculations; prototype
   single: driftcalc
   single: prototype

.. todo:: Consider eliminating :class:`DriftCalc` and using :class:`SnowDrift` directly, for DriftCalc does not add much. Why encapsulate it?

The :class:`DriftCalc` class was the first calculation created and was prepared in such a way as to act as a model for future calculations.

See :ref:`Architecture` for leglib design concepts.

Source Code
-----------

Contents of :mod:`structural.driftcalc`:

.. literalinclude:: ../../structural/driftcalc.py

Test Code
---------

Contents of :mod:`leglib.structural.tests.test_driftcalc`:

.. literalinclude:: ../../structural/tests/test_driftcalc.py

To execute the tests, type at a bash prompt:

.. code-block:: bash

   $ python structural/tests/test_driftcalc.py

Report Test Code
----------------

:class:`DriftCalc` also serves as the component used for testing the :class:`Report` class and its templates:

.. literalinclude:: ../../structural/tests/test_report.py

To execute the report tests, type at a bash prompt:

.. code-block:: bash

   $ python structural/tests/test_report.py

