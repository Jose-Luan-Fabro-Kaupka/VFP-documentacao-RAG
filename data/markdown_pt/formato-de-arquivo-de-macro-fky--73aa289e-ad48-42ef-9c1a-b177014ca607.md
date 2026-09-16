# Formato de arquivo de macro (.fky)

# Cabeçalho do arquivo

| Deslocamento de byte | Descrição |
| --- | --- |
| 01 – 03 | Assinatura, Hex 79FF |
| 04 – 15 | Ignorado |
| 16 – 17 | Número de macros (binário) |
| 18 – end | As macros |

# Macros individuais

| Deslocamento de byte | Descrição |
| --- | --- |
| 00 – 19 | Nome da macro |
| 20 – 21 | Tamanho da macro (em teclas, binário) |
| 22 – 23 | Tecla (dois bytes, binário) |
| 24 – end | Teclas da macro |
