# Método CursorAttach

Anexa um cursor existente à instância atual de um objeto CursorAdapter.

```foxpro
CursorAdapter.CursorAttach( [ cAlias [, lInheritCursorProperties ] ] )
```

#### Parâmetros
 **cAlias**
Especifica o alias do cursor ou tabela a ser anexado. Quando cAlias é especificado, CursorAttach preenche a propriedade Alias do CursorAdapter com o alias do cursor ou tabela anexado. Quando cAlias não é especificado, CursorAttach tenta anexar o cursor ou tabela, que deve existir, especificado pelo valor atual da propriedade Alias do CursorAdapter.
**lInheritCursorProperties**
Especifica se você deseja manter ou descartar as propriedades do cursor ou tabela sendo anexado. A tabela a seguir lista os valores possíveis para lInheritCursorProperties . lInheritCursorProperties Description True (.T.) Propriedades existentes definidas para o cursor são herdadas pelas propriedades correspondentes do objeto CursorAdapter. False (.F.) ou vazio Propriedades existentes definidas para o cursor não são copiadas nas propriedades correspondentes do objeto CursorAdapter. Esta opção adiciona flexibilidade quando você está anexando um cursor SQL Pass-Through, Remote View ou outro cursor.

# Valor de retorno

Tipo de dados lógico. CursorAttach retorna True (.T.) se o cursor for anexado com sucesso e False (.F.) se a anexação falhar.

> **Observação:** Para recuperar informações de erro quando CursorAttach retorna False (.F.), você deve chamar a função AERROR( ) Function porque o tratamento de erros do Visual Foxpro, como o comando ON ERROR, o evento Error e o comando TRY...CATCH...FINALLY, não captura essas informações de erro.

# Observações

Aplica-se a: CursorAdapter Class

Um cursor ou tabela pode ter apenas uma instância de um objeto CursorAdapter anexada a ele em um determinado momento.

Quando o Visual FoxPro anexa um cursor, você não pode alterar o cursor ou tabela usando os comandos MODIFY STRUCTURE ou SQL ALTER TABLE.

Chamar CursorAttach fecha o cursor atualmente anexado. Para preservar o cursor atualmente anexado, chame CursorDetach primeiro.

Chamar CursorAttach preenche a propriedade Alias da instância CursorAdapter com o alias do cursor ou tabela anexado.

Chamar CursorAttach ativa BufferModeOverride (3) ou BufferModeOverride (5), dependendo da propriedade BufferModeOverride para o objeto CursorAdapter, se ainda não estiver definida. Se o buffering já estiver ativado, mas for menos granular que Optimistic Row Buffering, o Visual FoxPro promove o buffering para Optimistic Row Buffering.

O Visual FoxPro gera mensagens de erro nas seguintes condições:
 - Se cAlias não puder ser encontrado.
- Se CursorAttach tentar anexar um cursor que já está anexado a outra instância de CursorAdapter .

A propriedade Tables não deve referenciar um cursor que foi anexado a um objeto CursorAdapter por CursorAttach.
