# Classe Collection

Você pode usar coleções para agrupar um conjunto de itens relacionados, geralmente objetos, que podem ser de qualquer tipo. As coleções fornecem um mecanismo para trabalhar com objetos armazenados em contêineres e incluem maneiras padrão de acessar e iterar por objetos em uma coleção. A classe Collection funciona como uma verdadeira classe de contêiner, embora não inclua o método AddObject como as classes Form e PageFrame.

A classe Collection é uma classe base que você pode subclassificar em arquivos de programa (.prg) ou bibliotecas de classes visuais (.vcx).

```foxpro
Collection
```

# Observações

A posição de um item em uma coleção pode variar e mudar quando ocorrem alterações na coleção.

As coleções suportam enumerações de itens realizadas com o comando FOR EACH baseadas na posição dos itens. Você pode controlar a posição desses itens usando os parâmetros eBeforeItem ou eAfterItem associados ao método Add para objetos de coleção. Você pode usar um valor de índice de 1, ou enumeração baseada em um, para referir-se ao primeiro item em uma coleção, ou pode usar um valor de chave definindo a propriedade KeySort. As coleções são baseadas em um para consistência e compatibilidade com outras coleções internas do Visual FoxPro.

Certifique-se de que todos os itens em uma coleção tenham chaves ou nenhum deles tenha chaves. Decidir se todos os itens têm chaves ou não fornece busca de itens mais eficiente ao usar o método Item para objetos de coleção e o comando FOR EACH.

Você pode usar uma coleção em um servidor Component Object Model (COM) do Visual FoxPro que outros servidores COM podem acessar.

Você pode ocultar os métodos Add e Remove para objetos de coleção do uso público subclassificando o objeto de coleção e marcando os membros subclassificados como Hidden ou Protected. Se fizer isso, você precisa adicionar os membros da coleção no evento Init ou por meio de outro método.

Itens adicionados a coleções têm o mesmo escopo que qualquer outra variável de memória.

Como os objetos Collection suportam métodos padrão, por exemplo, Item (Collection Class), você precisa estar ciente da ordem de busca para esses métodos. Um método de objeto Collection tem precedência sobre uma chamada de função definida pelo usuário (UDF) padrão. A lista a seguir mostra a ordem em que o Visual FoxPro busca um nome de função:
 - Função nativa do Visual FoxPro
- Método padrão de objeto Collection
- UDF definida no arquivo de programa (.prg) local
- UDF definida em arquivos de programa (.prg) chamadores
- Programa nomeado no arquivo de aplicação (.app ou .exe)
- Programa nomeado na lista SET PATH

Quando o Visual FoxPro libera uma coleção, que contém referências a objetos, ele também libera quaisquer objetos na coleção se não forem referenciados em outro lugar. Certifique-se de liberar objetos e quaisquer referências a esses objetos de uma coleção antes de liberar a coleção em si da memória.

O Visual FoxPro não suporta segurança de tipo intrínseca. Portanto, para impor segurança de tipo com coleções, você deve fornecê-la para a classe.

Uma coleção nativa do Visual FoxPro é projetada de forma que o método Item torna possível executar código definido pelo usuário. O Visual FoxPro Debugger não suporta a avaliação de membros de objeto que são implementados como chamadas de método. Portanto, você não pode avaliar os itens em uma coleção.

> **Observação:** Para ajudar a depurar uma coleção, você pode escrever código como os exemplos a seguir, que adicionam um array membro chamado "Items" para referenciar cada um dos itens da coleção:

```foxpro
LOCAL oCol AS Collection
oCol=CREATEOBJECT("collection")
oCol.Add(123)
oCol.Add("AAA")
oCol.Add(CREATEOBJECT("custom"))
oCol.Add(CREATEOBJECT("session"))
oCol.Add(CREATEOBJECT("collection"))
oCol.Item(5).Add(456)
oCol.Item(5).Add("BBB")
oCol.Item(5).Add(CREATEOBJECT("session"))
oCol.Item(5).Add(CREATEOBJECT("collection"))
oCol.Item(5).Item(4).Add(789)
oCol.Item(5).Item(4).Add("CCC")
oCol.Item(5).Item(4).Add(CREATEOBJECT("session"))
oCol.Item(5).Item(4).Add(CREATEOBJECT("Collection"))
DebugCollection(oCol)
DEBUG
SUSPEND
PROCEDURE DebugCollection(oCollection)
   IF oCollection.Count=0
      RETURN
   ENDIF
   oCollection.AddProperty("Items[1]")
   DIMENSION oCollection.Items[oCollection.Count]
   FOR i = 1 TO oCollection.Count
      oCollection.Items[m.i]=oCollection.Item[m.i]
      IF VARTYPE(oCollection.Item[m.i])="O" AND ;
         oCollection.Item[m.i].BaseClass="Collection"
         IF oCollection=oCollection.Item[m.i]
            LOOP
         ENDIF
         DebugCollection(oCollection.Item[m.i])
      ENDIF
   ENDFOR
ENDPROC
```

# Exemplo

Em tempo de execução, o exemplo a seguir cria formulários e uma coleção, adiciona formulários à coleção usando o método Add da classe Collection, exibe o nome de cada formulário na coleção e exibe o número de formulários na coleção:

```foxpro
loForm1 = CREATEOBJECT("Form")
loForm2 = CREATEOBJECT("Form")
loCol = CREATEOBJECT("Collection")
loCol.Add(loForm1)
loCol.Add(loForm2)
FOR EACH loObj IN loCol
   ? loObj.Name
ENDFOR
? loCol.Count
```

O exemplo a seguir define uma classe Form que adiciona caixas de texto, objetos de botão e uma coleção ao formulário. Quando adicionados ao formulário em tempo de execução, a classe de coleção adiciona todos os objetos no formulário a si mesma. O exemplo então itera pela coleção para ajustar a posição do controle e imprime seu nome na tela.

```foxpro
LOCAL loForm, loItem, lnTop
loForm = CREATEOBJECT("myForm")
lnTop=0
FOR EACH loItem IN loForm.myCollection
   TRY
      loItem.Top = lnTop
      lnTop=lnTop+20
      ? loItem.Name
   CATCH
   ENDTRY
ENDFOR
loForm.Show(1)
DEFINE CLASS myForm AS Form
   AllowOutput=.F.
   AutoCenter=.T.
   ADD OBJECT myTextBox1 AS TextBox
   ADD OBJECT myTextBox2 AS TextBox
   ADD OBJECT myButton1 AS CommandButton
   ADD OBJECT myButton2 AS CommandButton
   ADD OBJECT myCollection AS col1
ENDDEFINE
DEFINE CLASS col1 AS Collection
   PROCEDURE Init
      FOR i = 1 TO THISFORM.Objects.Count
         THIS.Add(THISFORM.Objects(m.i))
      ENDFOR
   ENDPROC
ENDDEFINE
```

Para outros exemplos usando os métodos Add, Remove e Item da classe Collection, consulte Método Add (Collection Class), Método Remove (Collection Class) e Método Item (Collection Class).
