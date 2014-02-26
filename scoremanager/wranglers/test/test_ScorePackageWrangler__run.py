# -*- encoding: utf-8 -*-
import os
import pytest
from abjad import *
import scoremanager


def test_ScorePackageWrangler__run_01():
    r'''Create score package. Remove score package.
    '''
    pytest.skip('unskip after deciding about cache.')

    score_manager = scoremanager.core.ScoreManager()
    name = 'testscore'
    assert not score_manager._configuration.package_exists(name)

    try:
        score_manager._run(pending_user_input=
            'new Test~score testscore 2012 '
            'q'
            )
        assert score_manager._configuration.package_exists(name)
        manager = scoremanager.managers.ScorePackageManager(name)
        assert manager.annotated_title == 'Test score (2012)'
        assert manager.composer is None
        assert manager.instrumentation is None
    finally:
        string = 'test removescore clobberscore remove default q'
        score_manager._run(pending_user_input=string)
        assert not score_manager._configuration.package_exists(name)
