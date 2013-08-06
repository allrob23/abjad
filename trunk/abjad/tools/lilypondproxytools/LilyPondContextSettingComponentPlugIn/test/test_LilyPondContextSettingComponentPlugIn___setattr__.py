# -*- encoding: utf-8 -*-
from abjad import *


def test_LilyPondContextSettingComponentPlugIn___setattr___01():
    r'''Define LilyPond autoBeaming context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.auto_beaming = True

    r'''
    \new Staff \with {
        autoBeaming = ##t
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            autoBeaming = ##t
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___02():
    r'''Remove LilyPond autoBeaming context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.auto_beaming = True
    del(t.set.auto_beaming)

    r'''
    \new Staff {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___03():
    r'''Define LilyPond currentBarNumber context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t[0].set.score.current_bar_number = 12

    r'''
    \new Staff {
        \set Score.currentBarNumber = #12
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            \set Score.currentBarNumber = #12
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___04():
    r'''Define LilyPond currentBarNumber context setting.
    '''

    t = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(t)
    t[0].set.score.current_bar_number = 12
    measuretools.set_always_format_time_signature_of_measures_in_expr(t)

    r'''
    \new Staff {
        {
            \set Score.currentBarNumber = #12
            \time 2/8
            c'8
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            {
                \set Score.currentBarNumber = #12
                \time 2/8
                c'8
                d'8
            }
            {
                \time 2/8
                e'8
                f'8
            }
        }
        '''
        )

def test_LilyPondContextSettingComponentPlugIn___setattr___05():
    r'''Define LilyPond fontSize context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.font_size = -3

    r'''
    \new Staff \with {
        fontSize = #-3
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            fontSize = #-3
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___06():
    r'''Define LilyPond instrumentName context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.instrument_name = 'Violini I'

    r'''
    \new Staff \with {
        instrumentName = "Violini I"
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            instrumentName = "Violini I"
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___07():
    r'''Define LilyPond instrumentName context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.instrument_name = markuptools.Markup(r'\circle { V }')

    r'''
    \new Staff \with {
        instrumentName = \markup { \circle { V } }
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            instrumentName = \markup { \circle { V } }
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___08():
    r'''Define LilyPond proportionalNotationDuration context setting.
    '''

    t = Score([Staff("c'8 d'8 e'8 f'8")])
    t.set.proportional_notation_duration = schemetools.SchemeMoment(Fraction(1, 56))

    r'''
    \new Score \with {
        proportionalNotationDuration = #(ly:make-moment 1 56)
    } <<
        \new Staff {
            c'8
            d'8
            e'8
            f'8
        }
    >>
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Score \with {
            proportionalNotationDuration = #(ly:make-moment 1 56)
        } <<
            \new Staff {
                c'8
                d'8
                e'8
                f'8
            }
        >>
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___09():
    r'''Define LilyPond shortInstrumentName context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.short_instrument_name = 'Vni. I'

    r'''
    \new Staff \with {
        shortInstrumentName = "Vni. I"
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            shortInstrumentName = "Vni. I"
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___10():
    r'''Define LilyPond shortInstrumentName context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.short_instrument_name = markuptools.Markup(r'\circle { V }')

    r'''
    \new Staff \with {
        shortInstrumentName = \markup { \circle { V } }
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            shortInstrumentName = \markup { \circle { V } }
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___11():
    r'''Define LilyPond suggestAccidentals context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t.set.suggest_accidentals = True

    r'''
    \new Staff \with {
        suggestAccidentals = ##t
    } {
        c'8
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            suggestAccidentals = ##t
        } {
            c'8
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___12():
    r'''Define LilyPond suggestAccidentals context setting.
    '''

    t = Staff("c'8 d'8 e'8 f'8")
    t[1].set.suggest_accidentals = True

    r'''
    \new Staff {
        c'8
        \set suggestAccidentals = ##t
        d'8
        e'8
        f'8
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
            c'8
            \set suggestAccidentals = ##t
            d'8
            e'8
            f'8
        }
        '''
        )


def test_LilyPondContextSettingComponentPlugIn___setattr___13():
    r'''Define LilyPond tupletFullLength context setting.
    '''

    t = Staff([])
    #t.tuplet_bracket.tuplet_full_length = True
    t.set.tuplet_full_length = True

    r'''
    \new Staff \with {
        tupletFullLength = ##t
    } {
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            tupletFullLength = ##t
        } {
        }
        '''
        )

    #t.tuplet_bracket.tuplet_full_length = False
    t.set.tuplet_full_length = False

    r'''
    \new Staff \with {
        tupletFullLength = ##f
    } {
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff \with {
            tupletFullLength = ##f
        } {
        }
        '''
        )

    #t.tuplet_bracket.tuplet_full_length = None
    del(t.set.tuplet_full_length)

    r'''
    \new Staff {
    }
    '''

    assert select(t).is_well_formed()
    assert testtools.compare(
        t.lilypond_format,
        r'''
        \new Staff {
        }
        '''
        )
