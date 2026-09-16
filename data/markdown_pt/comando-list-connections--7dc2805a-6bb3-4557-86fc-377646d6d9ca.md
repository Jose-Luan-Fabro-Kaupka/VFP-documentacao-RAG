# Comando LIST CONNECTIONS

Exibe continuamente informações sobre as conexões nomeadas no banco de dados atual.

```foxpro
LIST CONNECTIONS [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]]   [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de LIST CONNECTIONS para uma impressora. No Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo Print antes do início da impressão. Coloque PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de LIST CONNECTIONS para o arquivo especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se deseja substituir o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é substituído pelo valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

As informações exibidas incluem os nomes das conexões nomeadas, fontes de dados e cadeias de conexão no banco de dados atual. Use DBGETPROP( ) para retornar informações adicionais sobre conexões no banco de dados atual.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. O banco de dados `testdata` é aberto e uma conexão chamada `Myconn` é criada. LIST CONNECTIONS é usado para listar as conexões nomeadas no banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
CREATE CONNECTION Myconn DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
CLEAR
LIST CONNECTIONS     && Lists named connections in the database
```
