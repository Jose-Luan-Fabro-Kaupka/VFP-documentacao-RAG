# Função COMARRAY( )

Especifica como passar matrizes para objetos COM.

```foxpro
COMARRAY(oObject [, nNewValue])
```

#### Parâmetros
 **oObject**
Especifica uma referência de objeto a um objeto COM.
**nNewValue**
Especifica como passar uma matriz para um objeto COM especificado com oObject . A tabela a seguir lista as configurações de nNewValue e como passar a matriz para o objeto COM. nNewValue Description 0 The array is a zero-based array and is passed by value. 1 The array is a one-based array and is passed by value. Compatible with earlier versions of Visual FoxPro. (Default) 10 The array is a zero-based array and is passed by reference. 11 The array is a one-based array and is passed by reference. 100 The array is a fixed size array and cannot be redimensioned. 1000 Byte arrays are not converted to strings. To return the current setting, call COMARRAY( ) without an argument for the nNewValue parameter.

# Valor de retorno

Numeric. COMARRAY( ) retorna a configuração atual.

# Observações

Use COMARRAY( ) somente quando passar matrizes para objetos COM usando a seguinte sintaxe:

`oComObject.Method(@MyArray)`

> **Observação:** Se você omitir o sinal de arroba (@), apenas o primeiro elemento da matriz é passado para o objeto COM, e COMARRAY( ) não tem efeito. Este comportamento é o mesmo das versões anteriores do Visual FoxPro.

Quando você usa uma matriz de bytes (VT_UI1) para comunicar com um servidor COM, o Visual FoxPro converte a matriz de bytes em uma cadeia de caracteres. O valor aditivo nValue de 1000 mantém o tipo original adequado da matriz e não converte o resultado em uma cadeia de caracteres.

Se um cliente passa uma matriz de bytes por referência para um Servidor COM do Visual FoxPro, o Servidor COM do Visual FoxPro também deve definir o valor aditivo nValue como 1000. Você pode fazer isso colocando a seguinte chamada no evento Init do Servidor COM do Visual FoxPro:

```foxpro
COMARRAY(THIS,1000)
```

O valor aditivo nValue de 100 torna possível impedir a redimensionação de uma matriz. Você deve verificar possíveis erros após chamar o servidor, caso o servidor tente redimensionar a matriz. O exemplo a seguir mostra como impedir a redimensionação da matriz. Para executar este exemplo, primeiro compile a definição de classe em uma DLL chamada "t1.dll".

```foxpro
LOCAL loSvr, laTest
loSvr = NEWOBJECT("t1.arrayhandler")
DIMENSION laTest[10]
laTest=3
? COMARRAY(loSvr,11 + 100)
* The COM server will return an error on the next line of code
* because arrays passed to loSvr will not allow re-dimensioning.
loSvr.RedimensionArray(@laTest,4)
? ALEN(laTest)
DEFINE CLASS ARRAYHANDLER AS CUSTOM OLEPUBLIC
    PROCEDURE RedimensionArray(aArray, nRows)
        DIME aArray[nRows]
    ENDPROC
ENDDEFINE
```
