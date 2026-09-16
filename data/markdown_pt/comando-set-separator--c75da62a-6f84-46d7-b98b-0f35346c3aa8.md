# Comando SET SEPARATOR

Especifica o caractere que separa cada grupo de três dígitos à esquerda do ponto decimal ao exibir um valor numérico ou de moeda formatado.

# Sintaxe

```foxpro
SET SEPARATOR TO [expC]
```

# Parâmetros
 **exprC**
Especifica o caractere para o separador de posição numérica.

# Observações

Use SET SEPARATOR para alterar o separador de posição numérica do padrão, por exemplo, uma vírgula (,). Emita SET SEPARATOR sem seu argumento para redefinir o valor para o padrão.

> **Dica:** Se você usar o comando SET SYSFORMATS ON, o caractere para o separador de posição numérica é definido pelo Painel de Controle Opções Regionais do Windows. Usar este comando redefine o caractere para o padrão regional até a próxima vez que você emitir um comando SET SEPARATOR exprC.

SET SEPARATOR tem escopo na sessão de dados atual.

# Exemplo

```foxpro
SET SEPARATOR TO [expC]
```
