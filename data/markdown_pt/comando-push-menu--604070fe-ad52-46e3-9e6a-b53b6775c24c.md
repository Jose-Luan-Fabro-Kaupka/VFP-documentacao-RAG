# Comando PUSH MENU

Coloca uma definição de barra de menu em uma pilha de definições de barra de menu na memória.

```foxpro
PUSH MENU MenuBarName
```

#### Parâmetros
 **MenuBarName**
Especifica o nome da barra de menu cuja definição é colocada na pilha. A barra de menu pode ser definida pelo usuário ou a barra de menu do sistema do Visual FoxPro.

# Observações

Quando usado com POP MENU, PUSH MENU permite salvar uma definição de barra de menu, fazer alterações na definição da barra de menu e depois restaurar a definição da barra de menu ao seu estado original.

As definições de barra de menu são colocadas na pilha e removidas dela na ordem último a entrar, primeiro a sair. As definições de menu ocupam memória; portanto, todo PUSH MENU deve ter um POP MENU correspondente para garantir que o uso de memória do seu aplicativo não cresça desnecessariamente.

# Exemplo

No exemplo a seguir, a barra de menu do sistema do Visual FoxPro é colocada na pilha e depois modificada. A barra de menu do sistema original é então restaurada removendo-a da pilha.

```foxpro
WAIT WINDOW 'Press a key to push the system menu bar'
PUSH MENU _MSYSMENU
WAIT WINDOW 'Press a key to change the system menu bar'
SET SYSMENU TO _MFILE, _MEDIT
WAIT WINDOW 'Press a key to restore the system menu bar'
POP MENU _MSYSMENU
```
