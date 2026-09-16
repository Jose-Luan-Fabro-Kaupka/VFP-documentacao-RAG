# Comando POP MENU

Restaura a definição de barra de menus especificada que foi colocada na pilha com PUSH MENU.

```foxpro
POP MENU MenuBarName [TO MASTER]
```

#### Parâmetros
 **MenuBarName**
Especifica o nome da barra de menus cuja definição é retirada da pilha. A barra de menus especificada pode ser definida pelo usuário ou a barra de menus do sistema Visual FoxPro.
**TO MASTER**
Restaura a primeira definição de barra de menus empurrada na pilha e, em seguida, limpa a pilha.

# Observações

Quando usado com PUSH MENU, POP MENU permite salvar uma definição de barra de menus, fazer alterações na definição da barra de menus e, em seguida, restaurar a definição da barra de menus ao seu estado original.

As barras de menus são colocadas na pilha e removidas da pilha na ordem último a entrar, primeiro a sair.

As definições de menu ocupam memória, portanto todo POP MENU deve ter um PUSH MENU correspondente para garantir que o uso de memória do seu aplicativo não cresça desnecessariamente.

# Exemplo

No exemplo a seguir, a definição da barra de menus do sistema é empurrada para a pilha e, em seguida, modificada. A definição original do menu do sistema é então restaurada retirando-a da pilha.

```foxpro
PUSH MENU _MSYSMENU
SET SYSMENU TO _MFILE, _MEDIT
POP MENU _MSYSMENU
```
