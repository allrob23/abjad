# -*- encoding: utf-8 -*-
import os
from abjad import *
from experimental import *
import scoremanager


def test_ArticulationHandlerMaterialPackageManager_01():

    score_manager = scoremanager.core.ScoreManager()
    configuration = score_manager._configuration
    string = 'scoremanager.materials.testarticulationhandler'
    assert not score_manager._configuration.package_exists(string)
    try:
        score_manager._run(pending_user_input=
            'lmm nmm articulation testarticulationhandler default '
            'testarticulationhandler omi reiterated '
            "['^', '.'] (1, 64) (1, 4) c c'''' done default "
            'q '
            )
        path = configuration.abjad_material_packages_directory_path
        path = os.path.join(path, 'testarticulationhandler')
        manager = scoremanager.materialmanagers.ArticulationHandlerMaterialPackageManager(
            filesystem_path=path)
        assert manager._list_directory() == [
            '__init__.py', 
            '__metadata__.py',
            'illustration_builder.py',
            'output_material.py', 
            ]
        handler = handlertools.ReiteratedArticulationHandler(
            articulation_list=['^', '.'],
            minimum_duration=Duration(1, 64),
            maximum_duration=Duration(1, 4),
            minimum_written_pitch=NamedPitch('c'),
            maximum_written_pitch=NamedPitch("c''''"),
            )
        assert manager.output_material == handler
    finally:
        string = 'lmm testarticulationhandler rm default q'
        score_manager._run(pending_user_input=string)
        string = 'scoremanager.materials.testarticulationhandler'
        assert not score_manager._configuration.package_exists(string)
