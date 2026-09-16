# Comando PUSH POPUP

Coloca uma definição de menu em uma pilha de definições de menu na memória.

```foxpro
PUSH POPUP MenuName
```

#### Parâmetros
 **MenuName**
Especifica o nome do menu cuja definição é colocada na pilha. O menu também pode ser um menu de sistema do Visual FoxPro.

# Observações

Quando usado com POP POPUP, PUSH POPUP permite salvar uma definição de menu, fazer alterações na definição de menu e depois restaurar a definição de menu ao seu estado original.

Definições de menu são colocadas na pilha e removidas da pilha na ordem last-in, first-out. Definições de menu ocupam memória, portanto todo PUSH POPUP deve ter um POP POPUP correspondente para garantir que o uso de memória da sua aplicação não cresça desnecessariamente.

# Exemplo

No exemplo a seguir, um menu chamado `popExam` é criado. A definição do menu é empilhada e depois modificada. O menu original é então restaurado removendo-o da pilha.

```foxpro
DEFINE POPUP popExam FROM 5,5
DEFINE BAR 1 OF popExam PROMPT 'One'
DEFINE BAR 2 OF popExam PROMPT 'Two'
DEFINE BAR 3 OF popExam PROMPT 'Three'
DEFINE BAR 4 OF popExam PROMPT 'Four'
ACTIVATE POPUP popExam NOWAIT
PUSH POPUP popExam
WAIT 'Original Popup' WINDOW
RELEASE BAR 2 OF popExam
WAIT 'Modified Popup. Original Popup is pushed to a stack.' WINDOW
POP POPUP popExam
WAIT 'Original Popup restored' WINDOW
DEACTIVATE POPUP popExam
RELEASE POPUP popExam
```
