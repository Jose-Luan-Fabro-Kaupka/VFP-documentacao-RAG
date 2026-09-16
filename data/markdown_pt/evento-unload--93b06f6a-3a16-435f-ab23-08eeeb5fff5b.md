# Evento Unload

Ocorre quando um objeto é liberado.

Unload é o último evento a ocorrer antes que um formset ou formulário seja liberado.

```foxpro
PROCEDURE Object.Unload
```

# Observações

Aplica-se a: Form Object | FormSet Object

Unload ocorre após o evento Destroy e depois que todos os objetos contidos foram liberados. Além disso, Unload ocorre dependendo do tipo de objeto:
 - Objetos Form são liberados em código quando a variável de objeto que se refere ao formulário é liberada ou quando seu formset é liberado.
- Objetos Form set são liberados em código quando a variável de objeto que se refere ao formset é liberada.

Se um objeto container, como um formset, contém objetos, o evento Unload do objeto container ocorre após os eventos Unload dos objetos que ele contém. Por exemplo, um formset contendo um formulário que contém um controle (um CommandButton) é liberado nesta ordem:
 - FormSet Destroy event
- Form Destroy event
- CommandButton Destroy event
- Form Unload event
- FormSet Unload event

Para retornar um valor à cláusula TO VarName no comando DO FORM, use o comando RETURN no evento Unload. Para mais informações, consulte DO FORM Command.
