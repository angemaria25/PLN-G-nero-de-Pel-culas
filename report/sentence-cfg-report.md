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

## Oración 6 (NEW)

Texto: Aitana, maja, ¿Qué haces metida aquí?
POS: ['PROPN', 'PUNCT', 'NOUN', 'PUNCT', 'PUNCT', 'DET', 'VERB', 'ADJ', 'ADV', 'PUNCT']

```
S -> NP PUNCT NP PUNCT Q
Q -> PUNCT NP VP PUNCT
NP -> PROPN | NOUN | DET
VP -> VERB ADJ ADV
```

## Oración 7

Texto: Pues las tres caras de siempre, ninguna de las cuales sabe vocalizar, y luego las cuotas que tocan y para casa.
POS: ['SCONJ', 'DET', 'NUM', 'NOUN', 'ADP', 'ADV', 'PUNCT', 'PRON', 'ADP', 'DET', 'PRON', 'VERB', 'VERB', 'PUNCT', 'CCONJ', 'ADV', 'DET', 'NOUN', 'PRON', 'VERB', 'CCONJ', 'ADP', 'NOUN', 'PUNCT']

```
S -> CLAUSE PUNCT CLAUSE PUNCT CLAUSE PUNCT
CLAUSE -> CCONJ ADV NP | NP VP | SCONJ NP
NP -> PRON ADP NP | DET NOUN PRON VP | DET NUM NOUN ADP ADV | DET PRON
VP -> VERB VERB | VERB CCONJ ADP NOUN
```

## Oración 8

Texto: Los diálogos son penosos, los personajes son puras caricaturas, las tramas se ven venir de lejos y los actores...
POS: ['DET', 'NOUN', 'AUX', 'ADJ', 'PUNCT', 'DET', 'NOUN', 'AUX', 'NOUN', 'ADJ', 'PUNCT', 'DET', 'NOUN', 'PRON', 'VERB', 'VERB', 'ADP', 'ADV', 'CCONJ', 'DET', 'NOUN', 'PUNCT']

```
S -> CLAUSE PUNCT CLAUSE PUNCT CLAUSE CCONJ NP PUNCT
CLAUSE -> NP VP
NP -> DET NOUN
NP -> NOUN ADJ
VP -> AUX ADJ
VP -> AUX NP
VP -> PRON VERB VERB PP
PP -> ADP ADV
```

## Oración 9

Texto: Esa también es una serie ligera que no viene a salvar el mundo, pero es que no hay ápice posible de similitud.
POS: ['PRON', 'ADV', 'AUX', 'DET', 'NOUN', 'ADJ', 'PRON', 'ADV', 'VERB', 'ADP', 'VERB', 'DET', 'NOUN', 'PUNCT', 'CCONJ', 'AUX', 'SCONJ', 'ADV', 'AUX', 'NOUN', 'ADJ', 'ADP', 'NOUN', 'PUNCT']

```
S -> CLAUSE PUNCT CLAUSE
CLAUSE -> NP VP
NP -> PRON
VP -> ADV AUX NP
NP -> DET NOUN ADJ CLAUSE
CLAUSE -> PRON VP
VP -> ADV VERB ADP VERB NP
NP -> DET NOUN
CLAUSE -> CCONJ CLAUSE
CLAUSE -> AUX SCONJ CLAUSE
CLAUSE -> ADV AUX NP
NP -> NOUN ADJ PP
PP -> ADP NOUN
```

## Oración 10

Texto: En ningún sentido.
POS: ['ADP', 'DET', 'NOUN', 'PUNCT']

```
S -> PP PUNCT
PP -> ADP NP
NP -> DET NOUN
```

## Oración 11

Texto: Aquí no hay nada cuidado.
POS: ['ADV', 'ADV', 'AUX', 'PRON', 'ADJ', 'PUNCT']

```
S -> ADV CLAUSE PUNCT
CLAUSE -> ADV VP
VP -> AUX PRON ADJ
```

## Oración 12

Texto: Me he sentido insultado.
POS: ['PRON', 'AUX', 'VERB', 'ADJ', 'PUNCT']

```
S -> CLAUSE PUNCT
CLAUSE -> PRON VP
VP -> AUX VERB ADJ
```

