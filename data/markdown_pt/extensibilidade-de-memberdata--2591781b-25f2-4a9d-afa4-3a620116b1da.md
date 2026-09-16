# Extensibilidade de MemberData

O Visual FoxPro 9.0 fornece atributos de metadados estendidos para membros de classes. Esse modelo permite criar aprimoramentos em tempo de design:
 - Especificar um editor de propriedades personalizado.
- Adicionar uma propriedade, evento ou método à guia Favorites da janela Properties.
- Controlar a capitalização de propriedades e métodos personalizados na janela Properties e no IntelliSense.
- Adicionar atributos definidos pelo usuário.

# Modelo extensível de MemberData

MemberData usa uma cadeia XML para especificar metadados de propriedades e métodos. A personalização de _MemberData existe nos níveis de classe e global; o nível da classe sempre prevalece. A propriedade _MemberData é herdada e pode ser substituída por subclasses. No nível global, os dados ficam em registros especiais de Foxcode.dbf.

### Herança de MemberData

```foxpro
Class -> Container -> Global
```

O Visual FoxPro procura primeiro no nível Class da hierarquia pai, depois na hierarquia Container, do mais interno para o externo, e por fim no nível Global, na tabela indicada por _FOXCODE. A busca ocorre por atributo ou tag individual, portanto os dados podem estar distribuídos em vários locais.

O exemplo de Myprop usa os seguintes dados:

```foxpro
** Class Level - Mycmd (Myclasses.vcx)
<memberdata name="Myprop" display="MYProp" type="property"/>
** Class Level - _commandbutton (_base.vcx)
<memberdata name="Myprop" display="MYPROP" type="property"/>
** Container Level - mypageframe (myclasses.vcx)
<memberdata name="Myprop" favorites="True" display="myPRop" type="property"/>
** Container Level - myform (myclasses.vcx)
<memberdata name="Myprop" favorites="False" helpfile="Myhelp.chm" type="property"/>
** Global Level - foxcode.dbf
<memberdata name="Myprop" type="property" display="MYPROP" script="DO (_CODESENSE) WITH 'RunPropertyEditor','','MYPROP'"/>
```

Com a prioridade Class -> Container -> Global, os valores resultantes são:

```foxpro
display="MYProp"
favorites="True"
script="DO (_CODESENSE) WITH 'RunPropertyEditor','','myprop'"
helpfile="myhelp.chm"   (note: this is a custom user-defined attribute)
```

#### Observações

MemberData diferencia maiúsculas de minúsculas em atributos e valores. Não é necessário definir cada atributo em todos os níveis. `override="True"` interrompe a busca além daquele ponto. XML inválido é ignorado; um valor inválido também é ignorado e interrompe a busca.

# FOXCODE.dbf, o armazenamento global

FOXCODE.dbf armazena informações do IntelliSense. Se uma propriedade ou método de _MEMBERDATA não for encontrado na árvore de herança, essa tabela será pesquisada. Configurações globais aplicam-se a todas as propriedades ou métodos, salvo substituição por _MEMBERDATA.

> **Observação:** Para eventos, somente o atributo favorites é reconhecido.

### Formato MEMBERDATA de FOXCODE.dbf

Cada entrada usa um registro com Type igual a "E".

| Nome do campo | Valor | Descrição |
| --- | --- | --- |
| Type | E | |
| Abbrev | <name> | Nome da propriedade, evento ou método. |
| Cmd | {command} | Script executado para a propriedade ou método. |
| Tip | Cadeia XML MemberData da propriedade ou método. | |
| Data | Conteúdo do script do editor personalizado. | |

# Definição do conteúdo XML de MemberData

| Elemento | Atributo | Pai | Descrição |
| --- | --- | --- | --- |
| VFPData | Elemento raiz dos metadados da classe. | | |
| memberdata | VFPData | Metadados de um membro. | |
| memberdata | name | Nome do membro. | |
| memberdata | type | Property, event ou method. | |
| memberdata | display | Representação visual do membro. | |
| memberdata | favorites | True ou False. | |
| memberdata | override | True ou False. | |
| memberdata | script | Método de script a executar. | |

### Esquema XSD de MemberData

O esquema contém variantes para elementos memberdata de classes e reportdata do sistema de relatórios. O Visual FoxPro não usa reportdata diretamente, mas o projeto paralelo permite processar e armazenar as duas extensões de forma semelhante.

