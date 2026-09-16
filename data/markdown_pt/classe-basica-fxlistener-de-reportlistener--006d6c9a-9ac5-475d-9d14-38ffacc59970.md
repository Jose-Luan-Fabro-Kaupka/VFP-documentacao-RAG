# Classe básica FXListener de ReportListener

FXListener permite alterar as características de exibição dos controles de relatório durante a execução de um relatório. Você pode usar duas coleções de membros: FXs (ajusta instruções de conteúdo e formatação) e GFXs (ajusta ou substitui a renderização gráfica GDIPlus) para afetar a renderização do relatório.

| Categoria | Relatórios |
| --- | --- |
| Catálogo padrão | Visual FoxPro Catalog\Foundation Classes\Output\Report Listeners |
| Classe | FXListener |
| Classe base | ReportListener |
| Biblioteca de classes | _REPORTLISTENER.vcx |
| Classe pai | _ReportListener (Classe básica de fundação ReportListener) |

# Observações

Provavelmente você não instanciará esta classe diretamente. Em vez disso, instanciará uma das classes derivadas dela, como HtmlListener.

Para aproveitar a capacidade de FXListener de afetar a saída do relatório, é necessário criar objetos FX ou GFX.

> **Observação:** A classe fxAbstract da biblioteca de classes _REPORTLISTENER.vcx fornece uma instância abstrata da interface exigida para um objeto FX ou GFX.

Cada objeto FX ou GFX deve fornecer a seguinte interface:

```foxpro
PROCEDURE ApplyFX(toListener, tcMethodToken,tP1, tP2, tP3, tP4, tP5, tP6, tP7, tP8, tP9, tP10, tP11, tP12).
```

 **toListener**
Uma referência ao objeto listener.
**tcMethodToken**
O evento do report listener em execução no momento: AdjustObjectSize, AfterBand, AfterReport, BeforeBand, BeforeReport, Destroy, Error, EvaluateContents, Init, LoadReport ou UnloadReport.
**tP1 até tP12**
Os parâmetros do evento do report listener em execução. Por exemplo, o evento BeforeBand tem dois parâmetros, nBandObjCode e nFRXRecNo. Quando tcMethodToken é "BeforeBand", tP1 é nBandObjCode e tP2 é nFRXRecNo.

Você pode usar o método AddCollectionMember de FXListener para adicionar objetos FX ou GFX ao report listener. Por exemplo, o código a seguir no evento Init de um htmllistener adiciona um objeto FX à coleção.

```foxpro
THIS.AddCollectionMember("myFX", "myClassLibrary.vcx")
DODEFAULT()
```

Para cada evento do report listener, FXListener invoca seu método sendFX( ) para chamar o método ApplyFX( ) de cada objeto FX ou GFX das coleções. Você pode usar blocos IF...ENDIF ou instruções CASE para verificar o evento e tomar a ação apropriada. Por exemplo, o trecho a seguir no método ApplyFX de um objeto FX converte em maiúsculas o texto de um controle no relatório.

```foxpro
LPARAMETERS toListener, tcMethodToken,tP1, tP2, tP3, tP4, tP5, tP6, tP7, tP8, tP9, tP10, tP11, tP12
IF tcMethodToken == "RENDER"
  IF tP1 == 11
  * nFRXRecno is Render's 1st param (tP1) and 11 refers to
  * the record in the FRX of a particular control on the report
  tP7 = UPPER(tP7)
  * cContentsToBeRendered is Render's 7th param
  ENDIF
ENDIF
```

> **Observação:** As subclasses de fxAbstract (fxmemberdatascript, fxresetpagetotal, gfxexample, gfxnorender e gfxrotate) fornecem exemplos de classes FX e GFX que podem ser usadas com FXListener.

A tabela a seguir lista propriedades e métodos públicos adicionados por esta classe à classe pai, _ReportListener.

