# Comando LIST DATABASE

Exibe continuamente informações sobre o banco de dados atual.

```foxpro
LIST DATABASE [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de LIST DATABASE para uma impressora. No Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo Print antes do início da impressão. Coloque PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de LIST DATABASE para o arquivo especificado com FileName . Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

Use DBGETPROP( ) para retornar informações adicionais sobre o banco de dados atual.

# Exemplo

Este exemplo cria um banco de dados chamado `people`. Uma tabela chamada `friends` é criada e adicionada automaticamente ao banco de dados. DISPLAY TABLES é usado para exibir as tabelas no banco de dados, e LIST DATABASES é usado para listar informações sobre as tabelas no banco de dados.

```foxpro
CREATE DATABASE people
CREATE TABLE friends (FirstName C(20), LastName C(20))
CLEAR
DISPLAY TABLES  && Displays tables in the database
LIST DATABASE  && Lists table information
```
