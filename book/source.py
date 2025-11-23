# Void-Fragments.py
# Smells Like Beckett Spirit.
#
# Copyright (c) 2025 Joe ApocaLips <japocalips@gmail.com>
# Licensed under the MIT License.
#
# Copying and distribution of this file, with or without modification, are
# permitted in any medium without royalty provided the copyright notice and
# this notice are preserved. This file is offered as-is, without any warranty.
#
# A Beckettian Text Generator for NaNoGenMo 2025.
# This program generates a continuous, fragmented monologue inspired by
# Samuel Beckett's "Texts for Nothing" (1-13), structured in six generative modes:
#
# Mode A: Raw lexical shards -- sparse, aphoristic fragments (Texts 1-5)
# Mode B: Interrogative doubt -- obsessive questioning, modal paralysis (Texts 6, 10-11)
# Mode C: Continuous murmuring -- recursive, flowing voice (Text 13)
# Mode D: Compulsive repetition -- looping phrases, "again the same" (Texts 3, 5, 7)
# Mode E: Pure negation -- impossibility, aporia, "cannot" (Texts 2, 4, 8)
# Mode F: Anatomy of absence -- catalogues of void ("no body, no name...") (Texts 1, 6, 9)
#
# The voice speaks without body, circles around silence, repeats without progress,
# and persists despite having nothing to say--yet it says it anyway.
#
# All output is procedurally generated from original templates and meta-phrases.
# No text from Beckett's published works is reproduced verbatim.
#
# Source: https://github.com/JoeApocaLips/Void-Fragments
#
# version 1.0 Creation 16 November 2025
#
from pathlib import Path
import random as rd
from time import strftime
from collections import deque
import unicodedata

# rd.seed('9798670552141'[::-1]) # MY ISBN

