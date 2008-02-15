#!/usr/bin/python
import sys
# singleton selmao are colored black
singletons=dict.fromkeys('''\
BE	CEI	FEhU	JAI	KU	MEhU	NUhA	SI	VAU	ZOhU
BEhO	CO	FIhO	JOhI	LEhU	ME	NUhI	SOI	VEhO	ZO
BEI	CU	FOI	KEhE	LIhU	MOhE	NUhU	SU	VEI
BIhE	DAhO	FUhA	KEI	LOhO	MOhI	PEhE	TEhU	VUhO
BO	DOhU	FUhE	KE	LOhU	NAhU	PEhO	TEI	XI
BOI	DOI	FUhO	KI	LUhU	NAI	RAhO	TOI	Y
BU	FAhO	GEhU	KUhE	LU	NIhE	SA	TUhE	ZEI
CEhE	FEhE	GI	KUhO	MAhO		SEhU	TUhU	ZIhE
'''.split())
# mapping from cmavo to selmao
selmaodict=dict(pair.split() for pair in '''\
.a	A
.a'a	UI
.a'e	UI
.a'i	UI
.ai	UI
.a'o	UI
.a'u	UI
.au	UI
ba'a	UI
ba'e	BAhE
ba'i	BAI
bai	BAI
ba'o	ZAhO
ba	PU
bau	BAI
ba'u	UI
be'a	FAhA
be	BE
be'e	COI
be'i	BAI
bei	BEI
be'o	BEhO
be'u	UI
bi'e	BIhE
bi'i	BIhI
bi'o	BIhI
bi	PA
bi'u	UI
bo	BO
boi	BOI
bu'a	GOhA
bu	BU
bu'e	GOhA
bu'i	GOhA
bu'o	UI
bu'u	FAhA
by	BY
ca'a	CAhA
ca'e	UI
ca'i	BAI
cai	CAI
ca'o	ZAhO
ca	PU
cau	BAI
ca'u	FAhA
ce'a	LAU
ce'e	CEhE
cei	CEI
ce'i	PA
ce	JOI
ce'o	JOI
ce'u	KOhA
ci'e	BAI
ci'i	PA
ci'o	BAI
ci	PA
ci'u	BAI
co'a	ZAhO
co	CO
co'e	GOhA
coi	COI
co'i	ZAhO
co'o	COI
co'u	ZAhO
cu'a	VUhU
cu	CU
cu'e	CUhE
cu'i	CAI
cu'o	MOI
cu'u	BAI
cy	BY
da'a	PA
da'e	KOhA
da'i	UI
dai	UI
da	KOhA
da'o	DAhO
da'u	KOhA
dau	PA
de'a	ZAhO
de'e	KOhA
de'i	BAI
dei	KOhA
de	KOhA
de'o	VUhU
de'u	KOhA
di'a	ZAhO
di'e	KOhA
di'i	TAhE
di	KOhA
di'o	BAI
di'u	KOhA
do'a	UI
do'e	BAI
doi	DOI
do'i	KOhA
do	KOhA
do'o	KOhA
do'u	DOhU
du'a	FAhA
du'e	PA
du	GOhA
du'i	BAI
du'o	BAI
du'u	NU
dy	BY
.e	A
.e'a	UI
.e'e	UI
.e'i	UI
.ei	UI
.e'o	UI
.e'u	UI
fa'a	FAhA
fa'e	BAI
fa	FA
fai	FA
fa'i	VUhU
fa'o	FAhO
fau	BAI
fa'u	JOI
fe'a	VUhU
fe'e	FEhE
fe	FA
fei	PA
fe'i	VUhU
fe'o	COI
fe'u	FEhU
fi'a	FA
fi'e	BAI
fi	FA
fi'i	COI
fi'o	FIhO
fi'u	PA
fo'a	KOhA
fo'e	KOhA
fo	FA
foi	FOI
fo'i	KOhA
fo'o	KOhA
fo'u	KOhA
fu'a	FUhA
fu'e	FUhE
fu	FA
fu'i	UI
fu'o	FUhO
fu'u	VUhU
fy	BY
ga'a	BAI
ga'e	BY
ga	GA
gai	PA
ga'i	UI
ga'o	GAhO
gau	BAI
ga'u	FAhA
ge'a	VUhU
ge'e	UI
ge	GA
ge'i	GA
gei	VUhU
ge'o	BY
ge'u	GEhU
gi'a	GIhA
gi'e	GIhA
gi	GI
gi'i	GIhA
gi'o	GIhA
gi'u	GIhA
go'a	GOhA
go'e	GOhA
go	GA
go'i	GOhA
goi	GOI
go'o	GOhA
go'u	GOhA
gu'a	GUhA
gu'e	GUhA
gu	GA
gu'i	GUhA
gu'o	GUhA
gu'u	GUhA
gy	BY
.i'a	UI
.ia	UI
.i'e	UI
.ie	UI
.i	I
.i'i	UI
.ii	UI
.i'o	UI
.io	UI
.i'u	UI
.iu	UI
ja'a	NA
ja'e	BAI
ja'i	BAI
jai	JAI
ja	JA
ja'o	UI
jau	PA
je'a	NAhE
je'e	COI
je'i	JA
jei	NU
je	JA
je'o	BY
je'u	UI
ji	A
ji'a	UI
ji'e	BAI
ji'i	PA
ji'o	BAI
ji'u	BAI
jo'a	UI
jo'e	JOI
jo'i	JOhI
joi	JOI
jo	JA
jo'o	BY
jo'u	JOI
ju'a	UI
ju'e	JOI
ju'i	COI
ju	JA
ju'o	UI
ju'u	VUhU
jy	BY
ka'a	BAI
ka'e	CAhA
ka'i	BAI
kai	BAI
ka	NU
ka'o	PA
ka'u	UI
kau	UI
ke'a	KOhA
ke'e	KEhE
ke'i	GAhO
kei	KEI
ke	KE
ke'o	COI
ke'u	UI
ki'a	UI
ki'e	COI
ki'i	BAI
ki	KI
ki'o	PA
ki'u	BAI
ko'a	KOhA
ko'e	KOhA
koi	BAI
ko'i	KOhA
ko	KOhA
ko'o	KOhA
ko'u	KOhA
ku'a	JOI
ku'e	KUhE
ku'i	UI
ku	KU
ku'o	KUhO
ku'u	BAI
ky	BY
la'a	UI
la'e	LAhE
la'i	LA
lai	LA
la	LA
la'o	ZOI
la'u	BAI
lau	LAU
le'a	BAI
le'e	LE
le'i	LE
lei	LE
le	LE
le'o	UI
le'u	LEhU
li'a	UI
li'e	BAI
li'i	NU
li	LI
li'o	UI
li'u	LIhU
lo'a	BY
lo'e	LE
lo'i	LE
loi	LE
lo	LE
lo'o	LOhO
lo'u	LOhU
lu'a	LAhE
lu'e	LAhE
lu'i	LAhE
lu	LU
lu'o	LAhE
lu'u	LUhU
ly	BY
ma'a	KOhA
ma'e	BAI
ma'i	BAI
mai	MAI
ma	KOhA
ma'o	MAhO
mau	BAI
ma'u	PA
me'a	BAI
me'e	BAI
mei	MOI
me'i	PA
me	ME
me'o	LI
me'u	MEhU
mi'a	KOhA
mi'e	COI
mi'i	BIhI
mi	KOhA
mi'o	KOhA
mi'u	UI
mo'a	PA
mo'e	MOhE
mo	GOhA
mo'i	MOhI
moi	MOI
mo'o	MAI
mo'u	ZAhO
mu'a	UI
mu'e	NU
mu'i	BAI
mu'o	COI
mu	PA
mu'u	BAI
my	BY
na'a	BY
na'e	NAhE
nai	NAI
na'i	UI
na	NA
na'o	TAhE
nau	CUhE
na'u	NAhU
ne'a	FAhA
ne	GOI
ne'i	FAhA
nei	GOhA
ne'o	VUhU
ne'u	FAhA
ni'a	FAhA
ni'e	NIhE
ni'i	BAI
ni	NU
ni'o	NIhO
ni'u	PA
no'a	GOhA
no'e	NAhE
no'i	NIhO
noi	NOI
no'o	PA
no	PA
no'u	GOI
nu'a	NUhA
nu'e	COI
nu'i	NUhI
nu	NU
nu'o	CAhA
nu'u	NUhU
ny	BY
.o	A
.o'a	UI
.o'e	UI
.o'i	UI
.oi	UI
.o'o	UI
.o'u	UI
pa'a	BAI
pa'e	UI
pai	PA
pa'i	VUhU
pa'o	FAhA
pa	PA
pa'u	BAI
pau	UI
pe'a	UI
pe'e	PEhE
pe	GOI
pei	CAI
pe'i	UI
pe'o	PEhO
pe'u	COI
pi'a	VUhU
pi'e	PA
pi'i	VUhU
pi'o	BAI
pi	PA
pi'u	JOI
po'e	GOI
po	GOI
po'i	BAI
poi	NOI
po'o	UI
po'u	GOI
pu'a	BAI
pu'e	BAI
pu'i	CAhA
pu'o	ZAhO
pu	PU
pu'u	NU
py	BY
ra'a	BAI
ra'e	PA
ra'i	BAI
rai	BAI
ra	KOhA
ra'o	RAhO
rau	PA
ra'u	UI
re'a	VUhU
re'e	UI
re'i	COI
rei	PA
re'o	FAhA
re	PA
re'u	ROI
ri'a	BAI
ri'e	UI
ri'i	BAI
ri	KOhA
ri'o	VUhU
ri'u	FAhA
ro'a	UI
ro'e	UI
roi	ROI
ro'i	UI
ro'o	UI
ro	PA
ro'u	UI
ru'a	UI
ru'e	CAI
ru'i	TAhE
ru	KOhA
ru'o	BY
ru'u	FAhA
ry	BY
sa'a	UI
sa'e	UI
sai	CAI
sa'i	VUhU
sa'o	VUhU
sa	SA
sau	BAI
sa'u	UI
se'a	UI
se'e	BY
sei	SEI
se'i	UI
se'o	UI
se	SE
se'u	SEhU
si'a	UI
si'e	MOI
si'i	VUhU
si'o	NU
si	SI
si'u	BAI
so'a	PA
so'e	PA
so'i	PA
soi	SOI
so'o	PA
so	PA
so'u	PA
su'a	UI
su'e	PA
su'i	VUhU
su'o	PA
su	SU
su'u	NU
sy	BY
ta'a	COI
ta'e	TAhE
ta'i	BAI
tai	BAI
ta	KOhA
ta'o	UI
tau	LAU
ta'u	UI
te'a	VUhU
te'e	FAhA
tei	TEI
te'o	PA
te	SE
te'u	TEhU
ti'a	FAhA
ti'e	UI
ti'i	BAI
ti	KOhA
ti'o	SEI
ti'u	BAI
to'a	BY
to'e	NAhE
to'i	TO
toi	TOI
to'o	FAhA
to	TO
to'u	UI
tu'a	LAhE
tu'e	TUhE
tu'i	BAI
tu	KOhA
tu'o	PA
tu'u	TUhU
ty	BY
.u	A
.u'a	UI
.ua	UI
.u'e	UI
.ue	UI
.u'i	UI
.ui	UI
.u'o	UI
.uo	UI
.u'u	UI
.uu	UI
va'a	VUhU
va'e	MOI
vai	PA
va'i	UI
va'o	BAI
va'u	BAI
vau	VAU
va	VA
ve'a	VEhA
ve'e	VEhA
ve'i	VEhA
vei	VEI
ve'o	VEhO
ve	SE
ve'u	VEhA
vi'a	VIhA
vi'e	VIhA
vi'i	VIhA
vi'o	COI
vi'u	VIhA
vi	VA
vo'a	KOhA
vo'e	KOhA
vo'i	KOhA
voi	NOI
vo'o	KOhA
vo	PA
vo'u	KOhA
vu'a	FAhA
vu'e	UI
vu'i	LAhE
vu'o	VUhO
vu'u	VUhU
vu	VA
vy	BY
xa	PA
xe	SE
xi	XI
xo	PA
xu	UI
xy	BY
.y	Y
.y'y	BY
za'a	UI
za'e	BAhE
zai	LAU
za'i	NU
za'o	ZAhO
zau	BAI
za'u	PA
za	ZI
ze'a	ZEhA
ze'e	ZEhA
ze'i	ZEhA
zei	ZEI
ze'o	FAhA
ze	PA
ze'u	ZEhA
zi'e	ZIhE
zi'o	KOhA
zi	ZI
zo'a	FAhA
zo'e	KOhA
zo'i	FAhA
zoi	ZOI
zo'o	UI
zo'u	ZOhU
zo	ZO
zu'a	FAhA
zu'e	BAI
zu'i	KOhA
zu'o	NU
zu'u	UI
zu	ZI
zy	BY
'''.splitlines())
# mapping from cmavo to short description
cmavodict=dict(pair.split('\t') for pair in '''\
.e	sumti and
ji	sumti conn ?
.o	sumti iff
.a	sumti or
.u	sumti whether
ba'e	emphasize next
za'e	nonce-word next
du'o	according to
si'u	aided by
zau	approved by
ki'i	as a relation of
du'i	as much as
cu'u	as said by
tu'i	associated with site
ti'u	associated with time
di'o	at the locus of
ji'u	based on
ri'a	because of cause
ni'i	because of logic
mu'i	because of motive
ki'u	because of reason
va'u	benefiting from
koi	bounded by
ca'i	by authority of
ta'i	by method
pu'e	by process
ja'i	by rule
kai	characterizing
bai	compelled by
fi'e	created by
de'i	dated
ci'o	emotionally felt by
mau	exceeded by
mu'u	exemplified by
ri'i	experienced by
ra'i	from source
ka'a	gone to by
pa'u	having component
pa'a	in addition to
le'a	in category
ku'u	in culture
tai	in form
bau	in language
ma'i	in reference frame
ci'e	in system
fau	in the event of
po'i	in the sequence
cau	lacked by
ma'e	material object
ci'u	on the scale
ra'a	pertained to by
pu'a	pleased by
li'e	preceded by
la'u	quantifying
ba'i	replaced by
ka'i	represented by
sau	requiring
fa'e	reverse of
be'i	sent by
ti'i	suggested by
ja'e	therefore result
ga'a	to observer
va'o	under conditions
me'a	undercut by
ji'o	under direction of
do'e	unspecif modal
ji'e	up to limit
pi'o	used by
gau	with active agent
zu'e	with actor
me'e	with name
rai	with superlative
be'o	end linked sumti
bei	link more sumti
be	link sumti
bi'e	hi priority operator
mi'i	center-range
bi'o	ordered interval
bi'i	unordered interval
boi	end number or lerfu
bo	short scope link
bu	word to lerfu
jo'o	Arabic shift
na'a	cancel shifts
se'e	character code
ru'o	Cyrillic shift
ge'o	Greek shift
je'o	Hebrew shift
lo'a	Lojban shift
to'a	lower-case shift
ga'e	upper-case shift
.y'y	'
by	b
cy	c
dy	d
fy	f
gy	g
jy	j
ky	k
ly	l
my	m
ny	n
py	p
ry	r
sy	s
ty	t
vy	v
xy	x
zy	z
ca'a	actually is
pu'i	can and has
nu'o	can but has not
ka'e	innately capable of
pei	emotion ?
cai	intense emotion
cu'i	neutral emotion
sai	strong emotion
ru'e	weak emotion
ce'e	afterthought termset
cei	pro-bridi assign
ju'i	attention
coi	greetings
fi'i	hospitality
ta'a	interruption
mu'o	over
fe'o	over and out
co'o	partings
pe'u	please
ke'o	please repeat
nu'e	promise
re'i	ready to receive
be'e	request to send
je'e	roger
mi'e	self-introduction
ki'e	thanks
vi'o	wilco
co	tanru inversion
cu'e	modal ?
nau	reference point
cu	selbri separator
da'o	cancel pro-assigns
do'u	end vocative
doi	vocative marker
fa	1st sumti place
fe	2nd sumti place
fi	3rd sumti place
fo	4th sumti place
fu	5th sumti place
fai	extra sumti place
du'a	east of
be'a	north of
ne'u	south of
vu'a	west of
ga'u	above
ti'a	behind
ni'a	below
ca'u	in front of
zu'a	on the left of
ri'u	on the right of
ru'u	surrounding
re'o	adjacent to
te'e	bordering
bu'u	coincident with
ne'a	next to
pa'o	transfixing
ne'i	within
to'o	away from point
zo'i	inward
ze'o	outward
zo'a	tangential to
fa'a	towards point
fa'o	end of text
fi'a	sumti place ?
fe'e	space aspects
fe'u	end modal selbri
fi'o	selbri to modal
foi	end composite lerfu
fu'a	reverse Polish
fu'e	indicator scope
fu'o	end indicator scope
ge	fore and
ge'i	fore conn ?
go	fore iff
ga	fore or
gu	fore whether
ke'i	exclusive interval
ga'o	inclusive interval
ge'u	end relative phrase
gi	connective medial
gi'e	bridi and
gi'i	bridi conn ?
gi'o	bridi iff
gi'a	bridi or
gi'u	bridi whether
mo	bridi ?
nei	current bridi
go'u	earlier bridi
go'o	future bridi
go'i	last bridi
no'a	next outer bridi
go'e	penultimate bridi
go'a	recent bridi
du	same identity as
bu'a	some selbri 1
bu'e	some selbri 2
bu'i	some selbri 3
co'e	unspecif bridi
no'u	incidental identity
ne	incidental phrase
po	is specific to
goi	pro-sumti assign
po'u	restrictive identity
pe	restrictive phrase
po'e	which belongs to
gu'e	fore tanru and
gu'i	fore tanru conn ?
gu'o	fore tanru iff
gu'a	fore tanru or
gu'u	fore tanru whether
.i	sentence link
jai	modal conversion
je	tanru and
je'i	tanru conn ?
jo	tanru iff
ja	tanru or
ju	tanru whether
jo'i	array
fa'u	and respectively
pi'u	cross product
joi	in a mass with
ce'o	in a sequence with
ce	in a set with
jo'u	in common with
ku'a	intersection
jo'e	union
ju'e	vague connective
ke'e	end grouping
kei	end abstraction
ke	start grouping
ki	tense default
da	something 1
de	something 2
di	something 3
da'u	earlier utterance
da'e	eventual utterance
di'u	last utterance
di'e	next utterance
de'u	recent utterance
de'e	soon utterance
dei	this utterance
do'i	unspecif utterance
ko	imperative
mi	me
mi'o	me and you
mi'a	we, not you
ma'a	we with you
do	you
do'o	you and others
ko'a	it-1
fo'u	it-10
ko'e	it-2
ko'i	it-3
ko'o	it-4
ko'u	it-5
fo'a	it-6
fo'e	it-7
fo'i	it-8
fo'o	it-9
vo'a	x1 it
vo'e	x2 it
vo'i	x3 it
vo'o	x4 it
vo'u	x5 it
ru	earlier sumti
ri	last sumti
ra	recent sumti
ta	that there
tu	that yonder
ti	this here
zi'o	nonexistent it
ke'a	relativized it
ma	sumti ?
zu'i	typical it
zo'e	unspecif it
ce'u	lambda
ku	end sumti
ku'e	end mex forethought
ku'o	end relative clause
tu'a	the bridi implied by
lu'a	the individuals of
lu'o	the mass composed of
la'e	the referent of
vu'i	the sequence of
lu'i	the set composed of
lu'e	the symbol for
la	that named
lai	the mass of named
la'i	the set of named
ce'a	font shift
lau	punctuation mark
zai	select alphabet
tau	shift next lerfu
le'u	end error quote
le	the described
lei	the mass described
loi	the mass really is
lo	the really is
le'i	the set described
lo'i	the set really is
le'e	the stereotypical
lo'e	the typical
li'u	end quote
me'o	the mex
li	the number
lo'o	end mex sumti
lo'u	error quote
lu'u	end sumti qualifiers
lu	quote
ma'o	operand to operator
mo'o	section ordinal
mai	sentence ordinal
me'u	end sumti to selbri
me	sumti to selbri
mo'e	sumti to operand
mo'i	space motion
mei	cardinal selbri
moi	ordinal selbri
si'e	portion selbri
cu'o	probability selbri
va'e	scalar selbri
ja'a	bridi affirmer
na	bridi negator
to'e	polar opposite
je'a	scalar affirmer
na'e	scalar contrary
no'e	scalar midpoint not
na'u	selbri to operator
nai	negate last word
ni'e	selbri to operand
ni'o	new topic
no'i	old topic
voi	descriptive clause
noi	incidental clause
poi	restrictive clause
zu'o	activity abstract
mu'e	point-event abstract
pu'u	process abstract
za'i	state abstract
ni	amount abstract
du'u	bridi abstract
si'o	concept abstract
nu	event abstract
li'i	experience abstract
nu'a	operator to selbri
nu'i	start fore termset
nu'u	end fore termset
ka	property abstract
jei	truth abstract
su'u	unspecif abstract
no	0
pa	1
re	2
ci	3
vo	4
mu	5
xa	6
ze	7
bi	8
so	9
dau	hex digit A
fei	hex digit B
gai	hex digit C
jau	hex digit D
rei	hex digit E
vai	hex digit F
pi	decimal point
pi'e	digit separator
fi'u	fraction slash
za'u	greater than
me'i	less than
ni'u	negative number
ki'o	number comma
ce'i	percent
ma'u	positive number
ra'e	repeating decimal
da'a	all except
so'a	almost all
ji'i	approximately
su'o	at least
su'e	at most
ro	each
rau	enough
so'u	few
so'i	many
so'e	most
so'o	several
mo'a	too few
du'e	too many
te'o	exponential e
ka'o	imaginary i
ci'i	infinity
tu'o	null operand
xo	number ?
pai	pi
no'o	typical value
pe'e	termset conn mark
pe'o	fore mex operator
ba	after
pu	before
ca	during
ra'o	pro-assign update
re'u	ordinal tense
roi	quantified tense
sa	erase utterance
se	2nd conversion
te	3rd conversion
ve	4th conversion
xe	5th conversion
se'u	end discursive
sei	discursive bridi
ti'o	mex precedence
si	erase word
soi	reciprocal sumti
su	erase discourse
ru'i	continuously
ta'e	habitually
di'i	regularly
na'o	typically
te'u	end mex converters
tei	composite lerfu
to'i	editorial unquote
toi	end parenthesis
to	start parenthesis
tu'e	start text scope
tu'u	end text scope
.i'a	acceptance
.ie	agreement
.a'e	alertness
.u'i	amusement
.i'o	appreciation
.i'e	approval
.a'a	attentive
.ia	belief
.o'i	caution
.o'e	closeness
.e'e	competence
.oi	complaint
.uo	completion
.e'i	constraint
.u'o	courage
.au	desire
.ua	discovery
.a'i	effort
.i'u	familiarity
.ii	fear
.u'a	gain
.ui	happiness
.a'o	hope
.ai	intent
.a'u	interest
.iu	love
.ei	obligation
.o'o	patience
.e'a	permission
.uu	pity
.o'a	pride
.o'u	relaxation
.u'u	repentance
.e'o	request
.io	respect
.e'u	suggestion
.ue	surprise
.i'i	togetherness
.u'e	wonder
ba'a	I anticipate
ja'o	I conclude
ca'e	I define
su'a	I generalize
ti'e	I hear
ka'u	I know culturally
se'o	I know internally
za'a	I observe
pe'i	I opine
ru'a	I postulate
ju'a	I state
sa'a	editorial insertion
kau	indirect question
ta'u	making a tanru
na'i	metalinguistic not
jo'a	metalinguistic yes
bi'u	new information
li'o	omitted text
pau	question follows
mi'u	ditto
ku'i	however
ji'a	in addition
si'a	similarly
po'o	uniquely
ta'o	by the way
pe'a	figurative
ra'u	chiefly
li'a	clearly
ba'u	exaggeration
mu'a	for example
do'a	generously
to'u	in brief
va'i	in other words
pa'e	justice
zu'u	on the one hand
sa'e	precisely speaking
la'a	probability
ke'u	repeating
sa'u	simply speaking
da'i	supposing
je'u	truth
ro'i	emotional
ro'e	mental
ro'o	physical
ro'u	sexual
ro'a	social
re'e	spiritual
le'o	aggressive
ju'o	certainty
fu'i	easy
dai	empathy
ga'i	hauteur
zo'o	humorously
be'u	lack
ri'e	release of emotion
se'i	self-oriented
se'a	self-sufficiency
vu'e	virtue
ki'a	textual confusion
xu	true-false ?
ge'e	unspecif emotion
bu'o	start emotion
vi	here at
va	there at
vau	end simple bridi
vu	yonder at
ve'u	big space interval
ve'a	small space interval
ve'i	tiny space interval
ve'e	whole space interval
ve'o	right bracket
vei	left bracket
vi'i	1-space interval
vi'a	2-space interval
vi'u	3-space interval
vi'e	4-space interval
vu'o	long scope relative
ge'a	null operator
fu'u	unspecif operator
fe'i	divided by
vu'u	minus
su'i	plus
pi'i	times
gei	exponential notation
ju'u	number base
pa'i	ratio
fa'i	reciprocal of
te'a	to the power
cu'a	absolute value
va'a	additive inverse
ne'o	factorial
de'o	logarithm
fe'a	nth root of
sa'o	derivative
ri'o	integral
sa'i	matrix of columns
pi'a	matrix of rows
si'i	sigma summation
re'a	transpose
xi	subscript
.y	hesitation
co'i	achievative
pu'o	anticipative
co'u	cessative
mo'u	completive
ca'o	continuative
co'a	initiative
de'a	pausative
ba'o	perfective
di'a	resumptitive
za'o	superfective
ze'u	long time interval
ze'a	medium time interval
ze'i	short time interval
ze'e	whole time interval
zei	lujvo glue
zi'e	rel clause joiner
zu	long time
za	medium time
zi	short time
zo	1-word quote
zo'u	end prenex
zoi	non-Lojban quote
la'o	the non-Lojban named
'''.splitlines())
# CSS stylesheet
stylesheet='''
body { font-family: monospace; color: white; background-color: black; }
table { float: left; margin: .5em; }
.clear { clear: left; }
tr { border: none; margin: 0; padding: 0; }
td { border: none; margin: 0; padding: .2em; border: thin black solid; }
.hilite { border: thin red solid; background-color: black; color: yellow; }
.legend { float: left; min-width: 7em; margin-bottom: .5em; }
'''
# JavaScript (toggles highlighting)
script='''
function hilite(selmao) {
  divs = document.getElementsByTagName("div")
  for (i=0; i < divs.length; i++) {
    div=divs[i]
    if (div.className == "hilite") {
      div.className = ""
    }
    else if (div.id == selmao) {
      div.className = "hilite"
    }
  }
  tds = document.getElementsByTagName("td")
  for (i=0; i < tds.length; i++) {
    td=tds[i]
    if (td.getAttribute('name') == selmao) {
      td.className = "hilite"
    } 
    else {
      td.className = td.getAttribute('name')
    }
  }
}
'''
# list of selma'o
selmaos=sorted(dict.fromkeys(selmaodict.values()))
sys.stderr.write('%s selmaos\n' % len(selmaos))
sys.stderr.write('%s proper selmaos\n' % (len(selmaos)-len(singletons)))
# generate a color scale (RGB, three hex digits)
# def xselections(items, n):
#     if n==0: yield []
#     else:
#         for i in xrange(len(items)):
#             for ss in xselections(items, n-1):
#                 yield [items[i]]+ss
# colorscale = map(''.join, (xselections('27bf', 3)))
colorscale = []
digits = "7bf"
def gencolor(i,j,x,y):
    color=list("000")
    color[i]=x
    color[j]=y
    return ''.join(color)
