from abjad import *
from abjad.tools import seqtools


def test_seqtools_partition_sequence_cyclically_by_weights_exactly_without_overhang_01( ):

   sequence = [3, 3, 3, 3, 4, 4, 4, 4, 5]
   groups = seqtools.partition_sequence_cyclically_by_weights_exactly_without_overhang(
      sequence, [12])
   assert groups == [[3, 3, 3, 3], [4, 4, 4]]
