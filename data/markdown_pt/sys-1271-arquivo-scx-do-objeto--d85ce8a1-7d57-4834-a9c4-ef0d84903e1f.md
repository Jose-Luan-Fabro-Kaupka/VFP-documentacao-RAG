# SYS(1271) - Arquivo .SCX do objeto

Retorna o nome do arquivo .SCX no qual o objeto instanciado especificado está armazenado.

```foxpro
SYS(1271, oObjectName)
```

#### Parâmetros
 **oObjectName**
Especifica o nome do objeto para o qual o arquivo .scx é retornado.

# Valor de retorno

Character, Logical

# Observações

SYS(1271) retorna o nome do arquivo .scx no qual o objeto instanciado especificado está armazenado.

SYS(1271) retorna um falso lógico (.F.) se o objeto não puder ser localizado em um arquivo .scx (por exemplo, se o objeto foi criado na Janela de comando).
