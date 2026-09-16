# Variável de sistema _PEJECT

Incluída para compatibilidade com versões anteriores. Use o Report Designer.

Define a ocorrência de ejeção de página.

```foxpro
_PEJECT = expC
```

#### Parâmetros
 expC deve ser avaliado como um dos seguintes:

BEFORE Envia uma ejeção de página antes de iniciar a saída. BEFORE é o valor padrão no FoxPro para MS-DOS.

AFTER Envia uma ejeção de página após a conclusão da saída.

BOTH Envia uma ejeção de página antes e depois da saída de impressão.

NONE Não envia ejeção de página antes ou depois da saída de impressão. NONE é o valor padrão no FoxPro para Windows.

Se expC for uma cadeia de caracteres literal, ela deve estar entre aspas.

Você pode definir _PEJECT na janela Command ou durante a execução do programa, mas ela só tem efeito dentro da estrutura de comando PRINTJOB ... ENDPRINTJOB.

# Observações

Incluída para compatibilidade com versões anteriores — use o Report Writer.

_PEJECT contém um valor de caractere que determina quando o FoxPro envia uma ejeção de página durante a saída.
