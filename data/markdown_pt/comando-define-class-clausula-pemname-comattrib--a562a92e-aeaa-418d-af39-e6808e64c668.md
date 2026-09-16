# Comando DEFINE CLASS - Cláusula PEMName_COMATTRIB

Especifica atributos e valores de biblioteca de tipos para propriedades ou métodos PEMName_COMATTRIB. Os recursos descritos nesta seção se aplicam somente a classes OLEPUBLIC e são usados para especificar informações adicionais, como uma descrição ou atributo somente leitura, sobre a propriedade ou método que você deseja gravar na biblioteca de tipos COM.

> **Observação:** Diferentemente dos métodos Access e Assign, as propriedades PEMName_COMATTRIB são marcadas como ocultas automaticamente e não são acessíveis no Visual FoxPro. Elas são estritamente para uso pelo Visual FoxPro durante o processo de compilação ao gravar em uma biblioteca de tipos COM.

```foxpro
[PEMName_COMATTRIB = nFlags | DIMENSION PEMName_COMATTRIB[numElements]
   [PEMName_COMATTRIB[1] = nFlags
        PEMName_COMATTRIB[2] = cHelpString
        PEMName_COMATTRIB[3] = cPropertyCapitalization
        PEMName_COMATTRIB[4] = cPropertyType
        PEMName_COMATTRIB[5] = nOptionalParams]]
```

#### Parâmetros
 **[ PEMName _COMATTRIB = nFlags | DIMENSION PEMName _COMATTRIB[ numElements ]**
Especifica um valor nFlags para uma propriedade ou método PEMName ou usa o comando DIMENSION para criar uma matriz de propriedades que contém atributos de biblioteca de tipos para a propriedade PEMName. Ao criar uma matriz, numElements especifica o número de elementos na matriz até 5. A tabela a seguir descreve os elementos na matriz. Elemento COMATTRIB Descrição Tipo 1 Sinalizadores de atributo. Número 2 Cadeia de ajuda. Cadeia de caracteres 3 Capitalização. Cadeia de caracteres 4 Tipo de propriedade. Cadeia de caracteres 5 Número de parâmetros. Observação Se você especificar menos que o número real de parâmetros, os números maiores que os declarados são opcionais. Número Observação Para valores ou tipos inválidos na matriz PEMName _COMATTRIB, o Visual FoxPro gera um erro. Elementos vazios usam valores padrão.
**nFlags**
Especifica sinalizadores de atributo para a propriedade ou método PEMName conforme aparece na biblioteca de tipos. A tabela a seguir descreve os sinalizadores válidos. Valor nFlags #DEFINE Descrição 0x1 (1) COMATTRIB_RESTRICTED A propriedade ou método não deve ser acessível de linguagens de macro. Este sinalizador é destinado a funções de nível de sistema ou funções que navegadores de tipo não devem exibir. COMATTRIB_RESTRICTED significa que programadores orientados a macro não devem ter permissão para acessar este membro. Esses membros geralmente são tratados como _HIDDEN por ferramentas como o Visual Basic, com a principal diferença de que o código não pode se vincular a esses membros. 0x40 (64) COMATTRIB_HIDDEN A propriedade ou método não deve ser exibido ao usuário, embora exista e seja vinculável. COMATTRIB_HIDDEN significa que a propriedade nunca deve ser mostrada em navegadores de objetos, navegadores de propriedades e assim por diante. Esta função é útil para remover itens de um modelo de objeto. O código pode se vincular ao membro, mas o usuário nunca saberá que o membro existe. 0x400 (1024) COMATTRIB_NONBROWSABLE A propriedade ou método aparece em um navegador de objetos, mas não em um navegador de propriedades. COMATTRIB _NONBROWSABLE significa que a propriedade não deve ser exibida em um navegador de propriedades. É usado em circunstâncias em que ocorreria um erro se a propriedade fosse mostrada em um navegador de propriedades. Vinculação antecipada e tardia impõem restrições de acesso diferentes. Clientes de vinculação antecipada não poderão gravar em uma propriedade somente leitura, nem ler de uma propriedade somente gravação, porque não haverá uma entrada na vtable. Clientes de vinculação tardia ainda podem acessar um propertyget em somente gravação ou um propertyput em um PEMName somente leitura . 0x100000 COMATTRIB_READONLY A propriedade é somente leitura. Aplica-se somente a Properties. Equivalente a um PropertyGet. Observação Usar COMATTRIB_READONLY e COMATTRIB_WRITEONLY é equivalente a não usar nenhum. 0x200000 COMATTRIB_WRITEONLY A propriedade é somente gravação. Aplica-se somente a Properties. Equivalente a um PropertyLet. Observação Usar COMATTRIB_READONLY e COMATTRIB_WRITEONLY é equivalente a não usar nenhum.
**PEMName _COMATTRIB[2] = cHelpString**
Especifica um valor de cadeia de caracteres para armazenar na biblioteca de tipos para a propriedade PEMName . Para métodos, use a cláusula HELPSTRING cHelpString.
**PEMName _COMATTRIB[3] = cPropertyCapitalization**
Especifica o nome da propriedade como um valor de cadeia de caracteres conforme deve aparecer na biblioteca de tipos. Toda a capitalização é preservada. Se esta configuração for omitida, o Visual FoxPro grava a propriedade na biblioteca de tipos em letras maiúsculas.
**PEMName _COMATTRIB[4] = cPropertyType**
Especifica o tipo de dados da propriedade como um valor de cadeia de caracteres conforme aparece na biblioteca de tipos e funciona da mesma forma que a cláusula AS Type. Aplica-se somente a Properties.
**PEMName _COMATTRIB[5] = nOptionalParms ]]**
Especifica o número de parâmetros opcionais em um método. Por exemplo, se este valor for 2 para um método com 5 parâmetros, então os últimos 3 são opcionais. Aplica-se somente a Methods. Para clientes de vinculação tardia, os valores padrão para parâmetros opcionais ainda serão False (.F.), e a função PCOUNT( ) reflete com precisão o número real de parâmetros passados. Para clientes de vinculação antecipada, os valores padrão para parâmetros opcionais sempre serão definidos como uma cadeia de caracteres vazia (""), e PCOUNT( ) sempre retornará o número total de parâmetros para o método, não o número passado.

