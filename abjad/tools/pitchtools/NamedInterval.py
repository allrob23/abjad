# -*- coding: utf-8 -*-
import copy
import functools
from abjad.tools import mathtools
from abjad.tools.pitchtools.Interval import Interval
from abjad.tools.topleveltools import new


@functools.total_ordering
class NamedInterval(Interval):
    '''Named interval.

    ::

        >>> import abjad

    ..  container:: example

        Initializes ascending major ninth from string:

        ::

            >>> abjad.NamedInterval('+M9')
            NamedInterval('+M9')

    ..  container:: example

        Initializes descending major third from number of semitones:

        ::

            >>> abjad.NamedInterval(-4)
            NamedInterval('-M3')

    ..  container:: example

        Initializes from other named interval:

        ::

            >>> abjad.NamedInterval(abjad.NamedInterval(-4))
            NamedInterval('-M3')

    ..  container:: example

        Initializes from quality string and interval number:

        ::

            >>> abjad.NamedInterval('major', -3)
            NamedInterval('-M3')

    '''

    ### CLASS VARIABLES ##

    __slots__ = (
        '_number',
        '_quality_string',
        )

    _acceptable_quality_strings = (
        'perfect',
        'major',
        'minor',
        'diminished',
        'augmented',
        )

    _quality_abbreviation_to_quality_string = {
        'M': 'major',
        'm': 'minor',
        'P': 'perfect',
        'aug': 'augmented',
        'dim': 'diminished',
        }

    _semitones_to_quality_string_and_number = {
        0: ('perfect', 1),
        1: ('minor', 2),
        2: ('major', 2),
        3: ('minor', 3),
        4: ('major', 3),
        5: ('perfect', 4),
        6: ('diminished', 5),
        7: ('perfect', 5),
        8: ('minor', 6),
        9: ('major', 6),
        10: ('minor', 7),
        11: ('major', 7),
        }

    ### INITIALIZER ###

    def __init__(self, *arguments):
        from abjad.tools import pitchtools
        if len(arguments) == 1:
            if isinstance(arguments[0], type(self)):
                quality_string = arguments[0].quality_string
                number = arguments[0].number
            elif isinstance(arguments[0], str):
                match = \
                    pitchtools.Interval._interval_name_abbreviation_regex.match(
                        arguments[0])
                if match is None:
                    message = '{!r} does not have the form of a mdi abbreviation.'
                    message = message.format(arguments[0])
                    raise ValueError(message)
                direction_string, quality_abbreviation, number_string = \
                    match.groups()
                quality_string = self._quality_abbreviation_to_quality_string[
                    quality_abbreviation]
                number = int(direction_string + number_string)
            elif isinstance(arguments[0], pitchtools.NamedIntervalClass):
                quality_string = arguments[0].quality_string
                number = arguments[0].number
            elif isinstance(arguments[0], (
                int,
                float,
                int,
                pitchtools.NumberedInterval,
                pitchtools.NumberedIntervalClass,
                )):
                number = int(arguments[0])
                sign = mathtools.sign(number)
                octaves, semitones = divmod(abs(number), 12)
                quality_string, number = \
                    self._semitones_to_quality_string_and_number[semitones]
                number += abs(octaves) * 7
                if sign == -1:
                    number *= -1
            else:
                message = 'can not initialize {}: {!r}'
                message = message.format(type(self).__init__, arguments)
                raise ValueError(message)
        elif len(arguments) == 2:
            quality_string, number = arguments
        elif len(arguments) == 0:
            quality_string = 'perfect'
            number = 1
        else:
            message = 'can not initialize {}: {!r}'
            message = message.format(type(self).__init__, arguments)
            raise ValueError(message)
        self._quality_string = quality_string
        self._number = number

    ### SPECIAL METHODS ###

    def __abs__(self):
        r'''Absolute value of named interval.

        ..  container:: example

            ::

                >>> abs(abjad.NamedInterval('+M9'))
                NamedInterval('+M9')

            ::

                >>> abs(abjad.NamedInterval('-M9'))
                NamedInterval('+M9')

        Returns named interval.
        '''
        return type(self)(self.quality_string, abs(self.number))

    def __add__(self, argument):
        r'''Adds `argument` to named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('M9') + abjad.NamedInterval('M2')
                NamedInterval('+M10')

        Returns new named interval.
        '''
        from abjad.tools import pitchtools
        if not isinstance(argument, type(self)):
            message = 'must be named interval: {!r}.'
            message = message.format(argument)
            raise TypeError(message)
        dummy_pitch = pitchtools.NamedPitch(0)
        new_pitch = dummy_pitch + self + argument
        return pitchtools.NamedInterval.from_pitch_carriers(
            dummy_pitch, new_pitch)

    def __copy__(self, *arguments):
        r'''Copies named interval.

        ::

            >>> import copy

        ..  container:: example

            ::

                >>> copy.copy(abjad.NamedInterval('+M9'))
                NamedInterval('+M9')

        Returns new named interval.
        '''
        return type(self)(self.quality_string, self.number)

    def __eq__(self, argument):
        r'''Is true when named interval equal `argument`.
        Otherwise false.

        ..  container:: example

            ::

                >>> interval_1 = abjad.NamedInterval('m2')
                >>> interval_2 = abjad.NamedInterval('m2')
                >>> interval_3 = abjad.NamedInterval('m9')

            ::

                >>> interval_1 == interval_1
                True

            ::

                >>> interval_1 == interval_2
                True

            ::

                >>> interval_1 == interval_3
                False

            ::

                >>> interval_2 == interval_1
                True

            ::

                >>> interval_2 == interval_2
                True

            ::

                >>> interval_2 == interval_3
                False

            ::

                >>> interval_3 == interval_1
                False

            ::

                >>> interval_3 == interval_2
                False

            ::

                >>> interval_3 == interval_3
                True

        '''
        return super(NamedInterval, self).__eq__(argument)

    def __float__(self):
        r'''Changes number of named interval to a float.

        ..  container:: example

            ::

                >>> float(abjad.NamedInterval('+M9'))
                9.0

        Returns float.
        '''
        return float(self._number)

    def __hash__(self):
        r'''Hashes named interval.

        Returns number.
        '''
        return super(NamedInterval, self).__hash__()
        
    def __int__(self):
        r'''Returns number of named interval.

        ..  container:: example

            ::

                >>> int(abjad.NamedInterval('+M9'))
                9

        Returns integer.
        '''
        return self._number

    def __lt__(self, argument):
        r'''Is true when `argument` is a named interval with a number greater
        than that of this named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9') < abjad.NamedInterval('+M10')
                True

        ..  container:: example

            Also true when `argument` is a named interval with a
            number equal to this named interval and with semitones greater than
            this named interval:

            ::

                >>> abjad.NamedInterval('+m9') < abjad.NamedInterval('+M9')
                True

        ..  container:: example

            Otherwise false:

            ::

                >>> abjad.NamedInterval('+M9') < abjad.NamedInterval('+M2')
                False

        Returns true or false.
        '''
        if isinstance(argument, type(self)):
            if self.number == argument.number:
                return self.semitones < argument.semitones
            return self.number < argument.number
        return False

    def __mul__(self, argument):
        r'''Multiplies named interval by `argument`.

        ..  container:: example

            ::

                >>> 3 * abjad.NamedInterval('+M9')
                NamedInterval('+aug25')

        Returns new named interval.
        '''
        from abjad.tools import pitchtools
        if not isinstance(argument, int):
            message = 'must be integer: {!r}.'
            message = message.format(argument)
            raise TypeError(message)
        dummy_pitch = pitchtools.NamedPitch(0)
        for i in range(abs(argument)):
            dummy_pitch += self
        result = pitchtools.NamedInterval.from_pitch_carriers(
            pitchtools.NamedPitch(0), dummy_pitch)
        if argument < 0:
            return -result
        return result

    def __neg__(self):
        r'''Negates named interval.

        ..  container:: example

            ::

                >>> -abjad.NamedInterval('+M9')
                NamedInterval('-M9')

        ..  container:: example

            ::

                >>> -abjad.NamedInterval('-M9')
                NamedInterval('+M9')

        Returns new named interval.
        '''
        return type(self)(self.quality_string, -self.number)

    def __rmul__(self, argument):
        r'''Multiplies `argument` by named interval.

        ::

            >>> abjad.NamedInterval('+M9') * 3
            NamedInterval('+aug25')

        Returns new named interval.
        '''
        return self * argument

    def __str__(self):
        r'''String representation of named interval.

        ..  container:: example

            ::

                >>> str(abjad.NamedInterval('+M9'))
                '+M9'

        Returns string.
        '''
        return '{}{}{}'.format(
            self._direction_symbol,
            self._quality_abbreviation,
            abs(self.number),
            )

    def __sub__(self, argument):
        r'''Subtracts `argument` from named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9') - abjad.NamedInterval('+M2')
                NamedInterval('+P8')

            ::

                >>> abjad.NamedInterval('+M2') - abjad.NamedInterval('+M9')
                NamedInterval('-P8')

        Returns new named interval.
        '''
        from abjad.tools import pitchtools
        if not isinstance(argument, type(self)):
            message = 'must be named interval: {!r}.'
            message = message.format(argument)
            raise TypeError(message)
        dummy_pitch = pitchtools.NamedPitch(0)
        new_pitch = dummy_pitch + self - argument
        return pitchtools.NamedInterval.from_pitch_carriers(
            dummy_pitch, new_pitch)

    ### PRIVATE PROPERTIES ###

    @property
    def _format_string(self):
        return '{}{}'.format(self._quality_abbreviation, self.number)

    @property
    def _interval_string(self):
        interval_to_string = {
            1: 'unison',
            2: 'second',
            3: 'third',
            4: 'fourth',
            5: 'fifth',
            6: 'sixth',
            7: 'seventh',
            8: 'octave',
            9: 'ninth',
            10: 'tenth',
            11: 'eleventh',
            12: 'twelth',
            13: 'thirteenth',
            14: 'fourteenth',
            15: 'fifteenth',
            }
        try:
            interval_string = interval_to_string[abs(self.number)]
        except KeyError:
            abs_number = abs(self.number)
            residue = abs_number % 10
            if residue == 1:
                suffix = 'st'
            elif residue == 2:
                suffix = 'nd'
            elif residue == 3:
                suffix = 'rd'
            else:
                suffix = 'th'
            interval_string = '%s%s' % (abs_number, suffix)
        return interval_string

    @property
    def _quality_abbreviation(self):
        _quality_string_to_quality_abbreviation = {
            'major': 'M', 'minor': 'm', 'perfect': 'P',
            'augmented': 'aug', 'diminished': 'dim'}
        return _quality_string_to_quality_abbreviation[self.quality_string]

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        superclass = super(NamedInterval, self)
        format_specification = superclass._get_format_specification()
        return new(
            format_specification,
            template_names=['quality_string', 'number'],
            )

    def _transpose_pitch(self, pitch):
        from abjad.tools import pitchtools
        pitch_number = pitch.pitch_number + self.semitones
        diatonic_pitch_class_number = \
            (pitch.diatonic_pitch_class_number + self.staff_spaces) % 7
        diatonic_pitch_class_name = \
            pitchtools.PitchClass._diatonic_pitch_class_number_to_diatonic_pitch_class_name[
                diatonic_pitch_class_number]
        named_pitch = pitchtools.NamedPitch(
            pitch_number, diatonic_pitch_class_name)
        return type(pitch)(named_pitch)

    ### PUBLIC PROPERTIES ###

    @property
    def direction_number(self):
        r'''Direction number of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').direction_number
                1

        Returns ``-1``, ``0`` or ``1``.
        '''
        if self.quality_string == 'perfect' and abs(self.number) == 1:
            return 0
        else:
            return mathtools.sign(self.number)

    @property
    def direction_string(self):
        r'''Direction string of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').direction_string
                'ascending'

        ..  container:: example

            ::

                >>> abjad.NamedInterval('-M9').direction_string
                'descending'

        ..  container:: example

            ::

                >>> abjad.NamedInterval('P1').direction_string is None
                True

        Returns ``'ascending'``, ``'descending'`` or none.
        '''
        if self.direction_number == -1:
            return 'descending'
        elif self.direction_number == 0:
            return None
        elif self.direction_number == 1:
            return 'ascending'

    @property
    def interval_class(self):
        r'''Interval class of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').interval_class
                2

        Returns nonnegative integer.
        '''
        return ((abs(self.number) - 1) % 7) + 1

    @property
    def interval_string(self):
        r'''Interval string of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').interval_string
                'ninth'

        Returns string.
        '''
        return self._interval_string

    @property
    def named_interval_class(self):
        r'''Named interval class of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').named_interval_class
                NamedIntervalClass('+M2')

            ::

                >>> abjad.NamedInterval('-M9').named_interval_class
                NamedIntervalClass('-M2')

            ::

                >>> abjad.NamedInterval('P1').named_interval_class
                NamedIntervalClass('P1')

            ::

                >>> abjad.NamedInterval('+P8').named_interval_class
                NamedIntervalClass('+P8')

        Returns named inversion-equivalent interval-class.
        '''
        from abjad.tools import pitchtools
        quality_string, number = self._quality_string, self.number
        return pitchtools.NamedIntervalClass(quality_string, number)

    @property
    def number(self):
        r'''Number of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').number
                9

        Returns nonnegative number.
        '''
        return self._number

    @property
    def octaves(self):
        r'''Number of octaves in interval.

        Returns nonnegative number.
        '''
        return self.semitones // 12

    @property
    def quality_string(self):
        r'''Quality string of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').quality_string
                'major'

            ::

                >>> abjad.NamedInterval('+m9').quality_string
                'minor'

            ::

                >>> abjad.NamedInterval('+P8').quality_string
                'perfect'

            ::

                >>> abjad.NamedInterval('+aug4').quality_string
                'augmented'

        Returns string.
        '''
        return self._quality_string

    @property
    def semitones(self):
        r'''Semitones of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').semitones
                14

            ::

                >>> abjad.NamedInterval('-M9').semitones
                -14

            ::

                >>> abjad.NamedInterval('P1').semitones
                0

            ::

                >>> abjad.NamedInterval('+P8').semitones
                12

            ::

                >>> abjad.NamedInterval('-P8').semitones
                -12

        Returns number.
        '''
        from abjad.tools import pitchtools
        result = 0
        interval_class_number_to_semitones = {
            1: 0,
            2: 1,
            3: 3,
            4: 5,
            5: 7,
            6: 8,
            7: 10,
            8: 0,
            }
        perfect_interval_classes = (
            1,
            4,
            5,
            8,
            )
        interval_class_number = abs(
            pitchtools.NamedIntervalClass(self).number)
        result += interval_class_number_to_semitones[interval_class_number]
        result += (abs(self.number) - 1) // 7 * 12
        quality_string_to_semitones = {
            'perfect': 0,
            'major': 1,
            'minor': 0,
            'augmented': 1,
            'diminished': -1,
            }
        result += quality_string_to_semitones[self.quality_string]
        if interval_class_number not in perfect_interval_classes and \
            self.quality_string == "augmented":
            result += 1
        if self.number < 0:
            result *= -1
        return result

    @property
    def staff_spaces(self):
        r'''Staff spaces of named interval.

        ..  container:: example

            ::

                >>> abjad.NamedInterval('+M9').staff_spaces
                8

            ::

                >>> abjad.NamedInterval('-M9').staff_spaces
                -8

            ::

                >>> abjad.NamedInterval('P1').staff_spaces
                0

            ::

                >>> abjad.NamedInterval('+P8').staff_spaces
                7

            ::

                >>> abjad.NamedInterval('-P8').staff_spaces
                -7

        Returns nonnegative integer.
        '''
        if self.direction_string == 'descending':
            return self.number + 1
        elif self.direction_string is None:
            return 0
        elif self.direction_string == 'ascending':
            return self.number - 1

    ### PUBLIC METHODS ###

    @classmethod
    def from_pitch_carriers(class_, pitch_carrier_1, pitch_carrier_2):
        '''Calculate named interval from `pitch_carrier_1` to
        `pitch_carrier_2`.

        ..  container:: example

            ::

                >>> abjad.NamedInterval.from_pitch_carriers(
                ...     abjad.NamedPitch(-2),
                ...     abjad.NamedPitch(12),
                ...     )
                NamedInterval('+M9')

            ::

                ..  todo:: Improve this behavior.

                >>> abjad.NamedInterval.from_pitch_carriers(
                ...     abjad.NamedPitch("cs'"),
                ...     abjad.NamedPitch("cf'"),
                ...     )
                NamedInterval('-M2')

        Returns named interval.
        '''
        from abjad.tools import pitchtools
        pitch_1 = pitchtools.NamedPitch.from_pitch_carrier(pitch_carrier_1)
        pitch_2 = pitchtools.NamedPitch.from_pitch_carrier(pitch_carrier_2)
        degree_1 = pitch_1.diatonic_pitch_number
        degree_2 = pitch_2.diatonic_pitch_number
        named_interval_number = abs(degree_1 - degree_2) + 1
        numbered_interval_number = abs(
            pitchtools.NumberedPitch(pitch_1).pitch_number -
            pitchtools.NumberedPitch(pitch_2).pitch_number
            )
        numbered_interval = pitchtools.NumberedInterval(
            numbered_interval_number,
            )
        absolute_named_interval = numbered_interval.to_named_interval(
            named_interval_number
            )
        if pitch_2 < pitch_1:
            named_interval = -absolute_named_interval
        else:
            named_interval = absolute_named_interval
        return class_(named_interval)

    def transpose(self, pitch_carrier):
        r'''Transposes `pitch_carrier`.

        ..  container:: example

            Transposes chord:

            ::

                >>> chord = abjad.Chord("<c' e' g'>4")

            ::

                >>> interval = abjad.NamedInterval('+m2')
                >>> interval.transpose(chord)
                Chord("<df' f' af'>4")

        Returns new (copied) object of `pitch_carrier` type.
        '''
        from abjad.tools import pitchtools
        from abjad.tools import scoretools
        if isinstance(pitch_carrier, pitchtools.Pitch):
            return self._transpose_pitch(pitch_carrier)
        elif isinstance(pitch_carrier, scoretools.Note):
            new_note = copy.copy(pitch_carrier)
            new_pitch = self._transpose_pitch(pitch_carrier.written_pitch)
            new_note.written_pitch = new_pitch
            return new_note
        elif isinstance(pitch_carrier, scoretools.Chord):
            new_chord = copy.copy(pitch_carrier)
            pairs = zip(new_chord.note_heads, pitch_carrier.note_heads)
            for new_nh, old_nh in pairs:
                new_pitch = self._transpose_pitch(old_nh.written_pitch)
                new_nh.written_pitch = new_pitch
            return new_chord
        else:
            return pitch_carrier
