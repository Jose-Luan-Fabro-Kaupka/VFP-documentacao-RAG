# Comando DISPLAY DATABASE

Exibe informações sobre o banco de dados atual.

```foxpro
DISPLAY DATABASE [TO PRINTER [PROMPT] | TO FILE FileName [ADDITIVE]] [NOCONSOLE]
```

#### Parâmetros
 **[TO PRINTER [PROMPT]**
Direciona a saída sobre o banco de dados atual para uma impressora. A cláusula de palavra-chave PROMPT exibe uma caixa de diálogo Imprimir antes do início da impressão.
**TO FILE FileName [ADDITIVE]]**
Direciona a saída para um arquivo especificado por FileName . Se o arquivo já existir e SET SAFETY estiver ON, o Visual FoxPro solicita que você decida se deseja substituir o arquivo. A palavra-chave ADDITIVE anexa a saída ao final do arquivo especificado. Se você omitir ADDITIVE, o conteúdo do arquivo é substituído.
**[NOCONSOLE]**
Suprime a saída para a janela principal do Visual FoxPro ou para a janela definida pelo usuário ativa.

# Observações

Para retornar informações adicionais sobre o banco de dados atual, use a função DBGETPROP( ). Para obter mais informações, consulte Função DBGETPROP( ).

# Exemplo

O exemplo a seguir cria um banco de dados chamado `people`. Uma tabela chamada `friends` é criada e adicionada automaticamente ao banco de dados. DISPLAY TABLES é usado para exibir as tabelas no banco de dados, e DISPLAY DATABASES é usado para exibir informações sobre as tabelas no banco de dados.

```foxpro
CREATE DATABASE people
CREATE TABLE friends (FirstName C(20), LastName C(20))
CLEAR
DISPLAY TABLES  && Displays tables in the database
DISPLAY DATABASES  && Displays table information
```
