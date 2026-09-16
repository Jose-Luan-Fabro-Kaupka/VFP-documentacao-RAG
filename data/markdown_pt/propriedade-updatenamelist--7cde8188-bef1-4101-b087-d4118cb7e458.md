# Propriedade UpdateNameList

Especifica uma lista delimitada por vírgulas consistindo em pares de nomes de campos locais e remotos completos. Cada par de nomes consiste em um nome de campo local seguido do nome de campo remoto completo. O nome de campo remoto completo aparece como <remote table name>.<remote field name>, onde <remote table name> corresponde ao nome da propriedade Tables. Leitura/gravação.

> **Observação:** Definir UpdateNameList para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

> **Observação:** Você deve definir UpdateNameList, que também pode ser usado para especificar nomes válidos do Visual FoxPro para campos no cursor que têm nomes de campo inválidos do Visual FoxPro.

Ao trabalhar com esta propriedade para cursores regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ).

```foxpro
CursorAdapter.UpdateNameList [= cList]
```

# Valor de retorno
 **cList**
Tipo de dados Character. O parâmetro cList especifica uma lista delimitada por vírgulas consistindo em pares de nomes de campos locais e remotos completos.

# Observações

Aplica-se a: Classe CursorAdapter
