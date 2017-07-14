# -*- coding: utf-8 -*-
import numbers
from abjad.tools.pitchtools.NamedIntervalClass import NamedIntervalClass


class NamedInversionEquivalentIntervalClass(NamedIntervalClass):
    '''Named inversion-equivalent interval-class.

    ::

        >>> import abjad

    ..  container:: example

        Initializes from string:

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('-m14')
            NamedInversionEquivalentIntervalClass('+M2')

    ..  container:: example

        Initializes from quality string and number:

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('perfect', 1)
            NamedInversionEquivalentIntervalClass('P1')

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('perfect', -1)
            NamedInversionEquivalentIntervalClass('P1')

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('augmented', 4)
            NamedInversionEquivalentIntervalClass('+aug4')

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('augmented', -4)
            NamedInversionEquivalentIntervalClass('+aug4')

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('augmented', 11)
            NamedInversionEquivalentIntervalClass('+aug4')

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass('augmented', -11)
            NamedInversionEquivalentIntervalClass('+aug4')

    ..  container:: example

        Initializes from other interval-class:

        ::

            >>> interval_class = abjad.NamedInversionEquivalentIntervalClass(
            ...     'perfect',
            ...     1,
            ...     )
            >>> abjad.NamedInversionEquivalentIntervalClass(interval_class)
            NamedInversionEquivalentIntervalClass('P1')

    Named inversion-equivalent interval-classes are immutable.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_number',
        '_quality_string',
        )

    ### INITIALIZER ###

    def __init__(self, *arguments):
        from abjad.tools import pitchtools
        if len(arguments) == 1 and isinstance(arguments[0], type(self)):
            self._initialize_by_self_reference(arguments[0])
        elif len(arguments) == 1 and isinstance(arguments[0], str):
            self._initialize_by_string(arguments[0])
        elif len(arguments) == 1 and isinstance(arguments[0],
            pitchtools.NamedIntervalClass):
            self._initialize_by_string(str(arguments[0]))
        elif len(arguments) == 1 and isinstance(arguments[0],
            pitchtools.NamedInterval):
            interval_class = pitchtools.NamedIntervalClass(arguments[0])
            self._initialize_by_string(str(interval_class))
        elif len(arguments) == 1 and isinstance(arguments[0], tuple):
            self._initialize_by_quality_string_and_number(*arguments[0])
        elif len(arguments) == 2:
            self._initialize_by_quality_string_and_number(*arguments)
        elif len(arguments) == 0:
            self._initialize_by_string('P1')
        else:
            message = 'can not initialize {}: {!r}.'
            message = message.format(type(self).__name__, arguments)
            raise ValueError(message)

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        r'''Is true when `argument` is a named inversion-equivalent
        interval-class with quality string and number equal to those of this
        named inversion-equivalent interval-class. Otherwise false.

        Returns true or false.
        '''
        # custom definition because __init__(*arguments):
        if isinstance(argument, type(self)):
            if self.quality_string == argument.quality_string:
                if self.number == argument.number:
                    return True
        return False

    def __hash__(self):
        r'''Required to be explicitly redefined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(NamedInversionEquivalentIntervalClass, self).__hash__()

    def __ne__(self, argument):
        r'''Is true when named inversion-equivalent interval-class does not
        equal `argument`. Otherwise false.

        Returns true or false.
        '''
        return not self == argument

    ### PRIVATE METHODS ###

    def _initialize_by_quality_string_and_number(self, quality_string, number):
        if number == 0:
            message = 'named interval can not equal zero.'
            raise ValueError(message)
        elif abs(number) == 1:
            number = 1
        elif abs(number) % 7 == 0:
            number = 7
        elif abs(number) % 7 == 1:
            number = 8
        else:
            number = abs(number) % 7
        if self._is_representative_number(number):
            quality_string = quality_string
            number = number
        else:
            quality_string = self._invert_quality_string(quality_string)
            number = 9 - number
        self._quality_string = quality_string
        self._number = number

    def _initialize_by_self_reference(self, reference):
        quality_string = reference.quality_string
        number = reference.number
        self._initialize_by_quality_string_and_number(quality_string, number)

    def _initialize_by_string(self, string):
        from abjad.tools import pitchtools
        match = pitchtools.Interval._interval_name_abbreviation_regex.match(string)
        if match is None:
            raise ValueError(
                '{!r} does not have the form of a hdi abbreviation.'.format(
                string))
        direction_string, quality_abbreviation, number_string = \
            match.groups()
        quality_string = self._quality_abbreviation_to_quality_string[
            quality_abbreviation]
        number = int(number_string)
        self._initialize_by_quality_string_and_number(quality_string, number)

    def _invert_quality_string(self, quality_string):
        inversions = {
            'major': 'minor',
            'minor': 'major',
            'perfect': 'perfect',
            'augmented': 'diminished',
            'diminished': 'augmented',
            }
        return inversions[quality_string]

    def _is_representative_number(self, argument):
        if isinstance(argument, numbers.Number):
            if 1 <= argument <= 4 or argument == 8:
                return True
        return False

    ### PUBLIC METHODS ###

    @classmethod
    def from_pitch_carriers(class_, pitch_carrier_1, pitch_carrier_2):
        '''Makes named inversion-equivalent interval-class from
        `pitch_carrier_1` and `pitch_carrier_2`.

        ::

            >>> abjad.NamedInversionEquivalentIntervalClass.from_pitch_carriers(
            ...     abjad.NamedPitch(-2),
            ...     abjad.NamedPitch(12),
            ...     )
            NamedInversionEquivalentIntervalClass('+M2')

        Returns named inversion-equivalent interval-class.
        '''
        from abjad.tools import pitchtools
        named_interval = pitchtools.NamedInterval.from_pitch_carriers(
            pitch_carrier_1, pitch_carrier_2)
        return class_(named_interval)
