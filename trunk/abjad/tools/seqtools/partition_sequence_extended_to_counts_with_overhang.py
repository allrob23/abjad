from abjad.tools.seqtools._partition_sequence_extended_to_counts import _partition_sequence_extended_to_counts


def partition_sequence_extended_to_counts_with_overhang(sequence, counts):
   '''.. versionadded:: 1.1.2

   Partition `sequence` extended to `counts` with overhang::

      abjad> from abjad.tools import seqtools

   ::

      abjad> seqtools.partition_sequence_extended_to_counts_with_overhang([1, 2, 3, 4], [6, 6, 6])
      [[1, 2, 3, 4, 1, 2], [3, 4, 1, 2, 3, 4], [1, 2, 3, 4, 1, 2], [3, 4]]

   Return new object of `sequence` type.
   '''

   return _partition_sequence_extended_to_counts(sequence, counts, overhang = True)
