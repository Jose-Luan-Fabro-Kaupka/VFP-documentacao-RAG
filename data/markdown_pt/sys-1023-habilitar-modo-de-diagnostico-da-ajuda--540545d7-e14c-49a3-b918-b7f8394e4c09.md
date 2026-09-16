# SYS(1023) - Habilitar modo de diagnóstico da Ajuda

Habilita o modo de diagnóstico da Ajuda, permitindo capturar o HelpContextID passado ao sistema de Ajuda do Visual FoxPro.

```foxpro
SYS(1023)
```

# Valor de retorno

Character

# Observações

SYS(1023) é útil para depurar um sistema de Ajuda personalizado para sua aplicação. SYS(1023) retorna a cadeia de caracteres vazia.

Quando o modo de diagnóstico da Ajuda é habilitado com SYS(1023), uma caixa de diálogo é exibida sempre que você pressiona F1 ou emite HELP. A caixa de diálogo exibe o HelpContextID a ser passado ao sistema de Ajuda do Visual FoxPro, e você tem a opção de passar o HelpContextID ao sistema de Ajuda do Visual FoxPro.

Se você escolher Yes, o HelpContextID é passado ao sistema de Ajuda do Visual FoxPro e o tópico de Ajuda correspondente (se disponível) é exibido. Se você escolher No, o HelpContextID não é passado ao sistema de Ajuda do Visual FoxPro e o tópico de Ajuda correspondente não é exibido.

Use SYS(1024) para desabilitar o modo de diagnóstico da Ajuda e restaurar o processamento padrão do sistema de Ajuda do Visual FoxPro.
