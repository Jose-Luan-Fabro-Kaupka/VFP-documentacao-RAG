# Evento dbc_AfterModifyView

Ocorre depois de uma visualização ter sido modificada. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterModifyView(cViewName, lChanged)
```

```foxpro
PROCEDURE dbc_AfterModifyView
LPARAMETERS cViewName, lChanged
```

#### Parâmetros
 **cViewName**
Especifica o nome da visualização modificada.
**lChanged**
Especifica se uma modificação foi salva no View Designer.

# Observações

Você pode usar o evento dbc AfterModifyView para rastrear as alterações em um banco de dados, pois as visualizações são modificadas.

# Veja Também
- Como: Activar ou Desactivar DBC Eventos
- dbc BeforeModifyView Event
- Eventos (Visual FoxPro)
