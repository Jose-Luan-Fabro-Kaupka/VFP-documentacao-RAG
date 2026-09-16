# SYS(3050) - Definir tamanho da memória do buffer

Define o tamanho da memória do buffer de primeiro plano ou de segundo plano.

```foxpro
SYS(3050, nType, [nBuffMemSize])
```

#### Parâmetros
 **nType**
Especifica o buffer. A tabela a seguir lista os valores para nType e o buffer correspondente: nType Buffer 1 Primeiro plano 2 Segundo plano
**nBuffMemSize**
Especifica o tamanho máximo da memória do buffer em bytes. Se você especificar um valor para nBuffMemSize que seja menor que 256K bytes, o Visual FoxPro define o tamanho da memória do buffer para 256K bytes. Especifique 0 para nBuffMemSize para retornar o tamanho da memória do buffer ao valor de inicialização do Visual FoxPro. O valor de inicialização depende da quantidade de memória do seu computador. Se você omitir nBuffMemSize , SYS(3050) retorna o tamanho da memória do buffer para o buffer especificado com nType.

# Valor de retorno

Character

# Observações

SYS(3050) permite otimizar o desempenho do Visual FoxPro ajustando a quantidade de memória que o Visual FoxPro aloca para os buffers de primeiro plano e de segundo plano. O buffer de memória de primeiro plano é a memória disponível para o Visual FoxPro quando está operando em primeiro plano como o aplicativo atualmente ativo. O buffer de memória de segundo plano é a memória disponível para o Visual FoxPro quando está operando em segundo plano, quando outro aplicativo é o aplicativo de primeiro plano.

SYS(3050) retorna um valor numérico como uma cadeia de caracteres que indica a quantidade máxima de memória que o Visual FoxPro aloca para os buffers de primeiro plano ou de segundo plano.