for i in [0,1,2]:
    for x in digits:
        colorscale.append(gencolor(i,i,x,x))
    for x in '29':
        for j in [0,1,2]:
            if i != j:
                for y in digits:
                    colorscale.append(gencolor(i,j,x,y))
colorscale.append("222")
colorscale.append("555")
colorscale.append("888")
colorscale.append("aaa")
sys.stderr.write('%s colors generated\n' % len(colorscale))
# mapping from selma'o to RGB
colors = {}
for selmao in selmaos:
    colors[selmao]=colorscale.pop(0) \
        if selmao not in singletons else "000"
# assign dark grey to UI
def force_color(selmao, color):
    for k,v in colors.iteritems():
        if v == color:
            break
    colors[k]=colors[selmao]
    colors[selmao]=color
force_color("UI", "00f")
force_color("PA", "f00")
force_color("BAI", "f90")
force_color("KOhA", "b09")
# append coloring to stylesheet
for selmao, color in colors.iteritems():
    stylesheet += '.%s { background-color: #%s; }\n' % (selmao, color)
# mapping from first to second cmavo vowels
ws={
    'a': "'a 'e 'i 'o 'u i u".split(),
    'e': "'a 'e 'i 'o 'u i".split(),
    'i': "'a 'e 'i 'o 'u ".split(),
    'o': "'a 'e 'i 'o 'u i".split(),
    'u': "'a 'e 'i 'o 'u ".split(),
    'y': "'y".split(),
    }
