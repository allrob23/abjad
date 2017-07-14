# -*- coding: utf-8 -*-
from abjad.tools.pitchtools import PitchClassSet


class RootedChordClass(PitchClassSet):
    '''Rooted chord class.

    ::

        >>> from abjad.tools import tonalanalysistools

    ..  container:: example

        Initializes from pair:

        ::

            >>> tonalanalysistools.RootedChordClass('g', 'major')
            GMajorTriadInRootPosition

    ..  container:: example

        Initializes from triple:

        ::

            >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7)
            GDominantSeventhInRootPosition

    G dominant seventh represents a class of chords because there are many
    different spacings of a G dominant seventh.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_bass',
        '_chord_quality',
        '_root',
        )

    _cardinality_to_extent = {
        3: 5,
        4: 7,
        5: 9,
        6: 11,
        7: 13,
        }

    _extent_to_cardinality = {
        5: 3,
        7: 4,
        9: 5,
        11: 6,
        13: 7,
        }

    _extent_to_extent_name = {
        5: 'triad',
        7: 'seventh',
        9: 'ninth',
        11: 'eleventh',
        13: 'thirteenth',
        }

    ### INITIALIZER ###

    def __init__(
        self,
        root=None,
        quality_string='major',
        extent='triad',
        inversion='root',
        ):
        import abjad
        from abjad.tools import tonalanalysistools
        root = root or 'c'
        root = abjad.NamedPitchClass(root)
        chord_quality = tonalanalysistools.RootlessChordClass(
            quality_string=quality_string,
            extent=extent,
            inversion=inversion,
            )
        npcs = []
        for hdi in chord_quality:
            mdi = abjad.NamedInterval(hdi)
            npc = root + mdi
            npcs.append(npc)
        bass = npcs[0]
        PitchClassSet.__init__(
            self,
            items=npcs,
            item_class=abjad.NamedPitchClass,
            )
        self._root = root
        self._chord_quality = chord_quality
        self._bass = bass

    ### SPECIAL METHODS ###

    def __eq__(self, argument):
        r'''Is true when `argument` is a rooted chord-class with root, chord
        quality and inversion equal to those of this rooted chord-class.
        Otherwise false.

        Returns true or false.
        '''
        return super(RootedChordClass, self).__eq__(argument)

    def __hash__(self):
        r'''Hashes rooted chord-class.

        Returns integer.
        '''
        return super(RootedChordClass, self).__hash__()

    def __repr__(self):
        r'''Gets interpreter representation of rooted chord-class.

        Returns string.
        '''
        root = str(self.root).title()
        quality = self.chord_quality._title_case_name
        return root + quality

    ### PRIVATE PROPERTIES ###

    @property
    def _markup_root(self):
        if self.chord_quality._quality_string in (
            'major', 'augmented', 'dominant'):
            root = str(self.root).upper()
        else:
            root = str(self.root).lower()
        if len(root) == 2:
            adjustment = r'\hspace #-0.5 \raise #1 \fontsize #-3'
            if root[-1].lower() == 's':
                root = root[0] + r'{} \sharp'.format(adjustment)
            elif root[-1].lower() == 'f':
                root = root[0] + r'{} \flat'.format(adjustment)
            else:
                message = 'unknown note name: {}'
                message = message.format(root)
                raise ValueError(message)
        return root

    @property
    def _markup_symbol(self):
        circle = r'\draw-circle #0.35 #0 ##f'
        if self.chord_quality._quality_string == 'augmented':
            return '+'
        elif self.chord_quality._quality_string == 'diminished':
            return circle
        elif self.chord_quality._quality_string == 'half diminished':
            line = r"\draw-line #'(1 . 1)"
            markup = r'\concat {{ {} \hspace #-0.85 \raise #-0.5 {} }}'.format(
                circle, line)
            return markup
        elif self.chord_quality._quality_string == 'major' and \
            5 < self.extent.number:
            return 'M'
        elif self.chord_quality._quality_string == 'minor' and \
            5 < self.extent.number:
            return 'm'
        else:
            return ''

    ### PUBLIC PROPERTIES ###

    @property
    def bass(self):
        r'''Gets bass.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'major').bass
                NamedPitchClass('g')

        Returns named pitch-class.
        '''
        return self._bass

    @property
    def cardinality(self):
        r'''Gets cardinality.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7).cardinality
                4

        Returns nonnegative integer.
        '''
        return len(self)

    @property
    def chord_quality(self):
        r'''Gets chord quality.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7).chord_quality
                DominantSeventhInRootPosition('P1', '+M3', '+P5', '+m7')

        Returns chord quality.
        '''
        return self._chord_quality

    @property
    def extent(self):
        r'''Gets extent.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7).extent
                ChordExtent(7)

        Returns chord extent.
        '''
        from abjad.tools import tonalanalysistools
        extent = self.cardinality_to_extent(self.cardinality)
        return tonalanalysistools.ChordExtent(extent)

    @property
    def figured_bass(self):
        r'''Gets figured bass.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7).extent
                ChordExtent(7)

        Returns string.
        '''
        extent, inversion = self.extent, self.inversion
        if extent.number == 5:
            if inversion == 0:
                return ''
            elif inversion == 1:
                return '6/3'
            elif inversion == 2:
                return '6/4'
        elif extent.number == 7:
            if inversion == 0:
                return '7'
            elif inversion == 1:
                return '6/5'
            elif inversion == 2:
                return '4/3'
            elif inversion == 3:
                return '4/2'
        elif extent.number == 9:
            if inversion == 0:
                return ''
            elif inversion == 1:
                raise NotImplementedError
            elif inversion == 2:
                raise NotImplementedError
            elif inversion == 3:
                raise NotImplementedError
            elif inversion == 4:
                raise NotImplementedError

    @property
    def inversion(self):
        r'''Gets inversion.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass('g', 'dominant', 7).inversion
                0

        Returns nonnegative integer.
        '''
        return self._chord_quality.inversion

    @property
    def markup(self):
        r'''Markup of rooted chord-class.

        ..  container:: example

            ::

                >>> markup = tonalanalysistools.RootedChordClass('g', 'dominant', 7).markup
                >>> show(markup) # doctest: +SKIP

            ..  docs::

                >>> f(markup)
                _ \markup {
                    \fontsize
                        #1
                        G
                    \hspace
                        #-0.5
                    \raise
                        #1
                        \fontsize
                            #-3
                            \override
                                #'(baseline-skip . 1.5)
                                \column
                                    {
                                        7
                                    }
                    }

        Returns markup.
        '''
        import abjad
        markup = [self._markup_root, self._markup_symbol, self.figured_bass]
        markup = ''.join(markup)
        markup = r'\fontsize #1 {} \hspace #-0.5'.format(self._markup_root)
        symbol = self._markup_symbol
        if symbol:
            markup += r' \hspace #0.5 \raise #1 \fontsize #-3 {}'.format(
                symbol)
            if 'circle' in symbol:
                if 'sharp' in self._markup_root:
                    markup += r' \hspace #0'
                else:
                    markup += r' \hspace #-1.2'
        inversion = self.figured_bass
        if inversion:
            inv = r" \raise #1 \fontsize #-3 \override #'(baseline-skip . 1.5)"
            inv += r' \column {{ {} }}'.format(' '.join(inversion.split('/')))
            markup += inv
        return abjad.Markup(markup, Down)

    @property
    def quality_pair(self):
        r'''Gets quality pair.

        ..  container:: example

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'c',
                ...     'major',
                ...     'triad',
                ...     'root',
                ...     )
                >>> chord_class.quality_pair
                ('major', 'triad')

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'g',
                ...     'dominant',
                ...     7,
                ...     'second',
                ...     )
                >>> chord_class.quality_pair
                ('dominant', 'seventh')

        Returns pair.
        '''
        chord_quality = self.chord_quality
        return chord_quality.quality_string, chord_quality.extent_name

    @property
    def root(self):
        r'''Gets root.

        ..  container:: example

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'c',
                ...     'major',
                ...     'triad',
                ...     'root',
                ...     )
                >>> chord_class.root
                NamedPitchClass('c')

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'g',
                ...     'dominant',
                ...     7,
                ...     'second',
                ...     )
                >>> chord_class.root
                NamedPitchClass('g')
 
        Returns named pitch-class.
        '''
        return self._root

    @property
    def root_string(self):
        r'''Gets root string.

        ..  container:: example

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'c',
                ...     'major',
                ...     'triad',
                ...     'root',
                ...     )
                >>> chord_class.root_string
                'C'

            ::

                >>> chord_class = tonalanalysistools.RootedChordClass(
                ...     'g',
                ...     'dominant',
                ...     7,
                ...     'second',
                ...     )
                >>> chord_class.root_string
                'G'

        Returns string.
        '''
        capitalized_qualities = ('major', 'dominant', 'augmented')
        symbolic_name = self.root.pitch_class_label
        letter, accidental = symbolic_name[0], symbolic_name[1:]
        if self.chord_quality.quality_string in capitalized_qualities:
            letter = letter.upper()
        else:
            letter = letter.lower()
        return letter + accidental

    ### PUBLIC METHODS ###

    @staticmethod
    def cardinality_to_extent(cardinality):
        r'''Change `cardinality` to extent.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(3)
                5
                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(4)
                7
                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(5)
                9
                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(6)
                11
                >>> tonalanalysistools.RootedChordClass.cardinality_to_extent(7)
                13

        Returns integer.
        '''
        return RootedChordClass._cardinality_to_extent[cardinality]

    @staticmethod
    def extent_to_cardinality(extent):
        r'''Changes `extent` to cardinality.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(5)
                3
                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(7)
                4
                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(9)
                5
                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(11)
                6
                >>> tonalanalysistools.RootedChordClass.extent_to_cardinality(13)
                7

        Returns integer.
        '''
        return RootedChordClass._extent_to_cardinality[extent]

    @staticmethod
    def extent_to_extent_name(extent):
        r'''Changes `extent` to extent name.

        ..  container:: example

            ::

                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(5)
                'triad'
                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(7)
                'seventh'
                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(9)
                'ninth'
                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(11)
                'eleventh'
                >>> tonalanalysistools.RootedChordClass.extent_to_extent_name(13)
                'thirteenth'

        Returns string.
        '''
        return RootedChordClass._extent_to_extent_name[extent]

    def transpose(self):
        r'''Transposes rooted chord-class.

        Not yet implemented.

        Will return new rooted chord-class.
        '''
        raise NotImplementedError
