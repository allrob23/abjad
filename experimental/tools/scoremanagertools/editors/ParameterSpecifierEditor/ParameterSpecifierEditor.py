from experimental.tools.scoremanagertools.editors.InteractiveEditor import InteractiveEditor


class ParameterSpecifierEditor(InteractiveEditor):

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def target_name(self):
        if self.target:
            return self.target._one_line_menuing_summary
