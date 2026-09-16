# Comando CREATE

Abre o Table Designer para que você possa criar uma tabela do Visual FoxPro.

```foxpro
CREATE [FileName | ?]
```

#### Parâmetros
**[ FileName | ?]**
Especifica o nome da tabela a criar ou abre a caixa de diálogo Create, na qual você pode procurar um local para salvar a tabela e especificar seu nome.

# Observações

Se um banco de dados estiver aberto quando você criar uma tabela, ela será adicionada automaticamente ao banco de dados.

Ao executar no sistema operacional Windows, não é possível criar uma tabela com o nome de um dispositivo MS-DOS, como CON, NUL, PRN e COM1. Evite usar hifens no nome de uma tabela, pois nomes com hifens não aparecem na janela Data Session e podem ser confundidos com o ponteiro de alias (->).

Depois de abrir o Table Designer, você deve definir os atributos dos campos da tabela. Após criar a estrutura, poderá adicionar registros à tabela. Para obter mais informações, consulte Criando tabelas.

O comando SQL CREATE TABLE permite especificar campos e seus atributos programaticamente. Para obter mais informações, consulte Comando CREATE TABLE - SQL.
