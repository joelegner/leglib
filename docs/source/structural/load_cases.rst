.. _load-cases:

:mod:`load_cases` -- Load cases and combinations
================================================

Load Cases
----------

.. index::
   single: loads; cases
   single: load cases

List of load cases which are combined into :ref:`load-combinations`:

=====  ============  ================
Index  Abbreviation  Name
=====  ============  ================
0      D             Dead
1      L             Live
2      Lr            Roof Live
3      S             Snow
4      W+            Wind+
5      W-            Wind-
6      E             Earthquake
7      H             Lateral Pressure
=====  ============  ================

.. _load-combinations:

Load Combinations
-----------------

.. index::
   single: loads; combinations
   single: load combinations
   single: ASD; load combinations
   single: LRFD; load combinations

The following list is generated dynamically by ``python structural/load_cases.py``.

.. literalinclude:: _static/load_cases.txt

.. _load-case-vector:

Load Case Vector
----------------

.. index::
   single: loads; load case vector
   single: load case vector
   single: vector; load case

In leglib, a load is expressed as a vector of load cases using the indexes listed under :ref:`load-cases`.  See also :ref:`results-vector`. For example:

.. code-block:: python

   >>> #     D   L   Lr   S
   >>> P = [4.5, 7, 0.0, 5.4]    # other cases truncated = 0.0

This expresses a force *P* where its dead load magnitude is 4.5 kip, live load 7 kip, roof live load is zero (0) and snow load is 5.4 kips.  All other load cases truncated off the end are treated as zero (0).

As another example, to represent a single force, say 8.0 kips live load:

.. code-block:: python

   >>> P = [0, 8]

You can omit trailing empty load cases, but any leading empty load cases must be included with a magnitude of zero (0).


.. _results-vector:

Results Vector
--------------

.. index::
   single: loads; results vector
   single: results vector
   single: vector; results

A results vector is similar to a :ref:`load-case-vector`, except it stores the results of :ref:`load-combinations`.  The index of the results vector list equates to the index of the load combination for the specified methodology (ASD or LRFD).  So, for *methodology* = "ASD"::

       ASD0 ASD1   ASD2 ASD3 ASD4   ASD5    ...
      [5.4, 13.1, -1.0, 5.4, 6.375, 11.175, ... ]
   

leglib.structural.load_cases
----------------------------

.. data:: cases

   List of all load cases.  See :ref:`load-cases`.

   .. code-block:: python
   
      >>> print cases
      [('D', 'Dead'), ('L', 'Live'), ('Lr', 'Roof Live'), ('S', 'Snow'), ('W+',
      'Wind+'), ('W-', 'Wind-'), ('E', 'Earthquake'), ('H', 'Lateral
      Pressure')]

.. data:: case_abbrs

   List of case abbreviations.

   .. code-block:: python
   
      >>> print case_abbrs
      ['D', 'L', 'Lr', 'S', 'W+', 'W-', 'E', 'H']

.. data:: case_names

   List of case names.

   .. code-block:: python
   
      >>> print case_names
      ['Dead', 'Live', 'Roof Live', 'Snow', 'Wind+', 'Wind-', 'Earthquake',
      'Lateral Pressure']

.. data:: combos
   
   Dictionary whose key is a string, either "ASD" or "LRFD".  The data for each
   key is a list of load combinations of the form::

   [name, equation_string, factors]

   The *name* is "ASD0", "ASD1", etc.  The *equation_string* is a string 
   describing the load combination, such as "D + L" and *factors* is a list of
   load factors which correspond to the index under :ref:`load-cases`.

.. function:: calc_combos(methodology, load_vector)

   Calculate load combinations for either ASD or LRFD and return a
   :ref:`results-vector` with numerical values for all load combinations.  See
   :ref:`load-combinations` for allowable *methodology* values.

   *load_vector* is as specified under :ref:`load-case-vector`.

   Example:

   .. code-block:: python

      >>> #    D    L     W
      >>> P = [5.4, 7.7, -6.4]
      >>> print calc_combos("ASD", P)
      [5.4, 13.100000000000001, -1.0, 5.4, 6.375, 11.175, 5.4, 5.4, 5.4, 11.175,
      11.175, 11.175, 0.5999999999999996, 0.5999999999999996, 0.5999999999999996,
      3.24, 3.24, 3.24]

   It is easy to get maximum and minimum values to use for analysis or design.

   .. code-block:: python

      >>> #    D    L     W
      >>> P = [5.4, 7.7, -6.4]
      >>> results = calc_combos("ASD", P)
      >>> print max(results)
      13.1
      >>> print min(results)
      -1.0

