# Comando SET BLOCKSIZE

Especifica como o Visual FoxPro aloca espaço em disco para o armazenamento de campos memo.

```foxpro
SET BLOCKSIZE TO nBytes
```

#### Parâmetros
 **nBytes**
Especifica o tamanho do bloco em que o espaço em disco para campos memo é alocado. Se nBytes for 0, o espaço em disco é alocado em bytes individuais (blocos de 1 byte). Se nBytes for um inteiro entre 1 e 32, o espaço em disco é alocado em blocos de nBytes bytes multiplicados por 512. Se nBytes for maior que 32, o espaço em disco é alocado em blocos de nBytes bytes. Se você especificar um valor de tamanho de bloco maior que 32, pode economizar espaço substancial em disco.

# Observações

O valor padrão de SET BLOCKSIZE é 64. Para redefinir o tamanho do bloco para um valor diferente depois que o arquivo foi criado, defina-o para um novo valor e use COPY para criar uma nova tabela. A nova tabela terá o tamanho de bloco especificado.

SET BLOCKSIZE tem escopo na sessão de dados atual.
