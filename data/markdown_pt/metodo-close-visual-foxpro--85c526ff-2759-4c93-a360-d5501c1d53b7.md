# Método Close (Visual FoxPro)

Fecha um projeto e libera os objetos ProjectHook e Project do projeto.

```foxpro
Object.Close()
```

# Observações

Aplica-se a: Objeto Project (Visual FoxPro)

A execução do método Close faz ocorrer o evento ProjectHook.Destroy do projeto. Após o evento ProjectHook.Destroy, o objeto ProjectHook é liberado e, em seguida, o objeto Project é liberado.
