# -*- encoding: utf-8 -*-
from abjad.tools import componenttools
from abjad.tools import selectiontools
Selection = selectiontools.Selection


def get_spanners_that_dominate_component_pair(left, right):
    r'''Return Python list of (spanner, index) pairs.
    'left' must be either an Abjad component or None.
    'right' must be either an Abjad component or None.

    If both 'left' and 'right' are components,
    then 'left' and 'right' must be logical-voice-contiguous.

    This is a special version of 
    spannertools.get_spanners_that_dominate_components().
    This version is useful for finding spanners that dominant
    a zero-length 'crack' between components, as in t[2:2].

    Return spanners.
    '''
    from abjad.tools import spannertools

    if left is None or right is None:
        return set([])

    assert Selection._all_are_contiguous_components_in_same_logical_voice(
        [left, right])

    left_contained = left._get_descendants()._get_spanners()
    right_contained = right._get_descendants()._get_spanners()
    dominant_spanners = left_contained & right_contained

    right_start_offset = right._get_timespan().start_offset
    components_after_gap = []
    for component in right._get_lineage():
        if component._get_timespan().start_offset == right_start_offset:
            components_after_gap.append(component)

    receipt = set([])
    for spanner in dominant_spanners:
        for component in components_after_gap:
            if component in spanner:
                index = spanner.index(component)
                receipt.add((spanner, index))
                continue

    return receipt
