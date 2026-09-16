# Comando POP KEY

Restaura as atribuições ON KEY LABEL que foram colocadas na pilha com PUSH KEY.

```foxpro
POP KEY [ALL]
```

#### Parâmetros
 **ALL**
Limpa todas as atribuições de tecla atuais definidas com ON KEY LABEL e limpa todas as atribuições de tecla definidas com ON KEY LABEL da pilha.

# Observações

POP KEY, quando usado com PUSH KEY, permite salvar um conjunto de atribuições de tecla criadas com comandos ON KEY LABEL, fazer alterações nas atribuições de tecla com mais comandos ON KEY LABEL e, em seguida, restaurar as atribuições de tecla originais.

As atribuições de tecla ocupam memória; portanto, todo POP KEY deve ter um PUSH KEY correspondente para garantir que o uso de memória do seu aplicativo não aumente desnecessariamente.

Para obter mais informações sobre como colocar comandos ON KEY LABEL na pilha, consulte Comando PUSH KEY.
