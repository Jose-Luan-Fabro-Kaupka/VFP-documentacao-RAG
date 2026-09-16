# SYS(2040) - Detectar status do relatório

Detecta se um relatório está sendo impresso ou está em modo de visualização.

```foxpro
SYS(2040)
```

# Valor de retorno

Tipo de dados Character. Retorna o status atual do relatório da seguinte forma.

| Value | Description |
| --- | --- |
| 0 | There is no active report. |
| 1 | Report is in Preview Mode |
| 2 | Report is being sent as output (such as a printer or file). |

# Observações

A função SYS(2040) é útil quando você deseja controlar o conteúdo em um relatório dependendo de como ele está sendo visualizado. Por exemplo, você pode imprimir uma mensagem como Confidential ou Classified, mas não exibi-la quando o relatório estiver em Preview Mode.

> **Observação:** O valor retornado por SYS(2040) não fornece informações sobre se há uma janela de visualização ativa exibida. Ele fornece informações sobre se o Sistema de Relatórios Visual FoxPro está em processo de geração de saída apenas, não sobre o que acontece com esses resultados depois que foram gerados. Por exemplo, SYS(2040) retorna "0" depois que você usa o comando REPORT FORM OBJECT TYPE 1 (invocando uma visualização de relatório assistida por objeto), mesmo que a janela de visualização ainda esteja na tela, e retorna "0" depois de enviar saída para uma impressora e fechar a fila de impressão, mesmo que parte dessa saída ainda não tenha sido completamente impressa. Por outro lado, se seu manipulador de erros for acionado, você pode usar SYS(2040) para determinar se o erro foi acionado por código ocorrendo durante a execução de um relatório. Seu manipulador de erros pode usar o valor para determinar se deve fazer alguma limpeza específica de relatório antes de sair do aplicativo.

# Exemplo

O exemplo a seguir exibe como SYS(2040) pode ser usado para suprimir a variável de sistema _PAGETOTAL quando o relatório está em Preview Mode.

```foxpro
"Page: " + TRANS(_PAGENO) + ;
IIF( SYS(2040) = "1", "", " of " + TRANS(_PAGETOTAL))
```
