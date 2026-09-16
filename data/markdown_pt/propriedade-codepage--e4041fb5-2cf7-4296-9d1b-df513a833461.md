# Propriedade CodePage

Especifica o conjunto de caracteres usado para codificar ou decodificar um objeto. Para o objeto File, a propriedade é somente leitura. Para objetos XML, a propriedade é leitura/gravação em tempo de design e em tempo de execução.

```foxpro
oXMLAdapter.CodePage = nValue
oXMLTable.CodePage = nValue
oXMLField.CodePage = nNvalue
oFileObject.CodePage
```

# Valor de retorno
 **oXMLAdapter, oXMLTable, oXMLField**
Objetos XML que suportam páginas de código.
**oFileObject**
Objeto que representa um arquivo em um projeto Visual FoxPro.
**nValue**
Valor numérico associado a uma página de código. Para objetos XML, o valor padrão é zero (0).

# Observações

Aplica-se a: XMLAdapter Class, XMLTable Class, XMLField Class, File Object (Visual FoxPro)

Um valor numérico indica o conjunto de caracteres usado para o objeto. Páginas de código geralmente correspondem a diferentes plataformas e idiomas e são usadas em aplicativos internacionais.

Quando você usa os métodos LoadXML ou Attach para carregar um documento XML, o objeto XMLAdapter processa o XML para determinar a propriedade CodePage. Se o objeto XMLAdapter não conseguir determinar a página de código ou a página de código não estiver na lista de páginas de código suportadas, a propriedade CodePage é definida como zero (0).

Para obter mais informações sobre páginas de código e suporte internacional no Visual FoxPro, consulte Code Pages Supported by Visual FoxPro e Developing International Applications.

# Exemplo

Este exemplo conta quantos arquivos de projeto estão usando a página de código 1252 (ANSI Windows).

```foxpro
nCode1252=0
MODIFY PROJECT myproject NOWAIT
FOR i = 1 TO _VFP.ActiveProject.Files.Count
   IF  _VFP.ActiveProject.Files(i).CodePage = 1252
      nCode1252=nCode1252+1
   ENDIF
ENDFOR
?nCode1252    && Show the count in the Visual FoxPro screen.
```
