# -*- coding: utf-8 -*-
import collections
from abjad.tools.abctools.AbjadObject import AbjadObject


class CyclicTuple(AbjadObject):
    '''A cylic tuple.

    ..  container:: example

        **Example 1.** Initializes from string:

        ::

            >>> tuple_ = datastructuretools.CyclicTuple('abcd')

        ::

            >>> tuple_
            CyclicTuple(['a', 'b', 'c', 'd'])

        ::

            >>> for x in range(8):
            ...     print(x, tuple_[x])
            ...
            0 a
            1 b
            2 c
            3 d
            4 a
            5 b
            6 c
            7 d

    Cyclic tuples overload the item-getting method of built-in tuples.

    Cyclic tuples return a value for any integer index.

    Cyclic tuples otherwise behave exactly like built-in tuples.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_items',
        )

    ### INITIALIZER ###

    def __init__(self, items=None):
        items = items or ()
        items = tuple(items)
        self._items = items

    ### SPECIAL METHODS ###

    def __contains__(self, i):
        r'''Is true when cyclic tuple contains `item`.

        Returns true or false.
        '''
        return self._items.__contains__(i)

    def __eq__(self, argument):
        r'''Is true when `argument` is a tuple with items equal to those of this
        cyclic tuple. Otherwise false.

        Returns true or false.
        '''
        if isinstance(argument, tuple):
            return self._items == argument
        elif isinstance(argument, type(self)):
            return self._items == argument._items
        return False

    def __getitem__(self, i):
        r'''Gets `i` from cyclic tuple.

        ..  container:: example

            Gets slice open at right:

            ::

                >>> items = [0, 1, 2, 3, 4, 5]
                >>> tuple_ = datastructuretools.CyclicTuple(items=items)
                >>> tuple_[2:]
                (2, 3, 4, 5)

        ..  container:: example

            Gets slice closed at right:

            ::

                >>> items = [0, 1, 2, 3, 4, 5]
                >>> tuple_ = datastructuretools.CyclicTuple(items=items)
                >>> tuple_[:15]
                (0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2)

        Raises index error when `i` can not be found in cyclic tuple.

        Returns item.
        '''
        if isinstance(i, slice):
            if ((i.stop is not None and i.stop < 0) or
                (i.start is not None and i.start < 0)):
                return self._items.__getitem__(i)
            else:
                return self._get_slice(i.start, i.stop)
        if not self:
            message = 'cyclic tuple is empty: {!r}.'
            message = message.format(self)
            raise IndexError(message)
        i = i % len(self)
        return self._items.__getitem__(i)

    def __hash__(self):
        r'''Hashes cyclic tuple.

        Required to be explicitly redefined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(CyclicTuple, self).__hash__()

    def __iter__(self):
        r'''Iterates cyclic tuple.

        Iterates items only once.

        Does not iterate infinitely.
        '''
        return self._items.__iter__()

    def __len__(self):
        r'''Gets length of cyclic tuple.

        Returns nonnegative integer.
        '''
        assert isinstance(self._items, tuple)
        return self._items.__len__()

    def __str__(self):
        r'''Gets string representation of cyclic tuple.

        ..  container:: example

            Gets string:

            ::

                >>> str(datastructuretools.CyclicTuple('abcd'))
                '(a, b, c, d)'

        ..  container:: example

            Gets string:

            ::

                >>> str(datastructuretools.CyclicTuple([1, 2, 3, 4]))
                '(1, 2, 3, 4)'

        Returns string.
        '''
        if self:
            contents = [str(item) for item in self._items]
            contents = ', '.join(contents)
            string = '({!s})'.format(contents)
            return string
        return '()'

    ### PRIVATE METHODS ###

    def _get_format_specification(self):
        from abjad.tools import systemtools
        return systemtools.FormatSpecification(
            client=self,
            repr_is_indented=False,
            storage_format_args_values=[list(self._items)],
            )

    def _get_slice(self, start_index, stop_index):
        if stop_index is not None and 1000000 < stop_index:
            stop_index = len(self)
        result = []
        if start_index is None:
            start_index = 0
        if stop_index is None:
            indices = range(start_index, len(self))
        else:
            indices = range(start_index, stop_index)
        result = [self[n] for n in indices]
        return tuple(result)

    ### PUBLIC PROPERTIES ###

    @property
    def items(self):
        r'''Gets items in cyclic tuple.

        ..  container:: example

            Gets items:

            ::

                >>> tuple_ = datastructuretools.CyclicTuple('abcd')
                >>> tuple_.items
                ('a', 'b', 'c', 'd')

        ..  container:: example

            Gets items:

            ::

                >>> tuple_ = datastructuretools.CyclicTuple([1, 2, 3, 4])
                >>> tuple_.items
                (1, 2, 3, 4)

        Returns tuple.
        '''
        return self._items


collections.Sequence.register(CyclicTuple)
