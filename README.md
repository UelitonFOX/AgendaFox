
# AgendaFox - Gerenciamento de Tarefas

O projeto **AgendaFox** tem como objetivo fornecer um sistema simples e eficiente para o gerenciamento de tarefas pessoais. O sistema permite adicionar, listar, atualizar, excluir e marcar tarefas como concluídas, utilizando uma interface gráfica desenvolvida em Tkinter.

---

## Funcionalidades

- Adicionar tarefas.
- Listar todas as tarefas.
- Atualizar tarefas.
- Excluir tarefas.
- Marcar tarefas como concluídas.
- Interface gráfica intuitiva e organizada utilizando Tkinter.

---

## Cronograma

- **Planejamento**: 24/11/2024 (início).
- **Desenvolvimento das funcionalidades principais**: 24/11/2024.
- **Testes e ajustes finais**: 24/11/2024 (mesmo dia).
- **Conclusão**: 24/11/2024.

---

## Tecnologias Usadas

- **Python 3.x**: Linguagem de programação utilizada.
- **Tkinter**: Biblioteca para desenvolvimento da interface gráfica.
- **Git**: Controle de versão e organização do repositório.

---

## Uso do Git

- Utilizei **branches** para organizar as funcionalidades principais: `feature/interface`, `feature/models`, etc.
- Realizei **commits** frequentes com mensagens claras sobre o que foi alterado ou adicionado.
- Após finalizar uma funcionalidade, fiz o **merge** da branch correspondente para a branch principal (`main`).

---

## Desafios Enfrentados

Durante o desenvolvimento do projeto **AgendaFox**, enfrentei os seguintes desafios:

1. **Erro de Rastreamento no Git**:

   - **Problema**: O repositório rastreava arquivos grandes e indesejados, causando erros durante os commits e pushes.
   - **Solução**: Removi os arquivos indesejados com os comandos:
     ```bash
     git rm -r --cached <arquivo>
     git commit -m "Removendo arquivos indesejados do rastreamento"
     ```

     Adicionei as regras adequadas no arquivo `.gitignore` para evitar que esses arquivos fossem rastreados novamente.
2. **Falha ao Trocar de Branch**:

   - **Problema**: O Git apresentava um erro ao tentar alternar entre branches devido a arquivos bloqueados ou corrompidos.
   - **Solução**: Identifiquei o problema com o arquivo `index.lock` no diretório `.git` e o removi manualmente:
     ```bash
     rm -f .git/index.lock
     ```
3. **Estrutura do Layout da Interface**:

   - **Problema**: A interface inicial estava desalinhada e dificultava a navegação do usuário.
   - **Solução**: Adotei o uso do método `grid()` para organizar os elementos da interface, o que resultou em uma disposição mais clara e intuitiva.
4. **Validação de Dados**:

   - **Problema**: Durante a execução, tarefas com campos vazios causavam erros.
   - **Solução**: Implementei validações nos campos de entrada para garantir que todos os dados necessários fossem preenchidos antes de processar as tarefas.
5. **Integração entre Views e Models**:

   - **Problema**: Inicialmente, as funções de manipulação de tarefas estavam diretamente na interface, dificultando a manutenção do código.
   - **Solução**: Refatorei o código para separar as responsabilidades, movendo a lógica para o arquivo `models.py`.
6. **Gestão de Branches**:

   - **Problema**: Inicialmente, todo o trabalho estava sendo feito na branch principal (`main`), o que dificultava a organização e a rastreabilidade.
   - **Solução**: Implementei um fluxo de trabalho com branches específicas para cada funcionalidade, como `feature/interface` e `feature/models`, permitindo maior organização e controle.

---

## Observações Finais

Este projeto tem como objetivo aplicar o uso do Git para controle de versão, além de fornecer uma solução simples de gerenciamento de tarefas com uma interface gráfica.

Futuras melhorias podem incluir o cadastro de clientes, controle financeiro, e até mesmo a possibilidade de marcar tarefas como concluídas. O desenvolvimento contínuo do projeto será realizado conforme as necessidades surgirem.
