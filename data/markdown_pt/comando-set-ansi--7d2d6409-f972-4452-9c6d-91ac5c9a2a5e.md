# Comando SET ANSI

Especifica se deve preencher uma cadeia de caracteres mais curta com espaços ao fazer uma comparação de cadeia de caracteres SQL ou expressão binária com bytes zero (0) ao fazer uma comparação de expressão binária em comandos SQL usando o operador de sinal de igual (=).

> **Observação:** No Provedor OLE DB do Visual FoxPro, você não pode consultar o valor de ANSI usando o comando SET, embora SET ANSI seja suportado.

```foxpro
SET ANSI ON | OFF
```

#### Parâmetros
 **ON**
Preenche a cadeia de caracteres ou expressão binária mais curta com espaços ou bytes zero (0), respectivamente, necessários para torná-la igual ao comprimento da cadeia de caracteres ou expressão mais longa. Quando SET ANSI está definido como ON, as duas cadeias de caracteres ou expressões são comparadas caractere por caractere em todo o seu comprimento.
**OFF**
Especifica que a cadeia de caracteres mais curta não seja preenchida com espaços ou que a expressão binária não seja preenchida com bytes zero (0). (Padrão) Quando SET ANSI está definido como OFF, as duas cadeias de caracteres são comparadas caractere por caractere até o final da cadeia de caracteres mais curta ser atingido.

# Observações

SET ANSI não tem efeito no operador de sinal de igual duplo (==). Quando você usa o operador ==, a cadeia de caracteres ou expressão binária mais curta é sempre preenchida com espaços ou bytes zero (0), respectivamente, para a comparação. Para obter mais informações, consulte Operadores relacionais.

SET ANSI tem escopo na sessão de dados atual.

SET ANSI e o Query Designer O Visual FoxPro constrói um comando SELECT - SQL no Query and View Designers quando você cria uma consulta. Ao criar condições de Join e Filter, se você escolher as opções Equal ou Exactly Like, o operador = ou == é incluído no SELECT gerado. A configuração SET ANSI pode afetar os resultados das consultas que você cria e executa no Query Designer.

Ordem de cadeias de caracteres Em comandos SQL, a ordem da esquerda para a direita das duas cadeias de caracteres em uma comparação é irrelevante — trocar uma cadeia de caracteres de um lado do operador = ou == para o outro não afeta o resultado da comparação.

# Exemplo

O exemplo a seguir cria um cursor com um registro e depois demonstra como SET ANSI afeta os resultados da consulta. Quando SET ANSI está definido como OFF, o resultado é um porque as cadeias de caracteres são comparadas com base na mais curta. 'Tommy' torna-se 'Tom', e as cadeias de caracteres 'Tom' e 'Tom' correspondem caractere por caractere.

Quando SET ANSI está definido como ON, o resultado é zero porque as cadeias de caracteres são comparadas com base na mais curta preenchida com espaços. 'Tom' torna-se 'Tom ', e as cadeias de caracteres 'Tom ' e 'Tommy' não correspondem caractere por caractere:

```foxpro
CLEAR
CREATE CURSOR Dummy (name c(10))
INSERT INTO Dummy VALUES ("Tommy")
SET ANSI OFF
SELECT * FROM Dummy WHERE name="Tom" INTO CURSOR result
?"With ANSI",SET("Ansi"),_tally     && shows 1
SET ANSI ON
SELECT * FROM Dummy WHERE name="Tom" INTO CURSOR result
?"With ANSI",SET("Ansi"),_tally     && shows 0
```
