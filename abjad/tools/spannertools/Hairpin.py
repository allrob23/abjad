# -*- encoding: utf-8 -*-
from abjad.tools import scoretools
from abjad.tools import scoretools
from abjad.tools import marktools
from abjad.tools import stringtools
from abjad.tools.spannertools.Spanner import Spanner


class Hairpin(Spanner):
    r'''A dynamic hairpin spanner.

    ..  container:: example

        **Example 1.** Hairpin spanner that does not include rests:

        ::

            >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
            >>> hairpin = spannertools.Hairpin(
            ...     descriptor='p < f',
            ...     include_rests=False,
            ...     )
            >>> attach(hairpin, staff[:])
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> f(staff)
            \new Staff {
                r4
                c'8 \< \p
                d'8
                e'8
                f'8 \f
                r4
            }

    ..  container:: example

        **Example 2.** Hairpin spanner that includes rests:

        ::

            >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
            >>> hairpin = spannertools.Hairpin(
            ...     descriptor='p < f',
            ...     include_rests=True,
            ...     )
            >>> attach(hairpin, staff[:])
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> f(staff)
            \new Staff {
                r4 \< \p
                c'8
                d'8
                e'8
                f'8
                r4 \f
            }

    '''

    ### CLASS VARIABLES ###

    _hairpin_shape_strings = (
        '<',
        '>',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        components=None,
        descriptor='<',
        include_rests=True,
        direction=None,
        overrides=None,
        ):
        Spanner.__init__(
            self,
            components=components,
            overrides=overrides,
            )
        self.direction = direction
        self.include_rests = include_rests
        start_dynamic_string, shape_string, stop_dynamic_string = \
            self._parse_descriptor(descriptor)
        self.shape_string = shape_string
        self.start_dynamic_string = start_dynamic_string
        self.stop_dynamic_string = stop_dynamic_string

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        #Spanner._copy_keyword_args(self, new)
        new.direction = self.direction
        new.include_rests = self.include_rests
        new.shape_string = self.shape_string
        new.start_dynamic_string = self.start_dynamic_string
        new.stop_dynamic_string = self.stop_dynamic_string

    def _format_right_of_leaf(self, leaf):
        result = []
        direction_string = ''
        if self.direction is not None:
            direction_string = \
                stringtools.arg_to_tridirectional_lilypond_symbol(
                    self.direction)
            direction_string = '{} '.format(direction_string)
        if self.include_rests:
            if self._is_my_first_leaf(leaf):
                result.append('%s\\%s' % (direction_string, self.shape_string))
                if self.start_dynamic_string:
                    result.append('%s\\%s' % (
                        direction_string, self.start_dynamic_string))
            if self._is_my_last_leaf(leaf):
                if self.stop_dynamic_string:
                    result.append('%s\\%s' % (
                        direction_string, self.stop_dynamic_string))
                else:
                    effective_dynamic = leaf._get_effective_context_mark(
                        marktools.Dynamic)
                    if effective_dynamic is None or \
                        effective_dynamic not in \
                        leaf._start_marks:
                        result.append('\\!')
        else:
            if self._is_my_first(leaf, (scoretools.Chord, scoretools.Note)):
                result.append('%s\\%s' % (direction_string, self.shape_string))
                if self.start_dynamic_string:
                    result.append('%s\\%s' % (
                        direction_string, self.start_dynamic_string))
            if self._is_my_last(leaf, (scoretools.Chord, scoretools.Note)):
                if self.stop_dynamic_string:
                    result.append('%s\\%s' % (
                        direction_string, self.stop_dynamic_string))
                else:
                    effective_dynamic = leaf._get_effective_context_mark(
                        marktools.Dynamic)
                    if effective_dynamic is None:
                        result.append('\\!')
        return result

    def _parse_descriptor(self, descriptor):
        r'''Example descriptors:

        ::

            '<'
            'p <'
            'p < f'

        '''
        assert isinstance(descriptor, str)
        parts = descriptor.split()
        num_parts = len(parts)
        start, shape, stop = None, None, None
        if parts[0] in ('<', '>'):
            assert 1 <= num_parts <= 2
            if num_parts == 1:
                shape = parts[0]
            else:
                shape = parts[0]
                stop = parts[1]
        else:
            assert 2 <= num_parts <= 3
            if num_parts == 2:
                start = parts[0]
                shape = parts[1]
            else:
                start = parts[0]
                shape = parts[1]
                stop = parts[2]
        assert shape in ('<', '>')
        return start, shape, stop

    ### PUBLIC PROPERTIES ###

    @apply
    def direction():
        def fget(self):
            return self._direction
        def fset(self, arg):
            self._direction = \
                stringtools.arg_to_tridirectional_lilypond_symbol(arg)
        return property(**locals())

    @apply
    def include_rests():
        def fget(self):
            r'''Get boolean hairpin rests contextualize:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(
                ...     descriptor='p < f',
                ...     include_rests=True,
                ...     )
                >>> attach(hairpin, staff[:])
                >>> hairpin.include_rests
                True

            Set boolean hairpin rests contextualize:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(
                ...     descriptor='p < f',
                ...     include_rests=True,
                ...     )
                >>> attach(hairpin, staff[:])
                >>> hairpin.include_rests = False
                >>> hairpin.include_rests
                False

            Set boolean.
            '''
            return self._include_rests
        def fset(self, arg):
            self._include_rests = arg
        return property(**locals())

    @apply
    def shape_string():
        def fget(self):
            r'''Get hairpin shape string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.shape_string
                '<'

            Set hairpin shape string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.shape_string = '>'
                >>> hairpin.shape_string
                '>'

            Set string.
            '''
            return self._shape
        def fset(self, arg):
            assert arg in ('<', '>')
            self._shape = arg
        return property(**locals())

    @apply
    def start_dynamic_string():
        def fget(self):
            r'''Get hairpin start dynamic string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.start_dynamic_string
                'p'

            Set hairpin start dynamic string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.start_dynamic_string = 'mf'
                >>> hairpin.start_dynamic_string
                'mf'

            Set string.
            '''
            return self._start
        def fset(self, arg):
            self._start = arg
        return property(**locals())

    @apply
    def stop_dynamic_string():
        def fget(self):
            r'''Get hairpin stop dynamic string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.stop_dynamic_string
                'f'

            Set hairpin stop dynamic string:

            ::

                >>> staff = Staff("c'8 d'8 e'8 f'8")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> hairpin.stop_dynamic_string = 'mf'
                >>> hairpin.stop_dynamic_string
                'mf'

            Set string.
            '''
            return self._stop
        def fset(self, arg):
            self._stop = arg
        return property(**locals())

    ### PUBLIC METHODS ###

    @staticmethod
    def is_hairpin_shape_string(arg):
        r'''True when `arg` is a hairpin shape string. Otherwise false:

        ::

            >>> spannertools.Hairpin.is_hairpin_shape_string('<')
            True

        Returns boolean.
        '''
        return arg in Hairpin._hairpin_shape_strings

    @staticmethod
    def is_hairpin_token(arg):
        r'''True when `arg` is a hairpin token. Otherwise false:

        ::

            >>> spannertools.Hairpin.is_hairpin_token(('p', '<', 'f'))
            True

        ::

            >>> spannertools.Hairpin.is_hairpin_token(('f', '<', 'p'))
            False

        Returns boolean.
        '''
        Dynamic = marktools.Dynamic
        if isinstance(arg, tuple) and \
            len(arg) == 3 and \
            (not arg[0] or marktools.Dynamic.is_dynamic_name(arg[0])) and \
            Hairpin.is_hairpin_shape_string(arg[1]) and \
            (not arg[2] or marktools.Dynamic.is_dynamic_name(arg[2])):
            if arg[0] and arg[2]:
                start_ordinal = \
                    Dynamic.dynamic_name_to_dynamic_ordinal(arg[0])
                stop_ordinal = \
                    Dynamic.dynamic_name_to_dynamic_ordinal(arg[2])
                if arg[1] == '<':
                    return start_ordinal < stop_ordinal
                else:
                    return stop_ordinal < start_ordinal
            else:
                return True
        else:
            return False
