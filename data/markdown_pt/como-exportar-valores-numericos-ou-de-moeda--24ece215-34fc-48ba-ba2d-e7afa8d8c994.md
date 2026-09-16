# Como: exportar valores numéricos ou de moeda

Se você alterou o caractere de ponto decimal do Visual FoxPro para vírgula, dados numéricos e de moeda podem ser analisados em campos separados quando você anexa ou exporta os dados. Por exemplo, o Visual FoxPro traduzirá o valor 100,000 em dois campos porque ele parece estar delimitado por vírgula. Escolha um dos dois métodos para garantir que a vírgula seja traduzida corretamente:
 - Use tabulações para separar campos no arquivo de texto
- Altere o caractere de ponto decimal de volta para ponto

Se desejar exportar o texto, use o comando COPY TO com as palavras-chave DELIMITED WITH TAB.

Se desejar alterar o caractere de ponto decimal para ponto antes de exportar arquivos de texto, pode alterar o caractere de volta para vírgula após exportar o arquivo.

### Para alterar o caractere de ponto decimal
- Na janela Command, digite o seguinte comando. SET POINT TO
- Exporte o arquivo usando a palavra-chave DELIMITED.
- Na janela Command, digite o seguinte comando para redefinir o caractere de ponto decimal para vírgula. SET POINT TO ','
