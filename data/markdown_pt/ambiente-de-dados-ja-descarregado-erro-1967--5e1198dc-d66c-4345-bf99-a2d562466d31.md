# Ambiente de dados já descarregado (Erro 1967)

O formulário está tentando fechar tabelas ao encerrar.
 - AutoCloseTables está definido como true (.T.). Não feche programaticamente as tabelas do ambiente de dados.
- O método CloseTables está sendo chamado antes do formulário ser fechado. Defina AutoCloseTables como false (.F.).
