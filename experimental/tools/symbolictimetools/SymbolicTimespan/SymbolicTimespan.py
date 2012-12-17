import abc
import copy
import numbers
from abjad.tools import chordtools
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import leaftools
from abjad.tools import mathtools
from abjad.tools import notetools
from abjad.tools import timerelationtools
from abjad.tools.timespantools.Timespan import Timespan
from experimental.tools.symbolictimetools.SymbolicTimeObject import SymbolicTimeObject


class SymbolicTimespan(Timespan, SymbolicTimeObject):
    r'''.. versionadded:: 1.0

    ::
        
        >>> from experimental.tools import *

    Abstract base class from which conrete symbolic timespans inherit.
    '''

    ### CLASS ATTRIBUTES ###

    __metaclass__ = abc.ABCMeta

    ### INITIALIZER ###

    def __init__(self, timespan_modifications=None):
        from experimental.tools import specificationtools
        Timespan.__init__(self)
        SymbolicTimeObject.__init__(self)
        timespan_modifications = timespan_modifications or []
        self._timespan_modifications = datastructuretools.ObjectInventory(timespan_modifications)

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        '''True when mandatory and keyword arguments compare equal.
        Otherwise false.

        Return boolean.
        '''
        if not isinstance(expr, type(self)):
            return False
        if not self._positional_argument_values == expr._positional_argument_values:
            return False
        return self._keyword_argument_values == expr._keyword_argument_values

    ### PRIVATE READ-ONLY PROPERTIES ###

    @property
    def _keyword_argument_name_value_strings(self):
        result = SymbolicTimeObject._keyword_argument_name_value_strings.fget(self)
        if 'timespan_modifications=ObjectInventory([])' in result:
            result = list(result)
            result.remove('timespan_modifications=ObjectInventory([])')
        return tuple(result)

    @property
    def _timespan_abbreviation(self):
        '''Form of symbolic timespan suitable for writing to disk.
        '''
        return self

    ### PRIVATE METHODS ###

    def _adjust_timespan_offsets(self, start_offset, stop_offset, start_adjustment, stop_adjustment):
        original_start_offset, original_stop_offset = start_offset, stop_offset
        new_start_offset, new_stop_offset = start_offset, stop_offset
        if start_adjustment is not None and 0 <= start_adjustment:
            new_start_offset = original_start_offset + start_adjustment
        elif start_adjustment is not None and start_adjustment < 0:
            new_start_offset = original_stop_offset + start_adjustment
        if stop_adjustment is not None and 0 <= stop_adjustment:
            new_stop_offset = original_start_offset + stop_adjustment
        elif stop_adjustment is not None and stop_adjustment < 0:
            new_stop_offset = original_stop_offset + stop_adjustment
        return new_start_offset, new_stop_offset

    def _apply_timespan_modifications(self, start_offset, stop_offset):
        evaluation_context = {
            'self': self,
            'Duration': durationtools.Duration,
            'Multiplier': durationtools.Multiplier,
            'Offset': durationtools.Offset,
            }
        for timespan_modification in self.timespan_modifications:
            timespan_modification = timespan_modification.replace('original_start_offset', repr(start_offset))
            timespan_modification = timespan_modification.replace('original_stop_offset', repr(stop_offset))
            start_offset, stop_offset = eval(timespan_modification, evaluation_context)
            assert start_offset <= stop_offset
        return start_offset, stop_offset
        
    def _clone(self):
        return copy.deepcopy(self)

    # TODO: rename to self._divide_timespan() and accept integer (in addition to ratio)
    def _divide_by_ratio(self, start_offset, stop_offset, ratio, the_part):
        original_start_offset, original_stop_offset = start_offset, stop_offset
        original_duration = original_stop_offset - original_start_offset
        duration_shards = mathtools.divide_number_by_ratio(original_duration, ratio)
        duration_shards_before = duration_shards[:the_part]
        duration_before = sum(duration_shards_before)
        selected_duration_shard = duration_shards[the_part]
        new_start_offset = original_start_offset + duration_before
        new_stop_offset = new_start_offset + selected_duration_shard
        return new_start_offset, new_stop_offset

    @abc.abstractmethod
    def _get_offsets(self, score_specification, context_name):
        '''Get start offset and stop offset of symbolic timespan
        when applied to `context_name` in `score_specification`.

        Return pair.
        '''
        pass

    def _get_tools_package_qualified_keyword_argument_repr_pieces(self, is_indented=True):
        '''Do not show empty offset modifications list.
        '''
        filtered_result = []
        result = SymbolicTimeObject._get_tools_package_qualified_keyword_argument_repr_pieces(
            self, is_indented=is_indented)
        for string in result:
            if not 'timespan_modifications=datastructuretools.ObjectInventory([])' in string:
                filtered_result.append(string)
        return filtered_result

    def _scale(self, start_offset, stop_offset, multiplier):
        assert 0 < multiplier
        duration = stop_offset - start_offset
        new_duration = multiplier * duration
        new_stop_offset = start_offset + new_duration
        return start_offset, new_stop_offset

    def _set_duration(self, original_start_offset, original_stop_offset, duration):
        assert 0 < duration
        new_stop_offset = original_start_offset + duration
        return original_start_offset, new_stop_offset

    def _set_offsets(self, original_start_offset, original_stop_offset, 
        candidate_start_offset, candidate_stop_offset):
        if candidate_start_offset is not None:
            new_start_offset = candidate_start_offset
        else:
            new_start_offset = original_start_offset
        if candidate_stop_offset is not None:
            new_stop_offset = candidate_stop_offset
        else:
            new_stop_offset = original_stop_offset
        return new_start_offset, new_stop_offset

    # TODO: Remove timespan=None here and always store SymbolicTimespan._timespan_abbreviation instead.
    #       This means that one fewer parameters will be passed into this method.
    def _store_multiple_context_setting(self, attribute, source, contexts=None, timespan=None,
        index=None, count=None, reverse=None, rotation=None,
        persist=True, truncate=None):
        from experimental.tools import requesttools
        from experimental.tools import settingtools
        request = requesttools.expr_to_request(source)
        assert self.score_specification is not None
        context_names = self.score_specification._context_token_to_context_names(contexts)
        assert timespan is None
        timespan = timespan or self._timespan_abbreviation
        multiple_context_setting = settingtools.MultipleContextSetting(
            attribute, 
            request, 
            timespan, # eventually this should be self._timespan_abbreviation instead
            context_names=context_names,
            index=index,
            count=count,
            reverse=reverse,
            rotation=rotation,
            persist=persist, 
            truncate=truncate
            )
        self.score_specification.multiple_context_settings.append(multiple_context_setting)
        return multiple_context_setting

    def _translate_offsets(self, original_start_offset, original_stop_offset, 
        start_offset_translation, stop_offset_translation):
        new_start_offset = original_start_offset + start_offset_translation
        new_stop_offset = original_stop_offset + stop_offset_translation
        return new_start_offset, new_stop_offset

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def timespan_modifications(self):
        '''Read-only list of timespan_modifications to be applied 
        to symbolic timespan during evaluation.

        Return list.
        '''
        return self._timespan_modifications

    ### PUBLIC METHODS ###

    # TODO: eventually generalize self.set_offsets() to handle negative values; then remove this method.
    def adjust_timespan_offsets(self, start=None, stop=None):
        '''Add delayed evaluation offset setting command to symbolic timespan.
        
        Return symbolic timespan copy with offset modification.
        '''
        assert isinstance(start, (numbers.Number, tuple, type(None))), repr(start)
        assert isinstance(stop, (numbers.Number, tuple, type(None))), repr(stop)
        if start is not None:
            start = durationtools.Offset(start)
        if stop is not None:
            stop = durationtools.Offset(stop)
        timespan_modification = \
            'self._adjust_timespan_offsets(original_start_offset, original_stop_offset, {!r}, {!r})'
        timespan_modification = timespan_modification.format(start, stop)
        result = self._clone()
        result.timespan_modifications.append(timespan_modification)
        return result

    # TODO: rename to self.divide_timespan() and accept integer (in addition to ratio)
    def divide_by_ratio(self, ratio):
        result = []
        for part in range(len(ratio)):
            new_symbolic_timespan = self._clone()
            timespan_modification = \
                'self._divide_by_ratio(original_start_offset, original_stop_offset, {!r}, {!r})'
            timespan_modification = timespan_modification.format(ratio, part)
            new_symbolic_timespan.timespan_modifications.append(timespan_modification)
            result.append(new_symbolic_timespan)
        return tuple(result)

    def scale(self, multiplier):
        '''Scale timespan duration by `multiplier`.

        Return copy of timespan with appended modification.
        '''
        multiplier = durationtools.Multiplier(multiplier)
        timespan_modification = \
            'self._scale(original_start_offset, original_stop_offset, {!r})'
        timespan_modification = timespan_modification.format(multiplier)
        result = self._clone()
        result.timespan_modifications.append(timespan_modification)
        return result

    def select_background_measures(self, start=None, stop=None, time_relation=None):
        '''Select the first five background measures that start during segment 'red'::

            >>> score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
            >>> score_specification = specificationtools.ScoreSpecification(score_template=score_template)
            >>> red_segment = score_specification.append_segment(name='red')

        ::

            >>> selector = red_segment.select_background_measures(stop=5)

        ::

            >>> z(selector)
            symbolictimetools.BackgroundMeasureSelector(
                anchor='red',
                stop_identifier=5
                )

        Return background measure selector.
        '''
        assert isinstance(start, (int, type(None))), repr(start)
        assert isinstance(stop, (int, type(None))), repr(stop)
        assert isinstance(time_relation, (timerelationtools.TimeRelation, type(None))), repr(time_relation)
        assert time_relation is None or time_relation.is_fully_unloaded, repr(time_relation)
        from experimental.tools import symbolictimetools
        timespan = symbolictimetools.BackgroundMeasureSelector(
            anchor=self._timespan_abbreviation,
            start_identifier=start, 
            stop_identifier=stop, 
            time_relation=time_relation)
        timespan._score_specification = self.score_specification
        return timespan

    def select_divisions(self, voice, start=None, stop=None, time_relation=None):
        '''Select the first five divisions that start during segment 'red'::

            >>> selector = red_segment.select_divisions('Voice 1', stop=5)

        ::
            
            >>> z(selector)
            symbolictimetools.DivisionSelector(
                anchor='red',
                stop_identifier=5,
                voice_name='Voice 1'
                )

        Return division selector.
        '''
        assert isinstance(start, (int, type(None))), repr(start)
        assert isinstance(stop, (int, type(None))), repr(stop)
        assert isinstance(time_relation, (timerelationtools.TimeRelation, type(None))), repr(time_relation)
        assert time_relation is None or time_relation.is_fully_unloaded, repr(time_relation)
        from experimental.tools import symbolictimetools
        timespan = symbolictimetools.DivisionSelector(
            anchor=self._timespan_abbreviation,
            start_identifier=start, 
            stop_identifier=stop, 
            voice_name=voice,
            time_relation=time_relation)
        timespan._score_specification = self.score_specification
        return timespan

    def select_leaves(self, voice, start=None, stop=None, time_relation=None):
        '''Select the first ``40`` voice ``1`` leaves that start during segment ``'red'``::

            >>> selector = red_segment.select_leaves('Voice 1', stop=40)

        ::

            >>> z(selector)
            symbolictimetools.CounttimeComponentSelector(
                anchor='red',
                klass=leaftools.Leaf,
                stop_identifier=40,
                voice_name='Voice 1'
                )

        Return counttime component selector.
        '''
        assert isinstance(voice, (str, type(None)))
        assert isinstance(start, (int, type(None))), repr(start)
        assert isinstance(stop, (int, type(None))), repr(stop)
        assert isinstance(time_relation, (timerelationtools.TimeRelation, type(None))), repr(time_relation)
        assert time_relation is None or time_relation.is_fully_unloaded, repr(time_relation)
        from experimental.tools import symbolictimetools
        timespan = symbolictimetools.CounttimeComponentSelector(
            anchor=self._timespan_abbreviation,
            time_relation=time_relation, 
            klass=leaftools.Leaf, 
            start_identifier=start, 
            stop_identifier=stop, 
            voice_name=voice)
        timespan._score_specification = self.score_specification
        return timespan

    def select_notes_and_chords(self, voice, start=None, stop=None, time_relation=None):
        '''Select the first ``40`` voice ``1`` notes and chords 
        that start during segment ``'red'``::

            >>> timespan = red_segment.select_notes_and_chords('Voice 1', stop=40)

        ::

            >>> z(timespan)
            symbolictimetools.CounttimeComponentSelector(
                anchor='red',
                klass=helpertools.KlassInventory([
                    notetools.Note,
                    chordtools.Chord
                    ]),
                stop_identifier=40,
                voice_name='Voice 1'
                )

        Return counttime component selector.
        '''
        assert isinstance(start, (int, type(None))), repr(start)
        assert isinstance(stop, (int, type(None))), repr(stop)
        assert isinstance(time_relation, (timerelationtools.TimeRelation, type(None))), repr(time_relation)
        assert time_relation is None or time_relation.is_fully_unloaded, repr(time_relation)
        from experimental.tools import symbolictimetools
        timespan = symbolictimetools.CounttimeComponentSelector(
            anchor=self._timespan_abbreviation,
            time_relation=time_relation, 
            klass=(notetools.Note, chordtools.Chord),
            start_identifier=start, 
            stop_identifier=stop, 
            voice_name=voice)
        timespan._score_specification = self.score_specification
        return timespan

    def set_aggregate(self, source, contexts=None, timespan=None, persist=True):
        r'''Set aggregate of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'aggregate'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_articulations(self, source, contexts=None, timespan=None, persist=True):
        r'''Set articulations of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'articulations'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_chord_treatment(self, source, contexts=None, timespan=None, persist=True):
        r'''Set chord treatment of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'chord_treatment'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_divisions(self, source, contexts=None, timespan=None,
        index=None, count=None, reverse=None, rotation=None,
        persist=True, truncate=None):
        r'''Set divisions of segment `contexts` to `source`::

            >>> setting = red_segment.set_divisions([(3, 16)], contexts=['Voice 1', 'Voice 3'])

        ::

            >>> z(setting)
            settingtools.MultipleContextSetting(
                'divisions',
                requesttools.AbsoluteRequest(
                    [(3, 16)]
                    ),
                'red',
                context_names=['Voice 1', 'Voice 3'],
                persist=True
                )

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'divisions'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan,
            index=index, count=count, reverse=reverse, rotation=rotation,
            truncate=truncate, persist=persist)

    def set_duration(self, duration):
        '''Set timespan duration to `duration`.

        Return copy of timespan with appended modification.
        '''
        duration = durationtools.Duration(duration)
        timespan_modification = \
            'self._set_duration(original_start_offset, original_stop_offset, {!r})'
        timespan_modification = timespan_modification.format(duration)
        result = self._clone()
        result.timespan_modifications.append(timespan_modification)
        return result

    def set_dynamics(self, source, contexts=None, timespan=None, persist=True):
        r'''Set dynamics of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'dynamics'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_marks(self, source, contexts=None, timespan=None, persist=True):
        r'''Set marks of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'marks'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_markup(self, source, contexts=None, timespan=None, persist=True):
        r'''Set markup of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'markup'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_offsets(self, start_offset=None, stop_offset=None):
        '''Set timespan start offset to `start_offset`
        and stop offset to `stop_offset`.

        Return copy of timespan with appended modification.
        '''
        if start_offset is not None:
            start_offset = durationtools.Offset(start_offset)
        if stop_offset is not None:
            stop_offset = durationtools.Offset(stop_offset) 
        assert start_offset is None or 0 <= start_offset
        assert stop_offset is None or 0 <= stop_offset
        timespan_modification = \
            'self._set_offsets(original_start_offset, original_stop_offset, {!r}, {!r})'
        timespan_modification = timespan_modification.format(start_offset, stop_offset)
        result = self._clone()
        result.timespan_modifications.append(timespan_modification)
        return result

    def set_pitch_class_application(self, source, contexts=None, timespan=None, persist=True):
        r'''Set pitch-class application of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'pitch_class_application'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_pitch_class_transform(self, source, contexts=None, timespan=None, persist=True):
        r'''Set pitch-class transform of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'pitch_class_transform'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_pitch_classes(self, source, contexts=None, timespan=None, persist=True):
        r'''Set pitch-classes of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'pitch_classes'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_registration(self, source, contexts=None, timespan=None, persist=True):
        r'''Set registration of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'registration'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_rhythm(self, source, contexts=None, timespan=None,
        index=None, count=None, reverse=None, rotation=None,
        persist=True):
        r'''Set rhythm of segment `contexts` to `source`.

            >>> setting = red_segment.set_rhythm(library.sixteenths)

        ::

            >>> z(setting)
            settingtools.MultipleContextSetting(
                'rhythm',
                requesttools.AbsoluteRequest(
                    rhythmmakertools.TaleaRhythmMaker(
                        [1],
                        16,
                        prolation_addenda=[],
                        secondary_divisions=[],
                        beam_each_cell=False,
                        beam_cells_together=True,
                        tie_split_notes=False
                        )
                    ),
                'red',
                context_names=['Grouped Rhythmic Staves Score'],
                persist=True
                )

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'rhythm'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan,
            index=index, count=count, reverse=reverse, rotation=rotation,
            persist=persist)

    def set_tempo(self, source, contexts=None, timespan=None, persist=True):
        r'''Set tempo of segment `contexts` to `source`.

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'tempo'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan, persist=persist)

    def set_time_signatures(self, source, contexts=None, timespan=None,
        index=None, count=None, reverse=None, rotation=None,
        persist=True):
        r'''Set time signatures according to `source` for segment `contexts`.

            >>> setting = red_segment.set_time_signatures([(3, 8), (4, 8)])

        ::

            >>> z(setting)
            settingtools.MultipleContextSetting(
                'time_signatures',
                requesttools.AbsoluteRequest(
                    [(3, 8), (4, 8)]
                    ),
                'red',
                context_names=['Grouped Rhythmic Staves Score'],
                persist=True
                )

        Create, store and return ``MultipleContextSetting``.
        '''
        attribute = 'time_signatures'
        return self._store_multiple_context_setting(attribute, source, 
            contexts=contexts, timespan=timespan,
            index=index, count=count, reverse=reverse, rotation=rotation,
            persist=persist)

    def translate_offsets(self, start_offset_translation=None, stop_offset_translation=None):
        '''Translate timespan start offset by `start_offset_translation`
        and stop offset by `stop_offset_translation`.

        Return copy of timespan with appended modification.
        '''
        start_offset_translation = start_offset_translation or 0
        stop_offset_translation = stop_offset_translation or 0
        start_offset_translation = durationtools.Duration(start_offset_translation)
        stop_offset_translation = durationtools.Duration(stop_offset_translation)
        timespan_modification = \
            'self._translate_offsets(original_start_offset, original_stop_offset, {!r}, {!r})'
        timespan_modification = timespan_modification.format(start_offset_translation, stop_offset_translation)
        result = self._clone()
        result.timespan_modifications.append(timespan_modification)
        return result
