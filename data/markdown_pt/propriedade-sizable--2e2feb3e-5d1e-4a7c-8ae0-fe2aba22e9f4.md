# Propriedade Sizable

Especifica se um objeto pode ser redimensionado. Disponível em tempo de design; leitura/gravação em tempo de execução.

```foxpro
Object.Sizable = lExpr
```

# Valor de retorno
 **lExpr**
As configurações da propriedade Sizable são as seguintes: Configuração Descrição True (.T.) (Padrão) Você pode redimensionar o objeto. False (.F.) Você não pode redimensionar o objeto.

# Observações

Aplica-se a: controle OLE Bound | controle OLE Container | objeto ToolBar

Para controles OLE vinculados e não vinculados, Sizable afeta o objeto OLE que o controle contém. Se Sizable estiver definido como true (.T.) e você ativar o objeto OLE, poderá redimensioná-lo maior ou menor que o controle OLE. Se a propriedade AutoSize estiver definida como true (.T.), o controle OLE redimensiona automaticamente para ajustar-se ao novo tamanho do objeto OLE quando você o desativa.

> **Observação:** Para tornar um Form redimensionável, defina a propriedade BorderStyle como 3.
