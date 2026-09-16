# Este comando não é suportado para views (Erro 1777)

Views não podem ser alteradas com este comando. Este erro tem as seguintes causas e soluções:
 - Uso de um dos seguintes comandos para alterar a estrutura da view: ALTER TABLE, CREATE TRIGGER, DELETE TRIGGER e MODIFY STRUCTURE. Use um comando que opere em views ou use uma tabela.
- Modificação da estrutura de um cursor de view com o Table Designer. Use o View Designer para modificar permanentemente a estrutura de cursors produzidos com uma definição de view.
