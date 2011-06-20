def negate_sequence_elements_cyclically(sequence, indices, period):
   '''.. versionadded:: 1.1.2

   Negate `sequence` elements at `indices` cyclically according to `period`::

      abjad> from abjad.tools import seqtools

   ::

      abjad> sequence = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]

   ::

      abjad> seqtools.negate_sequence_elements_cyclically(sequence, [0, 1, 2], 5)
      [-1, -2, -3, 4, 5, 6, 7, 8, -9, -10]

   Return newly constructed list.
   '''
   
   if not isinstance(sequence, list):
      raise TypeError

   result = [ ]

   for i, element in enumerate(sequence):
      if (i in indices) or (period and i % period in indices):
         result.append(-element)
      else:
         result.append(element)

   return result
