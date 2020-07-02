import abjad


def test_Container___init___01():
    """
    Initialize empty container.
    """

    container = abjad.Container([])

    assert isinstance(container, abjad.Container)
    assert format(container) == abjad.String.normalize(
        r"""
        {
        }
        """
    )


def test_Container___init___02():
    """
    Initialize container with LilyPond note-entry string.
    """

    container = abjad.Container("c'8 d'8 e'8")

    assert isinstance(container, abjad.Container)
    assert format(container) == abjad.String.normalize(
        r"""
        {
            c'8
            d'8
            e'8
        }
        """
    )
