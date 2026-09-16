# Otimizando programas

Ao escrever seu código com cuidado, você pode escrever os programas mais rápidos possíveis. Existem várias maneiras de melhorar o desempenho de programas no Visual FoxPro:
 - Seguindo as dicas gerais de desempenho de programação fornecidas abaixo.
- Usando expressões de nome em vez de substituição de macro.
- Referenciando propriedades de objetos de forma eficiente.

# Dicas gerais de desempenho de programação

Para escrever os programas mais rápidos possíveis, siga as recomendações listadas abaixo.
 - Escolha o tipo de dados correto para seus dados. Em particular, use o tipo de dados Integer para informações numéricas sempre que possível, pois é processado com maior eficiência. Sempre que possível, use tipos de dados Integer para valores de chave primária e estrangeira, o que resultará em arquivos de dados menores, índices menores (e, portanto, mais rápidos) e junções mais rápidas. Observação Para um exemplo mostrando como criar um índice menor (e, portanto, mais rápido), execute Solution.app, localizado no diretório Visual FoxPro ...\Samples\Solution. Escolha View Samples by Filtered List, selecione Indexes na lista suspensa e depois escolha Create Small Indexes Using BINTOC( ) na lista que aparece.
- Evite reabrir arquivos, o que reduz o desempenho. Em vez disso, atribua arquivos a áreas de trabalho ao abri-los e use o comando SELECT para escolher uma área de trabalho específica conforme necessário.
- Use loops FOR ... ENDFOR em vez de loops DO WHILE ... ENDDO quando possível, pois são mais rápidos.
- Quando você copia dados de vários campos, SCATTER TO ARRAY é mais rápido que SCATTER MEMVAR.
- Para usar a memória com maior eficiência, evite criar objetos antes de precisar deles e limpe objetos quando terminar de usá-los para liberar memória. Dica Você pode testar quanta memória cada objeto consome chamando a função SYS(1016).
- Envie saída para a janela superior sempre que possível; atualizar janelas atrás da janela superior é substancialmente mais lento. Fazer a saída rolar atrás de uma janela é quase o pior caso possível.
- Desabilite a exibição de status com o comando SET TALK OFF, o que elimina a sobrecarga de atualização de tela.
- Defina o comando SET DOHISTORY como OFF para evitar atualizar a janela de comando cada vez que um programa é executado.

# Usando expressões de nome em vez de substituição de macro

Se você usar expressões de nome em vez de substituição de macro, o desempenho do programa melhorará significativamente. Por exemplo, se você atribuir um valor à variável `cFile`, uma expressão de nome criada com `cFile` é mais rápida que a substituição de macro.

```foxpro
cFile = "CUST"
use &cFile      && Macro substitution, slow
use (cFile)      && Name expression: faster, preferred
```

# Referenciando propriedades de objetos de forma eficiente

Ao entender como o Visual FoxPro trabalha com propriedades e objetos, você pode fazer seus aplicativos executarem com maior eficiência.

### Otimizando referências repetidas a uma propriedade

Quando você referencia uma propriedade de objeto com a sintaxe object.property, o Visual FoxPro deve procurar o objeto antes de poder acessar a propriedade. Se você precisar acessar a propriedade repetidamente, essa estratégia de busca pode reduzir o desempenho.

Para evitar referenciar o mesmo procedimento repetidamente (como em um loop), leia o valor da propriedade em uma variável, faça alterações e depois defina a propriedade quando terminar. Por exemplo, o código a seguir preenche uma matriz de propriedades primeiro criando uma matriz na memória, preenchendo-a e depois definindo a propriedade apenas uma vez no final:

```foxpro
* Copy string to a local variable
lcChar = THISFORM.cCharString
LOCAL laCharArray[256]   && Create local array
FOR nCounter = 1 to 256
   laCharArray[x] = SUBSTR(laChar,x,1)
ENDFOR
* Copy the local array to the property array
ACOPY(laCharArray,THISFORM.aCharArray)
```

### Referenciando várias propriedades de forma eficiente

Se você atualizar mais de uma propriedade para o objeto, o Visual FoxPro deve procurar o objeto várias vezes, o que pode afetar o desempenho. No exemplo a seguir, o código faz o Visual FoxPro procurar quatro objetos (como `THISFORM`, `pgfCstInfo`, `pgCstName` e `txtName`) para encontrar a propriedade a ser definida. Como o código define duas propriedades, a busca quádrupla é feita duas vezes:

```foxpro
THISFORM.pgfCstInfo.pgCstName.txtName.Value = ;
 "Fred Smith"
THISFORM.pgfCstInfo.pgCstName.txtName.BackColor = ;
 RGB (0,0,0)  & Dark red
```

Para evitar essa sobrecarga, use o comando WITH ... ENDWITH Command. Esse método faz o Visual FoxPro encontrar o objeto uma vez. Por exemplo, o exemplo a seguir realiza a mesma tarefa que o anterior, mas mais rapidamente:

```foxpro
WITH THISFORM.pgfCstInfo.pgCstName.txtName
   .Value = "Fred Smith"
   .BackColor = RGB (0,0,0)  & Dark red
ENDWITH
```

Você também pode armazenar uma referência de objeto em uma variável e incluir a variável no lugar da referência de objeto:

```foxpro
oControl = THISFORM.pgfCstInfo.pgCstName.txtName
oControl.Value = "Fred Smith"
oControl.BackColor = RGB (0,0,0)  & Dark red
```
