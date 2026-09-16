# Comando DISPLAY CONNECTIONS

Exibe informações sobre as conexões nomeadas no banco de dados atual.

```foxpro
DISPLAY CONNECTIONS [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **TO PRINTER [PROMPT]**
Direciona a saída de DISPLAY CONNECTIONS para uma impressora. No Visual FoxPro, você pode incluir a cláusula opcional PROMPT para exibir uma caixa de diálogo Print antes do início da impressão. Coloque PROMPT imediatamente após TO PRINTER.
**TO FILE FileName**
Direciona a saída de DISPLAY CONNECTIONS para o arquivo especificado com FileName. Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro exibe um prompt perguntando se você deseja sobrescrever o arquivo.
**ADDITIVE**
Anexa ao final do arquivo nomeado. Se você omitir ADDITIVE, o arquivo é sobrescrito com o valor da expressão.
**NOCONSOLE**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

DISPLAY CONNECTIONS exibe os nomes das conexões, a fonte de dados e a cadeia de conexão no banco de dados atual. Use DBGETPROP( ) para retornar informações adicionais sobre conexões no banco de dados atual.

# Exemplo

O exemplo a seguir assume que uma fonte de dados ODBC chamada MyFoxSQLNT está disponível. O banco de dados `testdata` é aberto e uma conexão chamada `Myconn` é criada. DISPLAY CONNECTIONS é usado para exibir as conexões nomeadas no banco de dados.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
CREATE CONNECTION Myconn DATASOURCE "MyFoxSQLNT" USERID "<userid>" PASSWORD "<password>"
CLEAR
DISPLAY CONNECTIONS     && Displays named connections in the database
```
