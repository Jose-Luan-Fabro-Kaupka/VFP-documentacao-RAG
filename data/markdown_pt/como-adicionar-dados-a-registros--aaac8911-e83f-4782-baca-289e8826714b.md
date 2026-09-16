# Como: adicionar dados a registros

Você pode adicionar dados a registros após criar registros em branco ou substituir dados em registros existentes. Você também pode editar cada campo em um registro em uma linha separada trabalhando com a tabela no modo de edição. Para obter mais informações, consulte How to: Add Records to Tables.

### Para adicionar ou substituir dados em registros
- Abra a tabela em uma janela de browse. Dica Para visualizar cada campo em uma linha separada, no menu View, clique em Edit .
- Na tabela, insira o cursor no campo do registro desejado e digite os dados apropriados para o tipo de dados do campo.

Para obter mais informações, consulte How to: View Records in Tables.

### Para armazenar dados em registros programaticamente
- Escolha uma das seguintes opções: Se o registro em branco que você adicionou é o registro atual, siga o comando APPEND BLANK com o comando REPLACE e especifique o registro no qual substituir valores. Dica Por padrão, REPLACE substitui valores em campos, incluindo campos vazios para o registro atual. Ao usar REPLACE , certifique-se de que a tabela está aberta, que o registro existe, que você especifica o campo no qual deseja armazenar valores e um valor para cada campo que é apropriado para o tipo de dados do campo. -OU- Abra a tabela, depois use os comandos EDIT ou CHANGE para exibir a tabela no modo de edição. -OU- Use o comando SQL UPDATE para atualizar registros em uma tabela.

Para obter mais informações, consulte REPLACE Command (Visual FoxPro), EDIT Command, CHANGE Command e UPDATE - SQL Command.

> **Dica:** Quando você usa o comando REPLACE ou o comando SQL UPDATE em uma aplicação multiusuário, pode editar dados sem bloquear o registro até que deseje confirmar as alterações ativando o buffer de registro ou tabela. Para obter mais informações, consulte Programming for Shared Access .

### Adicionar valores nulos a registros

Você pode digitar valores nulos para campos em registros.

> **Observação:** Para especificar o texto exibido para valores nulos, use o comando SET NULLDISPLAY. Para obter mais informações, consulte SET NULLDISPLAY Command .

### Para armazenar um valor nulo em um campo
- Abra a tabela em uma janela de browse.
- Na tabela, insira o cursor no campo do registro desejado e pressione CTRL+0 (zero).

### Para armazenar um valor nulo em um campo programaticamente
- Inclua a palavra-chave NULL com o comando que você usa para adicionar ou substituir dados.
