# Comando DOCK

Acopla uma janela de ferramenta do Ambiente de Desenvolvimento Integrado (IDE) ou barra de ferramentas à janela da área de trabalho do Visual FoxPro ou a outra janela do IDE. Há duas versões da sintaxe.

> **Observação:** DOCK WINDOW não é suportado em tempo de execução.

```foxpro
DOCK WINDOW WindowName1 | NAME ObjectName1 POSITION nPosition [ WINDOW WindowName2 | NAME ObjectName2 ]
```

```foxpro
DOCK WINDOW WindowName1 WINDOW WindowName2
```

#### Parâmetros
 **WindowName1**
Especifica o nome da janela ou barra de ferramentas a acoplar. Para uma barra de ferramentas definida pelo usuário, você pode usar a propriedade Caption como seu nome. Se você especificar uma janela não acoplável como a janela a ser acoplada, ela se torna acoplável internamente. Por exemplo: WDOCKABLE("Command", .F.) DOCK WINDOW Command ? WDOCKABLE("Command") && Returns .T. Se você quiser acoplar uma única janela que está atualmente vinculada dentro de um contêiner com guias ou vinculado a outra janela da área de trabalho principal do Visual FoxPro, primeiro desacople-a do contêiner, por exemplo, usando POSITION -1 ou WDOCKABLE(, .F.). Um contêiner com guias ou vinculado é um conjunto de janelas com guias ou vinculadas.
**NAME ObjectName1**
Especifica uma referência de objeto para um formulário acoplável válido a acoplar. Se ObjectName1 estiver acoplado, o Visual FoxPro desacopla e reacopla conforme especificado. Observação Se ObjectName1 estiver indefinido ou não for válido, o Visual FoxPro gera um erro.
**POSITION nPosition**
Especifica a posição de acoplamento da janela ou barra de ferramentas. A tabela a seguir lista os valores possíveis para nPosition. nPosition Posição de acoplamento -3 Desacoplar contêiner interno. -2 Desacoplar contêiner externo. -1 Desacoplar janela. Observação Quando você especifica um valor de -1 para POSITION, não pode incluir a cláusula WINDOW. Caso contrário, ocorre um erro de sintaxe. 0 Superior 1 Esquerda 2 Direita 3 Inferior Se nPosition estiver definido entre 0 e 3, a janela é acoplada por vínculo, por exemplo, aparece anexada ao lado de outra janela. 4 Com guias Se nPosition estiver definido como 4, a janela é acoplada com guias, por exemplo, aparece como uma janela com guias. Observação Se você especificar um valor de 4 para POSITION, deve especificar uma cláusula WINDOW. Caso contrário, ocorre um erro. Observação Acoplamento com guias e por vínculo não é suportado para janelas do depurador dentro do Debug Frame. Você pode controlar a configuração Frame na caixa de diálogo Options. Barras de ferramentas não suportam acoplamento vinculado ou com guias. Se um contêiner com guias ou vinculado estiver acoplado, você pode desacoplar esse contêiner se especificar um valor de -2 ou -3 para qualquer uma das janelas no contêiner, de acordo com os seguintes detalhes: Se você passar um valor de -2, todo o contêiner é desacoplado se o contêiner estiver acoplado à área de trabalho do Visual FoxPro. Se você passar um valor de -3, apenas o contêiner interno que faz parte de um contêiner externo maior é desacoplado. Isso se aplica somente a contêineres acoplados com guias vinculados dentro de contêineres acoplados por vínculo. Se a janela especificada não fizer parte de um contêiner interno acoplado com guias, o Visual FoxPro trata o valor de -3 como um valor de -2 e desacopla todo o contêiner externo. Se a janela especificada não fizer parte de um contêiner, o Visual FoxPro a desacopla como se você tivesse passado um valor de -1. Se a janela ou contêiner já estiver desacoplado, o Visual FoxPro não faz nada. Para obter mais informações sobre acoplamento vinculado e com guias, consulte Como: acoplar janelas.
**WINDOW WindowName2**
Especifica o nome da janela ou barra de ferramentas de destino para acoplar. Se você omitir o parâmetro WindowName2, a janela é acoplada à janela da área de trabalho do Visual FoxPro. Observação O Visual FoxPro desconsidera a palavra-chave WINDOW para barras de ferramentas. Você pode acoplar barras de ferramentas somente à área de trabalho. Nenhuma outra janela pode ser acoplada a uma barra de ferramentas. Você pode usar a cláusula WINDOW para acoplamento vinculado e com guias. DOCK WINDOW usa uma posição de acoplamento com guias como padrão se você usar DOCK WINDOW...WINDOW sem incluir uma cláusula POSITION. Para acoplar um contêiner inteiro com guias ou vinculado à janela da área de trabalho do Visual FoxPro, chame DOCK WINDOW com qualquer uma das janelas no contêiner e omita a cláusula WINDOW. Se você especificar uma janela não acoplável como destino de acoplamento, o Visual FoxPro gera "Function argument value, type, or count is invalid (Error 11)". Por exemplo: DOCK WINDOW Command WINDOW Standard && Generates an error.
**NAME ObjectName2**
Especifica uma referência de objeto para um formulário acoplável válido para acoplar. Se ObjectName2 estiver acoplado, o Visual FoxPro desacopla e reacopla conforme especificado. Observação Se ObjectName2 estiver indefinido ou não for válido, o Visual FoxPro gera um erro.

