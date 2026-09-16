# Propriedade Unicode

Especifica como os métodos LoadXML, Attach, AddTableSchema e ToXML do XMLAdapter e os métodos ToCursor, ChangesToCursor e ApplyDiffGram do XMLTable tratam cadeias de caracteres.

XMLField Unicode especifica se deve colocar uma cadeia de caracteres Unicode no campo.

> **Observação:** Se a propriedade IsBinary do XMLField é True (.T.) e XMLField Unicode é True (.T.), o Visual FoxPro gera a mensagem apropriada.

Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
Object.Unicode [= lValue]
```

#### Parâmetros
 **lValue**
Especifica um valor lógico que determina como as cadeias de caracteres são tratadas dependendo do método sendo executado ou são armazenadas. A tabela a seguir descreve os valores e comportamentos de Unicode dependendo do método sendo chamado ou objeto. Método ou Objeto lValue Métodos LoadXML e Attach do XMLAdapter True (.T.): Dobra o comprimento de uma cadeia de caracteres dada e atribui o resultado à propriedade MaxLength do XMLField. False (.F.): Atribui o comprimento de uma cadeia de caracteres dada à propriedade MaxLength do XMLField. Quando LoadXML e Attach são chamados, XMLField Unicode é definido como o valor de XMLAdapter Unicode para campos Character e Memo. Método AddTableSchema do XMLAdapter True (.T.): Atribui o valor de XMLAdapter Unicode (True, ou .T.) a XMLField Unicode . False (.F.): Atribui o valor de XMLAdapter Unicode (False, ou .F.) a XMLField Unicode . Método ToXML do XMLAdapter True (.T.): Divide o comprimento de um campo de caracteres dado por 2 e atribui o resultado a xsd:maxLength . False (.F.): Atribui o comprimento de um campo de caracteres dado a xsd:maxLength . Ao usar XMLAdapter ToXML , o conteúdo do campo é convertido de Unicode para a página de código do XML, e o símbolo nulo incorporado (CHR(0)+CHR(0)) é considerado um terminador de cadeia de caracteres. Para cadeias de caracteres Unicode armazenadas em campos Character, se o comprimento da cadeia de caracteres é menor que o tamanho do campo, o terminador nulo é necessário. Para terminar a cadeia de caracteres, use CHR(0)+CHR(0) . Métodos ToCursor , ChangesToCursor e ApplyDiffgram do XMLTable True (.T.): Cria o campo com a flag NOCPTRANS independentemente da propriedade NoCpTrans do XMLField e armazena uma cadeia de caracteres Unicode no campo. Para obter mais informações, consulte Comando SET NOCPTRANS . Observação Se a propriedade MaxLength do XMLField é um número ímpar, o Visual FoxPro gera a mensagem apropriada. False (.F.): Cria o campo como um campo Character ou Memo regular. Objeto XMLField True (.T.): Armazena uma cadeia de caracteres Unicode no campo. False (.F.): Armazena uma cadeia de caracteres não Unicode no campo.

# Observações

Aplica-se a: Classe XMLAdapter | Classe XMLField
