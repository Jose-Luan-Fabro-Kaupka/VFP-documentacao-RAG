# Como: retornar vários conjuntos de resultados

Se você executar um procedimento armazenado que contenha instruções SELECT com sintaxe nativa do servidor, cada conjunto de resultados é retornado a um cursor Visual FoxPro separado. Você pode usar esses cursores para retornar valores ou parâmetros de um procedimento armazenado em um servidor remoto para o cliente Visual FoxPro.

### Para retornar vários conjuntos de resultados
- Use a função SQLEXEC( ) para selecionar vários conjuntos de resultados usando a sintaxe nativa do servidor.

Por exemplo, o código a seguir cria e executa um procedimento armazenado SQL em um servidor remoto, `my_procedure`, que retorna três cursores Visual FoxPro: `sqlresult`, `sqlresult1` e `sqlresult2`:

```foxpro
=SQLEXEC(nConnectionHandle,'create procedure my_procedure as ;
      select * from sales; select * from authors;
      select * from titles')
=SQLEXEC(nConnectionHandle,'execute my_procedure')
```

A função SQLEXEC( ) permite enviar uma instrução SQL à origem de dados sem interpretação. No caso mais simples, qualquer cadeia de caracteres que você incluir no segundo parâmetro da função SQLEXEC( ) é passada à origem de dados sem interpretação. Isso permite executar qualquer instrução usando o SQL nativo da origem de dados.

Você também pode usar a função SQLEXEC( ) para criar uma consulta parametrizada ou passar extensões ODBC para SQL à origem de dados.
