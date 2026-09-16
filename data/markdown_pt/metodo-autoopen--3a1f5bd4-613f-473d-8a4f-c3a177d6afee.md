# Método AutoOpen

Executa o método CursorFill com o padrão de nenhum parâmetro. Quando o objeto CursorAdapter existe em um ambiente de dados, o ambiente de dados chama AutoOpen automaticamente a partir do método OpenTables do DataEnvironment.

```foxpro
CursorAdapter.AutoOpen()
```

# Valor de retorno

Tipo de dados Logical. AutoOpen retorna True (.T.) se bem-sucedido. Caso contrário, AutoOpen retorna False (.F.).

> **Observação:** Se AutoOpen falhar, o método OpenTables do DataEnvironment não relata um erro. Para recuperar informações de erro quando AutoOpen retorna False (.F.), você deve chamar a função AERROR( ), pois o tratamento de erros do Visual FoxPro, como o comando ON ERROR, o evento Error e o comando TRY...CATCH...FINALLY, não captura essas informações de erro.

# Observações

Aplica-se a: classe CursorAdapter

Você pode substituir AutoOpen usando o comando NODEFAULT e chamando explicitamente CursorFill.
