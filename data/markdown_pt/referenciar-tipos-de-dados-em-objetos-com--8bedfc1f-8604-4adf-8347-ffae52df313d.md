# Referenciar tipos de dados em objetos COM

Quando você usa o Visual FoxPro como cliente de early binding e deseja referenciar um tipo de dados variant em um objeto COM, você deve primeiro criar uma instância da variável com o tipo que espera recuperar. Por exemplo:

```foxpro
DEFINE CLASS varianttest AS SESSION OLEPUBLIC
   FUNCTION varret(outVal AS VARIANT@, inVal AS VARIANT) AS VOID
      OutVal = inVal
   ENDFUNC
ENDDEFINE
```

Depois de compilar esta classe em uma DLL chamada myServer, você pode referenciar os dados conforme mostrado no código a seguir:

```foxpro
x = CREATEOBJECT("myServer.varianttest","","")
ov = ""
tt.varret(@ov, "string")   && Sets string value.
ov = 0
tt.varret(@ov, 123)         && Sets ov to an integer value.
ov = 0.0
tt.varret(@ov, 44.44)      && Sets ov to a real numeric value.
ov = l
tt.varret(@ov, f)            && Sets ov to a Boolean value.
```
