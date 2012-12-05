from abjad.tools import durationtools
from abjad.tools.abctools.AbjadObject import AbjadObject


class SymbolicOffset(AbjadObject):
    r'''.. versionadded:: 1.0

    Infinitely thin vertical line coincident with an arbitrary object-relative offset in score.

    Symbolic offset indicating the left edge of score::

        >>> symbolictimetools.SymbolicOffset()
        SymbolicOffset()

    Symbolic offset indicating the right edge of score::

        >>> symbolictimetools.SymbolicOffset(edge=Right)
        SymbolicOffset(edge=Right)

    Symbolic offset ``1/8`` of a whole note into score::

        >>> symbolictimetools.SymbolicOffset(addendum=durationtools.Offset(1, 8))
        SymbolicOffset(addendum=Offset(1, 8))

    Symbolic offset one third of the way into score::

        >>> symbolictimetools.SymbolicOffset(edge=Right, multiplier=Multiplier(1, 3))
        SymbolicOffset(edge=Right, multiplier=Multiplier(1, 3))

    Symbolic offset ``1/8`` of a whole note after the first third of score::

        >>> symbolictimetools.SymbolicOffset(edge=Right, multiplier=Multiplier(1, 3), addendum=durationtools.Offset(1, 8))
        SymbolicOffset(edge=Right, multiplier=Multiplier(1, 3), addendum=Offset(1, 8))

    Symbolic offset indicating the left edge of segment ``'red'``::

        >>> segment_selector = symbolictimetools.SingleSegmentSymbolicTimespan(identifier='red')

    ::

        >>> symbolictimetools.SymbolicOffset(selector=segment_selector)
        SymbolicOffset(selector=SingleSegmentSymbolicTimespan(identifier='red'))

    Symbolic offset indicating the right edge of segment ``'red'``::

        >>> symbolictimetools.SymbolicOffset(selector=segment_selector, edge=Right)
        SymbolicOffset(selector=SingleSegmentSymbolicTimespan(identifier='red'), edge=Right)

    Symbolic offset indicating ``1/8`` of a whole note after the left edge of
    segment ``'red'``::

        >>> symbolictimetools.SymbolicOffset(selector=segment_selector, addendum=durationtools.Offset(1, 8))
        SymbolicOffset(selector=SingleSegmentSymbolicTimespan(identifier='red'), addendum=Offset(1, 8))

    Symbolic offset indicating one third of the way into segment ``'red'``::

        >>> symbolictimetools.SymbolicOffset(selector=segment_selector, edge=Right, multiplier=Multiplier(1, 3))
        SymbolicOffset(selector=SingleSegmentSymbolicTimespan(identifier='red'), edge=Right, multiplier=Multiplier(1, 3))

    Symbolic offset indicating ``1/8`` of a whole note after the right edge of the 
    first third of segment ``'red'``::
    
        >>> symbolictimetools.SymbolicOffset(selector=segment_selector, edge=Right, 
        ... multiplier=Multiplier(1, 3), addendum=durationtools.Offset(1, 8))
        SymbolicOffset(selector=SingleSegmentSymbolicTimespan(identifier='red'), edge=Right, multiplier=Multiplier(1, 3), addendum=Offset(1, 8))

    Symbolic offset indicating the left edge of note ``10`` that starts
    during segment ``'red'``::

        >>> segment_selector = symbolictimetools.SingleSegmentSymbolicTimespan(identifier='red')
        >>> time_relation = timerelationtools.timespan_2_starts_during_timespan_1(timespan_1=segment_selector.timespan)
        >>> counttime_component_selector = symbolictimetools.CounttimeComponentSymbolicTimespan(
        ... time_relation=time_relation, klass=Note, start_identifier=10, stop_identifier=11)
        >>> time_relation = timerelationtools.timespan_2_starts_during_timespan_1()
        >>> counttime_component_selector = symbolictimetools.CounttimeComponentSymbolicTimespan(
        ... anchor='red', klass=Note, start_identifier=10, stop_identifier=11, time_relation=time_relation)

    ::

        >>> offset = symbolictimetools.SymbolicOffset(selector=counttime_component_selector)

    ::

        >>> z(offset)
        symbolictimetools.SymbolicOffset(
            selector=symbolictimetools.CounttimeComponentSymbolicTimespan(
                anchor='red',
                klass=notetools.Note,
                start_identifier=10,
                stop_identifier=11,
                time_relation=timerelationtools.TimespanTimespanTimeRelation(
                    'timespan_1.start <= timespan_2.start < timespan_1.stop'
                    )
                )
            )

    Timepoint selectors can be arbitrary timespans. This allows recursion into the model.

    Symbolic offset one third of the way into the timespan of segments ``'red'`` through ``'blue'``::

        >>> stop = helpertools.SegmentIdentifierExpression("'blue' + 1")
        >>> segment_slice_selector = symbolictimetools.SegmentSymbolicTimespan(start_identifier='red', stop_identifier=stop)
        >>> timespan = symbolictimetools.SingleSourceSymbolicTimespan(selector=segment_slice_selector)

    ::
    
        >>> offset = symbolictimetools.SymbolicOffset(selector=timespan, edge=Right, multiplier=Multiplier(1, 3))

    ::
    
        >>> z(offset)
        symbolictimetools.SymbolicOffset(
            selector=symbolictimetools.SingleSourceSymbolicTimespan(
                selector=symbolictimetools.SegmentSymbolicTimespan(
                    start_identifier='red',
                    stop_identifier=helpertools.SegmentIdentifierExpression("'blue' + 1")
                    )
                ),
            edge=Right,
            multiplier=durationtools.Multiplier(1, 3)
            )

    Symbolic offset indicating the right edge of note ``10`` that starts
    during segment ``'red'``::

        >>> offset = symbolictimetools.SymbolicOffset(selector=counttime_component_selector, edge=Right)

    ::

        >>> z(offset)
        symbolictimetools.SymbolicOffset(
            selector=symbolictimetools.CounttimeComponentSymbolicTimespan(
                anchor='red',
                klass=notetools.Note,
                start_identifier=10,
                stop_identifier=11,
                time_relation=timerelationtools.TimespanTimespanTimeRelation(
                    'timespan_1.start <= timespan_2.start < timespan_1.stop'
                    )
                ),
            edge=Right
            )

    Symbolic offsets are immutable.
    '''

    ### INITIALIZER ###

    def __init__(self, selector=None, edge=None, multiplier=None, addendum=None): 
        from experimental import symbolictimetools
 
        assert isinstance(selector, (symbolictimetools.TimespanSymbolicTimespan, 
            symbolictimetools.SingleSourceSymbolicTimespan, type(None))), repr(selector)
        assert edge in (Left, Right, None), repr(edge)
        if multiplier is not None:
            multiplier = durationtools.Multiplier(multiplier)
        if addendum is not None:
            addendum = durationtools.Offset(addendum)
        self._selector = selector
        self._multiplier = multiplier
        self._edge = edge
        self._addendum = addendum

    ### SPECIAL METHODS ###

    def __eq__(self, other):
        '''True when `other` is a offset with score object indicator,
        edge and addendum all indicating those of `self`.
        
        Otherwise false.

        Return boolean.
        '''
        if not isinstance(other, type(self)):
            return False
        elif not self.selector == other.selector:
            return False
        elif not self.edge == other.edge:
            return False
        elif not self.multiplier == other.multiplier:
            return False
        elif not self.addendum == other.addendum:
            return False
        else:
            return True

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def addendum(self):
        '''Symbolic offset addendum specified by user.

            >>> offset.addendum is None
            True

        Value of none is interpreted as ``Offset(0)``.
            
        Return offset or none.
        '''
        return self._addendum

    @property
    def edge(self):
        '''Symbolic offset edge indicator specified by user.
        
            >>> offset.edge
            Right

        Value of none is interpreted as ``Left``.

        Return boolean or none.
        '''
        return self._edge

    @property
    def multiplier(self):
        '''Symbolic offset multiplier specified by user.

            >>> offset.multiplier is None
            True

        Value of none is interpreted as ``Multiplier(1)``.

        Return multiplier or none.
        '''
        return self._multiplier

    @property
    def selector(self):
        '''Symbolic offset selector specified by user.
        
            >>> z(offset.selector)
            symbolictimetools.CounttimeComponentSymbolicTimespan(
                anchor='red',
                klass=notetools.Note,
                start_identifier=10,
                stop_identifier=11,
                time_relation=timerelationtools.TimespanTimespanTimeRelation(
                    'timespan_1.start <= timespan_2.start < timespan_1.stop'
                    )
                )

        Value of none is taken equal the entire score.

        Return selector or none.
        '''
        return self._selector

    @property
    def start_segment_identifier(self):
        '''Symbolic offset start segment identifier.

            >>> offset.start_segment_identifier
            'red'

        Delegate to ``self.selector.start_segment_identifier``.

        Return string or none.
        '''
        return self.selector.start_segment_identifier

    ### PUBLIC METHODS ###

    def get_score_offset(self, score_specification, context_name):
        '''Evaluate score offset of symbolic offset when applied
        to `context_name` in `score_specification`.

        .. note:: add example.

        Return offset.
        '''
        edge = self.edge or Left
        start_offset, stop_offset = self.selector.get_offsets(score_specification, context_name)
        if edge == Left:
            score_offset = start_offset
        else:
            score_offset = stop_offset
        multiplier = self.multiplier or durationtools.Multiplier(1)
        score_offset = multiplier * score_offset
        offset = self.addendum or durationtools.Offset(0)
        score_offset = score_offset + offset
        return score_offset
