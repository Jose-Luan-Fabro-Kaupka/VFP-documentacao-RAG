# Comando CREATE TRIGGER

Cria um gatilho Delete, Insert ou Update para uma tabela.

```foxpro
CREATE TRIGGER ON TableName   FOR DELETE | INSERT |
UPDATE AS lExpression
```

#### Parâmetros
 **TableName**
Especifica a tabela do banco de dados atual para a qual um gatilho será criado.
**FOR DELETE | INSERT | UPDATE**
Especifica o tipo de gatilho criado pelo Visual FoxPro. Se já existir um gatilho desse tipo e SET SAFETY estiver ON, o Visual FoxPro perguntará se ele deve ser substituído. Se SET SAFETY estiver OFF, ele será substituído automaticamente.
**AS lExpression**
Especifica a expressão lógica avaliada quando o gatilho ocorre. lExpression pode ser uma função definida pelo usuário ou um procedimento armazenado que retorne um valor lógico. Procedimentos armazenados são criados para uma tabela com MODIFY PROCEDURE. Uma função ou procedimento pode usar AERROR( ) para determinar o nome da tabela e o tipo de gatilho. Se lExpression for verdadeiro (.T.), o comando ou evento causador será executado. Se for falso (.F.), ele não será executado. Se houver um procedimento ON ERROR ativo, ele será executado; caso contrário, o Visual FoxPro gerará uma mensagem de erro.

# Observações

Use CREATE TRIGGER para capturar eventos que excluem, adicionam ou alteram registros. Gatilhos Delete, Insert ou Update só podem ser criados para tabelas adicionadas a um banco de dados. Use CREATE DATABASE para criar o banco e ADD TABLE para adicionar a tabela.

A tabela a seguir descreve os eventos que causam cada gatilho.

| Evento | Resultado |
| --- | --- |
| Gatilho Delete | DELETE é emitido. Um registro é marcado para exclusão pelo menu Table em uma janela Browse ou Edit. ZAP não dispara o gatilho Delete. |
| Gatilho Insert | APPEND FROM, APPEND FROM ARRAY ou APPEND BLANK é emitido; um registro é acrescentado pelo menu Table; IMPORT, INSERT – SQL ou RECALL é emitido; ou um registro é recuperado pelo menu Table. |
| Gatilho Update | GATHER, REPLACE, REPLACE FROM ARRAY ou UPDATE – SQL é emitido, ou outro evento modifica um registro, como um formulário alterando um campo. INSERT não pode ser emitido para uma tabela com gatilho, mas INSERT – SQL pode ser usado. PACK não dispara gatilhos; ZAP não dispara Delete; e nenhum gatilho ocorre ao atualizar um registro marcado para exclusão. Dependendo do modo de buffer, o gatilho pode não ocorrer imediatamente. |

Se o buffer de tabela estiver ativo, o gatilho Update ocorrerá quando TABLEUPDATE( ) for emitido e cada registro em buffer for atualizado na tabela.

> **Observação:** Quando um gatilho é chamado, o Alias é sempre o do cursor que está sendo atualizado, independentemente do Alias selecionado no código que disparou o gatilho.

# Exemplo

O exemplo a seguir cria um gatilho Update que impede a inserção de valores maiores que 50 no campo `maxordamt` da tabela `customer`. O primeiro comando REPLACE gera erro porque o valor é maior que 50. O segundo não gera erro porque o valor é menor ou igual a 50.

```foxpro
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'data\testdata')
USE customer  && Open customer table
* Set trigger on maxordamt field to fail with values <= 50
CREATE TRIGGER ON customer FOR UPDATE AS maxordamt <= 50
ON ERROR  && Restore the system error handler
WAIT WINDOW "Press a key to test trigger with value of 60"+CHR(13);
 +"When you get the error message, press Ignore."
REPLACE maxordamt WITH 60    && Displays an error message
? maxordamt
WAIT WINDOW "Press a key to test with value of 50."
REPLACE maxordamt WITH 50    && Value is accepted
? maxordamt
DELETE TRIGGER ON customer FOR UPDATE  && Remove the trigger
```
