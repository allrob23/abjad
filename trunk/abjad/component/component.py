from abjad.accidental.interface import _AccidentalInterface
from abjad.barline.interface import _BarLineInterface
from abjad.beam.interface import _BeamInterface
from abjad.breaks.interface import _BreaksInterface
from abjad.comments.comments import _UserComments
from abjad.core.abjadcore import _Abjad
from abjad.clef.interface import _ClefInterface
from abjad.directives.interface import _UserDirectivesInterface
from abjad.dots.interface import _DotsInterface
from abjad.dynamics.interface import _DynamicsInterface
from abjad.glissando.interface import _GlissandoInterface
from abjad.helpers.iterate import iterate
from abjad.instrument.interface import _InstrumentInterface
from abjad.interfaces.aggregator import _InterfaceAggregator
from abjad.meter.interface import _MeterInterface
from abjad.navigator.navigator import _Navigator
from abjad.notehead.interface import _NoteHeadInterface
from abjad.numbering.interface import _NumberingInterface
from abjad.offset.interface import _OffsetInterface
from abjad.parentage.parentage import _Parentage
from abjad.pianopedal.interface import _PianoPedalInterface
from abjad.rational.rational import Rational
from abjad.receipt.component import _ComponentReceipt
from abjad.rest.interface import _RestInterface
from abjad.slur.interface import _SlurInterface
from abjad.stem.interface import _StemInterface
from abjad.tempo.interface import _TempoInterface
from abjad.thread.interface import _ThreadInterface
from abjad.tie.interface import _TieInterface
from abjad.text.interface import _TextInterface
from abjad.tremolo.interface import _TremoloInterface
from abjad.trill.interface import _TrillInterface
from abjad.tuplet.bracket import _TupletBracketInterface
from abjad.tuplet.number import _TupletNumberInterface
from abjad.update.interface import _UpdateInterface
from abjad.voice.interface import _VoiceInterface
import copy
import types


