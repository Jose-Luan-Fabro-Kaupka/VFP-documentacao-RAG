# Compreendendo e estendendo a estrutura de relatórios

No Visual FoxPro 9.0, extensões do Report System em tempo de design e em tempo de execução são mais viáveis e variadas do que nunca. Para garantir que você crie extensões com sucesso, deve compreender as estruturas de tabela de relatório (.frx) e etiqueta (.lbx).

> **Observação:** As estruturas de arquivo de relatório e etiqueta são idênticas no Visual FoxPro. Para obter mais informações sobre o conteúdo do diretório FILESPEC, consulte Table Structures of Table Files (.dbc, .frx, .lbx, .mnx, .pjx, .scx, .vcx) .

Este tópico discute como explorar e estender o uso das tabelas de várias colunas para descrever diferentes aspectos do layout e comportamento de relatórios. Também fornece limitações especificadas para extensões a essas tabelas.

Esta informação permite que você:
 - Manipule dados existentes de tabelas de relatório e etiqueta com sucesso.
- Descreva novos tipos de elementos e comportamento de relatórios nas tabelas.

# Compreendendo as alterações nas tabelas de relatório e etiqueta

O Visual FoxPro 9 não adiciona campos obrigatórios à estrutura nativa de tabela de relatório. Como nenhum campo novo é adicionado para migrar formulários de relatório e etiqueta, você pode usar os recursos de design aprimorados do Visual FoxPro 9 para editar relatórios existentes. Esses relatórios ainda serão executados quando distribuídos aos usuários finais de seus aplicativos existentes.

Para suportar várias melhorias em tempo de design e em tempo de execução, o Visual FoxPro 9 sobrecarrega alguns campos em tabelas de relatório e etiqueta, usando-os de novas formas para elementos de relatório que não usavam esses campos em versões anteriores. Alguns dos novos valores não são usados diretamente pelo produto, em vez disso fornecendo informações a aplicativos ReportBuilder ou outro código de usuário.

O novo conteúdo do Visual FoxPro 9, que suporta melhorias de design e processamento, também pode ser adicionado a relatórios existentes sem perturbar a compatibilidade com versões anteriores. O conteúdo adicional em campos de relatório e etiqueta será ignorado em tempo de execução pelo Visual FoxPro 8 e versões anteriores.

O Visual FoxPro fornece informações sobre as tabelas de sistema para vários elementos, incluindo relatórios, no diretório FILESPEC. O Visual FoxPro 9.0 fornece uma cópia atualizada de 60FRX.DBF, a tabela que especifica o uso dos vários campos nas tabelas de relatório e etiqueta.

### Alterações em 60FRX.DBF

A coluna 60FRX.Descriptio foi atualizada em quase todos os registros, para explicar melhor o uso de campos por relatórios e etiquetas. As informações atualizadas que você vê neste campo se aplicam a todas as versões do Visual FoxPro e adicionam uma seção separada indicando qualquer uso novo no Visual FoxPro 9.0.

O exemplo a seguir é a entrada 60FRX.Descriptio para o valor 60FRX.Fields `RULERLINES`.

```foxpro
RULERLINES is used only in the header record.
0 = Show Ruler Lines: No
1 = Show Ruler Lines: Yes
==============================
Visual FoxPro 9-only Information Below
==============================
RULERLINES is reserved in VFP9 for OBJTYPE=8 (Field) for StringTrimming.
Default is StringTrimmingEllipsisWord.
0 or not entered = Default
1 = StringTrimmingCharacter
2 = StringTrimmingWord
3 = StringTrimmingEllipsisCharacter
4 = StringTrimmingEllipsisWord
5 = StringTrimmingEllipsisPath (for filenames).
```

Para ajudá-lo a encontrar como cada tipo de campo de relatório e etiqueta é usado para diferentes tipos de elementos de layout, a versão 9.0 do Visual FoxPro de 60FRX.DBF contém um novo campo, 60FRX.Usedby_obj. O campo 60FRX.Usedby_obj contém uma lista de palavras-chave para todos os elementos de relatório que usam um determinado campo.

