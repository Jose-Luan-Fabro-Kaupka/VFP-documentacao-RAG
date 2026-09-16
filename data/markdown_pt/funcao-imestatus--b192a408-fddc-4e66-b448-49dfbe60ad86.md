# Função IMESTATUS( )

Ativa ou desativa a janela IME (Input Method Editor) ou retorna o status atual do IME.

```foxpro
IMESTATUS([nExpression])
```

#### Parâmetros
 **nExpression**
Ativa ou desativa a janela IME. A tabela a seguir lista os valores de nExpression e o estado correspondente da janela IME. nExpression Ação da janela IME 0 Desativa a janela IME. 1 Ativa a janela IME. Se nExpression for omitido, IMESTATUS( ) retorna o status atual do IME. A tabela a seguir lista os valores retornados para o status do IME. Use VERSION(3) para determinar o local atual. A tabela a seguir lista os valores retornados para o status do IME no local japonês. Valor de retorno Status do IME 0 Nenhum IME instalado 1 IME ativado 2 IME desativado 3 IME desabilitado 4 Modo Hiragana (double-byte) 5 Modo Katakana (double-byte) 6 Modo Katakana (single-byte) 7 Modo alfanumérico (double-byte) 8 Modo alfanumérico (single-byte) A tabela a seguir lista os valores retornados para o status do IME no local coreano. Valor de retorno Status do IME 0 Nenhum IME instalado 1 Modo Hangul (single-byte) 2 Modo inglês (single-byte) 11 Modo inglês (double-byte) 15 Modo Hangul (double-byte) 23 Modo de conversão Hanja (Hangul + single-byte) 31 Modo de conversão Hanja (Hangul + double-byte)

# Valor de retorno

Numérico

# Observações

Para obter mais informações, consulte Developing International Applications.

Esta função é útil para manipular conjuntos de caracteres de byte duplo para idiomas como Hiragana e Katakana.