## Oración 13

Texto: Tonto de baba.
POS: ['PROPN', 'ADP', 'VERB', 'PUNCT']

```
S -> NP PUNCT
NP -> ADJ PP
PP -> ADP NOUN
```

## Oración 14

Texto: La serie es un drama médico que intenta copiar los estilemas yankies adaptándolos al modo español.
POS: ['DET', 'NOUN', 'AUX', 'DET', 'NOUN', 'ADJ', 'PRON', 'VERB', 'VERB', 'DET', 'NOUN', 'ADJ', 'ADJ', 'ADP', 'NOUN', 'ADJ', 'PUNCT']

```
S -> CLAUSE PUNCT
CLAUSE -> NP VP
NP -> DET NOUN
VP -> AUX NP
NP -> DET NOUN ADJ CLAUSE
CLAUSE -> PRON VP
VP -> VERB VERB NP ADJ PP
NP -> DET NOUN ADJ
PP -> ADP NOUN ADJ
```

## Oración 15

Texto: La historia de base transcurre en un hospital valenciano representado de manera inverosímil pues el ambiente de hospital representado en la serie dista mucho de la realidad hospitalaria tanto valenciana como española.
POS: ['DET', 'NOUN', 'ADP', 'NOUN', 'VERB', 'ADP', 'DET', 'NOUN', 'ADJ', 'ADJ', 'ADP', 'NOUN', 'PROPN', 'SCONJ', 'DET', 'NOUN', 'ADP', 'NOUN', 'ADJ', 'ADP', 'DET', 'NOUN', 'ADJ', 'ADV', 'ADP', 'DET', 'NOUN', 'ADJ', 'ADV', 'ADJ', 'SCONJ', 'ADJ', 'PUNCT']

```
S -> CLAUSE SCONJ CLAUSE PUNCT
CLAUSE -> NP VP PP
NP -> DET NOUN PP
PP -> ADP NOUN
VP -> VERB
PP -> ADP NP
NP -> DET NOUN ADJ ADJ PP
PP -> ADP NOUN PROPN
CLAUSE -> NP ADJ PP ADJ ADV PP PP
NP -> DET NOUN PP
PP -> ADP NOUN
PP -> ADP DET NOUN
PP -> ADP NP
NP -> DET NOUN ADJ
PP -> ADV ADJ SCONJ ADJ
```

## Oración 16

Texto: El guión entremezcla dramas médicos mal plateados, con dramas cotidianos pueriles y riículos.
POS: ['DET', 'PROPN', 'VERB', 'NOUN', 'ADJ', 'ADV', 'NOUN', 'PUNCT', 'ADP', 'NOUN', 'ADJ', 'ADJ', 'CCONJ', 'VERB', 'PUNCT']

```
S -> CLAUSE PUNCT PP CCONJ VERB PUNCT
CLAUSE -> NP VP
NP -> DET PROPN
VP -> VERB NP
NP -> NOUN ADJ ADV NOUN
PP -> ADP NOUN ADJ ADJ
```

## Oración 17

Texto: Los diálogos dan pena, los personajes son de estereotipo.
POS: ['DET', 'NOUN', 'VERB', 'NOUN', 'PUNCT', 'DET', 'NOUN', 'AUX', 'ADP', 'NOUN', 'PUNCT']

```
S -> CLAUSE PUNCT CLAUSE PUNCT
CLAUSE -> NP VP
NP -> DET NOUN
VP -> VERB NOUN
CLAUSE -> NP VP
NP -> DET NOUN
VP -> AUX PP
PP -> ADP NOUN
```

## Oración 18

Texto: Típica serie de Netflix distribuidora que suele llenar su grilla con este tipo de bazofias.
POS: ['ADJ', 'NOUN', 'ADP', 'PROPN', 'ADJ', 'PRON', 'VERB', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'ADP', 'NOUN', 'PUNCT']

```
S -> NP CLAUSE PUNCT
NP -> ADJ NOUN PP ADJ
PP -> ADP PROPN
CLAUSE -> PRON VP
VP -> VERB VERB NP PP
NP -> DET NOUN
PP -> ADP NP
NP -> DET NOUN ADP NOUN
```

