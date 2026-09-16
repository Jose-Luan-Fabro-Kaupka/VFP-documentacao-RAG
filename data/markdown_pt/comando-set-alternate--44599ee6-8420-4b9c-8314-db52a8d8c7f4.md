# Comando SET ALTERNATE

Direciona a saída de tela ou impressora criada com ?, ??, DISPLAY ou LIST para um arquivo de texto.

```foxpro
SET ALTERNATE ON | OFF
-or-
SET ALTERNATE TO [FileName [ADDITIVE]]
```

#### Parâmetros
 **ON**
Direciona a saída para o arquivo de texto.
**OFF**
(Padrão) Desabilita a saída para o arquivo de texto.
**TO FileName**
Cria o arquivo de texto, que recebe a extensão padrão .txt, a menos que você inclua uma extensão diferente com o nome do arquivo. Se você usar SET ALTERNATE TO sem FileName , o último arquivo que você criou usando SET ALTERNATE TO FileName é fechado.
**ADDITIVE**
Anexa a saída ao final do arquivo especificado com FileName . Se você omitir ADDITIVE, o conteúdo do arquivo é substituído.
