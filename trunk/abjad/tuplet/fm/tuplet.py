from abjad.tuplet.fm.duration import _FMTupletDurationInterface
from abjad.duration.rational import Rational
from abjad.tuplet.tuplet import _Tuplet


class FixedMultiplierTuplet(_Tuplet):

   def __init__(self, multiplier, music = None):
      music = music or [ ]
      _Tuplet.__init__(self, music)
      self._duration = _FMTupletDurationInterface(self, multiplier)
      self._signifier = '*'

   ### REPR ###

   def __repr__(self):
      return 'FixedMultiplierTuplet(%s, [%s])' % ( 
         self.duration.multiplier, self._summary)

   def __str__(self):
      if len(self) > 0:
         return '{%s %s %s %s}' % (
            self._signifier, self.ratio, self._summary, self._signifier)
      else:
         return '{%s %s %s}' % (
            self._signifier, self.duration.multiplier, self._signifier)

   ### PROPERTIES ###

   @property
   def duration(self):
      return self._duration