class _Component(_Abjad):

   def __init__(self):
      self._accidental = _AccidentalInterface(self)
      self._barline = _BarLineInterface(self)
      self._beam = _BeamInterface(self)
      self._breaks = _BreaksInterface(self)
      self._clef = _ClefInterface(self)
      self._comments = _UserComments( )
      self._directives = _UserDirectivesInterface(self)
      self._dots = _DotsInterface(self)
      self._dynamics = _DynamicsInterface(self)
      self._glissando = _GlissandoInterface(self)
      self._instrument = _InstrumentInterface(self)
      self._interfaces = _InterfaceAggregator(self)
      self._meter = _MeterInterface(self)
      self._name = None
      self._navigator = _Navigator(self)
      self._notehead = _NoteHeadInterface(self)
      self._parentage = _Parentage(self)
      self._pianopedal = _PianoPedalInterface(self)
      self._rest = _RestInterface(self)
      self._slur = _SlurInterface(self)
      self._stem = _StemInterface(self)
      self._tempo = _TempoInterface(self)
      self._text = _TextInterface(self)
      self._thread = _ThreadInterface(self)
      self._tie = _TieInterface(self)
      self._tremolo = _TremoloInterface(self)
      self._trill = _TrillInterface(self)
      self._tupletbracket = _TupletBracketInterface(self)
      self._tupletnumber = _TupletNumberInterface(self)
      self._update = _UpdateInterface(self)
      ## Observer interfaces must instantiate lexically after _UpdateInterface
      self._numbering = _NumberingInterface(self, self._update)
      self._offset = _OffsetInterface(self, self._update)
      self._voice = _VoiceInterface(self)

   ## OVERLOADS ##

   def __mul__(self, n):
      from abjad.helpers.copy_unspan import copy_unspan
      return copy_unspan([self], n)

   def __rmul__(self, n):
      return self * n

   ## PRIVATE ATTRIBUTES ##

   @property
   def _ID(self):
      if self.name is not None:
         rhs = self.name
      else:
         rhs = id(self)
      lhs = self.__class__.__name__
      return '%s-%s' % (lhs, rhs)

   ## PUBLIC ATTRIBUTES ##

   @property
   def accidental(self):
      return self._accidental
   
   @property
   def barline(self):
      return self._barline
   
   @property
   def beam(self):
      return self._beam

   @property
   def breaks(self):
      return self._breaks

   @property
   def clef(self):
      return self._clef

   @property
   def comments(self):
      return self._comments

   @property
   def directives(self):
      return self._directives

   @property
   def dots(self):
      return self._dots

   @property
   def duration(self):
      return self._duration

   @property
   def dynamics(self):
      return self._dynamics

   @property
   def format(self):
      return self.formatter.format

   @property
   def formatter(self):
      return self._formatter

   @property
   def glissando(self):
      return self._glissando

   @property
   def instrument(self):
      return self._instrument

   @property
   def interfaces(self):
      return self._interfaces

   @property
   def leaves(self):
      '''Python list of all leaves in container.'''
      from abjad.leaf.leaf import _Leaf
      return list(iterate(self, _Leaf))

   @apply
   def meter( ):
      def fget(self):
         return self._meter
      def fset(self, arg):
         self._meter.forced = arg
      return property(**locals( ))

   @property
   def music(self):
      if hasattr(self, '_music'):
         return tuple(self._music)
      else:
         return tuple( )

   @apply
   def name( ):
      def fget(self):
         return self._name
      def fset(self, arg):
         assert isinstance(arg, (str, types.NoneType))
         self._name = arg
      return property(**locals( ))

   @property
   def notehead(self):
      return self._notehead

   @property
   def numbering(self):
      return self._numbering

   @property
   def offset(self):
      return self._offset

   @property
   def parentage(self):
      return self._parentage

   @property
   def pianopedal(self):
      return self._pianopedal

   @property
   def rest(self):
      return self._rest

   @property
   def slur(self):
      return self._slur

   @property
   def spanners(self):
      return self._spanners

   @property
   def stem(self):
      return self._stem

   @property
   def thread(self):
      return self._thread

   @property
   def tie(self):
      return self._tie

   @apply
   def tempo( ):
      def fget(self):
         return self._tempo
      def fset(self, expr):
         if expr is None:
            self._tempo._metronome = None
         elif isinstance(expr, (tuple)):
            assert isinstance(expr, tuple)
            assert isinstance(expr[0], (tuple, Rational))
            assert isinstance(expr[1], (int, float, long))
            from abjad.note.note import Note
            if isinstance(expr[0], tuple):
               self._tempo._metronome = (Note(0, expr[0]), expr[1])
            elif isinstance(expr[0], Rational):
               self._tempo._metronome = (Note(0, expr[0]), expr[1])
      return property(**locals( ))

   @property
   def text(self):
      return self._text

   @property
   def tremolo(self):
      return self._tremolo

   @property
   def trill(self):
      return self._trill
   
   @property
   def tupletbracket(self):
      return self._tupletbracket

   @property
   def tupletnumber(self):
      return self._tupletnumber

   @property
   def voice(self):
      return self._voice

   ## PUBLIC METHODS ##

   ## TODO: Externalize _Component.detach( ) ##

   def detach(self):
      '''Detach component from parentage.
         Detach component from spanners.
         Detach children of component from spanners.
         Return receipt.'''
      from abjad.helpers.detach_subtree import detach_subtree
      parent = self.parentage.parent
      receipt = detach_subtree(self)
      if parent is not None:
         parent._update._markForUpdateToRoot( )
      return receipt

   ## TODO: Externalize or eliminate _Component.reattach( ) ##

   def reattach(self, receipt):
      '''Reattach component to both parentage in receipt.
         Reattach component to spanners in receipt.
         Empty receipt and return component.'''
      assert self is receipt._component
      self.parentage._reattach(receipt._parentage)
      self.spanners._reattach(receipt._spanners)
      receipt._empty( )
      return self

   ## TODO: Externalize _Component.slip( ) ##

   def slip(self):
      '''Give spanners attached directly to container to children.
         Give children to parent.
         Return empty, childless container.'''
      from abjad.helpers.get_parent_and_indices import \
         get_parent_and_indices
      parent, start, stop = get_parent_and_indices([self])
      result = parent[start:stop+1] = list(self.music)
      return self

   def splice(self, components):
      '''Splice 'components' after self.
         Extend spanners to attached to all components in list.'''
      from abjad.helpers.assert_components import assert_components
      from abjad.helpers.get_dominant_spanners import get_dominant_spanners
      from abjad.helpers.get_parent_and_indices import get_parent_and_indices
      from abjad.helpers.spanner_get_component_at_score_offset import \
         spanner_get_component_at_score_offset
      assert_components(components)
      insert_offset = self.offset.score + self.duration.prolated
      receipt = get_dominant_spanners([self])
      for spanner, index in receipt:
         insert_component = spanner_get_component_at_score_offset(
            spanner, insert_offset)
         if insert_component is not None:
            insert_index = spanner.index(insert_component)
         else:
            insert_index = len(spanner)
         for component in reversed(components):
            spanner._insert(insert_index, component)
            component.spanners._add(spanner)
      parent, start, stop = get_parent_and_indices([self])
      if parent is not None:
         for component in reversed(components):
            component.parentage._switchParentTo(parent)
            parent._music.insert(start + 1, component)
      return [self] + components

   def splice_left(self, components):
      '''Splice 'components' before self.
         Extend spanners leftwards to attach 
         to all components in 'components'.'''
      from abjad.helpers.assert_components import assert_components
      from abjad.helpers.get_dominant_spanners import get_dominant_spanners
      from abjad.helpers.get_parent_and_indices import get_parent_and_indices
      from abjad.helpers.spanner_get_index_at_score_offset import \
         spanner_get_index_at_score_offset
      assert_components(components)
      offset = self.offset.score
      receipt = get_dominant_spanners([self])
      for spanner, x in receipt:
         index = spanner_get_index_at_score_offset(spanner, offset)
         for component in reversed(components):
            spanner._insert(index, component)
            component.spanners._add(spanner)
      parent, start, stop = get_parent_and_indices([self])
      if parent is not None:
         for component in reversed(components):
            component.parentage._switchParentTo(parent)
            parent._music.insert(start, component)
      return components + [self] 