| Propriedades e métodos | Descrição |
| --- | --- |
| AddCollectionMember Method | Adiciona uma instância de uma classe especificada em uma biblioteca de classes especificada à coleção FX ou GFX. Espera os parâmetros: tcClass, tcClassLib, tcModule, tlSingleton, tlInGFX, tlRequired. |
| CancelRequested Property | Sinalizador de notificação para objetos FX usado para solicitar o cancelamento de um relatório. |
| CheckCollectionForSpecifiedMember Method | Verifica se há uma instância de uma classe na coleção FX ou GFX pelo nome da classe e, se especificado, pelo nome da biblioteca de classes. Retorna o valor lógico (.F. se não encontrada) ou uma referência de objeto. |
| ClassPath Property | Local opcional que especifica o caminho para carregar objetos de bibliotecas externas. |
| FFCGraphics Property | Referência a um objeto FFCGraphic criado durante a execução. É fornecida aos membros da coleção GFXs e validada como instância de GpGraphics da classe de fundação FoxPro (FFC) _GDIPLUS.VCX ou de uma classe derivada de GpGraphics. |
| FRXCursor Property | Contém uma referência a um objeto auxiliar FRXCursor, usado para facilitar cálculos em tempo de execução relacionados a metadados, estrutura e memberdata de FRX. |
| FXFeedBackClass Property | Classe a instanciar na coleção FX para retorno ao usuário (o padrão é fxTherm). |
| FXFeedbackClassLib Property | Biblioteca de classes usada para instanciar o objeto da coleção FX que fornece retorno ao usuário. |
| FXFeedbackModule Property | Módulo de aplicativo (APP ou EXE) usado para instanciar o objeto da coleção FX que fornece retorno ao usuário. |
| FXMemberDataScriptClass Property | Classe a instanciar na coleção FX para tratamento de scripts baseado em memberdata (o padrão é fxMemberDataScript). |
| FXMemberDataScriptClassLib Property | Biblioteca de classes usada para instanciar o objeto da coleção FX que trata scripts baseados em memberdata. |
| FXMemberDataScriptModule Property | Módulo de aplicativo (APP ou EXE) usado para instanciar o objeto da coleção FX que trata scripts baseados em memberdata. |
| FXs Property | Coleção de objetos FX. Cada objeto deve ter a interface indicada acima. O valor retornado por esse procedimento é ignorado. |
| getFRXRecno Method | Determina o número da linha atual do cursor FRX a partir dos parâmetros passados a um evento ReportListener. |
| getPathForExternals Method | Determina o local esperado da tabela de configuração atual e de outros arquivos externos necessários. |
| GFXNoRenderClass Property | Classe a instanciar na coleção GFX para eliminar condicionalmente a renderização da classe base dos vários controles de layout. O padrão é gfxNoRender quando a renderização condicional vazia está desativada. |
| GFXNoRenderClassLib Property | Biblioteca de classes usada para instanciar o objeto da coleção GFX que fornece renderização condicional da classe base. |
| GFXNoRenderModule Property | Módulo de aplicativo (APP ou EXE) usado para instanciar o objeto da coleção GFX que fornece renderização condicional da classe base. |
| GFXRotateClass Property | Classe a instanciar na coleção GFX para girar controles de layout. O padrão é gfxRotate. |
| GFXRotateClassLib Property | Biblioteca de classes usada para instanciar o objeto da coleção GFX que fornece rotação. |
| GFXRotateModule Property | Módulo de aplicativo (APP ou EXE) usado para instanciar o objeto da coleção GFX que fornece rotação. |
| GFXs Property | Coleção de objetos GFX. Cada objeto deve ter a interface indicada. O método Render usa o valor retornado pelo procedimento. |
| loadFrxCursor Property | Determina se esta classe deve carregar dinamicamente uma instância da classe auxiliar FRXCursor quando uma referência a ela for acessada. |
| MemberDataAlias Property | Alias do cursor que contém memberdata em FRXDataSession. É lido do campo Style da tabela FRX para facilitar o acesso por outros objetos. |
| removeCollectionMember Method | Permite remover um objeto FX ou GFX das coleções de FXListener usando o nome da instância ou da classe. |
| reportStartRunDatetime Property | Valor datetime que indica quando começou a última geração de relatório. Contém dados significativos se o objeto membro de retorno tiver sido instanciado. Propriedade somente leitura. |
| reportStopRunDatetime Property | Valor datetime que indica quando terminou a última geração de relatório. Contém dados significativos se o objeto membro de retorno tiver sido instanciado. Propriedade somente leitura. |
| RunCollectorResetLevel Property | Indica com que frequência o membro runCollector deve ser redefinido automaticamente pelo report listener (0=nunca, 1=após cada relatório, 2=após uma execução de relatórios encadeados). |
