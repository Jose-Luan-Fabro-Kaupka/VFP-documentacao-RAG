# Comando CREATE VIEW

Cria um arquivo de view a partir do ambiente do Visual FoxPro.

```foxpro
CREATE VIEW FileName
```

#### Parâmetros
 **FileName**
Especifica o nome do arquivo de view a criar.

# Observações

CREATE VIEW cria um novo arquivo de view contendo informações sobre o ambiente do Visual FoxPro. SET VIEW restaura o ambiente salvo em um arquivo de view por CREATE VIEW. Arquivos de view criados com CREATE VIEW recebem a extensão .vue.

As informações salvas em um arquivo de view incluem:
 - Todas as tabelas, índices, arquivos alternativos e arquivos de formato atualmente abertos em todas as áreas de trabalho
- Todos os campos contidos na lista SET FIELDS
- Todas as relações estabelecidas entre tabelas abertas
- Todos os filtros em vigor para tabelas abertas
- As configurações DEFAULT e PATH
- A configuração do arquivo de procedimento
- O arquivo de Help atual
- O arquivo de recursos atual
- O status SET SKIP
- O estado da barra de status (ON ou OFF)

Arquivos de view são úteis tanto em programas quanto durante a depuração. Somente um comando, SET VIEW TO FileName, precisa ser executado para restaurar todo o ambiente. Durante a depuração, as configurações do ambiente podem ser salvas em um arquivo de view, os testes podem ser executados e o ambiente pode ser restaurado para continuar a execução do programa.
