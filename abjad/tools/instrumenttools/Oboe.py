from abjad.tools.instrumenttools.Instrument import Instrument


class Oboe(Instrument):
    r'''Oboe.

    ::

        >>> import abjad

    ..  container:: example

        ::

            >>> staff = abjad.Staff("c'4 d'4 e'4 fs'4")
            >>> oboe = abjad.instrumenttools.Oboe()
            >>> abjad.attach(oboe, staff[0])
            >>> show(staff) # doctest: +SKIP

        ..  docs::

            >>> f(staff)
            \new Staff {
                \set Staff.instrumentName = \markup { Oboe }
                \set Staff.shortInstrumentName = \markup { Ob. }
                c'4
                d'4
                e'4
                fs'4
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### INITIALIZER ###

    def __init__(
        self,
        name='oboe',
        short_name='ob.',
        name_markup=None,
        short_name_markup=None,
        allowable_clefs=None,
        middle_c_sounding_pitch=None,
        pitch_range='[Bb3, A6]',
        ):
        Instrument.__init__(
            self,
            name=name,
            short_name=short_name,
            name_markup=name_markup,
            short_name_markup=short_name_markup,
            allowable_clefs=allowable_clefs,
            middle_c_sounding_pitch=middle_c_sounding_pitch,
            pitch_range=pitch_range,
            )
        self._performer_names.extend([
            'wind player',
            'reed player',
            'double reed player',
            'oboist',
            ])
        self._is_primary_instrument = True

    ### PUBLIC PROPERTIES ###

    @property
    def allowable_clefs(self):
        r'''Gets oboe's allowable clefs.

        ..  container:: example

            ::

                >>> oboe.allowable_clefs
                ClefList([Clef(name='treble')])

            ::

                >>> show(oboe.allowable_clefs) # doctest: +SKIP

        Returns clef list.
        '''
        return Instrument.allowable_clefs.fget(self)

    @property
    def middle_c_sounding_pitch(self):
        r'''Gets sounding pitch of oboe's written middle C.

        ..  container:: example

            ::

                >>> oboe.middle_c_sounding_pitch
                NamedPitch("c'")

            ::

                >>> show(oboe.middle_c_sounding_pitch) # doctest: +SKIP

        Returns named pitch.
        '''
        return Instrument.middle_c_sounding_pitch.fget(self)

    @property
    def name(self):
        r'''Gets oboe's name.

        ..  container:: example

            ::

                >>> oboe.name
                'oboe'

        Returns string.
        '''
        return Instrument.name.fget(self)

    @property
    def name_markup(self):
        r'''Gets oboe's instrument name markup.

        ..  container:: example

            ::

                >>> oboe.name_markup
                Markup(contents=['Oboe'])

            ::

                >>> show(oboe.name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.name_markup.fget(self)

    @property
    def pitch_range(self):
        r'''Gets oboe's range.

        ..  container:: example

            ::

                >>> oboe.pitch_range
                PitchRange('[Bb3, A6]')

            ::

                >>> show(oboe.pitch_range) # doctest: +SKIP

        Returns pitch range.
        '''
        return Instrument.pitch_range.fget(self)

    @property
    def short_name(self):
        r'''Gets oboe's short instrument name.

        ..  container:: example

            ::

                >>> oboe.short_name
                'ob.'

        Returns string.
        '''
        return Instrument.short_name.fget(self)

    @property
    def short_name_markup(self):
        r'''Gets oboe's short instrument name markup.

        ..  container:: example

            ::

                >>> oboe.short_name_markup
                Markup(contents=['Ob.'])

            ::

                >>> show(oboe.short_name_markup) # doctest: +SKIP

        Returns markup.
        '''
        return Instrument.short_name_markup.fget(self)
