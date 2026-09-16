# Bandeiras Propriedade (Visual FoxPro)

Especifica as configurações da bandeira para o CursorAdapter conforme descrito pelo parâmetro nFlags em XMLUPDATEGRAM( ) Função. Ler/escrever no tempo de projeto e executar o tempo.

> **Note:** Flags applies only when the CursorAdapter DataSourceType Property is set to "XML". The CursorAdapter object passes flags specified by the Flags property when constructing an XML UpdateGram. The CursorAdapter object evaluates Flags only once per update operation.

```foxpro
CursorAdapter.Flags [= nFlags]
```

# Valor de Retorno
 **nFlags**
Integer data type. The nFlags parameter specifies nFlag settings from the XMLUPDATEGRAM( ) function and has a default value of 0.

Observações

Aplica-se a: Classe CursorAdapter

Veja também
- Propriedades, Métodos e Eventos do CursorAdapter Object
- UpdateGram Property
- Properties (Visual FoxPro)
