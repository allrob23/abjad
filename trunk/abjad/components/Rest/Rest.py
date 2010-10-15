from abjad.components._Leaf import _Leaf


class Rest(_Leaf):
   '''The Abjad model of a rest:

   ::

      abjad> Rest((3, 16))
      Rest('r8.')
   '''

   def __init__(self, *args, **kwargs):
      from abjad.tools.resttools._initialize_rest import _initialize_rest
      _initialize_rest(self, _Leaf, *args)
      self._initialize_keyword_values(**kwargs)

   ## OVERRIDES ##

   def __getnewargs__(self):
      if self.duration.multiplier is not None:
         return (self.duration.written, self.duration.multiplier)
      else:
         return (self.duration.written, )
   
   ## PRIVATE ATTRIBUTES ##

   @property
   def _body(self):
      '''Read-only body of rest.
      '''
      result = ''
      vertical_positioning_pitch = getattr(self, '_vertical_positioning_pitch', None)
      if vertical_positioning_pitch:
         result += str(vertical_positioning_pitch)
      else:
         result += 'r'
      result += str(self.duration)
      if vertical_positioning_pitch:
         result += r' \rest'
      return [result]

   @property
   def _compact_representation(self):
      return 'r%s' % self.duration
