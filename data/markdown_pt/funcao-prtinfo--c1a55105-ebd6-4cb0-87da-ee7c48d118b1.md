# Função PRTINFO( )

Retorna a configuração de impressora especificada atual.

```foxpro
PRTINFO(nPrinterSetting [, cPrinterName])
```

#### Parâmetros
 **nPrinterSetting**
Especifica qual configuração de impressora do Visual FoxPro retornar. A tabela a seguir lista descrições do tipo de configurações de impressora retornadas. nPrinterSetting FOXPRO.H Configuração retornada 1 PRT_ORIENTATION Orientação do papel 2 PRT_PAPERSIZE Tamanho do papel 3 PRT_PAPERLENGTH Comprimento do papel em incrementos de 0,1 milímetro 4 PRT_PAPERWIDTH Largura do papel em incrementos de 0,1 milímetro 5 PRT_SCALE Fator pelo qual a saída da impressora é dimensionada 6 PRT_COPIES Número de cópias a imprimir 7 PRT_DEFASOURCE Origem de papel padrão 8 PRT_PRINTQUAL Um valor positivo que indica a resolução horizontal em pontos por polegada (DPI) ou um valor negativo que indica a qualidade de impressão. 9 PRT_COLOR Um valor que indica se uma impressora colorida produz saída colorida ou monocromática 10 PRT_DUPLEX Modo duplex 11 PRT_YRESOLUTION A resolução vertical em pontos por polegada (DPI). Se não estiver disponível, um valor de -1 é retornado. 12 PRT_TTOPTION Um valor que indica como as fontes TrueType® são impressas 13 PRT_COLLATE Um valor que indica se a saída é agrupada
**cPrinterName**
Especifica o nome da impressora para a qual as informações são retornadas. Se cPrinterName for omitido, as informações são retornadas para a impressora padrão.

# Valor de retorno

Tipo de dados Numeric. As tabelas a seguir listam os valores retornados ao especificar valores particulares para nPrinterSetting.

Se nPrinterSetting for 1, PRTINFO( ) retorna a orientação do papel da seguinte forma:

| Valores de retorno | Orientação do papel |
| --- | --- |
| –1 | Informação não disponível |
| 0 | Portrait |
| 1 | Landscape |

Se nPrinterSetting for 2, PRTINFO( ) retorna o tamanho do papel da seguinte forma:

| Valores de retorno | Tamanho do papel |
| --- | --- |
| –1 ou valor diferente dos listados | Informação não disponível. Use nPrinterSetting = 3 e nPrinterSetting = 4 para retornar o tamanho do papel. |
| 1 | Letter, 8 1/2 x 11 in |
| 2 | Letter Small, 8 1/2 x 11 in |
| 3 | Tabloid, 11 x 17 in |
| 4 | Ledger, 17 x 11 in |
| 5 | Legal, 8 1/2 x 14 in |
| 6 | Statement, 5 1/2 x 8 1/2 in |
| 7 | Executive, 7 1/4 x 10 1/2 in |
| 8 | A3, 297 x 420 mm |
| 9 | A4, 210 x 297 mm |
| 10 | A4, Small 210 x 297 mm |
| 11 | A5, 148 x 210 mm |
| 12 | B4, 250 x 354 mm |
| 13 | B5, 182 x 257 mm |
| 14 | Folio, 8 1/2 x 13 in |
| 15 | Quarto, 215 x 275 mm |
| 16 | 10 x 14 in |
| 17 | 11 x 17 in |
| 18 | Note, 8 1/2 x 11 in |
| 19 | Envelope #9, 3 7/8 x 8 7/8 in |
| 20 | Envelope #10, 4 1/8 x 9 1/2 in |
| 21 | Envelope #11, 4 1/2 x 10 3/8 in |
| 22 | Envelope #12, 4 1/2 x 11 in |
| 23 | Envelope #14, 5 x 11 1/2 in |
| 24 | C size sheet |
| 25 | D size sheet |
| 26 | E size sheet |
| 27 | Envelope DL, 110 x 220 mm |
| 28 | Envelope C5, 162 x 229 mm |
| 29 | Envelope C3, 324 x 458 mm |
| 30 | Envelope C4, 229 x 324 mm |
| 31 | Envelope C6, 114 x 162 mm |
| 32 | Envelope C65, 114 x 229 mm |
| 33 | Envelope B4, 250 x 353 mm |
| 34 | Envelope B5, 176 x 250 mm |
| 35 | Envelope B6, 176 x 125 mm |
| 36 | Envelope, 110 x 230 mm |
| 37 | Envelope Monarch, 3 7/8 x 7.5 in |
| 38 | 6 3/4 Envelope, 3 5/8 x 6 1/2 in |
| 39 | US Std Fanfold, 14 7/8 x 11 in |
| 40 | German Std Fanfold, 8 1/2 x 12 in |
| 41 | German Legal Fanfold, 8 1/2 x 13 in |

Se nPrinterSetting for 7, PRTINFO( ) retorna a origem de papel padrão da seguinte forma:

| Valores de retorno | Origem de papel padrão |
| --- | --- |
| 1 | Upper bin |
| 2 | Lower bin |
| 3 | Middle bin |
| 4 | Manual feed |
| 5 | Envelope bin |
| 6 | Manual feed envelope |
| 7 | Automatic feed |
| 8 | Tractor feed |
| 9 | Small format |
| 10 | Large format |
| 11 | Large capacity |
| 14 | Cassette |
| 15 | Default input bin (automatically select) |

Se nPrinterSetting for 8 e PRTINFO( ) retornar um valor negativo, o valor de retorno indica a qualidade de impressão da seguinte forma:

| Valores de retorno | Qualidade de impressão |
| --- | --- |
| –1 | Draft |
| –2 | Low |
| –3 | Medium |
| –4 | High |

Se nPrinterSetting for 9, PRTINFO( ) retorna um valor indicando se uma impressora colorida produz saída colorida ou monocromática da seguinte forma:

| Valores de retorno | Cor da saída |
| --- | --- |
| 1 | Monochrome |
| 2 | Color |

Se nPrinterSetting for 10, PRTINFO( ) retorna o modo duplex da seguinte forma:

| Valores de retorno | Modo duplex |
| --- | --- |
| 1 | Simplex printing |
| 2 | Vertical duplex |
| 3 | Horizontal duplex |

Se nPrinterSetting for 12, PRTINFO( ) retorna um valor que indica como as fontes TrueType® são impressas da seguinte forma:

| Valores de retorno | Impressão de fontes TrueType® |
| --- | --- |
| 1 | Print as bitmapped graphics |
| 2 | Download as soft fonts |
| 3 | Substitute device fonts |

Se nPrinterSetting for 13, PRTINFO( ) retorna um valor que indica se a saída é agrupada da seguinte forma:

| Valores de retorno | Agrupamento |
| --- | --- |
| 0 | No collation |
| 1 | Collated |

# Observações

Você pode definir configurações de impressora do Visual FoxPro na caixa de diálogo Page Setup da impressora. Para obter mais informações, consulte Page Setup Dialog Box (Visual FoxPro).
