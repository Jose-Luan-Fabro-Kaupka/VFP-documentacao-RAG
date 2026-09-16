# Objeto Project (Visual FoxPro)

Instanciado quando um projeto é criado ou aberto, fornecendo acesso programático a propriedades e métodos do projeto.

```foxpro
Project
```

# Observações

Um objeto project é instanciado quando você emite o comando CREATE PROJECT, MODIFY PROJECT, BUILD APP, BUILD DLL, BUILD EXE, BUILD MTDLL ou BUILD PROJECT.

Observe que o objeto project e suas propriedades e métodos não estão disponíveis no evento Init do objeto ProjectHook. Valores de propriedades do objeto project que você define ou métodos que você invoca no evento Init do objeto ProjectHook são ignorados.

Observe que um objeto project é um objeto COM, portanto, atribuir uma referência de objeto project a uma variável de memória cria uma variável de memória da classe "Unknown Type."

Para obter mais informações sobre projetos, consulte Project Manager Hooks.
