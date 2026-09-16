# Método AutoFit

Controla o redimensionamento automático de colunas. AutoFit redimensiona todas as colunas visíveis nos níveis da grade ou da janela browse e redimensiona a coluna individual no nível da coluna.

```foxpro
Object.AutoFit()
```

# Valor de retorno

Tipo de dados Boolean. AutoFit retorna True (.T.) se as colunas forem redimensionadas com êxito e False (.F.) se não forem redimensionadas com êxito.

# Observações

Aplica-se a: Controle Grid | Comando BROWSE | Objeto Column

Você pode usar AllowAutoColumnFit ao criar uma referência de objeto para a janela browse usando a cláusula NAME no comando BROWSE.

Definir a propriedade AllowAutoColumnFit não afeta o redimensionamento realizado por AutoFit nos níveis da grade ou da coluna. Você pode substituir AllowAutoColumnFit usando AutoFit.

Para objetos Column, AutoFit funciona apenas com controles TextBox. Quando uma coluna é redimensionada, o evento Resize dessa coluna é disparado.

Você pode impedir o redimensionamento automático de uma coluna específica definindo a propriedade Resizable dessa coluna como False (.F.).

Colunas ocultas da grade, que têm a propriedade Visible definida como False (.F.) e um valor de propriedade Width de 0, não são redimensionadas.
