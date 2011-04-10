from abjad import *
import py.test


def test_Tuplet___cmp___01( ):
   '''Compare tuplet to itself.
   '''

   tuplet = Tuplet((2, 3), macros.scale(3))

   assert tuplet == tuplet
   assert not tuplet != tuplet

   comparison_string = 'tuplet <  tuplet'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet <= tuplet'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet >  tuplet'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet >= tuplet'
   assert py.test.raises(NotImplementedError, comparison_string)


def test_Tuplet___cmp___02( ):
   '''Compare tuplets.
   '''

   tuplet_1 = Tuplet((2, 3), macros.scale(3))
   tuplet_2 = Tuplet((2, 3), macros.scale(3))

   assert     tuplet_1.format == tuplet_2.format
   assert not tuplet_1.format != tuplet_2.format

   comparison_string = 'tuplet_1 <  tuplet_2'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet_1 <= tuplet_2'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet_1 >  tuplet_2'
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = 'tuplet_1 >= tuplet_2'
   assert py.test.raises(NotImplementedError, comparison_string)


def test_Tuplet___cmp___03( ):
   '''Compare tuplet to foreign type.
   '''

   tuplet = Tuplet((2, 3), macros.scale(3))

   assert not tuplet == 'foo'
   assert     tuplet != 'foo'

   comparison_string = "tuplet <  'foo'"
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = "tuplet <= 'foo'"
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = "tuplet >  'foo'"
   assert py.test.raises(NotImplementedError, comparison_string)
   comparison_string = "tuplet >= 'foo'"
   assert py.test.raises(NotImplementedError, comparison_string)