adverbs = "always,again,never,more,already,perhaps,almost,barely,simply,thus,there,just,often,long,now,here,somewhere,elsewhere,barely,vainly,dumbly".split(',')
adverb_weights = [4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print('adverbs', len(adverbs), len(adverb_weights))

verbs = "continue,speak,say,be silent,stay,repeat,whisper,end,begin,wait,feel,understand,leave,erase,go,be,can,have,know,exist,endure,persist".split(',')
verbs_weights = [3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1]
print('verbs', len(verbs), len(verbs_weights))

nouns = "body,name,face,place,time,voice,memory,reason,silence,nothing,mind,soul,thought,language,presence,past,future,space,movement,will,strength,purpose,sense,form,trace,shadow,breath,echo,dust,light,sound,eye,hand,foot,chair,room,word".split(',')
print('nouns', len(nouns))

pronouns = 'I she he one it'.split()

def expand(s,e=''): return sum(([b[0]+x+e for x in b[1:]] or [b[0]+e] for l in s.strip().splitlines() if (b:=l.split('|'))),[])

questions = expand("""
is it too |late|little|much
always the same
could it be nothing
truly everything
Does silence count as speaking
is that |all|already something|enough
and |after that|then
is this |the beginning|the end
what's the point
is it worse
is it |always nothing|better|different|finished|nothing|now|over|something|starting again|sufficient|surely nothing|the same
who |am I speaking to|is speaking
really the same
should we stop
What if nothing answers
what |am I saying|does it mean|if that's all|remains
is there anything left to say
am I speaking |again|for nothing
does it |mean anything|mean nothing|suffice
shall we go on
Is |being silent enough|existing enough|repeating enough
nothing else to say
has it begun
Must one mean, even without sense
so now
once more
why go on
after| that|wards""", '?')
print('questions', len(questions))

ends = expand("""
I go on, always
no reply.
another word
wordless.
barely a sound.
again| this|, nothing.
surely nothing
still |speaking.|this
one |more word|word too many
once again.
always the same thing.
a word, again
it |begins again|ends, perhaps|never ends
maybe |that's it|yes, maybe no
probably that's it
nothing| more.| remains.|, in truth|, or almost
almost nothing
that's all| there is| we have|.
...
void.
I stop, no
already |gone.|heard|said""")
print('ends', len(ends))

meta_sentences = expand("""
begin, not begin, begin again without having begun
he stays, without place, without name, without why
before, after, now: the same thing
does |he continue, or is it silence?|she persist, or is it silence?
a silence that speaks, that's already something
always, again, never
a shadow without light, that's all there is
not to |be, never to be, and yet be|speak, never to speak, and yet speak
a word
already| over|, soon, never
I have no past, yet I repeat
understanding undoes nothing, yet one understands
is it enough, to speak in the dark?
not there, and yet there, always there
another word, always a word, never the right one
to be silent is |to speak, but to speak is to fail|what I'd like, but it speaks
I don't want to speak, yet I speak
no |echo, and yet it answers|me|mouth, and yet it speaks|word, and yet it speaks ceaselessly
me, not me, me again
to persist is to fail, yet one persists
to whisper without breath, that's all there is
too late
I am not| I, but I say I| here, I am again there|, yet I speak again
I say nothing, |I say it ceaselessly, I repeat it|yet I say it again
there| is a voice, that's all there is|, again there, already gone|. again.
one must |mean, but meaning has fled|speak, since one can do nothing else
gone|, returned, never gone|. returned.
knowing changes nothing, yet one knows
nothing to say||, and yet I say it|, nothing to do, nothing to be
I must go on, I cannot go on, I'll go on
one |cannot endure, one goes endure|ought to fall silent, but silence speaks|repeats to say nothing, that's already something
go on, not go on, go on all the same
absolute silence
no body, no |name, and yet a voice|voice, and yet it speaks
speech. void. again.
it speaks||, without me, without anyone
never begun
must one |continue, even without reason?|speak, even without voice?
it continues, again, always, never begun
nothing| more, nothing less, just that: a voice| to begin, everything to begin, same thing|, again
it's the same thing, again the same, always the same
without |body|knowing, without power, without end|memory, without trace, and yet I know
who speaks? |I speak, she speaks, it speaks|me, perhaps, or someone else
I am |absent, yet present in speech|here, I am not, I am again|no one, yet I speak|silent, yet it continues
end, not end, begin again
a trace of voice, nothing more
a presence without body, that's already too much
to be |is to err, yet one is|there, not to be there, to be all the same
I vanish, yet I say
naked voice
a voice|| speaking into the void, that's already something| without body, that's already too much|, that's all
I, she, it, no one
it whispers, without ear, without echo, without end
speaking void
speak, |repeat, be silent|speak again, always speak, to say nothing
I speak, therefore I am perhaps
silence| speaks louder than I|, speech, silence again
one should |persist, but I cannot persist|understand, but understanding changes nothing
I cannot speak, I speak, I cannot be silent
here, there, nowhere
she persists, without reason, without end
neither here, nor elsewhere, nowhere and there
impossible to |begin, yet she continues|persist, yet one continues
to speak |of nothing, that's all that remains|to say nothing, that's all that remains|to say nothing, to say to say nothing, to say nothing and to speak|without mouth, that's all that remains
what if one speaks for nothing?""")
print('meta_sentences', len(meta_sentences))

templates = expand("""
a voice without {n}, that's all there is
a {n}. no {n2}. a voice.
impossible to {v}, yet {p} {continue_conj}
is |it {adv} over?|{v_ing} enough?
it {v_conj}, it {v2_conj}, it does not stop
must one |{v}, even without reason?|{v}?
neither {n}, nor {n2}, nor even the shadow of {n3}
no mouth, no {n}, and yet {v_conj}
no time, and yet {p} {v_conj}
no {n}, |and yet {p} {v_conj}|never {n2}, always without {n3}|no {n2}, and yet {v}
not to {v}, never to {v}, and yet {v}
nothing to {v}, everything to {v}, same thing
one should {v}, but |one cannot|{p} cannot {v}|{v} changes nothing|{v} has no meaning
one would like to {v}, but {v} is not possible
there is a voice that {v_conj}, that's all {p} {know_conj}
to |be silent is to {v}, but to {v} is to speak|{v} or not to {v}, makes no difference|{v}, again {v}, always {v}, for nothing
voice. {n}. silence.
what |else to do but {v}?|if {p} {v_conj} for nothing?
where is the {n} that {v_conj}? nowhere
who {v_conj}? {p}, perhaps, or no one
without {n}, without {n2}, without {n3}, and yet {p} {v_conj}
{adv} here, |{adv2} there, {adv3} nowhere|{adv2} there, {adv3} nowhere, and {p} {v_conj}
{adv} there|, but does it count?|. {adv2} gone. {adv3} returned.
{do_conj} {p} {v}|, or is it silence?|?
{n}, {n2}, {n3}: none of it
{p} {be_conj} |no one, yet {p} {v_conj}|not there, {p} {be_conj} {adv} there|there, {adv} there, {adv2} there
{p} {have_conj} no {n}, yet {p} {v_conj}|| all the same
{p} {v_conj}, again, always, never ending||, for nothing
{p} {v_conj}, without {n}, without {n2}, without |knowing why|{n3}, without end
{p} {v_conj}|, cannot stop| to say nothing, that's already something| without past, without future, without present|, {p} {do_conj} not know why
{p} |cannot {v}, {p} {go_conj} {v}|{go_conj} {v}, but {go_conj} nowhere|{look for_conj} a {n}, but {find_conj} nothing|{look_conj} for a {n}, but finds no {n}|{try_conj} to {v}, but {v} is impossible|{want_conj} to {v}, but cannot|{do_conj} not know if {p} {v_conj}, but {p} {v_conj}
""")
print('templates', len(templates))

def cycle(lst):
    while not rd.shuffle(lst): yield from lst

meta_sentences_it = cycle(meta_sentences)
questions_it = cycle(questions)
ends_it = cycle(ends)

# Mode A  Raw lexical shards
meta_A_it = (s for s in meta_sentences_it if len(s.split()) <= 8 and '?' not in s and not any(w in s for w in ('but', 'and yet', 'cannot', "I'll", 'perhaps', 'must', 'should', 'would', 'try', 'want')))
ends_A_it = (s for s in ends_it if len(s) < 15)

# Mode B  Interrogative doubt
templates_B = [t for t in templates if '?' in t or 'if ' in t or 'does ' in t or '{do_conj}' in t]
print('templates_B', len(templates_B))
meta_B_it = (s for s in meta_sentences_it if '?' in s)

# Mode D  Compulsive repetition
templates_D = [t for t in templates if any(w in t for w in ('again', 'always', 'never ending', 'begin again', 'same thing'))]
print('templates_D', len(templates_D))
meta_D_it = (s for s in meta_sentences_it if any(w in s for w in ('again','same','never ending','begin again','go on, not go on','always the same','again, always','go on','not to ','to be there, not to be there')))

# Mode E  Pure negation    
templates_E = [t for t in templates if any(p in t for p in ('cannot ','impossible to','not to ','never to ','one should ')) or ('but' in t and 'cannot' in t)]
print('templates_E', len(templates_E))
meta_E_it = (s for s in meta_sentences_it if any(p in s for p in ('cannot ','impossible to','but to speak is to fail','to be silent is to speak, but','I cannot speak, I speak')))
                                      
# Mode F  Anatomy of absence
templates_F = [t for t in templates if t.startswith(('no ', 'without ', 'neither ', '{n}, {n2}, {n3}:'))]
print('templates_F', len(templates_F))
meta_F_it = (s for s in meta_sentences_it if s.startswith(('no ','without ','neither ')) or ': none of it' in s)

translate = {'adv':(adverbs, adverb_weights), 'p':(pronouns,), 'v':(verbs, verbs_weights), 'n':(nouns,)}
gerondif_map = {'be':'being', 'begin':'beginning', 'can':'to be able'}

class Resolver(dict):
    def __init__(self, template):
        super()
        self.template = template
    def __missing__(self, key):
        oldkey = key
        key, conj = ((keys:=key.split('_'))[0], True) if '_' in key else (key, False)
        gerondif = conj and keys[1]=='ing'
        k, n = (key[:-1], int(key[-1])) if key[-1].isdigit() else (key, None)
        trsl = None 
        while True:
            if trsl or (trsl:=translate.get(k)):
                v = v if conj and (v:=self.get(key)) else ((rd.choices(*trsl, k=1)[0] if len(trsl)==2 else rd.choice(trsl[0]))) # selector choice with or without weight
            else: v = k
            if conj:
                vv = v.split()
                verb = vv[0]
                if gerondif: verb = gerondif_map.get(verb, (verb[:-1] if verb[-1]=='e' else verb)+'ing') # gerund
                else:
                    subject = self.get('p')
                    if not subject: subject = self.__missing__('p') if '?' in self.template else 'it' # create default subject if question
                    if_not_I = subject != 'I'
                    match verb: # conjugator
                        case 'be':
                            verb = 'is' if if_not_I else 'am'
                        case 'do'|'go':
                            if if_not_I: verb += 'es'
                        case 'have':
                            if if_not_I: verb = 'has'
                        case 'try':
                            if if_not_I: verb = 'tries'
                        case 'can':
                            pass
                        case _:
                            if if_not_I: verb += 's'
                vv[0] = verb
                v = ' '.join(vv)
            if not n or not trsl or not any(v==self.get(oldkey.replace(str(n),str(i) if i else '')) for i in range(0, n)): break # unique values for xx, xx1, xx2...
        self[oldkey] = v
        return v

_seen_cache = deque(maxlen=4) # window sentences

def next_unique(it):
    while (s:=next(it)) in _seen_cache: pass
    _seen_cache.append(s)
    return s
    
def capitalize(s): return s[0].upper() + s[1:]

def generate_sentences(templates_m=templates, metas_it=meta_sentences_it, count_min=8, count_max=12, meta_ratio=0.25, question_ratio=0.12):
    result = []
    templates_it = iter(lambda:capitalize((t:=rd.choice(templates_m)).format_map(Resolver(t))), 'dummy iterator')
    for i in range(rd.randint(count_min, count_max)):
        result.append(next_unique(metas_it if rd.random() < meta_ratio else templates_it))
        if i >= 1 and rd.random() < question_ratio: result.append(next_unique(questions_it))
    if rd.random() < 0.6:
        if rd.random() < 0.7: result.append(next_unique(questions_it))
        else: result.append(next(ends_it))
    return result

def generate_text(mode):
    _seen_cache.clear()
    match mode: 
        case 'A':  # Mode A: Raw lexical shards -- mimics the skeletal openings of Texts 15.
            result = [next_unique(meta_A_it) for _ in range(rd.randint(3, 6))]
            if rd.random() < 0.3: result.append(next(ends_A_it))
        case 'B':  # Mode B: Interrogative vertigo -- echoes the obsessive doubt of Texts 611.
            result = generate_sentences(templates_B, meta_B_it, 6, 10, 0.3, 0.25)
        case 'D':  # Mode D: Compulsive repetition -- captures the looped despair of Texts 3, 5, 7.
            result = generate_sentences(templates_D, meta_D_it, 5, 9, 0.4, 0.05)
        case 'E':  # Mode E: Pure negation / aporia -- inspired by the impossible imperatives in Texts 2, 4, 8.
            result = generate_sentences(templates_E, meta_E_it, 5, 9, 0.3, 0.1)
        case 'F':  # Mode F: Anatomy of absence -- channels the desolate catalogues of Texts 1, 6, 9.
            result = generate_sentences(templates_F, meta_F_it, 4, 8, 0.1, 0.02)
        case _:    # Mode C: Continuous murmuring -- reflects the flowing monologue of late Texts (esp. 1213).
            result = generate_sentences()
    return '\n'.join(result)

# Generate full output for NaNoGenMo
# normally one text by page
texts_count = 850 # for NaNoGenMo # estimate count
output = []
for m, p in [('F',12),('E',12),('D',12),('B',15),('A',9),('C',40)]:
    mc = (texts_count * p) // 100
    print(m, mc)
    output.extend(generate_text(m) for _ in range(mc))

thefulltext = '\n\n'.join(output)
print(f"Total words: {len(thefulltext.split())}")
Path(__file__[:-3]+strftime('-%y%m%d-%H%M%S.txt')).write_text(thefulltext, encoding='utf8')

# for the book
Path(__file__[:-2]+'md').write_text(''.join(f'\\clearpage\n{t.replace('\n','\n\n')}\n\n' for t in output), encoding='utf8')
# source code utf8 to ascii
srcode = Path(__file__).read_text(encoding='utf8').replace(''',"'").replace('"','"').replace('"', '"').replace('...', '...').replace('--', '--')
(Path(__file__).parent/'book'/'source.py').write_text(unicodedata.normalize("NFKD",srcode).encode("ascii","ignore").decode("ascii"),encoding="ascii")
