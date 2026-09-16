# Evento dbc_AfterModifyConnection

Ocorre após uma conexão ser modificada. Existem duas versões da sintaxe.

```foxpro
PROCEDURE dbc_AfterModifyConnection(cConnectionName, lChanged)
```

```foxpro
PROCEDURE dbc_AfterModifyConnection
LPARAMETERS cConnectionName, lChanged
```

#### Parâmetros
 **cConnectionName**
Especifica o nome da conexão modificada.
**lChanged**
Especifica se uma modificação na visualização foi salva no Designer de Conexões.

# Observações

Você pode usar o evento dbc AfterModifyView para rastrear ou gerenciar o acesso ao banco de dados após as conexões serem modificadas.

# Veja Também
- Como: Activar ou Desactivar DBC Eventos
- dbc BeforeModifyConnection Event
- Eventos (Visual FoxPro)
