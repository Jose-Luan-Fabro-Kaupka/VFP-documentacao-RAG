# Evento AfterBuild

Ocorre depois que um projeto é recompilado ou que um arquivo de aplicativo (.app), uma biblioteca de vínculo dinâmico (.dll) ou um arquivo executável (.exe) é criado a partir de um projeto.

```foxpro
PROCEDURE Object.AfterBuild
LPARAMETERS nError
```

#### Parâmetros
**nError**
O número de erro do Visual FoxPro retornado depois que o projeto é recompilado ou que um arquivo .app, .dll ou .exe é criado. Se nError for 0, nenhum erro ocorreu durante a recompilação do projeto ou a criação do arquivo .app, .dll ou .exe.

# Observações

Aplica-se a: objeto ProjectHook
