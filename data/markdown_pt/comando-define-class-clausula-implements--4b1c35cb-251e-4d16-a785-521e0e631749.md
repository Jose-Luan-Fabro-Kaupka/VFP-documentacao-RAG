# Comando DEFINE CLASS - Cláusula IMPLEMENTS

Especifica herdar a interface de outro componente COM.

```foxpro
[IMPLEMENTS cInterfaceName [EXCLUDE] IN TypeLib | TypeLibGUID | ProgID ]
```

#### Parâmetros
 **[IMPLEMENTS cInterfaceName [EXCLUDE] IN TypeLib | TypeLibGUID | ProgID ]**
Especifica que a definição de classe herda a interface ou a definição de classe de outro componente COM. Você pode incluir várias instruções IMPLEMENTS. Observação Certas tecnologias, como Microsoft COM+ Events, exigem que o componente COM implemente a interface da classe de eventos à qual está sendo vinculado. A palavra-chave EXCLUDE exclui a interface implementada da biblioteca de tipos. A cláusula IN especifica o local da interface do componente COM. Você pode especificar a biblioteca de tipos do objeto COM usando TypeLib , o GUID da biblioteca de tipos usando TypeLibGUID ou o ProgID do programa que inicializa o objeto COM. Quando você usa TypeLibGUID , inclua a designação de versão principal e secundária conforme mostrado no exemplo a seguir: IMPLEMENTS IDict1 IN {04BCEF93-7A77-11D0-9AED-CE3E5F000000}#1.0 Dica O parâmetro TypeLib é a forma menos recomendada de especificar a biblioteca de tipos porque isso requer um nome de arquivo cujo caminho pode diferir de computador para computador. Se você está distribuindo seu .dll, considere usar TypeLibGUID ou ProgID em vez disso. Observação Quando você usa a cláusula IMPLEMENTS, deve incluir todos os métodos dessa interface na definição de classe. Você deve usar o nome da interface exatamente como aparece na biblioteca de tipos. No entanto, para nomes de interface precedidos por sublinhado (_), como na classe RecordSet do ADODB, o sublinhado é opcional. Antepõe o nome do método com o nome da interface, por exemplo, Publisher_ShowPrice . Essa convenção ajuda a evitar conflito entre duas interfaces que contêm métodos com o mesmo nome quando você inclui várias instruções IMPLEMENTS em uma definição de classe. Como as propriedades são essencialmente armazenadas como dois métodos dentro de uma biblioteca de tipos, por exemplo, Put e Get, a definição de classe deve incluir ambos os métodos. Dica Para economizar tempo, você pode usar o Object Browser do Visual FoxPro para arrastar e soltar definições de interface no seu código. Junto com a instrução IMPLEMENTS, todos os métodos implementados com suas assinaturas de parâmetro apropriadas são escritos automaticamente para você. Para obter mais informações, consulte Janela Object Browser .

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

Para obter mais informações e a sintaxe completa, consulte Comando DEFINE CLASS. Para obter mais informações sobre uma cláusula específica do comando DEFINE CLASS, consulte os tópicos a seguir:
 - Cláusula DEFINE CLASS
- Cláusula Property Definition
- Cláusula PEMName_COMATTRIB
- Cláusula ADD OBJECT
- Cláusula Function or Procedure Definition

# Exemplo

O exemplo a seguir cria uma classe chamada MyPublisherClass como uma classe Custom, usa a palavra-chave OLEPUBLIC para especificar que clientes Automation podem acessar a classe quando incluída em um Automation server, usa a cláusula IMPLEMENTS para herdar a definição de classe da definição de classe Publisher na biblioteca de tipos MyBookStore.dll e inclui o método ShowPrice da interface Publisher.

```foxpro
DEFINE CLASS MyPublisherClass AS Custom OLEPUBLIC
   IMPLEMENTS Publisher IN "MyBookStore.dll"
   PROCEDURE Publisher_ShowPrice(cGetID AS Long) AS Short
   ENDPROC
ENDDEFINE
```
