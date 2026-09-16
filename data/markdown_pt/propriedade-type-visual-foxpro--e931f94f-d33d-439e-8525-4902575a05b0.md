# Propriedade Type (Visual FoxPro)

Contém um caractere que indica o tipo de arquivo de um arquivo em um projeto. Disponível em tempo de design e execução.

```foxpro
Object.Type
```

# Observações

Aplica-se a: File Object (Visual FoxPro)

A tabela a seguir lista os valores que a propriedade Type pode conter e os tipos de arquivo correspondentes.

| Value | FoxPro.H Constant | File Type and Extension |
| --- | --- | --- |
| d | FILETYPE_DATABASE | Database, .dbc |
| D | FILETYPE_FREETABLE | Free table, .dbf |
| Q | FILETYPE_QUERY | Query, .qpr |
| K | FILETYPE_FORM | Form, .scx |
| R | FILETYPE_REPORT | Report, .frx |
| B | FILETYPE_LABEL | Label, .lbx |
| V | FILETYPE_CLASSLIB | Visual class Library, .vcx |
| P | FILETYPE_PROGRAM | Program, .prg |
| L | FILETYPE_APILIB | Visual FoxPro dynamic link library, .fll |
| Z | FILETYPE_APPLICATION | Application, .app |
| M | FILETYPE_MENU | Menu, .mnx |
| T | FILETYPE_TEXT | Text file, varies |
| x | FILETYPE_OTHER | Other, varies |

Esses valores são armazenados no campo Type do arquivo .pjx do projeto.