Por exemplo, se você quisesse descobrir todos os campos usados no registro de cabeçalho de um arquivo de relatório ou etiqueta e uma descrição de como esses campos são usados, poderia emitir este comando:

```foxpro
SELECT Fields, Descriptio FROM 60FRX WHERE ATC("Header",Usedby_obj) > 0
```

A coluna Fields no cursor resultante fornece o nome de cada campo em uma tabela FRX ou LBX usado no registro Header. A coluna Descriptio informa como cada campo é usado.

> **Dica:** Se um campo de relatório tiver novos usos no Visual FoxPro 9.0, as palavras-chave para elementos que passam a usar o campo seguem um símbolo, " | ", na lista 60FRX.Usedby_obj. For example, for the 60FRX.Fields value RULERLINES , the 60FRX.Usedby_obj value reads HEADER | EXPR . As indicated in the 60FRX.Descriptio entry for RULERLINES above, previous versions of Visual FoxPro used this field in the header record only. Visual FoxPro 9.0 also uses this field for Field (or Expression) layout elements. As a result, the two keywords appear separated by the " | " symbol in the 60FRX.Usedby_obj column.

A tabela a seguir fornece as palavras-chave 60FRX.Usedby_obj para cada tipo de objeto de relatório.

| Valor do campo Objtype da tabela de relatório | Descrição do objeto de relatório | Valor 60FRX.Usedby_obj |
| --- | --- | --- |
| 0 | Comentário | N/A |
| 1 | Cabeçalho de relatório | HEADER |
| 2 | Workarea (FoxPro 2.x reports) | 20TABLE |
| 3 | Index (FoxPro 2.x reports) | 20INDEX |
| 4 | Relation (FoxPro 2.x reports) | 20RELATION |
| 5 | Etiqueta | TEXT |
| 6 | Linha | LINE |
| 7 | Retângulo / Forma | SHAPE |
| 8 | Campo | EXPR |
| 9 | Bandinfo | BAND |
| 10 | Grupo | GROUP |
| 17 | Imagem / OLE Bound | PICT |
| 18 | Variável | VAR |
| 21 | Printer Driver Setup (FoxPro 2.x reports) | 20PDRIVER |
| 23 | Recurso de fonte | FONTRES |
| 25 | Data Environment | DATAENV |
| 26 | Cursor, Relation, or CursorAdapter (See Name field to determine which) | CURSOR-RELATION |

### Criando conteúdo válido de relatório e etiqueta

O Visual FoxPro 9 fornece código de referência para mostrar como localizar e dimensionar os vários objetos usados em relatórios e etiquetas nas Foundation Classes. For more information, see FRX Cursor Foundation Class and FRX Device Helper Foundation Class. Essas classes fazem parte do ReportBuilder Application padrão. They give you the ReportBuilder Application's tools to use, when you want to determine appropriate placement and metrics for new report and label elements.

### Formatando e revisando informações de 60FRX.DBF

Um novo relatório no diretório FILESPEC, 90FRX.FRX, fornece informações consolidadas sobre o uso completo de tabelas de relatório e etiqueta em todas as versões, destacando o uso novo no Visual FoxPro 9. The earlier reports available for 60FRX.DBF, 60FRX1.FRX and 60FRX2.FRX, are still included in FILESPEC.

# Estendendo tabelas de relatório e etiqueta com segurança

O Visual FoxPro 9 fornece persistência confiável de conteúdo definido pelo usuário em relatórios e etiquetas. You can add your own content to these tables in the following ways:
 - Adicionar novas colunas a tabelas de relatório e etiqueta.
- Adicionar novos tipos de objetos de relatório e etiqueta como linhas às tabelas.
- Adicionar registros com novos valores Platform (registros com valores de plataforma diferentes de " Windows ").
- Adicionar dados privados em colunas, como a coluna User, não usadas nativamente por relatórios ou etiquetas.
- Add private attributes into the Reporting memberdata XML data schema. Reporting memberdata is stored in the Style column. For more information, see How to: Assign Structured Metadata to Report Controls .

