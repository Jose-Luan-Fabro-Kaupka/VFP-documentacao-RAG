# Comando POP POPUP

Restaura a definição de menu especificada que foi colocada na pilha com PUSH POPUP.

```foxpro
POP POPUP MenuName
```

#### Parâmetros
**MenuName**
Especifica o nome do menu cuja definição é retirada da pilha. O menu pode ser um menu definido pelo usuário criado com DEFINE MENU ou um menu do sistema do Visual FoxPro.

# Observações

Quando usado com PUSH POPUP, POP POPUP permite salvar uma definição de menu, fazer alterações nela e depois restaurá-la ao estado original.

As definições de menu são colocadas na pilha e removidas dela na ordem último a entrar, primeiro a sair.

As definições de menu ocupam memória; portanto, cada POP POPUP deve ter um PUSH POPUP correspondente para garantir que o uso de memória do aplicativo não aumente desnecessariamente.

# Exemplo

No exemplo a seguir, é criado um menu chamado `popExam`. A definição do menu é colocada na pilha e, em seguida, um dos itens do menu é modificado. A definição original do menu é então restaurada ao ser retirada da pilha.

```foxpro
DEFINE POPUP popExam FROM 5,5
DEFINE BAR 1 OF popExam PROMPT 'One'
DEFINE BAR 2 OF popExam PROMPT 'Two'
DEFINE BAR 3 OF popExam PROMPT 'Three'
DEFINE BAR 4 OF popExam PROMPT 'Four'
ACTIVATE POPUP popExam NOWAIT
PUSH POPUP popExam
WAIT 'Popup pushed' WINDOW
RELEASE BAR 2 OF popExam
WAIT 'This is the modified popup' WINDOW
POP POPUP popExam
WAIT 'Popup popped, original popup restored' WINDOW
DEACTIVATE POPUP popExam
RELEASE POPUP popExam
```
