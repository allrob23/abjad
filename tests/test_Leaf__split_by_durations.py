import abjad
import pytest


def test_Leaf__split_by_durations_01():
    """
    Splits note into assignable notes.

    Does not fracture spanners. Does not tie split notes.
    """

    staff = abjad.Staff("c'8 [ d'8 e'8 ]")

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            e'8
            ]
        }
        """
        ), print(format(staff))

    halves = staff[1]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=False,
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'32
            d'16.
            e'8
            ]
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_02():
    """
    Splits note into assignable notes.

    Fractures spanners. Does not tie split notes.
    """

    staff = abjad.Staff("c'8 [ d'8 e'8 ]")

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            e'8
            ]
        }
        """
        ), print(format(staff))

    halves = staff[1]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'32
            ]
            d'16.
            [
            e'8
            ]
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_03():
    """
    Splits note into assignable notes.

    Does not fracture spanners. Does tie split notes.
    """

    staff = abjad.Staff("c'8 [ d'8 e'8 ]")

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'8
            e'8
            ]
        }
        """
        ), print(format(staff))

    halves = staff[1]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=False,
        tie_split_notes=True,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'32
            ~
            d'16.
            e'8
            ]
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_04():
    """
    Splits note into assignable notes.

    Fractures spanners. Ties split notes.
    """

    staff = abjad.Staff("c'8 [ d'8 e'8 ]")

    halves = staff[1]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=True,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            d'32
            ~
            ]
            d'16.
            [
            e'8
            ]
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_05():
    """
    Adds tuplet.

    Does not fracture spanners. Does not tie split notes.
    """

    staff = abjad.Staff("c'8 [ d'8 e'8 ]")

    halves = staff[1]._split_by_durations(
        [abjad.Duration(1, 24)],
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            c'8
            [
            \times 2/3 {
                d'16
                d'8
            }
            e'8
            ]
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_06():
    """
    REGRESSION.
    
    Splits note into tuplet monads and then fuses monads.

    Does not fracture spanners. Ties split notes.

    This test comes from #272 in GitHub.
    """

    staff = abjad.Staff(r"\times 2/3 { c'8 [ d'8 e'8 ] }")
    leaf = abjad.inspect(staff).leaf(0)
    halves = leaf._split_by_durations([abjad.Duration(1, 20)])

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            \times 2/3 {
                \times 4/5 {
                    c'16.
                    ~
                    [
                    c'16
                }
                d'8
                e'8
                ]
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_07():
    """
    Assignable duration produces two notes.

    This test comes from a container-crossing spanner bug.
    """

    voice = abjad.Voice(r"c'8 \times 2/3 { d'8 e'8 f'8 }")
    leaves = abjad.select(voice).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves)

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            c'8
            [
            \times 2/3 {
                d'8
                e'8
                f'8
                ]
            }
        }
        """
        ), print(format(staff))

    halves = leaves[1]._split_by_durations(
        [abjad.Duration(1, 24)],
        tie_split_notes=False,
        )

    assert format(voice) == abjad.String.normalize(
        r"""
        \new Voice
        {
            c'8
            [
            \times 2/3 {
                d'16
                d'16
                e'8
                f'8
                ]
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(voice).is_wellformed()


def test_Leaf__split_by_durations_08():
    """
    Leaf duration less than split duration produces no change.
    """

    staff = abjad.Staff("c'4")
    staff[0]._split_by_durations([abjad.Duration(3, 4)])

    assert len(staff) == 1
    assert isinstance(staff[0], abjad.Note)
    assert staff[0].written_duration == abjad.Duration(1, 4)


def test_Leaf__split_by_durations_09():
    """
    Returns two lists of zero or more leaves.
    """

    note = abjad.Note("c'4")

    halves = note._split_by_durations(
        [abjad.Duration(1, 8)],
        tie_split_notes=False,
        )

    assert isinstance(halves, list)
    assert len(halves) == 2
    assert len(halves[0]) == 1
    assert len(halves[1]) == 1
    assert isinstance(halves[0][0], abjad.Note)
    assert isinstance(halves[1][0], abjad.Note)
    assert halves[0][0].written_duration == abjad.Duration(1, 8)
    assert halves[1][0].written_duration == abjad.Duration(1, 8)
    assert len(abjad.inspect(halves[0][0]).logical_tie()) == 1
    assert len(abjad.inspect(halves[1][0]).logical_tie()) == 1


def test_Leaf__split_by_durations_10():
    """
    Returns two lists of zero or more leaves.
    """

    note = abjad.Note("c'4")
    halves = note._split_by_durations([abjad.Duration(1, 16)])

    assert isinstance(halves, list)
    assert len(halves) == 2
    assert len(halves[0]) == 1
    assert len(halves[1]) == 1
    assert isinstance(halves[0][0], abjad.Note)
    assert isinstance(halves[1][0], abjad.Note)
    assert halves[0][0].written_duration == abjad.Duration(1, 16)
    assert halves[1][0].written_duration == abjad.Duration(3, 16)


def test_Leaf__split_by_durations_11():
    """
    Nonassignable power-of-two duration produces two lists.

    Left list contains two notes tied together.

    Right list contains only one note.
    """

    note = abjad.Note("c'4")

    halves = note._split_by_durations(
        [abjad.Duration(5, 32)],
        tie_split_notes=False,
        )

    assert isinstance(halves, list)
    assert len(halves) == 2
    assert len(halves[0]) == 2
    assert len(halves[1]) == 1
    assert isinstance(halves[0][0], abjad.Note)
    assert isinstance(halves[0][1], abjad.Note)
    assert isinstance(halves[1][0], abjad.Note)
    assert halves[0][0].written_duration == abjad.Duration(4, 32)
    assert halves[0][1].written_duration == abjad.Duration(1, 32)
    assert halves[1][0].written_duration == abjad.Duration(3, 32)
    assert len(abjad.inspect(halves[0][0]).logical_tie()) == 2
    assert len(abjad.inspect(halves[0][1]).logical_tie()) == 2
    assert len(abjad.inspect(halves[1][0]).logical_tie()) == 1


def test_Leaf__split_by_durations_12():
    """
    Lone spanned leaf results in two spanned leaves.
    """

    staff = abjad.Staff([abjad.Note("c'4")])
    tie = abjad.Tie()
    abjad.attach(tie, staff[:])
    halves = staff[0]._split_by_durations([abjad.Duration(1, 8)])

    assert len(staff) == 2
    for leaf in staff[:]:
        assert abjad.inspect(leaf).spanners() == [tie]
        prototype = (abjad.Tie,)
        assert abjad.inspect(leaf).spanner(prototype) is tie

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_13():
    """
    Leaves spanners unchanged.
    """

    staff = abjad.Staff("c'8 c'8 c'8 c'8")
    beam = abjad.Beam()
    abjad.attach(beam, staff[:])

    halves = staff[0]._split_by_durations(
        [abjad.Duration(1, 16)],
        tie_split_notes=False,
        )

    assert len(staff) == 5
    for l in staff:
        assert abjad.inspect(l).spanners() == [beam]
        assert l._get_spanner(abjad.Beam) is beam

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_14():
    """
    Returns three leaves with two tied.

    Spanner is shared by all 3 leaves.
    """

    staff = abjad.Staff([abjad.Note("c'4")])
    tie = abjad.Tie()
    abjad.attach(tie, staff[:])
    halves = staff[0]._split_by_durations([abjad.Duration(5, 32)])

    assert len(halves) == 2
    assert len(halves[0]) == 2
    assert len(halves[1]) == 1
    for l in staff:
        assert abjad.inspect(l).spanners() == [tie]
        assert abjad.inspect(l).spanner(abjad.Tie) is tie

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_15():
    """
    After grace notes are removed from first split leaf.
    """

    note = abjad.Note("c'4")
    after_grace = abjad.AfterGraceContainer([abjad.Note(0, (1, 32))])
    abjad.attach(after_grace, note)
    halves = note._split_by_durations([abjad.Duration(1, 8)])

    assert abjad.inspect(halves[0][0]).after_grace_container() is None
    assert len(abjad.inspect(halves[1][0]).after_grace_container()) == 1


def test_Leaf__split_by_durations_16():
    """
    After grace notes are removed from first split leaf.
    """

    note = abjad.Note("c'4")
    grace = abjad.AfterGraceContainer([abjad.Note(0, (1, 32))])
    abjad.attach(grace, note)
    halves = note._split_by_durations([abjad.Duration(5, 32)])

    assert len(halves) == 2
    assert getattr(halves[0][0], 'after_grace', None) is None
    assert getattr(halves[0][1], 'after_grace', None) is None
    assert len(halves[1]) == 1
    after_grace = abjad.inspect(halves[1][0]).after_grace_container()
    assert len(after_grace) == 1


def test_Leaf__split_by_durations_17():
    """
    Grace notes are removed from second split leaf.
    """

    note = abjad.Note("c'4")
    grace = abjad.GraceContainer([abjad.Note(0, (1, 32))])
    abjad.attach(grace, note)
    halves = note._split_by_durations([abjad.Duration(1, 16)])

    assert len(halves[0]) == 1
    assert len(halves[1]) == 1
    grace_container = abjad.inspect(halves[0][0]).grace_container()
    assert len(grace_container) == 1
    assert not hasattr(halves[1][0], 'grace') is None


def test_Leaf__split_by_durations_18():

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves[:2])
    beam = abjad.Beam()
    abjad.attach(beam, leaves[-2:])
    slur = abjad.Slur()
    abjad.attach(slur, leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    halves = leaves[0]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=False,
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'32
                [
                (
                c'16.
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_19():
    """
    Split one leaf in score.
    Do not fracture spanners. But do tie after split.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam()
    abjad.attach(beam, leaves[:2])
    beam = abjad.Beam()
    abjad.attach(beam, leaves[-2:])
    slur = abjad.Slur()
    abjad.attach(slur, leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    halves = leaves[0]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=False,
        tie_split_notes=True,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'32
                ~
                [
                (
                c'16.
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_20():
    """
    Split leaf in score and fracture spanners.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[:2])
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[-2:])
    slur = abjad.Slur()
    abjad.attach(slur, leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    halves = leaves[0]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'32
                [
                ]
                c'16.
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_21():
    """
    Split leaf in score at nonzero index.
    Fracture spanners.
    Test comes from a bug fix.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[:2])
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[-2:])
    slur = abjad.Slur()
    abjad.attach(slur, leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    halves = leaves[1]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=False,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'32
                ]
                )
                d'16.
                [
                ]
                (
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_22():
    """
    Split leaf outside of score and fracture spanners.
    """

    note = abjad.Note("c'8")
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, abjad.select(note))

    assert format(note) == "c'8\n[\n]"

    halves = note._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        )

    assert format(halves[0][0]) == "c'32\n~\n[\n]"
    assert abjad.inspect(halves[0][0]).is_wellformed()

    assert format(halves[1][0]) == "c'16.\n[\n]"
    assert abjad.inspect(halves[1][0]).is_wellformed()


