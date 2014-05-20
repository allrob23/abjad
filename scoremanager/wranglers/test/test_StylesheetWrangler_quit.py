# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_StylesheetWrangler_quit_01():
    
    input_ = 'red~example~score y q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    assert contents


def test_StylesheetWrangler_quit_02():
    
    input_ = 'y q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    assert contents