# HTML header
write=sys.stdout.write
write('''\
<html>
<head>
  <style type="text/css">%s</style>
  <script type="text/javascript">%s</script></head>
<body>''' % (stylesheet, script))
# the cheatsheet consists of floating tables for each vowel
for v in 'aeiou':
    write('<table>' if v not in 'y' else '<table class="clear">')
    for c in '.bcdfgjklmnprstvxz':
        write('<tr>')
        for w in [''] + ws[v]:
            cmavo = c + v + w
            if cmavo in selmaodict:
                selmao=selmaodict[cmavo]
                write('\n')
                write('<td name="%s" class="%s" title="%s" onclick="hilite(this.getAttribute(\'name\'))" id="%s">%s</td>' % (
                        selmao, selmao, cmavodict[cmavo], cmavo, cmavo))
            else:
                write('<td></td>')
        write('</tr>')
    write('</table>')
# at the bottom, we have the selma'o legend: floating blocks of 9 (color,selma'o) subblocks
def mklegend(xs):
    write('<div class="legend">')
    for x in xs:
        write('<div id="%s" onclick="hilite(this.id)"><span class="%s">&nbsp;&nbsp;&nbsp;</span>&nbsp;%s</div>' % (x, x, x))
        write('\n')
    write('</div>')
for collection in (set(selmaos)-set(singletons), singletons):
    write('\n')
    write('<hr class="clear">')
    xs=[]
    for selmao in sorted(collection):
        if len(xs)>=5:
            mklegend(xs)
            xs=[]
        xs.append(selmao)
    if xs:
        mklegend(xs)
# finish HTML
write('</body></html>')
write('\n')
