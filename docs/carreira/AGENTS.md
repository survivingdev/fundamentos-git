# Instruções de execução e continuidade

Estas instruções aplicam-se à documentação de Carreira Data & AI em docs/carreira. A solicitação mais recente do usuário prevalece. Ler HANDOFF.md ao assumir e retomar a próxima ação; não reiniciar etapas aprovadas.

## Aprendizagem e evidência

O mentor pode executar pesquisa, organização, revisão, verificações e documentação autorizadas. O participante realiza o raciocínio, a implementação fundamental, a conferência e a defesa das avaliações pessoais. Não resolver automaticamente um exercício destinado a medir autonomia. Registrar a ajuda; uma solução fornecida converte a tentativa em prática assistida.

Para cada checkpoint pedagógico: competência/escopo, objetivo observável, exercício curto, critérios e ajuda permitida. Oferecer explicação e exemplo progressivo quando necessário; colher tentativa antes de solução completa. Se houver ensino socrático intensivo, sugerir chat dedicado com contexto e devolver o resultado ao registro central. Não exigir troca de chat para duas perguntas simples.

Não atribuir domínio por publicação, tempo, curso, exame ou código de IA. Usar rubrica existente, com dimensões separadas e retenção posterior. Preservar os IDs e as avaliações pendentes. Este commit documental não é uma demonstração independente do aluno.

## Fechamento de cada sessão relevante

1. Registrar em PROGRESSO.md: data America/Sao_Paulo, tarefa/escopo, tentativa, resultado, evidência, ajuda, duração informada e pendência. Se desconhecido, indicar desconhecido; não criar nota zero.
2. Atualizar HANDOFF.md: etapa/subetapa, concluído, em andamento, próxima ação específica, evidências/versões e limites. Atualizar os demais registros apenas nas partes que realmente mudaram. Atualizar a planilha privada quando houver nova hora, avaliação, tarefa ou candidatura pertencente a ela; não converter todos os arquivos legados em diários duplicados.
3. Para encerramento de sessão ou marco significativo, reservar CP sequencial, sem sobrescrever manifesto anterior. Se a sessão for longa, salvar também antes de operação extensa ou mudança de contexto. Uma interrupção sem salvamento recupera somente o último checkpoint persistido.
4. Gerar checkpoints/CP-nnnn.json com data/fuso, checkpoint anterior, HEAD remoto esperado, resumo de estado, evidências e arquivos com tamanho/SHA-256. Registrar fontes externas com identidade/versão/hash quando houver alteração ou nova dependência. Não colocar o SHA do próprio commit dentro do manifesto; a versão é o commit que o contém.
5. Rodar scripts/verificar_checkpoint.py no manifesto. Revisar diferença, privacidade, links locais, coerência de estados e ausência de solução pronta da avaliação ativa. Publicar somente os arquivos autorizados desta documentação, em um commit com mensagem `Registra CP-nnnn: <mudança>`.
6. Preservar histórico: fast-forward, sem reescrever os commits do exercício. Usar o HEAD remoto observado como condição de atualização. Se tiver avançado, ler as mudanças e integrar antes de publicar. Não forçar ou sobrescrever alterações concorrentes.
7. Ler de volta o HEAD/commit e a árvore/arquivos relevantes e conferir hashes/ancestralidade. Só então informar o checkpoint como publicado, com link imutável do commit e link do HANDOFF atual. Atualizar as referências dos registros privados que forem alterados nesta sessão, preservando suas identidades. Não é necessário republicar toda a pesquisa.
8. Se falhar publicação ou gravação privada, dizer exatamente qual parte ficou sem confirmação; manter o último checkpoint bom e persistir o que for possível. Não declarar confirmação de uma etapa ainda em execução.

Um checkpoint de continuidade documenta o estado. Marco M1–M4 depende de avaliação própria. Não criar novas ferramentas, repositórios, cursos ou fluxos de aprovação sem necessidade.

## Fonte de verdade e privacidade

Usar FONTES.md para as referências públicas e o handoff privado para as fontes restritas. Registros correntes de execução ficam nestes Markdown; a planilha preserva seu papel privado de horas/avaliações/candidaturas. Os detalhes sensíveis e transcrições não são publicados no Git público. Não incluir links ou identificadores de arquivos privados no Git público; nunca gravar senha, token, credencial, URL autenticada temporária ou chave privada. O noreply já publicado não é segredo.

Antes de publicar novo conteúdo pessoal ou dados de fonte externa, verificar o escopo autorizado e as condições concretas. Gastos/inscrições e mudanças estruturais de rota/carga dependem de decisão explícita. A manutenção documental e verificações desta estrutura já foram autorizadas; não pedir nova confirmação para cada atualização.

## Retomar a prática local após atualização remota

O Work não operou o computador do participante. Antes de nova alteração local, pedir as consultas necessárias, por exemplo status resumido, branch atual, remoto e histórico recente. Não obter e-mails pessoais ou credenciais sem necessidade. Comparar com a referência remota atual.

Se for main, o remoto corresponder ao destino e a árvore estiver limpa, uma atualização operacional pode usar `git pull --ff-only origin main` dentro do repositório local confirmado. Confirmar o resultado e o conteúdo antes da prática. Se houver alterações, branch diferente, conflito ou divergência, preservar tudo e diagnosticar; não usar reset --hard, clean, rebase automático ou force push. Não repetir remote add quando origin já existe.

Essas consultas e a sincronização podem ser orientadas como apoio operacional. A avaliação individual posterior recebe objetivo e critérios, não uma solução completa de comandos. Não repetir o roteiro antigo que exigia exatamente dois commits; o CP acrescentou documentação ao histórico.

Referências técnicas: [git pull](https://git-scm.com/docs/git-pull), [git log](https://git-scm.com/docs/git-log) e [git ls-remote](https://git-scm.com/docs/git-ls-remote), consultadas em 25/10/2026 para o procedimento operacional.
