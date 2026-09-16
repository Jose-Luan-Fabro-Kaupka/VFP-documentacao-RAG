# Evento Error (Visual FoxPro)

Ocorre quando há um erro em um método durante a execução. Você pode adicionar código ao evento Error para que o objeto trate erros.

> **Observação:** O evento Error só ocorre para erros em código e quando contém código. Ele não ocorre se uma rotina ON ERROR já estiver na pilha de chamadas.

> **Dica:** Inclua código para tratar erros imprevistos; caso contrário, o evento será executado sem tratar o erro e a mensagem padrão não será exibida.

```foxpro
PROCEDURE Object.Error
LPARAMETERS nError, cMethod, nLine
```

#### Parâmetros
 **nError**
Contém o número do erro.
**cMethod**
Contém o nome do método que causou o erro ou, se ele chamou uma função definida pelo usuário onde ocorreu o erro, o nome dessa função.
**nLine**
Contém o número da linha no método ou função que causou o erro.

# Observações

Aplica-se aos objetos e controles do Visual FoxPro que expõem o evento Error.

O evento Error substitui a rotina ON ERROR e permite que cada objeto detecte e trate erros internamente.

Erros no próprio código do evento Error precisam ser tratados pelo objeto e não podem ser propagados para ON ERROR ou TRY...CATCH...FINALLY.