# Observações

As seguintes janelas e barras de ferramentas do IDE são suportadas por DOCK WINDOW:
 - Todas as barras de ferramentas do sistema
- Call Stack
- Command
- Data Session (View)
- Document View
- Locals
- Output
- Properties
- Trace
- Watch

Barras de ferramentas do sistema e definidas pelo usuário são suportadas por DOCK WINDOW.

> **Observação:** A janela especificada deve primeiro existir na área de trabalho do Visual FoxPro; caso contrário, ocorre um erro.

Em versões anteriores do Visual FoxPro, a janela Data Session é sempre referida como a janela View. Além disso, a linguagem usada para controlar essa janela, como HIDE WINDOW, ACTIVATE WINDOW, WONTOP( ), também se refere a essa janela como a janela View. O Visual FoxPro continua a se referir à janela View para o comando DOCK WINDOW.

DOCK WINDOW sempre força a janela, se existir, a se tornar acoplável e altera a configuração da propriedade Visible da janela para True (.T.).

Você pode acoplar várias janelas que estão acopladas como um grupo a outra janela especificando uma das janelas acopladas. No entanto, se o destino de acoplamento existir no mesmo contêiner que a janela especificada, apenas essa janela é acoplada. Isso evita relações cíclicas. Por exemplo, o código a seguir reacopla a janela Command ao lado direito da janela Properties:

```foxpro
DOCK WINDOW Command POSITION 4 WINDOW Properties
DOCK WINDOW Command POSITION 2 WINDOW Properties
```

Compare este exemplo ao código a seguir, que acopla as janelas Command e View à janela Properties como janelas com guias:

```foxpro
DOCK WINDOW Command POSITION 4 WINDOW View
DOCK WINDOW Command POSITION 4 WINDOW Properties
```

> **Dica:** Excluir ou editar o arquivo de recursos FoxUser.dbf, que contém suas configurações de usuário, restaura suas configurações de janela padrão.

# Exemplo

O exemplo a seguir usa o comando DOCK WINDOW para acoplar a janela Command à janela da área de trabalho do Visual FoxPro e usa ADOCKSTATE( ) para obter o estado de acoplamento da janela Command.

Primeiro, certifique-se de que a janela Command esteja aberta. Depois de acoplar a janela Command, você pode ver que a barra de ferramentas Standard e as janelas Command estão acopladas à janela da área de trabalho Microsoft Visual FoxPro. A posição das barras de ferramentas ou janelas na matriz retornada por ADOCKSTATE( ) pode variar dependendo da ordem em que as barras de ferramentas ou janelas foram acopladas.

```foxpro
CLEAR
DOCK WINDOW Command POSITION 0
dockNum = ADOCKSTATE(dockState)
? dockNum   && Returns 2 only if Command window and
            && Standard toolbar exist.
? dockState(1,1)  && Outputs "Standard".
? dockState(1,4)  && Outputs "Microsoft Visual FoxPro".
? dockState(2,1)  && Outputs "COMMAND".
? dockState(2,4)  && Outputs "Microsoft Visual FoxPro".
```
