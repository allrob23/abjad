from abjad.tools import componenttools
from abjad.tools import datastructuretools


def get_effective_context_mark(component, context_mark_class):
    r'''.. versionadded:: 2.0

    Get effective context mark of `context_mark_class` from `component`:

    ::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> contexttools.TimeSignatureMark((4, 8))(staff)
        TimeSignatureMark((4, 8))(Staff{4})

    ::

        >>> f(staff)
        \new Staff {
            \time 4/8
            c'8
            d'8
            e'8
            f'8
        }

    ::

        >>> contexttools.get_effective_context_mark(
        ...     staff[0], contexttools.TimeSignatureMark)
        TimeSignatureMark((4, 8))(Staff{4})

    Return context mark or none.
    '''
    from abjad.tools import contexttools
    from abjad.tools import measuretools

    # check input
    assert isinstance(component, componenttools.Component)

    # do special things for time signature marks
    if context_mark_class == contexttools.TimeSignatureMark:
        if isinstance(component, measuretools.Measure):
            if not getattr(component, '_time_signature_is_current', True):
                component._update_time_signature()
            if component._has_mark(contexttools.TimeSignatureMark):
                return component.get_mark(contexttools.TimeSignatureMark)

    # updating marks of entire score tree if necessary
    component._update_marks_of_entire_score_tree_if_necessary()

    # gathering candidate marks
    candidate_marks = datastructuretools.SortedCollection(
        key=lambda x: x.start_component.timespan.start_offset)
    for parent in component.select_parentage(include_self=True):
        parent_marks = parent._dependent_context_marks
        for mark in parent_marks:
            if isinstance(mark, context_mark_class):
                if mark.effective_context is not None:
                    candidate_marks.insert(mark)
                elif isinstance(mark, contexttools.TimeSignatureMark):
                    if isinstance(mark.start_component, measuretools.Measure):
                        candidate_marks.insert(mark)

    # elect most recent candidate mark
    if candidate_marks:
        try:
            return candidate_marks.find_le(component.timespan.start_offset)
        except ValueError:
            pass
