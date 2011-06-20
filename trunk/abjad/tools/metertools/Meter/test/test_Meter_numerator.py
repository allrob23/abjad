from abjad import *
from abjad.tools import metertools


def test_Meter_numerator_01( ):
   '''Meters are immutable.
   '''

   t = metertools.Meter(3, 8)

   assert t.numerator == 3
   assert t.denominator == 8
   assert t.duration == Duration(3, 8)

#   t.numerator = 4
#
#   assert t.numerator == 4
#   assert t.denominator == 8
#   assert t.duration == Duration(1, 2)
