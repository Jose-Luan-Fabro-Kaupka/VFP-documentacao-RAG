# Como: permitir que usuários adicionem itens a um List Box

Você pode permitir que os usuários adicionem itens a uma lista interativamente.

### Para permitir que usuários adicionem itens a uma lista interativamente
- Use o método AddItem.

No exemplo a seguir, quando o usuário pressiona ENTER, o código no evento KeyPress de um text box adiciona o texto no text box ao list box e limpa o texto no text box:

```foxpro
LPARAMETERS nKeyCode, nShiftAltCtrl
IF nKeyCode = 13   && Enter Key
   THISFORM.lstAdd.AddItem(This.Value)
   THIS.Value = ""
ENDIF
```

Você pode permitir que os usuários insiram dados em uma tabela a partir de uma lista. Se a propriedade ControlSource estiver definida para um campo, o que o usuário selecionar na lista é gravado na tabela. Esta é uma maneira fácil de ajudar a garantir a integridade dos dados em sua tabela. Embora o usuário ainda possa inserir dados errados, um valor ilegal não pode ser inserido.

Por exemplo, se você tem uma lista de estados ou condados para um usuário escolher, o usuário não pode inserir uma abreviação de estado ou condado inválida.

Você pode permitir que os usuários naveguem até um registro escolhendo um valor de uma lista. Frequentemente, você deseja permitir que os usuários selecionem o registro que desejam visualizar ou editar. Por exemplo, você poderia fornecer aos usuários uma lista de nomes de clientes. Quando o usuário seleciona um cliente da lista, você seleciona o registro desse cliente na tabela e exibe informações do cliente em text boxes no formulário. Você pode fazer isso de várias maneiras, dependendo da fonte de dados em seu formulário.

| RowSourceType | Selecionando o registro apropriado |
| --- | --- |
| 2 - Alias 6 - Fields | Quando o usuário escolhe um valor na lista, o ponteiro de registro é definido automaticamente para o registro desejado. Emita THISFORM.Refresh no evento InteractiveChange da lista para mostrar os novos valores em outros controles no formulário. |
| 0 - None 1 - Value 3 - SQL Statement 4 - QPR 5 - Array | No evento InteractiveChange, selecione a tabela que tem o registro com os valores desejados e, em seguida, pesquise o valor desejado. Por exemplo, se o RowSource contém números de identificação de clientes da tabela customer, use este código: SELECT customer LOCATE FOR THIS.Value = cust_id THISFORM.Refresh |
