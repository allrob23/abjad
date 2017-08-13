
from abjad.tools.pitchtools import NamedPitchClass


lilypond_version = "2.19.24"

language_pitch_names = {
    'nederlands':  {
        'ceses': NamedPitchClass('cff'),
        'ceh': NamedPitchClass('cqf'),
        'ces': NamedPitchClass('cf'),
        'ceseh': NamedPitchClass('ctqf'),
        'c': NamedPitchClass('c'),
        'cis': NamedPitchClass('cs'),
        'cih': NamedPitchClass('cqs'),
        'cisih': NamedPitchClass('ctqs'),
        'cisis': NamedPitchClass('css'),
        'deses': NamedPitchClass('dff'),
        'deh': NamedPitchClass('dqf'),
        'des': NamedPitchClass('df'),
        'deseh': NamedPitchClass('dtqf'),
        'd': NamedPitchClass('d'),
        'dis': NamedPitchClass('ds'),
        'dih': NamedPitchClass('dqs'),
        'disih': NamedPitchClass('dtqs'),
        'disis': NamedPitchClass('dss'),
        'eeses': NamedPitchClass('eff'),
        'eses': NamedPitchClass('eff'),
        'eeh': NamedPitchClass('eqf'),
        'ees': NamedPitchClass('ef'),
        'eeseh': NamedPitchClass('etqf'),
        'es': NamedPitchClass('ef'),
        'e': NamedPitchClass('e'),
        'eis': NamedPitchClass('es'),
        'eih': NamedPitchClass('eqs'),
        'eisih': NamedPitchClass('etqs'),
        'eisis': NamedPitchClass('ess'),
        'feses': NamedPitchClass('fff'),
        'feh': NamedPitchClass('fqf'),
        'fes': NamedPitchClass('ff'),
        'feseh': NamedPitchClass('ftqf'),
        'f': NamedPitchClass('f'),
        'fis': NamedPitchClass('fs'),
        'fih': NamedPitchClass('fqs'),
        'fisih': NamedPitchClass('ftqs'),
        'fisis': NamedPitchClass('fss'),
        'geses': NamedPitchClass('gff'),
        'geh': NamedPitchClass('gqf'),
        'ges': NamedPitchClass('gf'),
        'geseh': NamedPitchClass('gtqf'),
        'g': NamedPitchClass('g'),
        'gis': NamedPitchClass('gs'),
        'gih': NamedPitchClass('gqs'),
        'gisih': NamedPitchClass('gtqs'),
        'gisis': NamedPitchClass('gss'),
        'aeses': NamedPitchClass('aff'),
        'ases': NamedPitchClass('aff'),
        'aeh': NamedPitchClass('aqf'),
        'aes': NamedPitchClass('af'),
        'aeseh': NamedPitchClass('atqf'),
        'as': NamedPitchClass('af'),
        'a': NamedPitchClass('a'),
        'ais': NamedPitchClass('as'),
        'aih': NamedPitchClass('aqs'),
        'aisih': NamedPitchClass('atqs'),
        'aisis': NamedPitchClass('ass'),
        'beses': NamedPitchClass('bff'),
        'beh': NamedPitchClass('bqf'),
        'bes': NamedPitchClass('bf'),
        'beseh': NamedPitchClass('btqf'),
        'b': NamedPitchClass('b'),
        'bis': NamedPitchClass('bs'),
        'bih': NamedPitchClass('bqs'),
        'bisih': NamedPitchClass('btqs'),
        'bisis': NamedPitchClass('bss'),
    },

    'catalan':  {
        'dobb': NamedPitchClass('cff'),
        'dob': NamedPitchClass('cf'),
        'do': NamedPitchClass('c'),
        'dod': NamedPitchClass('cs'),
        'dodd': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'reb': NamedPitchClass('df'),
        're': NamedPitchClass('d'),
        'red': NamedPitchClass('ds'),
        'redd': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mib': NamedPitchClass('ef'),
        'mi': NamedPitchClass('e'),
        'mid': NamedPitchClass('es'),
        'midd': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fab': NamedPitchClass('ff'),
        'fa': NamedPitchClass('f'),
        'fad': NamedPitchClass('fs'),
        'fadd': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'solb': NamedPitchClass('gf'),
        'sol': NamedPitchClass('g'),
        'sold': NamedPitchClass('gs'),
        'soldd': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'lab': NamedPitchClass('af'),
        'la': NamedPitchClass('a'),
        'lad': NamedPitchClass('as'),
        'ladd': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sib': NamedPitchClass('bf'),
        'si': NamedPitchClass('b'),
        'sid': NamedPitchClass('bs'),
        'sidd': NamedPitchClass('bss'),
        'dos': NamedPitchClass('cs'),
        'doss': NamedPitchClass('css'),
        'res': NamedPitchClass('ds'),
        'ress': NamedPitchClass('dss'),
        'mis': NamedPitchClass('es'),
        'miss': NamedPitchClass('ess'),
        'fas': NamedPitchClass('fs'),
        'fass': NamedPitchClass('fss'),
        'sols': NamedPitchClass('gs'),
        'solss': NamedPitchClass('gss'),
        'las': NamedPitchClass('as'),
        'lass': NamedPitchClass('ass'),
        'sis': NamedPitchClass('bs'),
        'siss': NamedPitchClass('bss'),
    },

    'deutsch':  {
        'ceses': NamedPitchClass('cff'),
        'ceseh': NamedPitchClass('ctqf'),
        'ces': NamedPitchClass('cf'),
        'ceh': NamedPitchClass('cqf'),
        'c': NamedPitchClass('c'),
        'cih': NamedPitchClass('cqs'),
        'cis': NamedPitchClass('cs'),
        'cisih': NamedPitchClass('ctqs'),
        'cisis': NamedPitchClass('css'),
        'deses': NamedPitchClass('dff'),
        'deseh': NamedPitchClass('dtqf'),
        'des': NamedPitchClass('df'),
        'deh': NamedPitchClass('dqf'),
        'd': NamedPitchClass('d'),
        'dih': NamedPitchClass('dqs'),
        'dis': NamedPitchClass('ds'),
        'disih': NamedPitchClass('dtqs'),
        'disis': NamedPitchClass('dss'),
        'eses': NamedPitchClass('eff'),
        'eseh': NamedPitchClass('etqf'),
        'es': NamedPitchClass('ef'),
        'eeh': NamedPitchClass('eqf'),
        'e': NamedPitchClass('e'),
        'eih': NamedPitchClass('eqs'),
        'eis': NamedPitchClass('es'),
        'eisih': NamedPitchClass('etqs'),
        'eisis': NamedPitchClass('ess'),
        'feses': NamedPitchClass('fff'),
        'feseh': NamedPitchClass('ftqf'),
        'fes': NamedPitchClass('ff'),
        'feh': NamedPitchClass('fqf'),
        'f': NamedPitchClass('f'),
        'fih': NamedPitchClass('fqs'),
        'fis': NamedPitchClass('fs'),
        'fisih': NamedPitchClass('ftqs'),
        'fisis': NamedPitchClass('fss'),
        'geses': NamedPitchClass('gff'),
        'geseh': NamedPitchClass('gtqf'),
        'ges': NamedPitchClass('gf'),
        'geh': NamedPitchClass('gqf'),
        'g': NamedPitchClass('g'),
        'gih': NamedPitchClass('gqs'),
        'gis': NamedPitchClass('gs'),
        'gisih': NamedPitchClass('gtqs'),
        'gisis': NamedPitchClass('gss'),
        'asas': NamedPitchClass('aff'),
        'asah': NamedPitchClass('atqf'),
        'ases': NamedPitchClass('aff'),
        'aseh': NamedPitchClass('atqf'),
        'as': NamedPitchClass('af'),
        'aeh': NamedPitchClass('aqf'),
        'a': NamedPitchClass('a'),
        'aih': NamedPitchClass('aqs'),
        'ais': NamedPitchClass('as'),
        'aisih': NamedPitchClass('atqs'),
        'aisis': NamedPitchClass('ass'),
        'heses': NamedPitchClass('bff'),
        'heseh': NamedPitchClass('btqf'),
        'b': NamedPitchClass('bf'),
        'beh': NamedPitchClass('bqf'),
        'h': NamedPitchClass('b'),
        'hih': NamedPitchClass('bqs'),
        'his': NamedPitchClass('bs'),
        'hisih': NamedPitchClass('btqs'),
        'hisis': NamedPitchClass('bss'),
    },

    'english':  {
        'cff': NamedPitchClass('cff'),
        'ctqf': NamedPitchClass('ctqf'),
        'cf': NamedPitchClass('cf'),
        'cqf': NamedPitchClass('cqf'),
        'c': NamedPitchClass('c'),
        'cqs': NamedPitchClass('cqs'),
        'cs': NamedPitchClass('cs'),
        'ctqs': NamedPitchClass('ctqs'),
        'css': NamedPitchClass('css'),
        'cx': NamedPitchClass('css'),
        'dff': NamedPitchClass('dff'),
        'dtqf': NamedPitchClass('dtqf'),
        'df': NamedPitchClass('df'),
        'dqf': NamedPitchClass('dqf'),
        'd': NamedPitchClass('d'),
        'dqs': NamedPitchClass('dqs'),
        'ds': NamedPitchClass('ds'),
        'dtqs': NamedPitchClass('dtqs'),
        'dss': NamedPitchClass('dss'),
        'dx': NamedPitchClass('dss'),
        'eff': NamedPitchClass('eff'),
        'etqf': NamedPitchClass('etqf'),
        'ef': NamedPitchClass('ef'),
        'eqf': NamedPitchClass('eqf'),
        'e': NamedPitchClass('e'),
        'eqs': NamedPitchClass('eqs'),
        'es': NamedPitchClass('es'),
        'etqs': NamedPitchClass('etqs'),
        'ess': NamedPitchClass('ess'),
        'ex': NamedPitchClass('ess'),
        'fff': NamedPitchClass('fff'),
        'ftqf': NamedPitchClass('ftqf'),
        'ff': NamedPitchClass('ff'),
        'fqf': NamedPitchClass('fqf'),
        'f': NamedPitchClass('f'),
        'fqs': NamedPitchClass('fqs'),
        'fs': NamedPitchClass('fs'),
        'ftqs': NamedPitchClass('ftqs'),
        'fss': NamedPitchClass('fss'),
        'fx': NamedPitchClass('fss'),
        'gff': NamedPitchClass('gff'),
        'gtqf': NamedPitchClass('gtqf'),
        'gf': NamedPitchClass('gf'),
        'gqf': NamedPitchClass('gqf'),
        'g': NamedPitchClass('g'),
        'gqs': NamedPitchClass('gqs'),
        'gs': NamedPitchClass('gs'),
        'gtqs': NamedPitchClass('gtqs'),
        'gss': NamedPitchClass('gss'),
        'gx': NamedPitchClass('gss'),
        'aff': NamedPitchClass('aff'),
        'atqf': NamedPitchClass('atqf'),
        'af': NamedPitchClass('af'),
        'aqf': NamedPitchClass('aqf'),
        'a': NamedPitchClass('a'),
        'aqs': NamedPitchClass('aqs'),
        'as': NamedPitchClass('as'),
        'atqs': NamedPitchClass('atqs'),
        'ass': NamedPitchClass('ass'),
        'ax': NamedPitchClass('ass'),
        'bff': NamedPitchClass('bff'),
        'btqf': NamedPitchClass('btqf'),
        'bf': NamedPitchClass('bf'),
        'bqf': NamedPitchClass('bqf'),
        'b': NamedPitchClass('b'),
        'bqs': NamedPitchClass('bqs'),
        'bs': NamedPitchClass('bs'),
        'btqs': NamedPitchClass('btqs'),
        'bss': NamedPitchClass('bss'),
        'bx': NamedPitchClass('bss'),
        'c-flatflat': NamedPitchClass('cff'),
        'c-flat': NamedPitchClass('cf'),
        'c-natural': NamedPitchClass('c'),
        'c-sharp': NamedPitchClass('cs'),
        'c-sharpsharp': NamedPitchClass('css'),
        'd-flatflat': NamedPitchClass('dff'),
        'd-flat': NamedPitchClass('df'),
        'd-natural': NamedPitchClass('d'),
        'd-sharp': NamedPitchClass('ds'),
        'd-sharpsharp': NamedPitchClass('dss'),
        'e-flatflat': NamedPitchClass('eff'),
        'e-flat': NamedPitchClass('ef'),
        'e-natural': NamedPitchClass('e'),
        'e-sharp': NamedPitchClass('es'),
        'e-sharpsharp': NamedPitchClass('ess'),
        'f-flatflat': NamedPitchClass('fff'),
        'f-flat': NamedPitchClass('ff'),
        'f-natural': NamedPitchClass('f'),
        'f-sharp': NamedPitchClass('fs'),
        'f-sharpsharp': NamedPitchClass('fss'),
        'g-flatflat': NamedPitchClass('gff'),
        'g-flat': NamedPitchClass('gf'),
        'g-natural': NamedPitchClass('g'),
        'g-sharp': NamedPitchClass('gs'),
        'g-sharpsharp': NamedPitchClass('gss'),
        'a-flatflat': NamedPitchClass('aff'),
        'a-flat': NamedPitchClass('af'),
        'a-natural': NamedPitchClass('a'),
        'a-sharp': NamedPitchClass('as'),
        'a-sharpsharp': NamedPitchClass('ass'),
        'b-flatflat': NamedPitchClass('bff'),
        'b-flat': NamedPitchClass('bf'),
        'b-natural': NamedPitchClass('b'),
        'b-sharp': NamedPitchClass('bs'),
        'b-sharpsharp': NamedPitchClass('bss'),
    },

    'espanol':  {
        'dobb': NamedPitchClass('cff'),
        'dotcb': NamedPitchClass('ctqf'),
        'dob': NamedPitchClass('cf'),
        'docb': NamedPitchClass('cqf'),
        'do': NamedPitchClass('c'),
        'docs': NamedPitchClass('cqs'),
        'dos': NamedPitchClass('cs'),
        'dotcs': NamedPitchClass('ctqs'),
        'doss': NamedPitchClass('css'),
        'dox': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'retcb': NamedPitchClass('dtqf'),
        'reb': NamedPitchClass('df'),
        'recb': NamedPitchClass('dqf'),
        're': NamedPitchClass('d'),
        'recs': NamedPitchClass('dqs'),
        'res': NamedPitchClass('ds'),
        'retcs': NamedPitchClass('dtqs'),
        'ress': NamedPitchClass('dss'),
        'rex': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mitcb': NamedPitchClass('etqf'),
        'mib': NamedPitchClass('ef'),
        'micb': NamedPitchClass('eqf'),
        'mi': NamedPitchClass('e'),
        'mics': NamedPitchClass('eqs'),
        'mis': NamedPitchClass('es'),
        'mitcs': NamedPitchClass('etqs'),
        'miss': NamedPitchClass('ess'),
        'mix': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fatcb': NamedPitchClass('ftqf'),
        'fab': NamedPitchClass('ff'),
        'facb': NamedPitchClass('fqf'),
        'fa': NamedPitchClass('f'),
        'facs': NamedPitchClass('fqs'),
        'fas': NamedPitchClass('fs'),
        'fatcs': NamedPitchClass('ftqs'),
        'fass': NamedPitchClass('fss'),
        'fax': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'soltcb': NamedPitchClass('gtqf'),
        'solb': NamedPitchClass('gf'),
        'solcb': NamedPitchClass('gqf'),
        'sol': NamedPitchClass('g'),
        'solcs': NamedPitchClass('gqs'),
        'sols': NamedPitchClass('gs'),
        'soltcs': NamedPitchClass('gtqs'),
        'solss': NamedPitchClass('gss'),
        'solx': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'latcb': NamedPitchClass('atqf'),
        'lab': NamedPitchClass('af'),
        'lacb': NamedPitchClass('aqf'),
        'la': NamedPitchClass('a'),
        'lacs': NamedPitchClass('aqs'),
        'las': NamedPitchClass('as'),
        'latcs': NamedPitchClass('atqs'),
        'lass': NamedPitchClass('ass'),
        'lax': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sitcb': NamedPitchClass('btqf'),
        'sib': NamedPitchClass('bf'),
        'sicb': NamedPitchClass('bqf'),
        'si': NamedPitchClass('b'),
        'sics': NamedPitchClass('bqs'),
        'sis': NamedPitchClass('bs'),
        'sitcs': NamedPitchClass('btqs'),
        'siss': NamedPitchClass('bss'),
        'six': NamedPitchClass('bss'),
    },

    'italiano':  {
        'dobb': NamedPitchClass('cff'),
        'dobsb': NamedPitchClass('ctqf'),
        'dob': NamedPitchClass('cf'),
        'dosb': NamedPitchClass('cqf'),
        'do': NamedPitchClass('c'),
        'dosd': NamedPitchClass('cqs'),
        'dod': NamedPitchClass('cs'),
        'dodsd': NamedPitchClass('ctqs'),
        'dodd': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'rebsb': NamedPitchClass('dtqf'),
        'reb': NamedPitchClass('df'),
        'resb': NamedPitchClass('dqf'),
        're': NamedPitchClass('d'),
        'resd': NamedPitchClass('dqs'),
        'red': NamedPitchClass('ds'),
        'redsd': NamedPitchClass('dtqs'),
        'redd': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mibsb': NamedPitchClass('etqf'),
        'mib': NamedPitchClass('ef'),
        'misb': NamedPitchClass('eqf'),
        'mi': NamedPitchClass('e'),
        'misd': NamedPitchClass('eqs'),
        'mid': NamedPitchClass('es'),
        'midsd': NamedPitchClass('etqs'),
        'midd': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fabsb': NamedPitchClass('ftqf'),
        'fab': NamedPitchClass('ff'),
        'fasb': NamedPitchClass('fqf'),
        'fa': NamedPitchClass('f'),
        'fasd': NamedPitchClass('fqs'),
        'fad': NamedPitchClass('fs'),
        'fadsd': NamedPitchClass('ftqs'),
        'fadd': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'solbsb': NamedPitchClass('gtqf'),
        'solb': NamedPitchClass('gf'),
        'solsb': NamedPitchClass('gqf'),
        'sol': NamedPitchClass('g'),
        'solsd': NamedPitchClass('gqs'),
        'sold': NamedPitchClass('gs'),
        'soldsd': NamedPitchClass('gtqs'),
        'soldd': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'labsb': NamedPitchClass('atqf'),
        'lab': NamedPitchClass('af'),
        'lasb': NamedPitchClass('aqf'),
        'la': NamedPitchClass('a'),
        'lasd': NamedPitchClass('aqs'),
        'lad': NamedPitchClass('as'),
        'ladsd': NamedPitchClass('atqs'),
        'ladd': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sibsb': NamedPitchClass('btqf'),
        'sib': NamedPitchClass('bf'),
        'sisb': NamedPitchClass('bqf'),
        'si': NamedPitchClass('b'),
        'sisd': NamedPitchClass('bqs'),
        'sid': NamedPitchClass('bs'),
        'sidsd': NamedPitchClass('btqs'),
        'sidd': NamedPitchClass('bss'),
    },

    'norsk':  {
        'ceses': NamedPitchClass('cff'),
        'cessess': NamedPitchClass('cff'),
        'ces': NamedPitchClass('cf'),
        'cess': NamedPitchClass('cf'),
        'c': NamedPitchClass('c'),
        'cis': NamedPitchClass('cs'),
        'ciss': NamedPitchClass('cs'),
        'cisis': NamedPitchClass('css'),
        'cississ': NamedPitchClass('css'),
        'deses': NamedPitchClass('dff'),
        'dessess': NamedPitchClass('dff'),
        'des': NamedPitchClass('df'),
        'dess': NamedPitchClass('df'),
        'd': NamedPitchClass('d'),
        'dis': NamedPitchClass('ds'),
        'diss': NamedPitchClass('ds'),
        'disis': NamedPitchClass('dss'),
        'dississ': NamedPitchClass('dss'),
        'eeses': NamedPitchClass('eff'),
        'eessess': NamedPitchClass('eff'),
        'eses': NamedPitchClass('eff'),
        'essess': NamedPitchClass('eff'),
        'ees': NamedPitchClass('ef'),
        'eess': NamedPitchClass('ef'),
        'es': NamedPitchClass('ef'),
        'ess': NamedPitchClass('ef'),
        'e': NamedPitchClass('e'),
        'eis': NamedPitchClass('es'),
        'eiss': NamedPitchClass('es'),
        'eisis': NamedPitchClass('ess'),
        'eississ': NamedPitchClass('ess'),
        'feses': NamedPitchClass('fff'),
        'fessess': NamedPitchClass('fff'),
        'fes': NamedPitchClass('ff'),
        'fess': NamedPitchClass('ff'),
        'f': NamedPitchClass('f'),
        'fis': NamedPitchClass('fs'),
        'fiss': NamedPitchClass('fs'),
        'fisis': NamedPitchClass('fss'),
        'fississ': NamedPitchClass('fss'),
        'geses': NamedPitchClass('gff'),
        'gessess': NamedPitchClass('gff'),
        'ges': NamedPitchClass('gf'),
        'gess': NamedPitchClass('gf'),
        'g': NamedPitchClass('g'),
        'g': NamedPitchClass('g'),
        'gis': NamedPitchClass('gs'),
        'giss': NamedPitchClass('gs'),
        'gisis': NamedPitchClass('gss'),
        'gississ': NamedPitchClass('gss'),
        'aeses': NamedPitchClass('aff'),
        'aessess': NamedPitchClass('aff'),
        'ases': NamedPitchClass('aff'),
        'assess': NamedPitchClass('aff'),
        'aes': NamedPitchClass('af'),
        'aess': NamedPitchClass('af'),
        'as': NamedPitchClass('af'),
        'ass': NamedPitchClass('af'),
        'a': NamedPitchClass('a'),
        'ais': NamedPitchClass('as'),
        'aiss': NamedPitchClass('as'),
        'aisis': NamedPitchClass('ass'),
        'aississ': NamedPitchClass('ass'),
        'bes': NamedPitchClass('bff'),
        'bess': NamedPitchClass('bff'),
        'b': NamedPitchClass('bf'),
        'b': NamedPitchClass('bf'),
        'h': NamedPitchClass('b'),
        'his': NamedPitchClass('bs'),
        'hiss': NamedPitchClass('bs'),
        'hisis': NamedPitchClass('bss'),
        'hississ': NamedPitchClass('bss'),
    },

    'portugues':  {
        'dobb': NamedPitchClass('cff'),
        'dobtqt': NamedPitchClass('ctqf'),
        'dob': NamedPitchClass('cf'),
        'dobqt': NamedPitchClass('cqf'),
        'do': NamedPitchClass('c'),
        'dosqt': NamedPitchClass('cqs'),
        'dos': NamedPitchClass('cs'),
        'dostqt': NamedPitchClass('ctqs'),
        'doss': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'rebtqt': NamedPitchClass('dtqf'),
        'reb': NamedPitchClass('df'),
        'rebqt': NamedPitchClass('dqf'),
        're': NamedPitchClass('d'),
        'resqt': NamedPitchClass('dqs'),
        'res': NamedPitchClass('ds'),
        'restqt': NamedPitchClass('dtqs'),
        'ress': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mibtqt': NamedPitchClass('etqf'),
        'mib': NamedPitchClass('ef'),
        'mibqt': NamedPitchClass('eqf'),
        'mi': NamedPitchClass('e'),
        'misqt': NamedPitchClass('eqs'),
        'mis': NamedPitchClass('es'),
        'mistqt': NamedPitchClass('etqs'),
        'miss': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fabtqt': NamedPitchClass('ftqf'),
        'fab': NamedPitchClass('ff'),
        'fabqt': NamedPitchClass('fqf'),
        'fa': NamedPitchClass('f'),
        'fasqt': NamedPitchClass('fqs'),
        'fas': NamedPitchClass('fs'),
        'fastqt': NamedPitchClass('ftqs'),
        'fass': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'solbtqt': NamedPitchClass('gtqf'),
        'solb': NamedPitchClass('gf'),
        'solbqt': NamedPitchClass('gqf'),
        'sol': NamedPitchClass('g'),
        'solsqt': NamedPitchClass('gqs'),
        'sols': NamedPitchClass('gs'),
        'solstqt': NamedPitchClass('gtqs'),
        'solss': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'labtqt': NamedPitchClass('atqf'),
        'lab': NamedPitchClass('af'),
        'labqt': NamedPitchClass('aqf'),
        'la': NamedPitchClass('a'),
        'lasqt': NamedPitchClass('aqs'),
        'las': NamedPitchClass('as'),
        'lastqt': NamedPitchClass('atqs'),
        'lass': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sibtqt': NamedPitchClass('btqf'),
        'sib': NamedPitchClass('bf'),
        'sibqt': NamedPitchClass('bqf'),
        'si': NamedPitchClass('b'),
        'sisqt': NamedPitchClass('bqs'),
        'sis': NamedPitchClass('bs'),
        'sistqt': NamedPitchClass('btqs'),
        'siss': NamedPitchClass('bss'),
    },

    'suomi':  {
        'ceses': NamedPitchClass('cff'),
        'ces': NamedPitchClass('cf'),
        'c': NamedPitchClass('c'),
        'cis': NamedPitchClass('cs'),
        'cisis': NamedPitchClass('css'),
        'deses': NamedPitchClass('dff'),
        'des': NamedPitchClass('df'),
        'd': NamedPitchClass('d'),
        'dis': NamedPitchClass('ds'),
        'disis': NamedPitchClass('dss'),
        'eses': NamedPitchClass('eff'),
        'es': NamedPitchClass('ef'),
        'e': NamedPitchClass('e'),
        'eis': NamedPitchClass('es'),
        'eisis': NamedPitchClass('ess'),
        'feses': NamedPitchClass('fff'),
        'fes': NamedPitchClass('ff'),
        'f': NamedPitchClass('f'),
        'fis': NamedPitchClass('fs'),
        'fisis': NamedPitchClass('fss'),
        'geses': NamedPitchClass('gff'),
        'ges': NamedPitchClass('gf'),
        'g': NamedPitchClass('g'),
        'gis': NamedPitchClass('gs'),
        'gisis': NamedPitchClass('gss'),
        'asas': NamedPitchClass('aff'),
        'ases': NamedPitchClass('aff'),
        'as': NamedPitchClass('af'),
        'a': NamedPitchClass('a'),
        'ais': NamedPitchClass('as'),
        'aisis': NamedPitchClass('ass'),
        'bb': NamedPitchClass('bff'),
        'bes': NamedPitchClass('bff'),
        'heses': NamedPitchClass('bff'),
        'b': NamedPitchClass('bf'),
        'h': NamedPitchClass('b'),
        'his': NamedPitchClass('bs'),
        'hisis': NamedPitchClass('bss'),
    },

    'svenska':  {
        'cessess': NamedPitchClass('cff'),
        'cess': NamedPitchClass('cf'),
        'c': NamedPitchClass('c'),
        'ciss': NamedPitchClass('cs'),
        'cississ': NamedPitchClass('css'),
        'dessess': NamedPitchClass('dff'),
        'dess': NamedPitchClass('df'),
        'd': NamedPitchClass('d'),
        'diss': NamedPitchClass('ds'),
        'dississ': NamedPitchClass('dss'),
        'essess': NamedPitchClass('eff'),
        'ess': NamedPitchClass('ef'),
        'e': NamedPitchClass('e'),
        'eiss': NamedPitchClass('es'),
        'eississ': NamedPitchClass('ess'),
        'fessess': NamedPitchClass('fff'),
        'fess': NamedPitchClass('ff'),
        'f': NamedPitchClass('f'),
        'fiss': NamedPitchClass('fs'),
        'fississ': NamedPitchClass('fss'),
        'gessess': NamedPitchClass('gff'),
        'gess': NamedPitchClass('gf'),
        'g': NamedPitchClass('g'),
        'giss': NamedPitchClass('gs'),
        'gississ': NamedPitchClass('gss'),
        'assess': NamedPitchClass('aff'),
        'ass': NamedPitchClass('af'),
        'a': NamedPitchClass('a'),
        'aiss': NamedPitchClass('as'),
        'aississ': NamedPitchClass('ass'),
        'hessess': NamedPitchClass('bff'),
        'b': NamedPitchClass('bf'),
        'h': NamedPitchClass('b'),
        'hiss': NamedPitchClass('bs'),
        'hississ': NamedPitchClass('bss'),
    },

    'vlaams':  {
        'dobb': NamedPitchClass('cff'),
        'dob': NamedPitchClass('cf'),
        'do': NamedPitchClass('c'),
        'dok': NamedPitchClass('cs'),
        'dokk': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'reb': NamedPitchClass('df'),
        're': NamedPitchClass('d'),
        'rek': NamedPitchClass('ds'),
        'rekk': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mib': NamedPitchClass('ef'),
        'mi': NamedPitchClass('e'),
        'mik': NamedPitchClass('es'),
        'mikk': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fab': NamedPitchClass('ff'),
        'fa': NamedPitchClass('f'),
        'fak': NamedPitchClass('fs'),
        'fakk': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'solb': NamedPitchClass('gf'),
        'sol': NamedPitchClass('g'),
        'solk': NamedPitchClass('gs'),
        'solkk': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'lab': NamedPitchClass('af'),
        'la': NamedPitchClass('a'),
        'lak': NamedPitchClass('as'),
        'lakk': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sib': NamedPitchClass('bf'),
        'si': NamedPitchClass('b'),
        'sik': NamedPitchClass('bs'),
        'sikk': NamedPitchClass('bss'),
    },

    'español':  {
        'dobb': NamedPitchClass('cff'),
        'dotcb': NamedPitchClass('ctqf'),
        'dob': NamedPitchClass('cf'),
        'docb': NamedPitchClass('cqf'),
        'do': NamedPitchClass('c'),
        'docs': NamedPitchClass('cqs'),
        'dos': NamedPitchClass('cs'),
        'dotcs': NamedPitchClass('ctqs'),
        'doss': NamedPitchClass('css'),
        'dox': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'retcb': NamedPitchClass('dtqf'),
        'reb': NamedPitchClass('df'),
        'recb': NamedPitchClass('dqf'),
        're': NamedPitchClass('d'),
        'recs': NamedPitchClass('dqs'),
        'res': NamedPitchClass('ds'),
        'retcs': NamedPitchClass('dtqs'),
        'ress': NamedPitchClass('dss'),
        'rex': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mitcb': NamedPitchClass('etqf'),
        'mib': NamedPitchClass('ef'),
        'micb': NamedPitchClass('eqf'),
        'mi': NamedPitchClass('e'),
        'mics': NamedPitchClass('eqs'),
        'mis': NamedPitchClass('es'),
        'mitcs': NamedPitchClass('etqs'),
        'miss': NamedPitchClass('ess'),
        'mix': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fatcb': NamedPitchClass('ftqf'),
        'fab': NamedPitchClass('ff'),
        'facb': NamedPitchClass('fqf'),
        'fa': NamedPitchClass('f'),
        'facs': NamedPitchClass('fqs'),
        'fas': NamedPitchClass('fs'),
        'fatcs': NamedPitchClass('ftqs'),
        'fass': NamedPitchClass('fss'),
        'fax': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'soltcb': NamedPitchClass('gtqf'),
        'solb': NamedPitchClass('gf'),
        'solcb': NamedPitchClass('gqf'),
        'sol': NamedPitchClass('g'),
        'solcs': NamedPitchClass('gqs'),
        'sols': NamedPitchClass('gs'),
        'soltcs': NamedPitchClass('gtqs'),
        'solss': NamedPitchClass('gss'),
        'solx': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'latcb': NamedPitchClass('atqf'),
        'lab': NamedPitchClass('af'),
        'lacb': NamedPitchClass('aqf'),
        'la': NamedPitchClass('a'),
        'lacs': NamedPitchClass('aqs'),
        'las': NamedPitchClass('as'),
        'latcs': NamedPitchClass('atqs'),
        'lass': NamedPitchClass('ass'),
        'lax': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sitcb': NamedPitchClass('btqf'),
        'sib': NamedPitchClass('bf'),
        'sicb': NamedPitchClass('bqf'),
        'si': NamedPitchClass('b'),
        'sics': NamedPitchClass('bqs'),
        'sis': NamedPitchClass('bs'),
        'sitcs': NamedPitchClass('btqs'),
        'siss': NamedPitchClass('bss'),
        'six': NamedPitchClass('bss'),
    },

    'français':  {
        'dobb': NamedPitchClass('cff'),
        'dobsb': NamedPitchClass('ctqf'),
        'dob': NamedPitchClass('cf'),
        'dosb': NamedPitchClass('cqf'),
        'do': NamedPitchClass('c'),
        'dosd': NamedPitchClass('cqs'),
        'dod': NamedPitchClass('cs'),
        'dodsd': NamedPitchClass('ctqs'),
        'dodd': NamedPitchClass('css'),
        'rebb': NamedPitchClass('dff'),
        'rebsb': NamedPitchClass('dtqf'),
        'reb': NamedPitchClass('df'),
        'resb': NamedPitchClass('dqf'),
        're': NamedPitchClass('d'),
        'resd': NamedPitchClass('dqs'),
        'red': NamedPitchClass('ds'),
        'redsd': NamedPitchClass('dtqs'),
        'redd': NamedPitchClass('dss'),
        'mibb': NamedPitchClass('eff'),
        'mibsb': NamedPitchClass('etqf'),
        'mib': NamedPitchClass('ef'),
        'misb': NamedPitchClass('eqf'),
        'mi': NamedPitchClass('e'),
        'misd': NamedPitchClass('eqs'),
        'mid': NamedPitchClass('es'),
        'midsd': NamedPitchClass('etqs'),
        'midd': NamedPitchClass('ess'),
        'fabb': NamedPitchClass('fff'),
        'fabsb': NamedPitchClass('ftqf'),
        'fab': NamedPitchClass('ff'),
        'fasb': NamedPitchClass('fqf'),
        'fa': NamedPitchClass('f'),
        'fasd': NamedPitchClass('fqs'),
        'fad': NamedPitchClass('fs'),
        'fadsd': NamedPitchClass('ftqs'),
        'fadd': NamedPitchClass('fss'),
        'solbb': NamedPitchClass('gff'),
        'solbsb': NamedPitchClass('gtqf'),
        'solb': NamedPitchClass('gf'),
        'solsb': NamedPitchClass('gqf'),
        'sol': NamedPitchClass('g'),
        'solsd': NamedPitchClass('gqs'),
        'sold': NamedPitchClass('gs'),
        'soldsd': NamedPitchClass('gtqs'),
        'soldd': NamedPitchClass('gss'),
        'labb': NamedPitchClass('aff'),
        'labsb': NamedPitchClass('atqf'),
        'lab': NamedPitchClass('af'),
        'lasb': NamedPitchClass('aqf'),
        'la': NamedPitchClass('a'),
        'lasd': NamedPitchClass('aqs'),
        'lad': NamedPitchClass('as'),
        'ladsd': NamedPitchClass('atqs'),
        'ladd': NamedPitchClass('ass'),
        'sibb': NamedPitchClass('bff'),
        'sibsb': NamedPitchClass('btqf'),
        'sib': NamedPitchClass('bf'),
        'sisb': NamedPitchClass('bqf'),
        'si': NamedPitchClass('b'),
        'sisd': NamedPitchClass('bqs'),
        'sid': NamedPitchClass('bs'),
        'sidsd': NamedPitchClass('btqs'),
        'sidd': NamedPitchClass('bss'),
    },

    }
