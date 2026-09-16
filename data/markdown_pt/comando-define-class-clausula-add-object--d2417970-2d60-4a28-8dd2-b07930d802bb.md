# Comando DEFINE CLASS - Cláusula ADD OBJECT

Adiciona objetos de outras classes à definição de classe.

```foxpro
[ADD OBJECT [PROTECTED] ObjectName AS ClassName2 [NOINIT] [WITH cPropertylist]]
```

#### Parâmetros
 **[ADD OBJECT [PROTECTED] ObjectName AS ClassName2**
Especifica a adição de um objeto de uma classe base do Visual FoxPro, classe ou subclasse definida pelo usuário, ou controle ActiveX personalizado à definição de classe. A palavra-chave PROTECTED impede o acesso e alterações nas propriedades do objeto fora da definição de classe ou subclasse.
**[NOINIT]**
Especifica que o método Init do objeto não será executado ao adicioná-lo.
**[WITH cPropertyList ]]**
Especifica uma lista de propriedades e seus valores para o objeto que você adiciona à definição de classe. Para obter mais informações, consulte a seção Exemplos.

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

Para obter mais informações e a sintaxe completa, consulte DEFINE CLASS Command. Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS, consulte:
 - DEFINE CLASS Clause
- Property Definition Clause
- PEMName_COMATTRIB Clause
- IMPLEMENTS Clause
- Function or Procedure Definition Clause

# Exemplo

O exemplo a seguir cria uma classe chamada MyForm a partir da classe base Form e adiciona um botão de comando da classe base CommandButton e uma caixa de seleção da classe base CheckBox:

```foxpro
DEFINE CLASS MyForm AS Form
   ADD OBJECT cmdButton1 AS CommandButton
   ADD OBJECT chkBox1 AS CheckBox
ENDDEFINE
```

Como outro exemplo, o código a seguir cria uma classe chamada MyForm, adiciona um botão de comando e uma caixa de seleção à classe e especifica valores para as propriedades Caption do botão de comando e da caixa de seleção.

```foxpro
DEFINE CLASS MyForm AS Form
   ADD OBJECT cmdButton1 AS CommandButton WITH Caption = "Yes"
   ADD OBJECT chkBox1 AS CheckBox WITH Caption = "Click Me"
ENDDEFINE
```
