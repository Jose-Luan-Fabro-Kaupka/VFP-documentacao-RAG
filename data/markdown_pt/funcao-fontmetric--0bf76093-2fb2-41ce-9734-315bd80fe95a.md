# Função FONTMETRIC( )

Retorna atributos de fonte para as fontes atualmente instaladas no sistema operacional.

```foxpro
FONTMETRIC(nAttribute [, cFontName, nFontSize [, cFontStyle]])
```

#### Parâmetros
**nAttribute**
Determina o atributo de fonte retornado por FONTMETRIC( ). Se você omitir cFontName, nFontSize e cFontStyle, FONTMETRIC( ) retornará o atributo da fonte atual na janela de saída ativa. A tabela a seguir lista os valores de nAttribute e os atributos de fonte correspondentes. nAttribute Atributo 1 Altura do caractere em pixels 2 Ascendente do caractere (unidades acima da linha de base) em pixels 3 Descendente do caractere (unidades abaixo da linha de base) em pixels 4 Entrelinha (espaço entre linhas) em pixels 5 Entrelinha adicional em pixels 6 Largura média do caractere em pixels 7 Largura máxima do caractere em pixels 8 Peso da fonte. 9 Itálico (0 = não, diferente de zero = sim) 10 Sublinhado (0 = não, diferente de zero = sim) 11 Tachado (0 = não, diferente de zero = sim) 12 Primeiro caractere definido na fonte 13 Último caractere definido na fonte 14 Caractere padrão (substitui caracteres ausentes na fonte) 15 Caractere de quebra de palavra 16 Espaçamento e família 17 Conjunto de caracteres 18 Saliência (largura adicional) 19 Proporção horizontal do dispositivo de fonte 20 Proporção vertical do dispositivo de fonte Para obter mais informações sobre os valores numéricos retornados por FONTMETRIC( ), consulte a função TEXTMETRIC na Referência do programador do Microsoft Windows.
**cFontName**
Especifica o nome de uma fonte instalada.
**nFontSize**
Especifica o tamanho, em pontos, da fonte indicada por cFontName.
**cFontStyle**
Especifica um código de estilo para a fonte indicada por cFontName. Se cFontStyle for omitido, FONTMETRIC( ) retornará o atributo do estilo Normal. cFontStyle pode ser um caractere ou uma combinação dos caracteres listados na tabela de estilos a seguir. Por exemplo, a combinação BI especifica o estilo Bold Italic. Caractere Estilo de fonte B Negrito I Itálico N Normal O Contorno Q Opaco S Sombra – Tachado T Transparente U Sublinhado

# Valor de retorno

Numérico

# Observações

FONTMETRIC( ) retorna os atributos da fonte atual da janela de saída ativa. A função WFONT( ) pode ser usada para determinar a fonte atual da janela.
