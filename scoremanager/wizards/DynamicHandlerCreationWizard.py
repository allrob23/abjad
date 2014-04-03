# -*- encoding: utf-8 -*-
from scoremanager.wizards.Wizard import Wizard


class DynamicHandlerCreationWizard(Wizard):
    r'''Dynamic handler creation wizard.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_handler_editor_class_name_suffix',
        '_selector',
        )

    ### INITIALIZER ###

    def __init__(self, session=None, target=None):
        from scoremanager import iotools
        Wizard.__init__(
            self,
            session=session,
            target=target,
            )
        selector = iotools.Selector(session=self._session)
        selector = selector.make_dynamic_handler_class_name_selector()
        self._selector = selector
        self._handler_editor_class_name_suffix = 'Editor'

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return 'dynamic handler creation wizard'