from abjad import *
import py.test


def test_spannertools_get_the_only_spanner_attached_to_any_improper_parent_of_component_01():
    '''Without klass keyword.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    beam = beamtools.BeamSpanner(staff.leaves[:-1])
    slur = spannertools.SlurSpanner(staff.leaves[:-1])
    trill = spannertools.TrillSpanner(staff)

    r'''
    \new Staff {
        c'8 [ ( \startTrillSpan
        d'8
        e'8 ] )
        f'8 \stopTrillSpan
    }
    '''

    assert spannertools.get_the_only_spanner_attached_to_any_improper_parent_of_component(
        staff) == trill

    assert py.test.raises(ExtraSpannerError,
        'spannertools.get_the_only_spanner_attached_to_component(staff[0])')

    assert spannertools.get_the_only_spanner_attached_to_any_improper_parent_of_component(
        staff[-1]) == trill
