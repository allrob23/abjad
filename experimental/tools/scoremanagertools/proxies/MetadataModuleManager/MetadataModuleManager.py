# -*- encoding: utf-8 -*-
import collections
import os
from experimental.tools.scoremanagertools.proxies.ModuleManager \
    import ModuleManager
from experimental.tools.scoremanagertools.proxies.ParseableModuleMixin \
    import ParseableModuleMixin


class MetadataModuleManager(ModuleManager, ParseableModuleMixin):
#class MetadataModuleManager(ModuleManager):

    ### INITIALIZER ###

    def __init__(self, filesystem_path=None, session=None):
        assert '__metadata__' in filesystem_path, repr(filesystem_path)
        packagesystem_path = \
            self.configuration.filesystem_path_to_packagesystem_path(
            filesystem_path)
        ModuleManager.__init__(
            self,
            packagesystem_path=packagesystem_path,
            session=session,
            )
        ParseableModuleMixin.__init__(self)
        self.metadata_lines = []
        self.parse()

    ### CLASS VARIABLES ###

    extension = '.py'

    ### PUBLIC PROPERTIES ##

    @property
    def file_sections(self):
        return (
            (self.encoding_directives, True, 0),
            (self.docstring_lines, False, 1),
            (self.setup_statements, True, 2),
            (self.metadata_lines, False, 1),
            (self.teardown_statements, True, 0),
            )

    ### PUBLIC METHODS ###

    def has_line(self, line):
        file_reference = open(self.filesystem_path, 'r')
        for file_line in file_reference.readlines():
            if file_line == line:
                file_reference.close()
                return True
        file_reference.close()
        return False

    def interactively_restore(self, prompt=True):
        from experimental.tools import scoremanagertools
        getter = self.session.io_manager.make_getter(where=self._where)
        getter.append_yes_no_string('handmade')
        result = getter._run()
        if self.session.backtrack():
            return
        if 'yes'.startswith(result.lower()):
            material_package_maker_class_name = None
            getter = self.session.io_manager.make_getter(where=self._where)
            getter.append_yes_no_string('should have illustration')
            result = getter._run()
            if self.session.backtrack():
                return
            should_have_illustration = 'yes'.startswith(result.lower())
        else:
            material_package_maker_wrangler = \
                scoremanagertools.wranglers.MaterialPackageMakerWrangler(
                session=self.session)
            with self.backtracking:
                wrangler = material_package_maker_wrangler
                material_package_maker_class_name = \
                    wrangler.select_material_proxy_class_name_interactively(
                    clear=False, 
                    cache=True,
                    )
            if self.session.backtrack():
                return
            should_have_illustration = True
        metadata = collections.OrderedDict([])
        metadata['should_have_illustration'] = should_have_illustration
        metadata['material_package_maker_class_name'] = \
            material_package_maker_class_name
        self.write_stub_to_disk()
        message = 'initializer restored.'
        self.session.io_manager.proceed(message, is_interactive=prompt)

    def make_metadata_lines(self, metadata):
        if metadata:
            lines = []
            for key, value in sorted(metadata.iteritems()):
                key = repr(key)
                if hasattr(value, '_get_multiline_repr'):
                    repr_lines = \
                        value._get_multiline_repr(include_tools_package=True)
                    value = '\n    '.join(repr_lines)
                    lines.append('({}, {})'.format(key, value))
                else:
                    value = getattr(
                        value, '_tools_package_qualified_repr', repr(value))
                    lines.append('({}, {})'.format(key, value))
            lines = ',\n    '.join(lines)
            result = 'tags = collections.OrderedDict([\n    {}])'.format(lines)
        else:
            result = 'tags = collections.OrderedDict([])'
        return result

    def parse(self, initializer_file_name=None):
        is_parsable = True
        if initializer_file_name is None:
            initializer_file_name = self.filesystem_path
        if not os.path.exists(initializer_file_name):
            return
        initializer = file(initializer_file_name, 'r')
        encoding_directives = []
        docstring_lines = []
        setup_statements = []
        metadata_lines = []
        teardown_statements = []
        current_section = None
        for line in initializer.readlines():
            if line == '\n':
                continue
            elif line.startswith('# -*-'):
                current_section = 'encoding'
            elif line.startswith("'''"):
                current_section = 'docstring'
            elif line.startswith(('from', 'import')):
                current_section = 'setup'
            elif line.startswith('tags ='):
                current_section = 'tags'
            elif line.startswith('rm'):
                current_section = 'teardown'
            if current_section == 'encoding':
                encoding_directives.append(line)
            elif current_section == 'docstring':
                docstring_lines.append(line)
            elif current_section == 'setup':
                setup_statements.append(line)
            elif current_section == 'tags':
                metadata_lines.append(line)
            elif current_section == 'teardown':
                teardown_statements.append(line)
            else:
                is_parsable = False
        initializer.close()
        self.encoding_directives = encoding_directives[:]
        self.docstring_lines = docstring_lines[:]
        self.setup_statements = setup_statements[:]
        self.metadata_lines = metadata_lines[:]
        self.teardown_statements = teardown_statements[:]
        return is_parsable

    def read_file(self):
        return self.parse()

    def write_stub_to_disk(self):
        self.clear()
        self.write_to_disk()

    def write_metadata_to_disk(self, metadata):
        self.parse()
        self.encoding_directives[:] = ['# -*- encoding: utf-8 -*-\n']
        ordered_dict_import_statement = 'import collections\n'
        if ordered_dict_import_statement not in self.setup_statements:
            self.setup_statements.append(ordered_dict_import_statement)
        metadata_lines = self.make_metadata_lines(metadata)
        self.metadata_lines = metadata_lines[:]
        self.write_to_disk()
