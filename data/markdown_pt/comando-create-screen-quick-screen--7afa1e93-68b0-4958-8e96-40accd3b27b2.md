# Comando CREATE SCREEN - Quick Screen

Incluído para compatibilidade com versões anteriores. Use o Form Designer em vez disso.

Cria programaticamente uma tela.

```foxpro
CREATE SCREEN file1
| ? FROM file2
	[ROW | COLUMN]
	[FIELDS field list] [ALIAS]
	[NOOVERWRITE]
	[SIZE expN1,expN2] [SCREEN]
```

#### Parâmetros
 file1

 Quando um nome de arquivo file1 é incluído, o arquivo de tela é salvo com esse nome. Uma extensão .SCX é automaticamente atribuída. Se um arquivo de tela com esse nome já existir e a opção NOOVERWRITE não estiver incluída, você será perguntado se deseja sobrescrever o arquivo existente (se SET SAFETY estiver ON).

?

 A caixa de diálogo Open aparece quando o ponto de interrogação (?) é incluído. Uma lista de arquivos de relatório existentes é exibida. Escolha um dos relatórios existentes ou insira o nome de um novo relatório para criar.

FROM file2

 Especifique o nome da tabela da qual o quick screen deve ser criado com file2. A tabela não precisa estar aberta.

ROW | COLUMN

 Se você incluir ROW, o quick screen é criado com os campos e seus nomes dispostos de cima para baixo. Se você não incluir ROW ou COLUMN, o quick screen usa esse formato por padrão.

 Se você incluir COLUMN, o quick screen é criado com os campos e seus nomes dispostos da esquerda para a direita na tela. Se a largura total dos campos for maior que a largura da tela, os campos podem ser exibidos no formato ROW.

FIELDS field list

 Incluir FIELDS permite especificar os campos da tabela que aparecem no quick screen. Separe os campos na field list com vírgulas.

ALIAS

 Inclua ALIAS para adicionar o alias da tabela aos nomes dos campos no quick screen.

NOOVERWRITE

 NOOVERWRITE impede que uma tela existente seja sobrescrita. Se uma tela já existir com o nome file1, a tela não é criada.

SIZE expN1, expN2

 Você pode designar a altura e a largura da janela incluindo a cláusula SIZE. A altura da janela em linhas é especificada por expN1, a largura da janela em colunas por expN2.

SCREEN

 Incluir SCREEN cria um quick screen que é colocado na janela principal do FoxPro. Esta cláusula permite colocar explicitamente um quick screen na janela principal do FoxPro quando uma janela definida pelo usuário está ativa. Quick screens são colocados na janela principal do FoxPro por padrão.

# Observações

Esta forma de CREATE SCREEN cria um quick screen sem abrir uma janela de layout de tela. A tela é criada como se você escolhesse a opção Quick Screen... enquanto a janela Screen Design está aberta.

Outra forma de CREATE SCREEN, discutida no tópico anterior, abre o Screen Builder para permitir criar interativamente uma tela em uma janela de layout.

Para obter mais informações sobre criação interativa de quick screens, consulte o capítulo "Designing Screens with the Screen Builder" no FoxPro User's Guide.
