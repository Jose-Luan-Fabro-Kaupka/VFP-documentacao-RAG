# Propriedade AutoComplete

Especifica que a caixa de texto rastreia valores inseridos anteriormente e os disponibiliza em uma lista dinâmica de entradas sugeridas. Leitura/gravação em tempo de design e execução.

```foxpro
Textbox.AutoComplete [ = nValue]
```

# Valor de retorno
 **nValue**
Tipo de dados Integer. A tabela a seguir lista os valores para nValue. nValue Setting 0 Não exibe uma lista de entradas. 1 Alphabetical Ordena entradas alfabeticamente e não diferencia maiúsculas de minúsculas. 2 Most Frequently Used (MFU) Ordena entradas com base na contagem mais alta. 3 Most Recently Used Ordena entradas com base no campo Updated na tabela de origem com as mais recentes primeiro. 4 Custom Usa o campo Weight preenchido usando seu próprio algoritmo para especificar como deseja que as entradas sejam ordenadas. Os resultados são ordenados em ordem decrescente (do maior para o menor valor). Em caso de empate, o campo Updated é usado (a mais recente aparece primeiro).

# Observações

Aplica-se a: TextBox Control (Visual FoxPro)

Defina a propriedade AutoComplete para fornecer uma caixa de texto que armazena e sugere valores automaticamente. À medida que os caracteres são digitados, uma lista suspensa exibe palavras inseridas recentemente que correspondem ao padrão dos caracteres digitados. Quando o usuário seleciona uma entrada da lista, o valor da caixa de texto torna-se igual a essa entrada e atualiza as informações de uso dessa entrada em Autocomp.dbf ou outra tabela que você tenha especificado.

Para mais informações sobre como os dados são armazenados, consulte AutoCompTable Property.

Se você usar a opção de ordenação personalizada (4), precisa definir a ordem ponderada atualizando o campo Weight na tabela AutoComplete, que está reservado para seu uso. Por exemplo, você pode especificar código no evento Valid da caixa de texto que atualiza o campo Weight com base na frequência de tempo em que entradas mais recentes recebem um valor de peso maior.

Se você deseja controlar o número de itens que aparecem na lista dinâmica, pode definir a opção List Display Count na caixa de diálogo Options. Você também pode especificar esta configuração com SYS(2910) - List Display Count.
