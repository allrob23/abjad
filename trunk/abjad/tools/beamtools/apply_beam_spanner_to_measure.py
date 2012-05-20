from abjad.tools import measuretools


def apply_beam_spanner_to_measure(measure):
    r'''.. versionadded:: 2.0

    Apply beam spanner to `measure`::

        abjad> measure = Measure((2, 8), "c'8 d'8")

    ::

        abjad> f(measure)
        {
            \time 2/8
            c'8
            d'8
        }

    ::

        abjad> beamtools.apply_beam_spanner_to_measure(measure)
        BeamSpanner(|2/8(2)|)

    ::

        abjad> f(measure)
        {
            \time 2/8
            c'8 [
            d'8 ]
        }

    Return beam spanner.

    .. versionchanged:: 2.9
        renamed ``measuretools.apply_beam_spanner_to_measure()`` to
        ``beamtools.apply_beam_spanner_to_measure()``.
    '''
    from abjad.tools import beamtools

    # check measure type
    if not isinstance(measure, measuretools.Measure):
        raise TypeError('must be measure: {!r}'.format(measure))

    # apply beam spanner to measure
    beam = beamtools.BeamSpanner(measure)

    # return beam spanner
    return beam
