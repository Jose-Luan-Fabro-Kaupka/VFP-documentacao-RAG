# Controle TextBox (Visual FoxPro)

Cria uma caixa de texto.

```foxpro
TextBox
```

# Observações

Uma caixa de texto permite editar uma variável de memória, elemento de array ou campo. Em um Grid, ela pode exibir um campo Blob somente para leitura. Campos Blob vazios mostram "blob"; com dados, mostram "Blob". Clique duas vezes para exibir os dados em uma janela de leitura.

Todos os recursos padrão de edição estão disponíveis, exceto durante a exibição de dados Blob.

> **Dica:** Ao editar um valor Date ou DateTime inteiramente selecionado, pressione MAIS (+) ou MENOS (-) para avançar ou retroceder um dia.

Use InputMask e Format para definir como os valores são inseridos e exibidos. Use AutoComplete para habilitar o preenchimento automático.

| Propriedade | Descrição |
| --- | --- |
| Alignment | Especifica o alinhamento do conteúdo. |
| ControlSource | Especifica o campo ou variável exibido. |
| InputMask | Especifica a regra de entrada de cada caractere. |
| SelectOnEntry | Determina se o conteúdo é selecionado ao receber o foco. |
| TabStop | Especifica se o usuário pode alcançar o controle com TAB. |