def test_Leaf__split_by_durations_23():
    """
    Split leaf in score and fracture spanners.
    Tie leaves after split.
    """

    staff = abjad.Staff()
    staff.append(abjad.Container("c'8 d'8"))
    staff.append(abjad.Container("e'8 f'8"))
    leaves = abjad.select(staff).leaves()
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[:2])
    beam = abjad.Beam(beam_lone_notes=True)
    abjad.attach(beam, leaves[-2:])
    slur = abjad.Slur()
    abjad.attach(slur, leaves)

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'8
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    halves = leaves[0]._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=True,
        )

    assert format(staff) == abjad.String.normalize(
        r"""
        \new Staff
        {
            {
                c'32
                ~
                [
                ]
                c'16.
                [
                (
                d'8
                ]
            }
            {
                e'8
                [
                f'8
                ]
                )
            }
        }
        """
        ), print(format(staff))

    assert abjad.inspect(staff).is_wellformed()


def test_Leaf__split_by_durations_24():
    """
    Split leaf with LilyPond multiplier.
    Split at split offset with power-of-two denominator.
    Halves carry original written duration.
    Halves carry adjusted LilyPond multipliers.
    """

    note = abjad.Note(0, (1, 8))
    abjad.attach(abjad.Multiplier(1, 2), note)

    assert format(note) == "c'8 * 1/2"

    halves = note._split_by_durations(
        [abjad.Duration(1, 32)],
        fracture_spanners=True,
        tie_split_notes=False,
        )

    assert format(halves[0][0]) == "c'8 * 1/4"
    assert format(halves[1][0]) == "c'8 * 1/4"

    assert abjad.inspect(halves[0][0]).is_wellformed()
    assert abjad.inspect(halves[1][0]).is_wellformed()


def test_Leaf__split_by_durations_25():
    """
    Split leaf with LilyPond multiplier.
    Split at offset without power-of-two denominator.
    Halves carry original written duration.
    Halves carry adjusted LilyPond multipliers.
    """

    note = abjad.Note(0, (1, 8))
    abjad.attach(abjad.Multiplier(1, 2), note)

    assert format(note) == "c'8 * 1/2"

    halves = note._split_by_durations(
        [abjad.Duration(1, 48)],
        fracture_spanners=True,
        tie_split_notes=False,
        )

    assert format(halves[0][0]) == "c'8 * 1/6"
    assert format(halves[1][0]) == "c'8 * 1/3"

    assert abjad.inspect(halves[0][0]).is_wellformed()
    assert abjad.inspect(halves[1][0]).is_wellformed()
