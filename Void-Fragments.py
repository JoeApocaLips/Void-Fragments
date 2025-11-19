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
# Samuel Beckett’s “Texts for Nothing” (1–13), structured in six generative modes:
#
#   • Mode A: Raw lexical shards — sparse, aphoristic fragments (Texts 1–5)
#   • Mode B: Interrogative doubt — obsessive questioning, modal paralysis (Texts 6, 10–11)
#   • Mode C: Continuous murmuring — recursive, flowing voice (Text 13)
#   • Mode D: Compulsive repetition — looping phrases, “again the same” (Texts 3, 5, 7)
#   • Mode E: Pure negation — impossibility, aporia, “cannot” (Texts 2, 4, 8)
#   • Mode F: Anatomy of absence — catalogues of void (“no body, no name…”) (Texts 1, 6, 9)
#
# The voice speaks without body, circles around silence, repeats without progress,
# and persists despite having nothing to say—yet it says it anyway.
#
# All output is procedurally generated from original templates and meta-phrases.
# No text from Beckett’s published works is reproduced verbatim.
#
# Source: https://github.com/JoeApocaLips/Void-Fragments
#
# version 1.0 Creation 16 November 2025
#
from pathlib import Path
import random as rd
from time import strftime
from collections import deque

adverbs = "always,again,never,more,already,perhaps,almost,barely,simply,thus,there,just,often,long,now,here,somewhere,elsewhere,barely,vainly,dumbly".split(',')
adverb_weights = [4, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print('adverbs', len(adverbs), len(adverb_weights))

verbs = "continue,speak,say,be silent,stay,repeat,whisper,end,begin,wait,feel,understand,leave,erase,go,be,can,have,know,exist,endure,persist".split(',')
verbs_weights = [3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 1, 1]
print('verbs', len(verbs), len(verbs_weights))

nouns = "body,name,face,place,time,voice,memory,reason,silence,nothing,mind,soul,thought,language,presence,past,future,space,movement,will,strength,purpose,sense,form,trace,shadow,breath,echo,dust,light,sound,eye,hand,foot,chair,room,word".split(',')
print('nouns', len(nouns))

pronouns = 'I she he one it'.split()

#def cut(s): return sum((ss if len(ss)==1 else [ss[0]+x for x in ss[1:]] for l in s.strip().splitlines() if (ss:=l.split('|')) ), [])

questions = """
is that already something?
what if that’s all?
and then?
is that all?
truly everything?
nothing else to say?
is that enough?
and after that?
so now?
is it over?
has it begun?
is it the same?
is it different?
is it worse?
is it better?
is it sufficient?
is it too much?
is it too little?
is it something?
is it nothing?
could it be nothing?
is it surely nothing?
is it always nothing?
what am I saying?
am I speaking again?
am I speaking for nothing?
who am I speaking to?
what’s the point?
what does it mean?
does it mean anything?
does it mean nothing?
is it too late?
should we stop?
is this the end?
is this the beginning?
is it starting again?
shall we go on?
once more?
always the same?
really the same?
after that?
afterwards?
is it now?
is it finished?
does it suffice?
why go on?
who is speaking?
what remains?
is there anything left to say?
Is repeating enough?
Must one mean, even without sense?
Is being silent enough?
What if nothing answers?
Does silence count as speaking?
Is existing enough?
""".strip().splitlines()
print('questions', len(questions))

ends = """
nothing more.
…
once again.
always the same thing.
maybe yes, maybe no
again this
still this
already heard
already said
it begins again
it never ends
it ends, perhaps
that’s all there is
that’s all we have
I stop, no
I go on, always
another word
one more word
one word too many
a word, again
nothing, or almost
almost nothing
nothing, in truth
maybe that’s it
probably that’s it
surely nothing
that’s all.
nothing remains.
wordless.
void.
again, nothing.
still speaking.
no reply.
already gone.
barely a sound.
""".strip().splitlines()
print('ends', len(ends))

meta_sentences = """
there is a voice, that’s all there is
a voice speaking into the void, that’s already something
I speak, therefore I am perhaps
no mouth, and yet it speaks
to be silent is what I’d like, but it speaks
I say nothing, yet I say it again
to speak of nothing, that’s all that remains
one must speak, since one can do nothing else
I am no one, yet I speak
who speaks? me, perhaps, or someone else
is it enough, to speak in the dark?
nothing more, nothing less, just that: a voice
there, again there, already gone
not there, and yet there, always there
I am here, I am not, I am again
gone, returned, never gone
I cannot speak, I speak, I cannot be silent
I say nothing, I say it ceaselessly, I repeat it
to speak to say nothing, to say to say nothing, to say nothing and to speak
silence, speech, silence again
I must go on, I cannot go on, I’ll go on
go on, not go on, go on all the same
end, not end, begin again
begin, not begin, begin again without having begun
I, she, it, no one
me, not me, me again
who speaks? I speak, she speaks, it speaks
I am not I, but I say I
nothing to say, nothing to do, nothing to be
no body, no voice, and yet it speaks
neither here, nor elsewhere, nowhere and there
without knowing, without power, without end
always, again, never
already, soon, never
here, there, nowhere
speak, repeat, be silent
it speaks, without me, without anyone
no body, no name, and yet a voice
speak, speak again, always speak, to say nothing
to be there, not to be there, to be all the same
it’s the same thing, again the same, always the same
a voice, that’s all
to speak without mouth, that’s all that remains
a voice without body, that’s already too much
I am not, yet I speak again
nothing to say, and yet I say it
silence speaks louder than I
I am silent, yet it continues
another word, always a word, never the right one
a trace of voice, nothing more
I don’t want to speak, yet I speak
to speak to say nothing, that’s all that remains
a voice
nothing to say
there. again.
gone. returned.
absolute silence
no me
it speaks
naked voice
without body
speaking void
a word
too late
never begun
already over
nothing, again
speech. void. again.
before, after, now: the same thing
I vanish, yet I say
a silence that speaks, that’s already something
no echo, and yet it answers
I am absent, yet present in speech
to whisper without breath, that’s all there is
she persists, without reason, without end
nothing to begin, everything to begin, same thing
I have no past, yet I repeat
he stays, without place, without name, without why
it continues, again, always, never begun
one repeats to say nothing, that’s already something
a shadow without light, that’s all there is
no word, and yet it speaks ceaselessly
I am not here, I am again there
to be silent is to speak, but to speak is to fail
without memory, without trace, and yet I know
a presence without body, that’s already too much
it whispers, without ear, without echo, without end
""".strip().splitlines()
print('meta_sentences', len(meta_sentences))

templates = """
{p} {be_conj} there, {adv} there, {adv2} there
{p} {be_conj} not there, {p} {be_conj} {adv} there
{p} cannot {v}, {p} {go_conj} {v}
{p} {do_conj} not know if {p} {v_conj}, but {p} {v_conj}
one should {v}, but {p} cannot {v}
it {v_conj}, it {v2_conj}, it does not stop
there is a voice that {v_conj}, that’s all {p} {know_conj}
what else to do but {v}?
no {n}, no {n2}, and yet {v}
{p} {be_conj} no one, yet {p} {v_conj}
{p} {v_conj}, {p} {do_conj} not know why
{p} {v_conj}, cannot stop
{p} {v_conj}, again, always, never ending
who {v_conj}? {p}, perhaps, or no one
what if {p} {v_conj} for nothing?
is {v_ing} enough?
{adv} there, but does it count?
{p} {v_conj} to say nothing, that’s already something
{p} {v_conj}, without {n}, without {n2}, without {n3}, without end
no {n}, never {n2}, always without {n3}
{adv} here, {adv2} there, {adv3} nowhere, and {p} {v_conj}
to {v}, again {v}, always {v}, for nothing
{p} {have_conj} no {n}, yet {p} {v_conj} all the same
not to {v}, never to {v}, and yet {v}
one would like to {v}, but {v} is not possible
nothing to {v}, everything to {v}, same thing
to {v} or not to {v}, makes no difference
{do_conj} {p} {v}?
must one {v}?
one should {v}, but one cannot
is it {adv} over?
{p} {look_conj} for a {n}, but finds no {n}
without {n}, without {n2}, without {n3}, and yet {p} {v_conj}
{p} {v_conj}, without {n}, without {n2}, without knowing why
neither {n}, nor {n2}, nor even the shadow of {n3}
{adv} here, {adv2} there, {adv3} nowhere
no {n}, and yet {p} {v_conj}
impossible to {v}, yet {p} {continue_conj}
must one {v}, even without reason?
{do_conj} {p} {v}, or is it silence?
no time, and yet {p} {v_conj}
{p} {v_conj} without past, without future, without present
to be silent is to {v}, but to {v} is to speak
one should {v}, but {v} changes nothing
voice. {n}. silence.
{adv} there. {adv2} gone. {adv3} returned.
a {n}. no {n2}. a voice.
{n}, {n2}, {n3}: none of it
{p} {go_conj} {v}, but {go_conj} nowhere
{p} {look for_conj} a {n}, but {find_conj} nothing
{p} {want_conj} to {v}, but cannot
{p} {try_conj} to {v}, but {v} is impossible
one should {v}, but {v} has no meaning
{p} {have_conj} no {n}, yet {p} {v_conj}
a voice without {n}, that’s all there is
where is the {n} that {v_conj}? nowhere
no mouth, no {n}, and yet {v_conj}
{p} {v_conj}, again, always, never ending, for nothing
""".strip().splitlines()
print('templates', len(templates))

gerondif_map = {'be':'being', 'begin':'beginning', 'can':'to be able'}
                        
def cycle(lst):
    while not rd.shuffle(lst): yield from lst

meta_sentences_it = cycle(meta_sentences)
questions_it = cycle(questions)
ends_it = cycle(ends)

meta_A_it = (s for s in meta_sentences_it if len(s.split()) <= 8 and not any(w in s for w in ('but', 'and yet', 'cannot', 'I’ll')))
ends_A_it = (s for s in ends_it if len(s) < 15)

templates_B = [t for t in templates if '?' in t or 'if ' in t or 'does ' in t or '{do_conj}' in t]
print('templates_B', len(templates_B))
meta_B_it = (s for s in meta_sentences_it if '?' in s or 'perhaps' in s)

templates_D = [t for t in templates if any(w in t for w in ('again', 'always', 'never ending', 'begin again', 'same thing'))]
print('templates_D', len(templates_D))
meta_D_it = (s for s in meta_sentences_it if any(w in s for w in ('again', 'same', 'never ending', 'begin again', 'go on, not go on', 'always the same', 'again, always')))
templates_E = [t for t in templates if any(neg in t for neg in ('cannot ', 'impossible to', 'not to ', 'never to ', 'one should ', 'but {p} cannot', 'cannot stop'))]
print('templates_E', len(templates_E))
meta_E_it = (s for s in meta_sentences_it if any(phrase in s for phrase in ('cannot ', 'impossible to', 'not to ', 'never to ','one should ', 'but one cannot', 'cannot stop', 'cannot be silent', 'cannot speak')))
templates_F = [t for t in templates if t.startswith(('no ', 'without ', 'neither ', '{n}, {n2}, {n3}:'))]
print('templates_F', len(templates_F))
meta_F_it = (s for s in meta_sentences_it if any(w in s for w in ('no body', 'no name', 'no me', 'no {', 'without ', 'neither ', ': none of it')))

translate = {'adv':(adverbs, adverb_weights), 'p':(pronouns,), 'v':(verbs, verbs_weights), 'n':(nouns,)}

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
                v = v if conj and (v:=self.get(key)) else ((rd.choices(*trsl, k=1)[0] if len(trsl)==2 else rd.choice(trsl[0])))
            else: v = k
            if conj:
                vv = v.split()
                verb = vv[0]
                if gerondif: verb = gerondif_map.get(verb, (verb[:-1] if verb[-1]=='e' else verb)+'ing')
                else:
                    subject = self.get('p')
                    if not subject: subject = self.__missing__('p') if '?' in self.template else 'it' # create default subject if question
                    if_not_I = subject != 'I'
                    match verb:
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
            if not n or not trsl or not any(v==self.get(oldkey.replace(str(n),str(i) if i else '')) for i in range(0, n)): break
        self[oldkey] = v
        return v

_seen_cache = deque(maxlen=2) # window sentences

def next_unique(it):
    while True:
        s = next(it)
        if s not in _seen_cache:
            _seen_cache.append(s)
            return s
    
def capitalize(s): return s[0].upper() + s[1:]

def generate_sentence(templates_m, metas_it, meta_ratio):
    if rd.random() < meta_ratio: return next_unique(metas_it)
    else: return next_unique(capitalize((t:=rd.choice(templates_m)).format_map(Resolver(t))) for _ in iter(int,42)) # dummy iterator

def generate_sentences(templates_m=templates, metas_it=meta_sentences_it, count_min=8, count_max=12, meta_ratio=0.25, question_ratio=0.12):
    _seen_cache.clear()
    result = []
    for i in range(rd.randint(count_min, count_max)):
        result.append(generate_sentence(templates_m, metas_it, meta_ratio))
        if i >= 1 and rd.random() < question_ratio: result.append(next_unique(questions_it))
    if rd.random() < 0.6:
        if rd.random() < 0.7: result.append(next_unique(questions_it))
        else: result.append(next(ends_it))
    return result

def generate_text(mode):
    match mode: 
        case 'A':  # Mode A: Raw lexical shards — mimics the skeletal openings of Texts 1–5.
            result = [next_unique(meta_A_it) for _ in range(rd.randint(3, 6))]
            if rd.random() < 0.3: result.append(next(ends_A_it))
        case 'B':  # Mode B: Interrogative vertigo — echoes the obsessive doubt of Texts 6–11.
            result = generate_sentences(templates_B, meta_B_it, 6, 10, 0.3, 0.25)
        case 'D':  # Mode D: Compulsive repetition — captures the looped despair of Texts 3, 5, 7.
            result = generate_sentences(templates_D, meta_D_it, 5, 9, 0.4, 0.05)
        case 'E':  # Mode E: Pure negation / aporia — inspired by the impossible imperatives in Texts 2, 4, 8.
            result = generate_sentences(templates_E, meta_E_it, 5, 9, 0.3, 0.1)
        case 'F':  # Mode F: Anatomy of absence — channels the desolate catalogues of Texts 1, 6, 9.
            result = generate_sentences(templates_F, meta_F_it, 4, 8, 0.1, 0.02)
        case _:    # Mode C: Continuous murmuring — reflects the flowing monologue of late Texts (esp. 12–13).
            result = generate_sentences()
    return '\n'.join(result)

# Generate full output for NaNoGenMo
# normally one text by page
texts_count = 300 # estimate count
output = []
for m, p in [('F',12),('E',12),('D',12),('B',15),('A',9),('C',40)]:
    mc = (texts_count * p) // 100
    print(m, mc)
    output.extend(generate_text(m) for _ in range(mc))
    #output.append('*'*25) # debug

thefulltext = '\n\n'.join(output)
print(f"Total words: {len(thefulltext.split())}")
Path(__file__[:-3]+strftime('-%y%m%d-%H%M%S.txt')).write_text(thefulltext, encoding='utf8')
