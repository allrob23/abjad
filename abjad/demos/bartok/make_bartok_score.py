import abjad
import copy


def make_bartok_score():
    score = abjad.Score()
    piano_staff = abjad.StaffGroup([], context_name='PianoStaff')
    upper_staff = abjad.Staff([])
    lower_staff = abjad.Staff([])
    piano_staff.append(upper_staff)
    piano_staff.append(lower_staff)
    score.append(piano_staff)
    upper_measures = []
    upper_measures.append(abjad.Measure((2, 4), []))
    upper_measures.append(abjad.Measure((3, 4), []))
    upper_measures.append(abjad.Measure((2, 4), []))
    upper_measures.append(abjad.Measure((2, 4), []))
    upper_measures.append(abjad.Measure((2, 4), []))
    lower_measures = copy.deepcopy(upper_measures)
    upper_staff.extend(upper_measures)
    lower_staff.extend(lower_measures)
    upper_measures[0].extend("a'8 g'8 f'8 e'8")
    upper_measures[1].extend("d'4 g'8 f'8 e'8 d'8")
    upper_measures[2].extend("c'8 d'16 e'16 f'8 e'8")
    upper_measures[3].append("d'2")
    upper_measures[4].append("d'2")
    lower_measures[0].extend("b4 d'8 c'8")
    lower_measures[1].extend("b8 a8 af4 c'8 bf8")
    lower_measures[2].extend("a8 g8 fs8 g16 a16")
    upper_voice = abjad.Voice("b2", name='upper voice')
    command = abjad.LilyPondCommand('voiceOne')
    abjad.attach(command, upper_voice)
    lower_voice = abjad.Voice("b4 a4", name='lower voice')
    command = abjad.LilyPondCommand('voiceTwo')
    abjad.attach(command, lower_voice)
    lower_measures[3].extend([upper_voice, lower_voice])
    lower_measures[3].is_simultaneous = True
    upper_voice = abjad.Voice("b2", name='upper voice')
    command = abjad.LilyPondCommand('voiceOne')
    abjad.attach(command, upper_voice)
    lower_voice = abjad.Voice("g2", name='lower voice')
    command = abjad.LilyPondCommand('voiceTwo')
    abjad.attach(command, lower_voice)
    lower_measures[4].extend([upper_voice, lower_voice])
    lower_measures[4].is_simultaneous = True
    clef = abjad.Clef('bass')
    leaf = abjad.inspect(lower_staff).get_leaf(0)
    abjad.attach(clef, leaf)
    dynamic = abjad.Dynamic('pp')
    abjad.attach(dynamic, upper_measures[0][0])
    dynamic = abjad.Dynamic('mp')
    abjad.attach(dynamic, upper_measures[1][1])
    dynamic = abjad.Dynamic('pp')
    abjad.attach(dynamic, lower_measures[0][1])
    dynamic = abjad.Dynamic('mp')
    abjad.attach(dynamic, lower_measures[1][3])
    score.add_final_bar_line()
    abjad.selector = abjad.select().leaves()
    upper_leaves = abjad.selector(upper_staff)
    lower_leaves = abjad.selector(lower_staff)
    beam = abjad.Beam()
    abjad.attach(beam, upper_leaves[:4])
    beam = abjad.Beam()
    abjad.attach(beam, lower_leaves[1:5])
    beam = abjad.Beam()
    abjad.attach(beam, lower_leaves[6:10])
    slur = abjad.Slur()
    abjad.attach(slur, upper_leaves[:5])
    slur = abjad.Slur()
    abjad.attach(slur, upper_leaves[5:])
    slur = abjad.Slur()
    abjad.attach(slur, lower_leaves[1:6])
    crescendo = abjad.Hairpin('<')
    abjad.attach(crescendo, upper_leaves[-7:-2])
    decrescendo = abjad.Hairpin('>')
    abjad.attach(decrescendo, upper_leaves[-2:])
    markup = abjad.Markup('ritard.')
    text_spanner = abjad.TextSpanner()
    abjad.override(text_spanner).text_spanner.bound_details__left__text = markup
    abjad.attach(text_spanner, upper_leaves[-7:])
    tie = abjad.Tie()
    abjad.attach(tie, upper_leaves[-2:])
    note_1 = lower_staff[-2]['upper voice'][0]
    note_2 = lower_staff[-1]['upper voice'][0]
    notes = abjad.select([note_1, note_2])
    abjad.attach(abjad.Tie(), notes)
    return score
