# GitHub prática de mercado

# **Branch**

**Começar a codar ———→  untracked ——> git add . ——> staged ——> git commit -m “” ———-> local ( Git ) ——→ git push ——→ remote ( GitHub)**

#### User 1 → new branch

git clone ( cópia completa de um repositório que já existe (no GitHub)  ———->  Fazer alterações necessárias no projeto ———→ new branch git checkout -b … ———> Nova branch ( ex, usuário_um ) ——→ git add . ou  < … >  ———> git commit -m “” ( alterações feitas ) ———→       git push ——→ Ir no repositório do projeto, criar um pull requests 

- Despois de fazer toda a documentação do pull requests e cria-lo, a parte de merge pull requests vai ser todo configurado a partir das metricas da empresa, normalmente vai precissar de correção de outros devs mais experientes

#### git pull --rebase origin main

**O que ele faz?**

Quando você roda esse comando, o Git faz o seguinte:

1. Puxa as novidades da branch `main` do servidor (`origin`).
2. **Retira** temporariamente os seus commits locais que ainda não foram enviados.
3. Aplica os commits novos que vieram do servidor.
4. **Reaplica** os seus commits logo após os commits que acabaram de chegar.
- Use para **limpar** seu histórico local.
- Use para **organizar** sua branch antes do Pull Request.

#### git rebase —continue

O comando correto é **`git rebase --continue`**. Você o utiliza exclusivamente quando acontece um **conflito** durante o processo de rebase.

Pense no rebase como uma "pausa" que o Git faz sempre que encontra uma dúvida (conflito) ao tentar reaplicar seus commits.

**Pontos importantes:**

- **Não use `git commit`:** Durante um rebase, você não faz um novo commit para resolver conflitos. Você apenas dá o `git add` e o `-continue`. O Git vai "refazer" o seu commit original já com a correção.
- **Vários conflitos:** Se você tiver 5 commits locais, o Git pode parar 5 vezes (uma para cada commit). Você repetirá o processo de resolver, dar `add` e `-continue` até ele terminar.
- **Bateu o desespero?** Se os conflitos estiverem muito difíceis e você quiser cancelar tudo e voltar para como estava antes de começar o rebase, use:
    
    **bash**
    
    `git rebase --abort`
    

no final de um rebase ele abre o **editor de texto padrão** do seu terminal (geralmente o **Vim** ou o **Nano**).

**Para salvar e sair:** Digite `:wq` e aperte **Enter**
**Para sair sem salvar (cancelar):** Digite `:q!` e aperte **Enter**

O comando `git push -f` (ou `--force`) **é usado para forçar o envio dos seus commits para o servidor**, substituindo o histórico que está lá pelo histórico que está na sua máquina.