O Visual FoxPro 9 preserva todos esses tipos de conteúdo definido pelo usuário, quer ocorram em registros usados nativamente ou em registros adicionais. It makes this content available to user code in Report Designer sessions, through Report Builder hooks. When you process reports and labels, it makes the full content of the report or label table available to ReportListener events and methods.

> **Cuidado:** Versões anteriores do Visual FoxPro não preservavam conteúdo de usuário em sessões de design e não permitiam registros ou colunas definidos pelo usuário em tabelas de relatório e etiqueta. As a result, you should not add new types of content into reports and tables using Visual FoxPro 9 if you expect to edit these files in earlier versions later, because the new content can be lost. You can add new content into existing records of reports and labels and distribute them successfully to users of earlier versions. However, do not add new columns into these tables, to ensure that the earlier versions can recognize the tables as reports and labels.

As limitações a seguir devem ser observadas ao estender relatórios e etiquetas com novos tipos de conteúdo.

### Diferenciando entre tipos de registro nativos e definidos pelo usuário

Existem 100 valores Objtype possíveis no total (0 a 99). Visual FoxPro 9 explicitly reserves Objtype values 49 and below for internal or native Report Designer use. Only records with recognized and documented Objtype values, and only records containing Objcode field values natively associated with these Objtype values, are manipulated in the native Report Designer.

Users and add-ons such as ReportBuilder Applications can alter the contents of records with natively-recognized values in the Objtype field of the report or label. They can also add new records with native Objtypes, taking care to follow standard usage of columns for all native types.

Users and add-ons should not add unknown or undocumented Objcode values to records with native Objtype values (49 and below). They may be removed by the native Report Designer without warning.

You can add records with user-defined Objtype values of 50 and above. These records can have any Objcode values. The native Report Designer preserves and ignores all content of such records, but ReportBuilder Applications and other add-ons can be used to add and modify them.

> **Observação:** Although user-added records with Objtype values of 50 and above are preserved, the position of such records within the report or label table is not guaranteed. A Report Designer session may change the order of records in the report table. User-defined records will usually appear at the end of the table after the report is saved by the Report Designer. If record order is significant to your application, store information relevant to record order in an additional column.

### Garantindo valores UniqueID para registros com conteúdo definido pelo usuário

Extra content in any records without UniqueID values,including content in native fields such as the User field, will not be preserved. The restriction holds for records with native Objtype values as well as user-defined Objtype values.

> **Dica:** Use a função SYS(2015) para criar valores para o campo UniqueID de novos registros. Use the FRXCursor Foundation Class's getFrxTimeStamp method to create appropriate Timestamp values.

Reports and labels have a few native Objtype values without UniqueIDs, notably font (objtype 23) and data environment-related resources (objtypes 25 and 26), used in specific ways by the Report Engine at runtime. It is also possible to have a “comment” record (objtype 0 or blank). The Report Designer and ReportBuilder Application are not guaranteed to preserve user-defined content in these records. You can add new records of the appropriate objtypes for these resources, giving them standard contents. You can also extend these resources by associating user-defined object types with them. For example, a record of objtype 53 could represent an "extended font resource record.

### Localizando conteúdo adicionado pelo usuário em estruturas de tabela de relatório e etiqueta

Colunas adicionadas pelo usuário devem estar no final da estrutura de tabela Report ou Label. If native columns are re-ordered, deleted, edited for size, type or name, etc., Visual FoxPro will consider the report or label to be invalid.

O registro de cabeçalho da tabela, descrevendo atributos globais de relatório ou etiqueta, deve permanecer em sua posição padrão (primeiro registro na tabela).

The Expr, Tag, and Tag2 columns in the header record (used for printer setup attributes) are reserved for internal use.

In some limited cases, users may edit the values in the Expr column and, if these values are reasonable for the associated attributes, they will be recognized by the Designer, remain stable and be available during design sessions, and used by the Report Engine at run time. However, this behavior is not supported and not extensible. In particular, user-defined value-pairs in the Expr field will not be saved back to the report table after design sessions, even if no explicit changes to Page Setup are made during these sessions. You can use the Picture field of the header record to store user-override information for printer instructions, instead. For more information, see SYS(1037) - Page Setup Dialog Box.