```foxpro
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
  elementFormDefault="qualified" attributeFormDefault="unqualified">
 <xs:element name="VFPData">
  <xs:complexType>
   <xs:choice>
    <xs:sequence>
     <xs:element name="reportdata" maxOccurs="unbounded">
      <xs:complexType>
       <xs:attributeGroup ref="Common"/>
       <xs:attributeGroup ref="ReportTemplate"/>
       <xs:anyAttribute processContents="lax"/>
      </xs:complexType>
     </xs:element>
    </xs:sequence>
    <xs:sequence>
     <xs:element name="memberdata" maxOccurs="unbounded">
      <xs:complexType>
       <xs:attributeGroup ref="Common"/>
       <xs:attributeGroup ref="PropertySheet"/>
       <xs:anyAttribute processContents="lax"/>
      </xs:complexType>
     </xs:element>
    </xs:sequence>
   </xs:choice>
  </xs:complexType>
 </xs:element>
 <xs:annotation>
  <xs:documentation>
  You can add extension attributes as required.
  </xs:documentation>
  <xs:documentation>
Use the name and ref attributes of the Common attribute group to
declare that certain rows "belong" to you. Use the script attribute of
the Common attribute group for design-time scripting.
  </xs:documentation>
 </xs:annotation>
 <xs:attributeGroup name="Common">
  <xs:attribute name="name" type="xs:string" use="required"/>
  <xs:attribute name="type" type="xs:string"/>
  <xs:attribute name="script" type="xs:string"/>
 </xs:attributeGroup>
<xs:annotation>
<xs:documentation>
The ReportTemplate-specific execute attribute is a script run at
runtime (by Listeners) whereas the Common script attribute is
potentially run by design-time tools. The declass and declasslib
attributes are looked for in the header record's template information,
not individual DataEnvironment related object records. The class and
classlib attributes in the header record are not used, and can be
leveraged for a custom helper class for report builders or listeners as
desired. Class and classlib attributes in layout objects are meant for
use in run-time and design-time templating. You can use these template
classes to build custom rendering objects at runtime or to assign
common style attributes at design-time, or both.
</xs:documentation>
 </xs:annotation>
 <xs:attributeGroup name="ReportTemplate">
  <xs:attribute name="class" type="xs:string"/>
  <xs:attribute name="classlib" type="xs:string"/>
  <xs:attribute name="declass" type="xs:string"/>
  <xs:attribute name="declasslib" type="xs:string"/>
  <xs:attribute name="execute" type="xs:string"/>
  <xs:attribute name="execwhen" type="xs:string"/>
 </xs:attributeGroup>
 <xs:attributeGroup name="PropertySheet">
  <xs:attribute name="override" type="xs:boolean"/>
  <xs:attribute name="display" type="xs:string"/>
  <xs:attribute name="favorites" type="xs:boolean"/>
 </xs:attributeGroup>
</xs:schema>
```

### Exemplo de MemberData

A primeira entrada adiciona BorderStyle à guia Favorites e a exibe em maiúsculas. A segunda cria MyProperty e executa MyPropertyScript ao escolher reticências ou clicar duas vezes.

```foxpro
<?xml version="1.0" encoding="Windows-1252" standalone="yes"?>
<VFPData>
<memberdata name="borderstyle" type="property" favorites="True" display="BORDERSTYLE"override="False"/>
<memberdata name="MyProperty" type="property" display="MyProperty" favorites="True" override="False" script="MyPropertyScript"/>
</VFPData>
```

# Editores de propriedades personalizados

Um editor personalizado é executado pelo botão de reticências ou clique duplo. O Visual FoxPro procura o atributo script em _MemberData e em sua árvore de herança. Propriedades personalizadas e nativas podem ter editores; para as nativas, o script deve retornar o tipo e valor corretos. O editor personalizado substitui o nativo e é responsável por definir o valor, podendo usar ASELOBJ( ).

### Ganchos de menu do editor

As opções MemberData Editor… e Add to Favorites… chamam o aplicativo de _BUILDER com quatro parâmetros: referência ao objeto de nível superior, `"MemberData"`, código numérico do designer e nome do membro selecionado.

```foxpro
DO (_BUILDER) WITH oForm, "MemberData", 1
```

```foxpro
DO (_BUILDER) WITH oForm, "MemberData", 11, "Caption"
```

# MemberDataEditor.app

O MemberDataEditor.app edita metadados de propriedades, eventos e métodos. Ele permite criar MemberData local ou global, controlar substituição e padrões, adicionar favoritos, criar scripts, definir a exibição e formatar XML.

# Ganchos de script de Foxcode.dbf

Registros especiais de script em _FOXCODE podem ser chamados em tempo de design.

### Script _GetMemberData

Pode adicionar _MEMBERDATA a containers ou controles ao abrir designers, adicionar controles ou selecionar objetos. O registro usa Type E, Abbrev `_GETMEMBERDATA` e Data com o script. Nenhum parâmetro é passado; ASELOBJ( ) pode obter o objeto selecionado.

### Script MenuHit

É chamado quando um menu do sistema é escolhido e pode substituir uma caixa de diálogo. Recebe um objeto com UserTyped e MenuItem. Para impedir o comportamento nativo, defina ValueType como V ou L.

### Script MenuContext

É chamado antes da exibição de um menu de atalho e pode substituí-lo. Recebe um objeto com Items, UserTyped e MenuItem. Para suprimir o menu nativo, defina ValueType como V ou L; use DEFINE MENU com SHORTCUT para criar outro.
