# Variável de sistema _PAGETOTAL

Contém o número total de páginas em um relatório.

Você pode usar _PAGETOTAL para configurar numeração "Página X de Y" em relatórios. _PAGETOTAL é suportado nas versões de desenvolvimento e de tempo de execução do Visual FoxPro e em todas as operações de relatório, incluindo REPORT FORM...TO FILE...ASCII e com argumentos opcionais como RANGE.

```foxpro
_PAGETOTAL [ = nValue ]
```

#### Parâmetros
 **nValue**
Especifica um número positivo representando o número total de páginas em um relatório.

# Observações

Você pode definir _PAGETOTAL a qualquer momento. O Visual FoxPro avalia e atualiza _PAGETOTAL somente quando uma operação de relatório como REPORT FORM ocorre. No início da operação de relatório, o Visual FoxPro inicializa _PAGETOTAL com o valor 0, independentemente de _PAGETOTAL ser usado no relatório.

Se você incluir _PAGETOTAL em qualquer lugar em um relatório do Visual FoxPro, o Visual FoxPro realiza duas passagens pelo relatório. A primeira passagem não é visível nem impressa e calcula a variável _PAGETOTAL. Durante a primeira passagem, _PAGETOTAL é definido com o valor -1.

Por motivos de desempenho, você pode suprimir um relatório de duas passagens não chamando _PAGETOTAL em uma visualização de impressão usando uma expressão como a seguinte:

```foxpro
TRANS(_PAGENO) + IIF(SYS(2040)="1", "", " OF " + TRANS(_PAGETOTAL))
```

Se você não incluir uma referência a _PAGETOTAL no relatório, o Visual FoxPro define o valor de _PAGETOTAL como o número total de páginas no final da impressão e realiza apenas uma passagem pelo relatório.

Você pode forçar uma segunda passagem pelo relatório usando uma expressão como a seguinte:

```foxpro
IIF( _PAGETOTAL = 0, "","" )
```

Iniciar outra passagem permite operações adicionais usando variáveis de relatório, como reportar % do número total de páginas.

> **Dica:** Para que uma segunda passagem ocorra, em versões anteriores do Visual FoxPro, você precisava de uma referência a _PAGETOTAL no layout do relatório. No Visual FoxPro 9.0, você também pode usar uma referência ReportListener no comando REPORT FORM. Definindo a propriedade TwoPassProcess do ReportListener como .T . antes de uma execução de relatório, você pode forçar o relatório a realizar duas passagens, mesmo se não usou _PAGETOTAL em nenhuma expressão no relatório. Para mais informações, consulte a propriedade TwoPassProcess .

O valor de _PAGETOTAL deve ser igual ao valor de _PAGENO no final da impressão de um relatório, independentemente de o relatório incluir _PAGETOTAL.

# Exemplo

O exemplo a seguir ilustra como incluir numeração "Página X de Y" em seu relatório usando a variável de sistema _PAGETOTAL e adicionando a seguinte expressão na caixa de texto do relatório:

```foxpro
"Page " + TRANS(_PAGENO) + " of " + TRANS( _PAGETOTAL)
```
