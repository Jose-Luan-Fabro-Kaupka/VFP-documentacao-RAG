# Comando SET EXACT

Especifica as regras que o Visual FoxPro usa ao comparar duas cadeias de caracteres de comprimentos diferentes.

> **Observação:** Diferentemente de SET ANSI, SET EXACT não se aplica a comandos SQL do Visual FoxPro. Para obter mais informações, consulte Comando SET ANSI.

```foxpro
SET EXACT ON | OFF
```

#### Parâmetros
 **ON**
Especifica que as expressões devem corresponder caractere por caractere ao comparar dados de caractere, ou byte por byte ao comparar dados binários, para serem equivalentes. Observação Para corresponder ao comprimento da expressão mais longa, a expressão mais curta das duas é preenchida à direita com espaços ou bytes zero (0). No entanto, quaisquer espaços à direita ou bytes zero nas expressões são desconsiderados na comparação.
**OFF**
Especifica que as expressões devem corresponder caractere por caractere ao comparar dados de caractere, ou byte por byte ao comparar dados binários, até o final da expressão do lado direito ser atingido para serem equivalentes. (Padrão)

# Observações

Se ambas as cadeias de caracteres têm o mesmo comprimento, SET EXACT não tem efeito.

SET EXACT tem escopo na sessão de dados atual.
