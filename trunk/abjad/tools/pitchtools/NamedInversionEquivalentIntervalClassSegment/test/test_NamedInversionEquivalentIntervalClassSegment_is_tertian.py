# -*- encoding: utf-8 -*-
from abjad import *


def test_NamedInversionEquivalentIntervalClassSegment_is_tertian_01():

    dicseg = pitchtools.NamedInversionEquivalentIntervalClassSegment([
        pitchtools.NamedInversionEquivalentIntervalClass('major', 3),
        pitchtools.NamedInversionEquivalentIntervalClass('minor', 3),
        pitchtools.NamedInversionEquivalentIntervalClass('diminshed', 3)])

    assert dicseg.is_tertian


def test_NamedInversionEquivalentIntervalClassSegment_is_tertian_02():

    dicseg = pitchtools.NamedInversionEquivalentIntervalClassSegment([
        pitchtools.NamedInversionEquivalentIntervalClass('major', 2),
        pitchtools.NamedInversionEquivalentIntervalClass('minor', 3),
        pitchtools.NamedInversionEquivalentIntervalClass('diminshed', 3)])

    assert not dicseg.is_tertian
