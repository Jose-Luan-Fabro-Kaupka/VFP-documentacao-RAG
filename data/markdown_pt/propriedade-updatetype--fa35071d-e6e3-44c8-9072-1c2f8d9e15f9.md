# Propriedade UpdateType

Especifica o que fazer com dados antigos ao executar atualizações. Ao trabalhar com esta propriedade para cursors regulares, use as funções CURSORSETPROP( ) e CURSORGETPROP( ). Leitura/gravação.

> **Observação:** Definir UpdateType para objetos CursorAdapter substitui a configuração da propriedade de um cursor quando anexado a um objeto CursorAdapter. Ou seja, alterar as configurações no cursor usando CURSORSETPROP() não tem efeito.

```foxpro
CursorAdapter.UpdateType [= nValue]
```

# Valor de retorno
 **nValue**
Tipo de dados numérico. A tabela a seguir lista os valores para nValue. nValue Descrição 1 Atualizar dados antigos com novos dados. (Padrão) 2 Excluir dados antigos e inserir novos dados.

# Observações

Aplica-se a: Classe CursorAdapter
