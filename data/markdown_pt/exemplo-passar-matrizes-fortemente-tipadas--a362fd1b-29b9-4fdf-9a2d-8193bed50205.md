# Exemplo Passar matrizes fortemente tipadas

Arquivo: ...\Samples\Solution\Toledo\ComArray.scx

Este exemplo demonstra como passar uma matriz fortemente tipada por referência a um servidor COM usando a função COMARRAY. O servidor COM executa cálculos e modifica o conteúdo da matriz. O formulário cliente então usa o comando DIMENSION com a cláusula AS para declarar a matriz fortemente tipada.

Neste exemplo, o servidor COM é escrito em Visual FoxPro. O exemplo também demonstra a sintaxe de declaração de interface para especificar matrizes de tipo ByRef na biblioteca de tipos COM gerada.

Ao abrir o exemplo, você é solicitado a registrar um servidor COM. O servidor COM é removido do registro quando você fecha o exemplo.

### Para passar uma matriz como matriz fortemente tipada a um servidor COM
- No exemplo, digite valores na matriz e clique em Determinant .

O servidor COM calcula o determinante da matriz usando Redução de Gauss-Jordan.

Para obter mais informações, consulte Função COMARRAY( ) e Comando DIMENSION.

# Passando matrizes fortemente tipadas

No exemplo, o formulário usa DIMENSION...AS para declarar uma matriz fortemente tipada conforme mostrado no método personalizado CallCOMServer:

```foxpro
DIMENSION laMatrix(ThisForm.Matrixdim, ThisForm.Matrixdim) AS Double
```

A matriz é passada por referência ao servidor COM Visual FoxPro usando a função COMARRAY( ):

```foxpro
* Instantiate COM server.
loMatrixCalc = CREATEOBJECT("VFPCOMArray.COMARRAYDemo")
* Array is one based and is passed by reference.
COMARRAY(loMatrixCalc,11)
* Pass array to COM server by reference "As Double".
lnResult = loMatrixCalc.Determinant(@laMatrix)
```

# Passando parâmetros COM por referência

No exemplo, o método personalizado RegisterCOMServer contém código que compila um servidor COM Visual FoxPro sob demanda e o registra. O código do servidor COM ilustra a sintaxe de declaração de interface para especificar matrizes tipadas ByRef na biblioteca de tipos COM gerada da seguinte forma:

```foxpro
FUNCTION Determinant(mat[] AS Double @) AS Double
```

A matriz é corretamente gravada na biblioteca de tipos como uma matriz fortemente tipada. O sinal de arroba (@) indica que a matriz é passada ByRef na biblioteca de tipos.
