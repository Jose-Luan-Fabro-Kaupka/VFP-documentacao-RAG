# SYS(3052) — Substituir bloqueio de SET REPROCESS

Especifica se o Visual FoxPro usa a configuração SET REPROCESS ao tentar bloquear um arquivo de índice ou memo.

```foxpro
SYS(3052, nFileType, [lHonorReprocess])
```

#### Parâmetros
 **nFileType**
Especifica o tipo de arquivo. A tabela a seguir lista os valores de nType e o tipo de arquivo correspondente: nFileType Tipo de arquivo 1 Índice 2 Memo.
**lHonorReprocess**
Especifica se o Visual FoxPro usa a configuração SET REPROCESS para tentativas malsucedidas de bloqueio de arquivos de índice e memo. Especifique verdadeiro (.T.) para usar SET REPROCESS quando o Visual FoxPro tentar bloquear os arquivos especificados com nFileType. Especifique falso (.F.), o padrão, para substituir SET REPROCESS quando o Visual FoxPro tentar bloquear os arquivos especificados com nFileType. Quando definido como falso, o Visual FoxPro espera indefinidamente pelos bloqueios nos arquivos especificados; essa opção equivale ao comportamento de bloqueio das versões anteriores do FoxPro. Se lHonorReprocess for omitido, SYS(3052) retornará a configuração atual do tipo de arquivo especificado com nFileType.

# Valor de retorno

Character

# Observações

SYS(3052) fornece controle adicional sobre o bloqueio de arquivos no Visual FoxPro. É recomendável definir lHonorReprocess como verdadeiro (.T.) para reduzir o risco de contenção de bloqueio de arquivos caso o aplicativo use processamento de transações.

SYS(3052) retorna, como uma cadeia de caracteres, o valor numérico 0 (correspondente a falso (.F.)) ou 1 (correspondente a verdadeiro (.T.)). Se lHonorReprocess for incluído em SYS(3052), o valor retornado será idêntico ao valor lógico especificado para lHonorReprocess. Se lHonorReprocess for omitido, o valor retornado será a configuração atual do tipo de arquivo especificado com nFileType.
