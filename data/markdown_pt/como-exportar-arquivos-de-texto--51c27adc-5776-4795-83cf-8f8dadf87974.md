# Como: exportar arquivos de texto

Se você exportar para um arquivo de texto, o Visual FoxPro assume que seus campos são separados por vírgulas e que cada campo de caracteres é delimitado por aspas. Se você definiu o caractere de ponto decimal para ser exibido como vírgula, dados numéricos e de moeda podem ser analisados em campos separados.

### Para exportar para um arquivo de texto
- Use o comando COPY TO com a cláusula DELIMITED apropriada conforme mostrado na tabela a seguir. Para estes separadores Use esta cláusula DELIMITED Vírgulas entre campos e aspas delimitando campos de caracteres DELIMITED Campos de caracteres delimitados por um caractere diferente de aspas DELIMITED WITH delimiter Tabulações entre campos DELIMITED WITH TAB Espaços entre os campos DELIMITED WITH BLANK* * Datas e horas separadas por espaço serão analisadas como dois campos com estas palavras-chave
