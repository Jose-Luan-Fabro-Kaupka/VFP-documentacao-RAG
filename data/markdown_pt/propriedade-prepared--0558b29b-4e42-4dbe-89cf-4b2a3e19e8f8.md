# Propriedade Prepared

Especifica se as instruções SQL devem ser preparadas para chamadas subsequentes da função REQUERY( ). Você pode usar REQUERY( ) para recuperar novamente os dados de uma exibição SQL. Para cursores comuns, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** A definição de Prepared em objetos CursorAdapter substitui a configuração da propriedade de um cursor quando ele é anexado ao CursorAdapter. Portanto, alterar o cursor com CURSORSETPROP( ) não tem efeito.

Para obter mais informações, consulte as funções REQUERY( ) e SQLPREPARE( ).

```foxpro
CursorAdapter.Prepared [= lValue]
```

# Valor de retorno
 **lValue**
Tipo de dados Logical. Verdadeiro (.T.) prepara as instruções SQL para chamadas subsequentes de REQUERY( ) (padrão). Falso (.F.) não prepara as instruções.

# Observações

Aplica-se a: classe CursorAdapter
