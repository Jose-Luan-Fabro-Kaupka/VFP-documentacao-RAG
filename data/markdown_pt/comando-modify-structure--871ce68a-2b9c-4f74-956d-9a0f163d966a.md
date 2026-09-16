# Comando MODIFY STRUCTURE

Exibe o Table designer, permitindo modificar a estrutura de uma tabela.

```foxpro
MODIFY STRUCTURE
```

# Observações

Em versões anteriores do FoxPro, MODIFY STRUCTURE abre a caixa de diálogo Table Structure.

Se uma tabela não estiver aberta na área de trabalho atualmente selecionada, a caixa de diálogo Open é exibida, permitindo escolher uma tabela para modificar.

As alterações que você pode fazer na estrutura de uma tabela incluem adicionar e excluir campos; modificar nomes, tamanhos e tipos de dados de campos; adicionar, excluir ou modificar tags de índice; e especificar suporte a valores nulos para campos.

> **Cuidado:** Alterar um campo de um tipo de dados para outro pode não transferir o conteúdo do campo corretamente, ou de forma alguma. Por exemplo, se você converter um campo do tipo data para um tipo numérico, o conteúdo do campo não é transferido.

O Visual FoxPro faz automaticamente uma cópia de backup da tabela atual antes de você alterar a estrutura da tabela. Quando as modificações são concluídas, os dados contidos na cópia de backup da tabela são anexados à estrutura de tabela recém-modificada. Se a tabela tem um campo memo, um arquivo de backup de memo também é criado. O arquivo de backup da tabela tem extensão .bak, e o arquivo de backup de memo tem extensão .tbk.

Se você aceitar as alterações de estrutura e depois interromper o processo de cópia de dados, o novo arquivo não conterá todos os registros da tabela original.

Lembre-se de que o Visual FoxPro cria um arquivo .bak para o arquivo de tabela original e, se a tabela tem um campo memo, uma cópia .tbk do arquivo de memo original. Se você tiver problemas com MODIFY STRUCTURE, pode excluir o(s) novo(s) arquivo(s) e renomear o arquivo .bak e o arquivo .tbk, se houver, para as extensões de arquivo originais (.dbf e .fpt).

Quando você modifica a estrutura de uma tabela que tem um campo memo, o blocksize do arquivo de memo é definido para a configuração atual de blocksize. Você pode especificar o blocksize do arquivo de memo com SET BLOCKSIZE.
