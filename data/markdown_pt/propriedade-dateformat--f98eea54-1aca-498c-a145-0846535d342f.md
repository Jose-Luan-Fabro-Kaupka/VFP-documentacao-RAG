# Propriedade DateFormat

Especifica o formato para valores Date e DateTime exibidos em uma caixa de texto. Disponível em tempo de design e em tempo de execução.

```foxpro
Object.DateFormat[ = nValue]
```

# Valor de retorno
 **nValue**
Uma das seguintes configurações: Configuração Descrição Formato 0 (Padrão) O formato de data exibido é determinado pela configuração de SET DATE. Determinado por SET DATE 1 Americano mm/dd/aa 2 ANSI aa.mm.dd 3 Britânico dd/mm/aa 4 Italiano dd-mm-aa 5 Francês dd/mm/aa 6 Alemão dd.mm.aa 7 Japão aa/mm/dd 8 Taiwan aa/mm/dd 9 EUA mm-dd-aa 10 MDY mm/dd/aa 11 DMY dd/mm/aa 12 YMD aa/mm/dd 13 Curto Determinado pela configuração de data curta do Painel de Controle do Windows 14 Longo Determinado pela configuração de data longa do Painel de Controle do Windows

# Observações

Aplica-se a: Controle TextBox (Visual FoxPro)

Um valor Date ou DateTime exibido em uma caixa de texto pode ser exibido em um formato diferente quando a caixa de texto não tem o foco. Certos formatos de data curta e longa que você pode especificar no Painel de Controle do Windows não correspondem a formatos válidos do Visual FoxPro e são exibidos em um formato padrão.

A propriedade Format substitui a propriedade DateFormat quando as configurações YS, YL, E ou D são especificadas para a propriedade Format.
