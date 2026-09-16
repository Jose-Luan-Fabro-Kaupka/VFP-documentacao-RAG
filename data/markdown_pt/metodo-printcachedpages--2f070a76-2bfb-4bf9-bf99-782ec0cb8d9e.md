# Método PrintCachedPages

Permite que um usuário imprima páginas em cache em uma execução de relatório com ListenerType 1 ou 3 sem fechar a janela de visualização.

```foxpro
Object.PrintCachedPages()
```

# Observações

Object pode ser qualquer objeto derivado da classe base _ReportListener ou suas subclasses.

O uso mais comum de PrintCachedPages é enviar saída para a impressora quando um usuário ainda tem uma janela Print Preview aberta.

# Exemplo

O exemplo de código a seguir vem do método ActionPrint da classe frxpreviewform no projeto ReportPreview. Este projeto contém o código-fonte do aplicativo _REPORTPREVIEW padrão, ReportPreview.app. Você pode encontrar e modificar o código-fonte na subpasta Tools\xsource da pasta de instalação do Visual FoxPro 9.0.

```foxpro
if THIS.oReport.commandClauses.NOWAIT
THIS.oReport.PrintCachedPages()
else
* Terminate:
THIS.suppressRendering = .T.
THIS.printOnExit       = .T.
THIS.Release()
endif
```

Como o aplicativo ReportPreview incluído com o Visual FoxPro usa PrintCachedPages( ), você pode controlar o comportamento do botão Print na barra de ferramentas Print Preview. Se você quiser que a janela Print Preview permaneça aberta depois que um usuário clicar em Print, inclua a cláusula NOWAIT no seu comando REPORT FORM, por exemplo:

```foxpro
REPORT FORM (filename) OBJECT oReportListener PREVIEW NOWAIT
```

Se você quiser que a janela Print Preview feche quando um usuário clicar em Print, não inclua a cláusula NOWAIT no seu comando REPORT FORM. Por exemplo:

```foxpro
REPORT FORM (filename) OBJECT oReportListener PREVIEW
```