## Oración 20

Texto: Una vez más una producción española me saca de su visionado y me obliga a la crítica negativa.
POS: ['DET', 'NOUN', 'ADV', 'DET', 'NOUN', 'ADJ', 'PRON', 'VERB', 'ADP', 'DET', 'NOUN', 'CCONJ', 'PRON', 'VERB', 'ADP', 'DET', 'NOUN', 'ADJ', 'PUNCT']

```
S -> NP NP VP PUNCT
NP -> NP ADV | NP ADJ
NP -> DET NOUN
VP -> VP CCONJ VP
VP -> PRON VERB PP
PP -> ADP DET NOUN
VP -> PRON VERB PP
PP -> ADP DET NOUN ADJ
```

## Oración 21

Texto: Respira no da opción y resulta ofensiva como tantas otras que consiguen producirse y estrenarse en plataformas y canales de televisión.
POS: ['PROPN', 'ADV', 'VERB', 'NOUN', 'CCONJ', 'VERB', 'NOUN', 'SCONJ', 'DET', 'PRON', 'PRON', 'VERB', 'VERB', 'CCONJ', 'VERB', 'ADP', 'NOUN', 'CCONJ', 'NOUN', 'ADP', 'NOUN', 'PUNCT']

```

```

## Oración 22

Texto: Voy a ir dándome de baja de alguna plataforma porque no merece la pena.
POS: ['AUX', 'ADP', 'VERB', 'VERB', 'ADP', 'NOUN', 'ADP', 'DET', 'NOUN', 'SCONJ', 'ADV', 'VERB', 'DET', 'NOUN', 'PUNCT']

```

```

## Oración 23

Texto: Está serie da vergüenza ajena.
POS: ['AUX', 'NOUN', 'VERB', 'NOUN', 'ADJ', 'PUNCT']

```

```

## Oración 24

Texto: Una serie donde al parecer las únicas personas que trabajan en el hospital son los médicos, ni rastro de enfermeras, TCAE, celadores, personal de limpieza...
POS: ['DET', 'NOUN', 'PRON', 'ADP', 'VERB', 'DET', 'ADJ', 'NOUN', 'PRON', 'VERB', 'ADP', 'DET', 'NOUN', 'AUX', 'DET', 'NOUN', 'PUNCT', 'CCONJ', 'NOUN', 'ADP', 'NOUN', 'PUNCT', 'NOUN', 'PUNCT', 'NOUN', 'PUNCT', 'NOUN', 'ADP', 'NOUN', 'PUNCT']

```

```

## Oración 25

Texto: Por favor, si quieren hacer una serie sobre un hospital que se informen un poquito más sobre el funcionamiento de el.
POS: ['ADP', 'NOUN', 'PUNCT', 'SCONJ', 'VERB', 'VERB', 'DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'PRON', 'PRON', 'VERB', 'DET', 'ADJ', 'ADV', 'ADP', 'DET', 'NOUN', 'ADP', 'DET', 'PUNCT']

```

```

## Oración 26

Texto: Escenas ridículas con diálogos sin sentido.
POS: ['NOUN', 'ADJ', 'ADP', 'NOUN', 'ADP', 'NOUN', 'PUNCT']

```

```

## Oración 27

Texto: Bueno, y lo más gracioso es que siempre están liados todos con todos.
POS: ['INTJ', 'PUNCT', 'CCONJ', 'PRON', 'ADV', 'ADJ', 'AUX', 'SCONJ', 'ADV', 'AUX', 'ADJ', 'PRON', 'ADP', 'PRON', 'PUNCT']

```

```

## Oración 28

Texto: Vamos que eso es una discoteca más que un hospital.
POS: ['VERB', 'SCONJ', 'PRON', 'AUX', 'DET', 'NOUN', 'ADV', 'SCONJ', 'DET', 'NOUN', 'PUNCT']

```

```

## Oración 29

Texto: Vamos, si no quieres perder tu tiempo no veas esta serie sin sentido
POS: ['AUX', 'PUNCT', 'SCONJ', 'ADV', 'VERB', 'VERB', 'DET', 'NOUN', 'ADV', 'VERB', 'DET', 'NOUN', 'ADP', 'NOUN']

```

```
