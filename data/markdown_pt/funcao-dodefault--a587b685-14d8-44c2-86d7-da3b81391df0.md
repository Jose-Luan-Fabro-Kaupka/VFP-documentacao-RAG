# Função DODEFAULT( )

Executa o evento ou método da classe pai de mesmo nome a partir de uma subclasse.

Por exemplo, se você colocar DODEFAULT( ) no evento Click de uma subclasse, o Visual FoxPro executa o evento Click da classe pai. O operador de resolução de escopo (::), diferentemente de DODEFAULT( ), executa um evento ou método da classe pai com um nome diferente.

> **Observação:** Você pode colocar DODEFAULT( ) somente dentro de um evento ou método.

```foxpro
DODEFAULT( [ eParameter1 [, eParameter2] ...] )
```

#### Parâmetros
 **eParameter1 [, eParameter2 ] ...**
Especifica parâmetros que são passados para o evento ou método da classe pai.

# Valor de retorno

Character, Numeric, Currency, Date, DateTime, Logical ou Memo

# Observações

O valor que DODEFAULT( ) retorna é determinado pelo valor de retorno do evento ou método.

Em versões anteriores ao Visual FoxPro 8.0, você não podia chamar DODEFAULT( ) em um método que não existia na classe pai sem que o Visual FoxPro gerasse um erro, "Property name is not found (Error 1734)", retornasse True (.T.) e ignorasse DODEFAULT( ) e quaisquer parâmetros passados. No entanto, o Visual FoxPro agora ignora isso e não gera um erro, mas os seguintes resultados ainda ocorrem:
 - O Visual FoxPro ignora quaisquer parâmetros passados porque nenhum código é executado.
- O Visual FoxPro sempre retorna True (.T.), que é o comportamento padrão para qualquer procedimento sem uma instrução RETURN explícita.

Este comportamento afeta os seguintes cenários:
 - Métodos personalizados definidos em uma classe. Por exemplo, a linha x.Test() gerava um erro antes do Visual FoxPro 8.0, mas não gera mais: CLEAR x=CREATEOBJECT("s1") x.ReadMethod("Init") x.Test() DEFINE CLASS s1 AS Session PROCEDURE Test DODEFAULT() ENDPROC PROCEDURE ReadMethod(cMethod) DODEFAULT(cMethod) ENDPROC PROCEDURE Error(nError, cMethod, nLine) ? "Error:", nError, cMethod, nLine ENDPROC ENDDEFINE
- Métodos nativos marcados com a palavra-chave HIDDEN na classe pai. Por exemplo: CLEAR x=CREATEOBJECT("s2") x.Test() DEFINE CLASS s2 AS s1 PROCEDURE Test THIS.ReadMethod("Init") ENDPROC PROCEDURE ReadMethod(cMethod) DODEFAULT(cMethod) ENDPROC ENDDEFINE DEFINE CLASS s1 AS Session HIDDEN PROCEDURE ReadMethod(cMethod) DODEFAULT(cMethod) ENDPROC PROCEDURE Error(nError, cMethod, nLine) ? "Error:", nError, cMethod, nLine ENDPROC ENDDEFINE

A partir do Visual FoxPro 7.0, chamar um método nativo em uma classe base que contém DODEFAULT( ) não causa um erro. Por exemplo:

```foxpro
CLEAR
x=CREATEOBJECT("s1")
x.ReadMethod("Init")
DEFINE CLASS s1 AS Session
   PROCEDURE ReadMethod(cMethod)
      DODEFAULT(cMethod)
   ENDPROC
   PROCEDURE Error(nError, cMethod, nLine)
      ? "Error:", nError, cMethod, nLine
   ENDPROC
ENDDEFINE
```
