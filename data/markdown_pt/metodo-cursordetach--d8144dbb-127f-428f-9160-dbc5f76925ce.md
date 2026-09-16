# Método CursorDetach

Libera o cursor atualmente anexado da instância atual de CursorAdapter.

```foxpro
CursorAdapter.CursorDetach()
```

# Valor de retorno

Tipo de dados lógico. CursorDetach retorna True (.T.) se o cursor for desanexado com sucesso e False (.F.) se não for desanexado com sucesso.

> **Observação:** Para recuperar informações de erro quando CursorDetach retorna False (.F.), você deve chamar a função AERROR( ) porque o tratamento de erros do Visual FoxPro, como o comando ON ERROR, o evento Error e o comando TRY...CATCH...FINALLY, não captura essas informações de erro.

# Observações

Aplica-se a: classe CursorAdapter

O Visual FoxPro preserva todas as configurações, como buffering e assim por diante, disponíveis para um cursor normal no cursor liberado.

O Visual FoxPro preserva todas as alterações não salvas. Por exemplo, você não precisa chamar a função TABLEUPDATE antes de desanexar o cursor.
