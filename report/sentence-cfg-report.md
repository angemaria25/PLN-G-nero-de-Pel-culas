# Gramáticas CFL

## Oración 1 

Texto: Como fan de las series españolas y de Najwa, esto duele, la serie es muy mala

Tokens: ['como', 'fan', 'de', 'las', 'series', 'españolas', 'y', 'de', 'najwa', ',', 'esto', 'duele', ',', 'la', 'serie', 'es', 'muy', 'mala']
POS: ['SCONJ', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADJ', 'CCONJ', 'ADP', 'PROPN', 'PUNCT', 'PRON', 'VERB', 'PUNCT', 'DET', 'NOUN', 'AUX', 'ADV', 'ADJ']

```
S -> PRELUDE PUNCT CLAUSE PUNCT CLAUSE
PRELUDE -> SCONJ NP
CLAUSE -> NP VP
NP -> NP ADP NP CCONJ ADP NP
NP -> DET NOUN | DET NOUN ADJ
NP -> NOUN | PRON | PROPN 
VP -> VERB
VP -> AUX ADV ADJ
```

## Oración 2 

Texto: Manu Ríos da para lo que da, enseñar cacho, Najwa hace de mala, papel repetido que no aporta ninguna capa nueva

Tokens: ['manu', 'ríos', 'da', 'para', 'lo', 'que', 'da', ',', 'enseñar', 'cacho', ',', 'najwa', 'hace', 'de', 'mala', ',', 'papel', 'repetido', 'que', 'no', 'aporta', 'ninguna', 'capa', 'nueva']
POS: ['PROPN', 'PROPN', 'VERB', 'ADP', 'PRON', 'SCONJ', 'VERB', 'PUNCT', 'VERB', 'NOUN', 'PUNCT', 'PROPN', 'VERB', 'ADP', 'ADJ', 'PUNCT', 'NOUN', 'NOUN', 'SCONJ', 'ADV', 'VERB', 'DET', 'NOUN', 'ADJ']

```
S -> CLAUSE PUNCT CLAUSE PUNCT CLAUSE PUNCT CLAUSE
CLAUSE -> NP VP | VP NP
CLAUSE -> NP SCONJ VP
NP -> PROPN | PROPN NP
NP -> NOUN | NOUN NP   
NP -> DET NOUN ADJ
VP -> VERB ADP PRON SCONJ VERB
VP -> VERB | VERB ADP ADJ
VP -> ADV VERB NP
```

## Oración 3 

Texto: Telenovela de mediodía con un guión mediocre y diálogos planos

Tokens: ['telenovela', 'de', 'mediodía', 'con', 'un', 'guión', 'mediocre', 'y', 'diálogos', 'planos']
POS: ['PROPN', 'ADP', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADJ', 'CCONJ', 'NOUN', 'ADJ']

```
S -> NP
NP -> PROPN | PROPN PP | PROPN NP PUNCT NP | PROPN NP CCONJ NP
NP -> PP
NP -> DET NP 
NP -> NOUN | NOUN ADJ 
PP -> ADP NP | ADP NP PP
```

## Oración 4 

Texto: En aspectos técnicos como fotografía, sonido, también deja que desear

Tokens: ['en', 'aspectos', 'técnicos', 'como', 'fotografía', ',', 'sonido', ',', 'también', 'deja', 'que', 'desear']
POS: ['ADP', 'NOUN', 'ADJ', 'SCONJ', 'NOUN', 'PUNCT', 'NOUN', 'PUNCT', 'ADV', 'VERB', 'SCONJ', 'VERB']

```
S -> CLAUSE SCONJ NP CLAUSE
CLAUSE -> ADP NP | ADV VERB SCONJ VERB
NP -> NOUN ADJ
NP -> NOUN PUNCT | NOUN PUNCT NP | NOUN 
```

## Oración 5 

Texto: Lo peor de Carlos Montero, de largo.

Tokens: ['lo', 'peor', 'de', 'carlos', 'montero', ',', 'de', 'largo', '.']
POS: ['PRON', 'ADJ', 'ADP', 'PROPN', 'PROPN', 'PUNCT', 'ADP', 'NOUN', 'PUNCT']

```
S -> NP PP PUNCT PP PUNCT
NP -> PRON ADJ
PP -> ADP NPP | ADP NOUN 
NPP -> PROPN PROPN
PUNCT -> COMMA
```
