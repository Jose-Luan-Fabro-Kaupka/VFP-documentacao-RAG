# Recursos e arquivos distribuíveis e restritos do Visual FoxPro

O Visual FoxPro e seu ambiente de desenvolvimento contêm muitos arquivos e recursos licenciados apenas para seu uso no design, desenvolvimento e teste de suas aplicações. Se sua aplicação contiver qualquer um desses recursos ou arquivos restritos, bem como arquivos diferentes daqueles criados por você ou listados em Redist.txt, você deve removê-los. Nos termos do Contrato de Licença da Microsoft que você recebeu com este produto, você não pode distribuir esses arquivos em sua aplicação ou em seus discos.

Você pode distribuir qualquer arquivo do Visual FoxPro que não seja restrito. Para uma lista de arquivos redistribuíveis, consulte Redist.txt, localizado no diretório de instalação do Visual FoxPro, e as diretrizes para incluir arquivos redistribuíveis neste tópico.

# Recursos restritos do Visual FoxPro

Você não pode incluir os seguintes menus restritos do Visual FoxPro e seus comandos de menu em um arquivo executável (.exe) distribuído:
 - Database
- Form
- Menu
- Program
- Project
- Query
- Table

A tabela a seguir lista comandos para os quais sua aplicação retorna a mensagem "Feature not available", se incluídos. Embora você não possa incluir comandos que criam ou modificam menus, formulários ou consultas, você pode executar programas de menu, formulário ou consulta compilados em sua aplicação.

| Comandos indisponíveis | |
| --- | --- |
| APPEND PROCEDURES | MODIFY DATABASE |
| BUILD APP | MODIFY FORM |
| BUILD EXE | MODIFY MENU |
| BUILD PROJECT | MODIFY PROCEDURE |
| CREATE FORM | MODIFY PROJECT |
| CREATE MENU | MODIFY QUERY |
| CREATE QUERY | MODIFY SCREEN |
| CREATE SCREEN | MODIFY VIEW |
| CREATE VIEW | MODIFY CONNECTION |
| SET STEP | |

A tabela a seguir lista comandos que são ignorados quando usados em uma aplicação distribuída.

| Comandos ignorados | |
| --- | --- |
| ASSERT | DEBUGOUT |
| SET DEBUG | SET DOHISTORY |
| SET DEVELOPMENT | SET ECHO |

# Arquivos restritos do Visual FoxPro

O Visual FoxPro instala arquivos no seu computador que são restritos e não podem ser reproduzidos ou distribuídos, incluindo:
 - Alguns arquivos de assistentes
- Fontes TrueType
- Arquivos de ajuda do Visual FoxPro

# Arquivos distribuíveis do Visual FoxPro

De acordo com o Contrato de Licença da Microsoft que você recebeu com este produto, você deve distribuir arquivos em conjunto com uma aplicação correspondente. As diretrizes a seguir se aplicam a arquivos distribuíveis.

### Exemplos

O Visual FoxPro fornece arquivos no diretório Visual FoxPro \Samples para você aprender e construir sobre eles. Embora você não possa distribuir exemplos não modificados do Visual FoxPro, você pode referenciar partes do código de aplicação de exemplo como exemplos para construir sua própria aplicação.

Se você usar quaisquer arquivos nesses diretórios, incluindo todos os arquivos .bmp, .ico e .cur, você deve incluí-los em seu projeto e build de aplicação. Eles não devem aparecer por nome nos discos distribuíveis e não podem ser distribuídos independentemente de suas aplicações.

### Bibliotecas de classes

Você pode usar qualquer arquivo .vcx, incluindo aqueles nos diretórios \Ffc e \Gallery, a biblioteca de classes de assistentes, Wizstyle.vcx, e as bibliotecas de classes de exemplo sem modificação em suas aplicações. Você deve incluir as bibliotecas em seu projeto e no build de sua aplicação.

### Arquivos ODBC

Consulte o Contrato de Licença da Microsoft que você recebeu com este produto para restrições específicas com relação à redistribuição de arquivos ODBC.

### Controles ActiveX

O Visual FoxPro inclui um conjunto de controles ActiveX (.ocx files) que você pode adicionar e distribuir com suas aplicações.