# Observações

O código a seguir mostra um resumo das principais cláusulas do comando DEFINE CLASS:

```foxpro
DEFINE CLASS Clause
   [Property_Definition_Clause]
   [PEMName_COMATTRIB Clause]
   [ADD OBJECT Clause]
   [IMPLEMENTS Clause]
   [Function_Procedure_Definition_Clause]
ENDDEFINE
```

Para obter mais informações e sintaxe completa, consulte DEFINE CLASS Command. Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS, consulte os seguintes tópicos:
 - DEFINE CLASS Clause
- Property Definition Clause
- ADD OBJECT Clause
- IMPLEMENTS Clause
- Function or Procedure Definition Clause

# Exemplo

O exemplo a seguir demonstra como definir uma matriz de atributos de biblioteca de tipos usando a cláusula DIMENSION PEMName_COMATTRIB:

```foxpro
#INCLUDE foxpro.h
DEFINE CLASS myOLEClass AS Custom OLEPUBLIC
   MyProperty = 5.2
   * Set COM attributes for MyProperty.
   DIMENSION MyProperty_COMATTRIB[4]
   myProperty_COMATTRIB[1] = COMATTRIB_READONLY
   myProperty_COMATTRIB[2] = "Help text displayed in object browser"
   myProperty_COMATTRIB[3] = "MyProperty"  && Proper capitalization.
   myProperty_COMATTRIB[4] = "Float"        && Data type
ENDDEFINE
```

No entanto, se você desejar definir somente o elemento nFlags, não precisa criar uma matriz:

```foxpro
#INCLUDE foxpro.h
DEFINE CLASS myOLEClass AS Custom OLEPUBLIC
   MyProperty = "Test"
   * Set the only the nFlags attribute for MyProperty.
   myProperty_COMATTRIB = COMATTRIB_READONLY
ENDDEFINE
```
