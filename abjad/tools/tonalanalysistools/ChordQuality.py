# -*- coding: utf-8 -*-
from abjad.tools.abctools import AbjadValueObject


class ChordQuality(AbjadValueObject):
    '''Chord quality. Major, minor, dominant, diminished and so on.

    ::

        >>> from abjad.tools import tonalanalysistools

    Chord qualities are immutable.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_quality_string',
        )

    _acceptable_quality_strings = (
        'augmented',
        'diminished',
        'dominant',
        'half diminished',
        'major',
        'minor',
        )

    _uppercase_quality_strings = (
        'augmented',
        'dominant',
        'major',
        )

    ### INITIALIZER ###

    def __init__(self, quality_string='major'):
        if quality_string not in self._acceptable_quality_strings:
            message = 'can not initialize chord quality: {!r}.'
            message = message.format(quality_string)
            raise ValueError(message)
        self._quality_string = quality_string

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        r'''Is true when `argument` is a chord quality with quality string equal to
        that of this chord quality. Otherwise false.

        Returns true or false.
        '''
#        if isinstance(argument, type(self)):
#            if self.quality_string == argument.quality_string:
#                return True
#        return False
        return super(ChordQuality, self).__eq__(argument)

    def __hash__(self):
        r'''Hashes chord quality.

        Required to be explicitly redefined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(ChordQuality, self).__hash__()

    def __ne__(self, argument):
        r'''Is true when chord quality does not equal `argument`. Otherwise false.

        Returns true or false.
        '''
        return not self == argument

    def __repr__(self):
        r'''Gets interpreter representation of chord quality.

        Returns string.
        '''
        return '{}({})'.format(type(self).__name__, self.quality_string)

    ### PUBLIC PROPERTIES ###

    @property
    def is_uppercase(self):
        r'''Is true when chord quality is uppercase. Otherwise false.

        Returns true or false.
        '''
        return self.quality_string in self._uppercase_quality_strings

    @property
    def quality_string(self):
        r'''Quality string of chord quality.

        Returns string.
        '''
        return self._quality_string
