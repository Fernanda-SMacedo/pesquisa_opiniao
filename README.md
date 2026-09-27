📊 Pesquisa de Satisfação - Atendimento ao Cliente

📌 Sobre o Projeto

Este projeto consiste em um sistema em Python desenvolvido para automatizar a coleta e compilação de feedbacks de atendimento ao cliente.

O script realiza o atendimento interativo de 50 entrevistados, coletando informações pessoais e avaliações do serviço prestado, exibindo ao final um relatório com a contagem de respostas satisfatórias e insatisfatórias.

⚙️ Regras de Negócio e Funcionalidades

Coleta de Dados: Para cada entrevistado, o sistema solicita:
Nome do participante.
Idade do participante.
Opinião sobre o atendimento:
1: EXCELENTE; 2: BOM ou 3: RUIM

Estrutura de Repetição:
Utilização do laço while para gerenciar o fluxo de entrevistas até atingir o limite de 50 pessoas.

Contabilidade e Relatório Final:
Durante a execução, o programa incrementa contadores específicos para as avaliações extremas.

Ao término do ciclo, o sistema exibe:
a) Quantidade total de respostas EXCELENTE (Opção 1).
b) Quantidade total de respostas RUIM (Opção 3).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3
Estruturas de Repetição: Laço while com variável contadora.
Estruturas Condicionais: if e elif para classificação e acumulação das notas.

💡 Dica de Teste: Caso queira testar a execução completa sem preencher os 50 cadastros, você pode alterar temporariamente a linha while contador <= 50: para um número menor (como while contador <=3:).