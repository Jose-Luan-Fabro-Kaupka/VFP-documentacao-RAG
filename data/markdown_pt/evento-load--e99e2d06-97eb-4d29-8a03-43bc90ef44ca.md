# Evento Load

Ocorre imediatamente antes de um objeto ser criado.

```foxpro
PROCEDURE Object.Load
```

# Observações

Aplica-se a: Form Object | FormSet Object

O evento Load ocorre primeiro para o formset e depois para os formulários contidos. O evento Load ocorre antes dos eventos Activate e GotFocus.

Para impedir que um formulário seja criado, retorne false (.F.) do evento Load; o evento Destroy não será executado.
