# Remoção de espaços e concatenação de expressões

Expressões com vários campos podem não ser exibidas como desejado devido a espaços indesejados. Você pode remover espaços e concatenar expressões. Por exemplo, uma linha de endereço com cidade, região e código postal em campos separados pode apresentar espaços indesejados entre os valores.

# Remoção de espaços de campos e concatenação de expressões

Você pode combinar expressões com vários campos de tamanhos variáveis em uma única expressão. Envolva cada nome de campo com ALLTRIM( ), insira pontuação ou o espaço desejado entre aspas (" ") e concatene as expressões com um sinal de adição (+).

O espaço exigido por cada valor pode variar. Porém, se os comprimentos não variarem, como em códigos postais ou abreviações, envolva com ALLTRIM( ) apenas o nome do campo variável, como no exemplo:

```foxpro
ALLTRIM(city) + ", " + region + "  " + postal_code
```

> **Observação:** Um espaço, e não uma vírgula, entre aspas separa a região do código postal.

Para obter mais exemplos, consulte o relatório Invoice.frx no diretório ...\Samples\Solution\Reports do Visual FoxPro.

# Remoção rápida de espaços e concatenação de expressões

Quando não precisar incluir pontuação, você pode remover espaços e concatenar expressões rapidamente inserindo vírgulas (,) entre elas. O valor da expressão anterior à vírgula terá os espaços removidos.

> **Observação:** Desde que o valor resultante tenha comprimento maior que zero, você pode usar ponto e vírgula (;) para colocar a expressão em uma nova linha.

O exemplo a seguir mostra uma expressão sem espaços excedentes e concatenada, com vários campos de um endereço:

```foxpro
contact_name; address; city, region, postal_code
```
