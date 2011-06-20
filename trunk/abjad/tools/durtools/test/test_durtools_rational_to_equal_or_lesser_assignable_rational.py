from abjad import *
from abjad.tools import durtools


def test_durtools_rational_to_equal_or_lesser_assignable_rational_01( ):
   '''Wrapper around _naivedurtools.rational_to_equal_or_lesser_assignable_rational( ) 
   that returns dotted and double dotted durations where appropriate.'''

   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(1, 16)) == Fraction(1, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(2, 16)) == Fraction(2, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(3, 16)) == Fraction(3, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(4, 16)) == Fraction(4, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(5, 16)) == Fraction(4, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(6, 16)) == Fraction(6, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(7, 16)) == Fraction(7, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(8, 16)) == Fraction(8, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(9, 16)) == Fraction(8, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(10, 16)) == Fraction(8, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(11, 16)) == Fraction(8, 16)
   assert durtools.rational_to_equal_or_lesser_assignable_rational(
      Fraction(12, 16)) == Fraction(12, 16)
