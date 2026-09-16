# Propriedade ReleaseType

Retorna um inteiro que determina como um objeto Form é liberado. Não disponível em tempo de design; somente leitura em tempo de execução.

```foxpro
Object.ReleaseType
```

# Valor de retorno

As configurações da propriedade ReleaseType são:

| Configuração | Descrição |
| --- | --- |
| 0 | Variável liberada. |
| 1 | Comando de menu Close ou caixa de fechamento. |
| 2 | Sair do Visual FoxPro. |

# Observações

Aplica-se a: Form Object | _SCREEN System Variable

A propriedade ReleaseType é definida antes de o evento QueryUnload ser chamado.
