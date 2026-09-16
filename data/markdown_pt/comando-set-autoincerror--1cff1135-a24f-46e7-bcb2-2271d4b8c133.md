# Comando SET AUTOINCERROR

Especifica se tentativas de atualizar ou inserir valores em um campo com valores incrementados automaticamente geram erros.

> **Observação:** Um cursor herda a configuração atual de SET AUTOINCERROR quando é aberto. Alterá-la durante uma sessão não afeta cursores já abertos. Para alterar um cursor aberto, use CURSORSETPROP( ).

```foxpro
SET AUTOINCERROR ON | OFF
```

#### Parâmetros
 **ON**
Gera um erro ao atualizar ou inserir um valor em um campo com incremento automático. ON é o padrão para sessões de dados globais ou privadas.
**OFF**
Não gera erro e ignora o valor especificado para o campo, usando o valor incrementado apropriado.

# Observações

OFF oferece maior utilidade com tabelas que contêm campos de incremento automático em operações como APPEND FROM e INSERT INTO, nas quais, de outra forma, seria necessário especificar uma lista de campos e omitir os campos com incremento automático.

SET AUTOINCERROR tem escopo de sessão de dados.
