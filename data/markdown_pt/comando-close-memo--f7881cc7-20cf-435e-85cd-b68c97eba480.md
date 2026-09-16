# Comando CLOSE MEMO

Fecha uma ou mais janelas de edição de memo.

```foxpro
CLOSE MEMO MemoFieldName1 [, MemoFieldName2 ...] | ALL
```

#### Parâmetros
 **MemoFieldName1 [, MemoFieldName2 ...]**
Especifica o nome do campo memo cuja janela de edição de memo você deseja fechar. Para fechar um conjunto de janelas de edição de memo, inclua uma lista de nomes de campos memo separados por vírgulas. Você pode fechar a janela de edição de memo de um campo memo em uma tabela aberta em outra área de trabalho incluindo o alias da tabela.
**ALL**
Fecha todas as janelas de edição de memo de todos os campos memo em quaisquer tabelas abertas.

# Observações

CLOSE MEMO fecha janelas de edição de memo abertas com MODIFY MEMO ou abertas a partir de uma janela Browse ou Edit. CLOSE MEMO salva quaisquer alterações feitas nos campos memo.

Fechar uma tabela que contém o campo ou campos memo também salva quaisquer alterações feitas e fecha as janelas de memo.
