# Comando SET COLLATE

Especifica uma sequência de ordenação para campos de caractere em operações subsequentes de indexação e classificação.

```foxpro
SET COLLATE TO cSequenceName
```

#### Parâmetros
 **cSequenceName**
Especifica uma sequência de ordenação. A tabela a seguir lista as opções de sequência de ordenação disponíveis. cSequenceName Idioma ARABIC Árabe CZECH Tcheco DUTCH Holandês GENERAL Inglês, francês, alemão, espanhol moderno, português e outros idiomas da Europa Ocidental GERMAN Ordem de agenda telefônica alemã (DIN) GREEK Grego HEBREW Hebraico HUNGARY Húngaro ICELAND Islandês JAPANESE Japonês KOREAN Coreano MACHINE Máquina (a sequência de ordenação padrão para versões anteriores do FoxPro) NORDAN Norueguês, dinamarquês PINYIN Chinês simplificado POLISH Polonês RUSSIAN Russo SLOVAK Eslovaco SPANISH Espanhol tradicional STROKE Chinês simplificado e tradicional SWEFIN Sueco, finlandês THAI Tailandês TURKISH Turco UNIQWT Peso único Observação Quando você especifica a opção SPANISH, "ch" é uma única letra que se ordena entre "c" e "d", e "ll" se ordena entre "l" e "m". Se você especificar uma opção de sequência de ordenação como uma cadeia de caracteres literal, certifique-se de colocar a opção entre aspas: SET COLLATE TO "SWEFIN" MACHINE é a opção de sequência de ordenação padrão e é a sequência com a qual os usuários do FoxPro estão familiarizados. Os caracteres são ordenados conforme aparecem na página de código atual. A sequência de ordenação MACHINE oferece o melhor desempenho. Usar uma sequência de ordenação diferente de MACHINE pode reduzir o desempenho principalmente em operações de comparação e indexação, e pode criar arquivos de índice maiores. GENERAL pode ser preferível para usuários dos EUA e da Europa Ocidental. Os caracteres são ordenados conforme aparecem na página de código atual. Em versões do FoxPro anteriores à 2.5, você poderia ter usado UPPER( ) ou LOWER( ) em campos de caractere ao criar índices. Em versões do FoxPro posteriores à 2.5, você pode especificar a opção de sequência de ordenação GENERAL e omitir a conversão UPPER( ) em vez disso. Se você especificar uma opção de sequência de ordenação diferente de MACHINE e criar um arquivo .idx, um .idx compacto é sempre criado. Use SET("COLLATE") para retornar a sequência de ordenação atual. Se você incluir a seguinte linha no arquivo de configuração do Visual FoxPro, uma sequência de ordenação é especificada quando você inicia o Visual FoxPro: COLLATE = cSequenceName Isso é idêntico a emitir o seguinte comando: SET COLLATE TO cSequenceName

# Observações

SET COLLATE permite ordenar tabelas contendo caracteres acentuados para qualquer um dos idiomas suportados. Alterar a configuração de SET COLLATE não afeta a sequência de ordenação de índices abertos anteriormente. O Visual FoxPro mantém automaticamente os índices existentes, proporcionando a flexibilidade de criar muitos tipos diferentes de índices, mesmo para o mesmo campo.

Por exemplo, se um índice é criado com SET COLLATE definido como GENERAL, e a configuração de SET COLLATE for alterada posteriormente para SPANISH, o índice mantém a sequência de ordenação GENERAL.

SET COLLATE tem escopo na sessão de dados atual.

Ao usar o comando SET COLLATE TO, você pode receber o erro "Collating sequence <sequencename> is not found." Isso ocorre quando você tenta usar uma sequência de ordenação que não é suportada pela página de código atual. Para evitar esse erro, você deve especificar uma página de código compatível no arquivo de configuração do Visual FoxPro. Por exemplo, você pode ver o erro "Collating sequence 'CZECH' is not found" ao emitir o comando `SET COLLATE TO 'CZECH'`. Para habilitar o suporte à sequência de ordenação tcheca, adicione a seguinte linha ao seu arquivo config.fpw e reinicie o Visual FoxPro:

```foxpro
CODEPAGE = 1250
```

Para informações adicionais sobre páginas de código e o suporte internacional do Visual FoxPro, consulte Páginas de código suportadas pelo Visual FoxPro em Desenvolvendo aplicativos internacionais.

Para obter mais informações sobre como configurar o Visual FoxPro, consulte Personalizando o ambiente do Visual FoxPro e Termos especiais para arquivos de configuração.
