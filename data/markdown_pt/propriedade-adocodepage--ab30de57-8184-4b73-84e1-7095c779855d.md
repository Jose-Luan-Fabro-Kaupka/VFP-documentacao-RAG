# Propriedade ADOCodePage

Especifica um code page para o objeto CursorAdapter usar durante a tradução de dados de caractere ao trabalhar com dados ADO. Leitura/gravação em tempo de design e em tempo de execução.

```foxpro
CursorAdapter.AllowInsert [ = nCodePage ]
```

# Valor de retorno
 **nCodePage**
O code page (inteiro) a usar para tradução de dados de caractere ao usar fontes de dados ADO. Ocorrerá um erro se você tentar definir um code page inválido. A configuração padrão é 0.

# Observações

Aplica-se a: CursorAdapter Class

O code page especificado pela propriedade ADOCodePage é usado para traduzir os seguintes comandos:
 - Select
- Insert
- Update
- Delete
- ConflictCheck
- InsertRefresh
- UpdateRefresh
- Refresh
- FetchMemo

Também é usado com todos os parâmetros de caractere passados para e da fonte de dados ADO.

Após uma chamada do método CursorFill Method ou CursorRefresh Method, o cursor aberto torna-se vinculado ao code page especificado pela propriedade ADOCodePage no momento em que o cursor é preenchido ou atualizado. Isso significa que, independentemente da configuração atual de ADOCodePage, todos os dados de caractere buscados da fonte de dados são traduzidos usando o code page vinculado. Isso inclui o processo normal de busca, busca durante auto-refresh, refresh sob demanda e busca de memo atrasada.

Você só pode vincular um code page (conforme especificado por ADOCodePage) a um cursor baseado em ADO. No entanto, ADOCodePage ainda pode ser usado com cursors não baseados em ADO. Quando um cursor não baseado em ADO é anexado a um objeto CursorAdapter, a configuração ADOCodePage é usada para traduzir dados de caractere buscados durante auto-refresh, refresh sob demanda e busca de memo atrasada.

Um cursor pode ser revinculado a um code page diferente alterando a propriedade ADOCodePage e executando o método CursorRefresh Method.

Você pode recuperar o code page associado a um cursor baseado em ADO passando "ADOCodePage" como parâmetro para a função CURSORGETPROP( ).

Se um code page diferente de 0 é usado para traduzir um parâmetro e o CursorAdapter cria o parâmetro (o método Parameters.Refresh falha ao criá-lo), o parâmetro é criado como adVarWChar/adLongVarWChar em vez de adVarChar/adLongVarChar.
