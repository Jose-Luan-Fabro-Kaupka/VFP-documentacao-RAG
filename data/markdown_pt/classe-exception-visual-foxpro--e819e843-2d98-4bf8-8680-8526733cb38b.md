# Classe Exception (Visual FoxPro)

Quando ocorre um erro no bloco TRY dentro de uma estrutura de tratamento de erros TRY...CATCH...FINALLY, o Visual FoxPro cria automaticamente um objeto Exception e usa a variável de memória VarName especificada na cláusula CATCH TO para armazenar uma referência à exceção. O comando THROW também gera um objeto Exception. No entanto, se nenhuma estrutura TRY...CATCH...FINALLY capturar a exceção lançada, o Visual FoxPro encaminha a exceção para outro manipulador de erros ou para o manipulador de erros global do Visual FoxPro.

Você pode definir e criar subclasses da classe Exception.

```foxpro
Exception
```

# Observações

O Visual FoxPro suporta a classe Exception apenas em arquivos de programa (.prg).

Objetos Exception não oferecem suporte a todas as várias informações de erro, incluindo Component Object Model (COM), Open Database Connectivity (ODBC) e triggers de banco de dados, que você normalmente pode obter com a função AERROR( ). No entanto, você pode acessar as informações de AERROR( ) dentro do bloco TRY...CATCH.

# Exemplo

```foxpro
oError = CREATEOBJECT("exception")
```
