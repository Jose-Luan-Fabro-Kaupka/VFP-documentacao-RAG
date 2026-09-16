# Função VERSION( )

Retorna informações sobre a versão do Visual FoxPro que você está usando.

```foxpro
VERSION([nExpression])
```

#### Parâmetros
 **nExpression**
Especifica que VERSION( ) retorna informações adicionais sobre o Visual FoxPro. Se você omitir nExpression, VERSION( ) retorna o número da versão do Visual FoxPro. A tabela a seguir lista os valores de nExpression e as informações adicionais do Visual FoxPro retornadas. nExpression Informações adicionais do Visual FoxPro retornadas 1 Data e número de série do Visual FoxPro. 2 Tipo de versão do Visual FoxPro: 0 - Versão run time 1 - Standard Edition (versões anteriores) 2 - Professional Edition (versões anteriores) 3 Idioma localizado do Visual FoxPro. Os seguintes valores de dois caracteres indicam o idioma para o qual o Visual FoxPro está localizado: 00 - Inglês 07 - Russo 33 - Francês 34 - Espanhol 39 - Tcheco 48 - Alemão 55 - Coreano 42 - Tcheco 49 - Alemão 82 - Coreano 86 - Chinês simplificado 88 - Chinês tradicional 4 O número da versão do Visual FoxPro em um formato padrão, facilmente analisável. Para versões anteriores ao Visual FoxPro 8.0, o formato padrão é "MM.mm.0000.DDDD", onde MM é o número da versão principal, mm é o número da revisão incremental menor, 0000 é um espaço reservado fixo e DDDD é a data do produto de quatro dígitos do dia em que a versão foi criada. Para o Visual FoxPro 8.0, a fórmula para calcular a data do produto, DDDD, é 8000 + número de dias desde o início de 1998. Por exemplo, 8397 corresponde a 1 de fevereiro de 1999. Para o Visual FoxPro 9.0, a fórmula para calcular a data do produto, DDDD, é o número de meses desde 1 de janeiro de 2003 concatenado com o dia do mês atual. Por exemplo, 2215 corresponde a 15 de outubro de 2004. O formato para o Visual FoxPro 8.0 e 9.0 é "MM.mm.0000.NNNN", onde MM é o número da versão principal, mm é o número da revisão incremental menor, 0000 é um espaço reservado fixo e NNNN é o número de compilação. 5 A versão de lançamento do Visual FoxPro no formato Mmm, onde M é o número da versão principal e mm é o número da revisão incremental menor. Por exemplo, VERSION(5) retorna 700 no Visual FoxPro 7.0.

# Valor de retorno

Caractere, Numérico

# Observações

Use VERSION( ) para executar condicionalmente partes de código específicas da versão.

VERSION( ), VERSION(1), VERSION(3) e VERSION(4) retornam cadeias de caracteres; VERSION(2) e VERSION(5) retornam valores numéricos.

# Exemplo

```foxpro
CLEAR
? VERSION()
? VERSION(1)
? VERSION(2)
? VERSION(3)
? VERSION(4)
? VERSION(5)
```
