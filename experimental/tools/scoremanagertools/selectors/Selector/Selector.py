import os
from experimental.tools.scoremanagertools.core.ScoreManagerObject import ScoreManagerObject


class Selector(ScoreManagerObject):

    ### INITIALIZER ###

    def __init__(self, is_keyed=False, is_numbered=False,
        is_parenthetically_numbered=True, is_ranged=False, items=None, session=None):
        ScoreManagerObject.__init__(self, session=session)
        self.is_keyed = is_keyed
        self.is_numbered = is_numbered
        self.is_parenthetically_numbered = is_parenthetically_numbered
        self.is_ranged = is_ranged
        self.items = items or []

    ### PRIVATE PROPERTIES ###

    def _make_main_menu(self, head=None):
        tokens = self.make_menu_tokens(head=head)
        menu, section = self._io.make_menu(where=self._where,
            is_keyed=self.is_keyed,
            is_numbered=self.is_numbered,
            is_parenthetically_numbered=self.is_parenthetically_numbered,
            is_ranged=self.is_ranged,
            tokens=tokens,
            return_value_attribute='prepopulated',
            )
        return menu

    ### PRIVATE METHODS ###

    def _run(self, cache=False, clear=True, head=None, user_input=None):
        self._io.assign_user_input(user_input=user_input)
        self._session.cache_breadcrumbs(cache=cache)
        while True:
            self._session.push_breadcrumb(self._breadcrumb)
            menu = self._make_main_menu(head=head)
            result = menu._run(clear=clear)
            if self._session.backtrack():
                break
            elif not result:
                self._session.pop_breadcrumb()
                continue
            else:
                break
        self._session.pop_breadcrumb()
        self._session.restore_breadcrumbs(cache=cache)
        return result

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def _breadcrumb(self):
        if getattr(self, 'explicit_breadcrumb', None):
            return self.explicit_breadcrumb
        elif hasattr(self, 'space_delimited_lowercase_target_name'):
            return 'select {}:'.format(self.space_delimited_lowercase_target_name)
        else:
            return 'select:'

    ### READ / WRITE PUBLIC PROPERTIES ###

    @apply
    def items():
        def fget(self):
            if self._items:
                return self._items
            else:
                return self.list_items()
        def fset(self, items):
            self._items = items
        return property(**locals())

    ### PUBLIC METHODS ###

    def change_expr_to_menu_token(self, expr):
        return (None, self._io.get_one_line_menuing_summary(expr), None, expr)

    def get_tag_from_directory_path(self, directory_path, tag_name):
        tags_file_name = os.path.join(directory_path, 'tags.py')
        if os.path.isfile(tags_file_name):
            tags_file = open(tags_file_name, 'r')
            tags_file_string = tags_file.read()
            tags_file.close()
            exec(tags_file_string)
            result = locals().get('tags') or OrderedDict([])
            return result.get(tag_name)

    def list_items(self):
        result = []
        return result

    def make_menu_tokens(self, head=None):
        return [self.change_expr_to_menu_token(item) for item in self.items]
