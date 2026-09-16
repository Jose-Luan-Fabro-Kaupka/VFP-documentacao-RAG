# Método GetDockState

Retorna informações em uma matriz sobre o estado de encaixe de um formulário.

> **Observação:** Para usar GetDockState , a propriedade Dockable do formulário deve ser definida como 1.

```foxpro
Form.GetDockState(ArrayName)
```

#### Parâmetros
 **ArrayName**
Retorna uma matriz de uma linha e seis colunas contendo informações de encaixe para um formulário. Observação Você deve primeiro criar a matriz antes de passar um nome de matriz. A tabela a seguir descreve a matriz retornada por GetDockState . Coluna Descrição 1 Nome do formulário de encaixe. 2 Estado de encaixe: 1 - Docked 2 - Not docked 3 Posição de encaixe. Para valores, consulte DockPosition Property . 4 Formulário de destino ou Caption do formulário ao qual o formulário especificado está encaixado. 5 Referência de objeto para o formulário de encaixe. 6 Referência de objeto para a janela ou formulário de destino.

# Valor de retorno

Aplica-se a: Form Object

Tipo de dados lógico. GetDockState retorna True (.T.) se a matriz for atualizada com sucesso com o estado de encaixe. Caso contrário, GetDockState retorna False. (.F.).

# Observações

Se um formulário estiver encaixado em uma janela IDE, o valor da coluna 6 será uma cadeia de caracteres vazia. Se um formulário estiver encaixado na área de trabalho do Visual FoxPro, a coluna 6 conterá uma referência de objeto a _SCREEN.

GetDockState é uma variação limitada da função ADOCKSTATE( ) , pois limita seus detalhes ao formulário atual. Como GetDockState é um subconjunto limitado da função ADOCKSTATE( ) , pode não fornecer todas as informações necessárias sobre o estado de encaixe atual do formulário. Você pode precisar chamar ADOCKSTATE( ) também para obter um quadro mais completo. Para obter mais informações, consulte ADOCKSTATE( ) Function.
