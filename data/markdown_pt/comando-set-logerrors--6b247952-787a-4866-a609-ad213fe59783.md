# Comando SET LOGERRORS

Determina se as mensagens de erro de compilação do Visual FoxPro devem ser enviadas a um arquivo de texto.

Você pode usar SET LOGERRORS para salvar mensagens de erro de compilação em um arquivo de texto ao compilar programas.

```foxpro
SET LOGERRORS ON | OFF
```

#### Parâmetros
 **ON**
Especifica criar um arquivo de erro de compilação (.err) usando o mesmo nome do programa compilado. (Padrão) Se um arquivo .err com o mesmo nome existir, ele é substituído.
**OFF**
Especifica não criar um arquivo de erro de compilação (.err) ao compilar um programa.

# Observações

> **Observação:** Se o programa compilar sem erro e um arquivo .err existir com o mesmo nome do programa compilado, o arquivo .err é excluído.
