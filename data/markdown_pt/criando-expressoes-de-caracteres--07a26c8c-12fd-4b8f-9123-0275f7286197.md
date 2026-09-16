# Criando expressões de caracteres

Componha expressões de caracteres combinando operadores de caracteres com os seguintes elementos do Visual FoxPro:
 - Campos de caracteres.
- Funções que retornam valores de caracteres.
- Variáveis e elementos de matriz que contêm dados de caracteres.
- Constantes de caracteres, chamadas de literais de cadeia de caracteres.

Você pode incorporar aspas ("" ou '') em uma cadeia de caracteres colocando-a entre colchetes ([]):

```foxpro
STORE [Robert's Diner] TO cCompanyName
STORE [See the "Sunday Special"] TO cBanner
```

Você também pode incorporar aspas colocando a cadeia de caracteres entre aspas do tipo alternativo:

```foxpro
STORE "Robert's Diner" TO cCompanyName
STORE 'See the "Sunday Special"' TO cBanner
```

Para obter mais informações, consulte o comando STORE.
