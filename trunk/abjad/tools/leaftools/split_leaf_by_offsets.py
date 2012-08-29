import copy
from abjad.tools import durationtools
from abjad.tools import sequencetools
from abjad.tools import pitchtools


def split_leaf_by_offsets(leaf, offsets, cyclic=False, 
    fracture_spanners=False, tie_split_notes=True, tie_split_rests=False):
    r'''.. versionadded:: 2.10

    Split `leaf` by `offsets`.

    Example 1. Split note once by `offsets` and tie split notes::

        >>> staff = Staff("c'1 ( d'1 )")

    ::

        >>> f(staff)
        \new Staff {
            c'1 (
            d'1 )
        }

    ::

        >>> leaftools.split_leaf_by_offsets(staff[0], [(3, 8)], tie_split_notes=True)
        [[Note("c'4.")], [Note("c'2"), Note("c'8")]]

    ::

        >>> f(staff)
        \new Staff {
            c'4. ( ~
            c'2 ~
            c'8
            d'1 )
        }

    Example 2. Split note cyclically by `offsets` and tie split notes::

        >>> staff = Staff("c'1 ( d'1 )")

    ::

        >>> f(staff)
        \new Staff {
            c'1 (
            d'1 )
        }

    ::

        >>> leaftools.split_leaf_by_offsets(staff[0], [(3, 8)], cyclic=True, tie_split_notes=True)
        [[Note("c'4.")], [Note("c'4.")], [Note("c'4")]]

    ::

        >>> f(staff)
        \new Staff {
            c'4. ( ~
            c'4. ~
            c'4
            d'1 )
        }

    Example 3. Split note once by `offsets` and do no tie split notes::

        >>> staff = Staff("c'1 ( d'1 )")

    ::

        >>> f(staff)
        \new Staff {
            c'1 (
            d'1 )
        }

    ::

        >>> leaftools.split_leaf_by_offsets(staff[0], [(3, 8)], tie_split_notes=False)
        [[Note("c'4.")], [Note("c'2"), Note("c'8")]]

    ::

        >>> f(staff)
        \new Staff {
            c'4. (
            c'2 ~
            c'8
            d'1 )
        }

    Example 4. Split note cyclically by `offsets` and do not tie split notes::

        >>> staff = Staff("c'1 ( d'1 )")

    ::

        >>> f(staff)
        \new Staff {
            c'1 (
            d'1 )
        }

    ::

        >>> leaftools.split_leaf_by_offsets(staff[0], [(3, 8)], cyclic=True, tie_split_notes=False)
        [[Note("c'4.")], [Note("c'4.")], [Note("c'4")]]

    ::

        >>> f(staff)
        \new Staff {
            c'4. (
            c'4.
            c'4
            d'1 )
        }

    .. note:: Add examples showing mark and context mark handling.

    Return list of shards.
    '''
    from abjad.tools import componenttools
    from abjad.tools import contexttools
    from abjad.tools import gracetools
    from abjad.tools import leaftools
    from abjad.tools import marktools
    from abjad.tools import spannertools
    from abjad.tools import tietools
    
    assert isinstance(leaf, leaftools.Leaf) 
    offsets = [durationtools.Offset(offset) for offset in offsets]

    if cyclic:
        offsets = sequencetools.repeat_sequence_to_weight_exactly(offsets, leaf.written_duration)

    durations = [durationtools.Duration(offset) for offset in offsets]

    if sum(durations) < leaf.written_duration:
        last_duration = leaf.written_duration - sum(durations)
        durations.append(last_duration) 

    sequencetools.truncate_sequence_to_weight(durations, leaf.written_duration)

    result = []
    leaf_copy = copy.deepcopy(leaf)
    for duration in durations:
        new_leaf = copy.deepcopy(leaf)
        shard = leaftools.set_preprolated_leaf_duration(new_leaf, duration)
        result.append(shard)

    flattened_result = sequencetools.flatten_sequence(result)
    componenttools.move_parentage_and_spanners_from_components_to_components([leaf], flattened_result)

    if fracture_spanners:
        first_shard = result[0]
        spannertools.fracture_spanners_attached_to_component(first_shard[-1], direction=Right) 
        last_shard = result[-1]
        spannertools.fracture_spanners_attached_to_component(last_shard[0], direction=Left) 
        for middle_shard in result[1:-1]:
            spannertools.fracture_spanners_attached_to_component(middle_shard[0], direction=Left) 
            spannertools.fracture_spanners_attached_to_component(middle_shard[-1], direction=Right) 
    
    # adjust first leaf
    first_leaf = flattened_result[0]
    gracetools.detach_grace_containers_attached_to_leaf(leaf, kind='after')

    # adjust any middle leaves
    for middle_leaf in flattened_result[1:-1]:
        gracetools.detach_grace_containers_attached_to_leaf(middle_leaf, kind='grace')
        gracetools.detach_grace_containers_attached_to_leaf(leaf, kind='after')
        marktools.detach_marks_attached_to_component(middle_leaf)
        contexttools.detach_context_marks_attached_to_component(middle_leaf)

    # adjust last leaf
    last_leaf = flattened_result[-1]
    gracetools.detach_grace_containers_attached_to_leaf(last_leaf, kind='grace')
    marktools.detach_marks_attached_to_component(last_leaf)
    contexttools.detach_context_marks_attached_to_component(last_leaf)

    # tie split notes, rests or chords as specified
    if  (pitchtools.is_pitch_carrier(leaf) and tie_split_notes) or \
        (not pitchtools.is_pitch_carrier(leaf) and tie_split_rests):
        tietools.remove_tie_spanners_from_components_in_expr(flattened_result)
        tietools.TieSpanner(flattened_result)
     
    # return result
    return result
