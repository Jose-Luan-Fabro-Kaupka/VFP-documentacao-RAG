# SYS(2334) - Modo de invocação do servidor de automação

Retorna um valor que indica como um método do servidor de automação do Visual FoxPro foi invocado.

```foxpro
SYS(2334)
```

# Valor de retorno

Caractere

# Observações

A tabela a seguir lista os valores que SYS(2334) retorna para servidores de automação:

| Valor de retorno | Método de invocação |
| --- | --- |
| 0 | Desconhecido (por exemplo, invocado do método INIT, que não é VTable nem IDispatch) |
| 1 | Método OLEPUBLIC invocado via associação VTable |
| 2 | IDispatch |

SYS(2334) também retorna zero quando executado de dentro de um executável autônomo (.exe). Use a propriedade StartMode para determinar como uma instância do Visual FoxPro foi iniciada.
