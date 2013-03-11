def offset_happens_during_timespan(timespan=None, offset=None, hold=False):
    r'''.. versionadded:: 2.11

    Make time relation indicating that `offset` happens during `timespan`:

    ::

        >>> z(timerelationtools.offset_happens_during_timespan())
        timerelationtools.OffsetTimespanTimeRelation(
            'timespan.start <= offset < timespan.stop',
            ['timespan.start <= offset', 'offset < timespan.stop']
            )

    '''
    from abjad.tools import timerelationtools

    time_relation = timerelationtools.OffsetTimespanTimeRelation(
        'timespan.start <= offset < timespan.stop',
        [
            'timespan.start <= offset',
            'offset < timespan.stop',
        ],
        timespan=timespan, offset=offset)

    if time_relation.is_fully_loaded and not hold:
        return time_relation()
    else:
        return time_relation
