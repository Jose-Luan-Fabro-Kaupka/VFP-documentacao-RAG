# Função DISKSPACE( )

Recupera o número de bytes com o tipo especificado que estão disponíveis na unidade de disco rígido ou volume padrão ou especificado.

```foxpro
DISKSPACE([cVolumeName [, nType]])
```

#### Parâmetros
 **cVolumeName**
Especifica o nome da unidade de disco rígido ou volume para o qual o espaço disponível é retornado. Se você omitir cVolumeName, o espaço disponível é retornado para a unidade de disco ou volume padrão.
**nType**
Especifica o tipo de espaço em disco rígido a recuperar. A tabela a seguir lista os valores de nType. Valor Descrição 1 Quantidade total de espaço na unidade de disco rígido. 2 Quantidade total de espaço livre na unidade de disco rígido. (Padrão) 3 Quantidade total de espaço livre disponível para o usuário associado à thread de chamada.

# Valor de retorno

Numeric. DISKSPACE( ) retorna o número de bytes com o tipo especificado. Se o disco rígido estiver cheio, DISKSPACE( ) retorna um valor de 0 ou -1. Se ocorrer um erro ao ler a unidade de disco rígido ou volume, DISKSPACE( ) também pode retornar um valor de –1.

> **Observação:** O valor de retorno de DISKSPACE( ) pode não ser preciso para unidades de rede grandes em algumas redes. Além disso, DISKSPACE( ) pode retornar -1 para certos diretórios com nomes longos no Windows 98.

# Observações

Você pode usar DISKSPACE( ) para determinar se há espaço suficiente disponível para fazer backup de arquivos ou executar comandos como SORT que exigem espaço adicional em disco para arquivos de trabalho temporários.

Você pode especificar a unidade de disco ou volume padrão usando o comando SET DEFAULT.

# Exemplo

O exemplo a seguir usa DISKSPACE( ) para determinar se há espaço em disco suficiente para realizar uma operação de classificação.

```foxpro
*** Check DISKSPACE before sort ***
CLOSE DATABASES
OPEN DATABASE (HOME(2) + 'Data\testdata')
USE customer  && Opens Customer table
*** Get size of table header ***
gnTableHead = HEADER()
*** Calculate size of table ***
gnFileSize = gnTableHead + (RECSIZE() * RECCOUNT() + 1)
IF DISKSPACE() > (gnFileSize * 3)
   WAIT WINDOW 'Sufficient diskspace to sort.'
ELSE
   WAIT WINDOW 'Insufficient diskspace. Sort cannot be done.'
ENDIF
```
