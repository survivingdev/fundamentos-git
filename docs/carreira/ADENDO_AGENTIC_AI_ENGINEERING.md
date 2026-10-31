# ADENDO — AGENTIC AI ENGINEERING

**Escopo aprovado em 31/10/2026 · CP-0003.** Integração curricular dentro da Etapa 7, com aprendizagem ainda em F0. Nenhuma competência nova estudada ou avaliada por este checkpoint.

Preservam-se C01–C30, R01–R19, K01–K09, E01–E08 e P01/P02. Os sete subescopos e AG-Rxx complementam os registros. Blocos condicionais: F3 12–20 h (base 16), F4 16–24 h (base 20), F5/X-IA 20–36 h (base 28); total adicional 48–80 h, base 64, após pré-requisitos. Não são barreira universal de M1/M2/M3 nem aprovação de compra.

## 3. Auditoria da base anterior à integração

A tabela descreve o currículo auditado antes da inclusão dos novos subescopos. As seções curriculares seguintes registram o detalhamento aprovado, ainda não estudado ou avaliado.

**Critérios:** explícita = há conteúdo e evidência prevista para o tema; parcial = há uma parte útil, mas falta especificação necessária; ausente = não foi localizada previsão operacional explícita no corpus consultado. Essas categorias avaliam o currículo, não a competência de Paulo.

| Tema | Cobertura atual | Evidência canônica | Lacuna ou ajuste necessário |
| --- | --- | --- | --- |
| Python, software, testes, Git e APIs | Explícita | C06/C11/C13/C14/C26; F3; R06/R08/R09 | Reaproveitar como pré-requisitos; não reaprender como curso paralelo |
| Baseline sem IA e justificativa de utilidade | Explícita | C27; X-IA; DoD de F5 | Acrescentar decisão específica entre fluxo fixo, chamada de LLM e agente |
| Saídas estruturadas | Explícita | C27 | Detalhar validação de esquema, resposta inválida e integração com ferramentas |
| Consulta por ferramentas com acesso controlado | Parcial | X-IA prevê parâmetros e leitura controlada; proíbe banco irrestrito | Falta especificar seleção de ferramenta, argumentos, despacho, resultados e limites do ciclo |
| Workflow versus agente que decide próximos passos | Ausente como objetivo avaliável | Baseline em C27 ajuda, mas não descreve esse mecanismo | Exigir comparação arquitetural e critério de parada |
| Estado persistente, retomada e isolamento de sessões | Ausente para agentes | C16/C19 tratam pipelines; isso não cobre automaticamente sessões de agentes | Definir estado, persistência, retomada e teste entre sessões |
| Gestão de contexto e memória | Ausente para agentes | Não há exercício explícito de orçamento de contexto ou memória | Incluir seleção, compactação, retenção e prevenção de contaminação entre sessões |
| RAG e qualidade de recuperação | Explícita, condicional | C28; X-IA; recuperação e resposta avaliadas separadamente | Reaproveitar; ampliar vínculo entre permissões, versão do índice e resposta |
| MCP | Ausente | Nenhum objetivo/exercício específico localizado | Introduzir cliente/servidor, schemas, erros, transportes e autorização proporcional |
| Avaliação de qualidade e casos adversos | Explícita em aplicações; parcial em agentes | C27; X-IA já tem casos versionados, reservados e abstenção | Acrescentar trajetórias, múltiplas chamadas, repetições e regressão por versão |
| Observabilidade e sustentação | Parcial | C19/C20 e P02 têm logs, recuperação e operação de dados | Falta tracing por execução de agente, ferramenta e versão; triagem de incidentes de LLM |
| Segurança e autorização | Parcial | C21; X-IA inclui segredos, acesso e instruções adversas | Falta política executável por ferramenta, autorização fora do prompt e ataque indireto via conteúdo |
| Custo e latência | Explícita; detalhamento operacional parcial | C27; F5/X-IA | Incluir custo por tarefa bem-sucedida, limites de passos/tokens e análise de cauda |
| Versionamento e deploy | Explícita para software; parcial para agentes | C06/C20; reprodução e rollback | Versionar também prompt, modelo, ferramentas, avaliação, contexto e índice quando existir |

**Conclusão:** seria incorreto afirmar que agentes estão ausentes de todo o programa. Também seria incorreto considerar o ciclo de vida completo coberto por C27, por uma API de LLM ou pelo título da certificação K09. A maior parte do ajuste é tornar explícita e avaliável a interseção entre C13/C14/C19/C20/C21/C26/C27/C28.

O recurso R15 pode evoluir e conter novos exemplos. Sua disponibilidade atual não acrescenta automaticamente ao currículo temas que não foram selecionados, exercitados ou ligados a critérios de avaliação. Da mesma forma, “agentes de tratamento” no material da ANPD refere-se à proteção de dados, não a agentes de IA.
## 5. Automação simples, workflow e agente

A distinção arquitetural segue a orientação da [Anthropic sobre agentes e workflows][AG-R01]: fluxos predefinidos têm comportamento mais controlável; agentes decidem dinamicamente passos e ferramentas. Maior autonomia deve resolver uma necessidade observável e justificar seu custo.

| Problema | Solução inicial preferida | Quando investigar alternativa |
| --- | --- | --- |
| Baixar arquivo, validar esquema, atualizar tabela e agendar execução | Pipeline determinístico de P02 | LLM não é necessário para seguir regras conhecidas |
| Somar vendas ou calcular preço por período | SQL/Python com regras testadas | Linguagem natural pode ser interface; cálculo continua determinístico |
| Extrair campos ou classificar texto com sequência fixa | Regra ou chamada estruturada de modelo dentro de workflow | Agente só se precisar escolher ações ou buscar evidências de forma variável |
| Responder consulta delimitada sobre um conjunto de dados | Consulta parametrizada ou workflow com ferramentas | Agente candidato se houver escolha variável entre métricas, frescor e metodologia, com benefício medido |
| Diagnosticar uma solicitação ambígua e decidir quais fontes consultar | Agente único, limitado e observável | Comparar qualidade, abstenção, custo e tempo com o fluxo fixo |

RAG, MCP e múltiplos agentes não são sinônimos de agente. RAG é recuperação; MCP é uma interface de integração. Múltiplos agentes só entram depois de um agente único e uma comparação que justifique a coordenação adicional. Browser automation, fine-tuning, Kubernetes e memória de longo prazo irrestrita não entram no núcleo proposto.

## 6. Currículo aprovado e avaliação

### 6.1 Pré-requisitos observáveis

Antes do primeiro laboratório, Paulo deverá implementar e explicar uma função Python, tratar entrada inválida, escrever teste útil, consumir uma API validando a resposta e registrar uma mudança compreendida no Git. Esses são recortes de C06/C11/C13/C14/C21, não exigência de dominar toda a engenharia de software.

Não se exige concluir toda a formação de DS, estatística avançada ou P02 para começar o laboratório de agentes. A atual prática de Git continua sendo o próximo passo, sem inserir estudo de agentes em F0.

### 6.2 Subescopos aprovados, preservando C01–C30

Os sufixos abaixo são **identificadores suplementares aprovados**, incluídos sem renumerar as competências de base. Todos começam como **planejados / não avaliados**. Eles detalham capacidades novas ou aprofundamentos; não criam um novo currículo independente.

| Subescopo | Conhecimento reaproveitado | Aprendizagem nova ou aprofundada | Evidência individual exigida |
| --- | --- | --- | --- |
| C27-A1 — Arquitetura e ferramentas | C13/C14/C27; structured outputs já previstos | Distinguir workflow/agente; schema de ferramentas; despacho; ciclo limitado e critérios de parada | Implementar ferramenta e variação de argumento; defender o limite e diagnosticar chamada inválida |
| C27-A2 — Estado e contexto | Python, persistência e testes | Estado da execução versus histórico; sessão isolada; contexto selecionado; compactação; retomada | Recuperar execução interrompida e provar ausência de troca de contexto entre duas sessões |
| C27-A3 — Avaliação de agentes | Baseline, casos reservados e avaliação de C27 | Resultado final versus trajetória; repetições; regressão; calibração de avaliadores | Criar avaliador verificável, analisar falha inédita e defender métrica sem usar só avaliação por LLM |
| C19-A1 — Operação e manutenção de agentes | Logs, retries, alertas e recuperação de C19 | Traces correlacionados, triagem de falhas de ferramenta/modelo, limites e degradação controlada | Usar trace para localizar falha e demonstrar recuperação/reexecução coerente |
| C26-A1 — Integração MCP | HTTP/JSON, validação, autenticação e serviços | Cliente/servidor, descrição de ferramentas, erros e transportes; autorização conforme exposição | Expor uma ferramenta de leitura e consumi-la por cliente, tratando argumento inválido e acesso indevido |
| C21-A1 — Segurança de agentes | Segredos, minimização, permissões e casos adversos | Autorização executada pelo sistema, conteúdo não confiável, injeção indireta, confirmação de ações e isolamento | Criar teste adverso que detecte uma falha; justificar política de acesso que não depende de obedecer ao prompt |
| C20-A1 — Releases de aplicações com agentes | C06/C13/C20; CI e rollback | Versão conjunta de código/prompt/modelo/tool schema/avaliação e configuração; índice quando existir | Reproduzir release, bloquear regressão crítica e retornar à versão conhecida |

C28 continua condicional. Permissões na recuperação e identificação da versão documental entram como aprofundamento do escopo já existente, sem renumerá-lo.

### 6.3 Inserção aprovada por fase

| Bloco | Ativação e objetivo | Exercício e critérios | Carga adicional líquida |
| --- | --- | --- | ---: |
| F3 — fundamentos delimitados | Depois dos pré-requisitos; ativação por interesse confirmado/oportunidade compatível | **E08-A1:** comparar regra/fluxo fixo e agente único com até três ferramentas de leitura; esquema validado, limite de execução, erro tratado e pequena avaliação definida antes do ajuste | 12–20 h; base 16 h |
| F4 — confiabilidade e operação | Após E08-A1; aprofundamento seletivo, sem bloquear M3 de dados | **E08-A2:** estado persistente, tracing, falhas deliberadas, política de autorização e regressão. Retomar execução, isolar sessões, reconhecer dados desatualizados e preservar resultado válido | 16–24 h; base 20 h |
| F5 — AI Agent Engineering em X-IA | Somente se a especialização de IA for escolhida | **E08-A3:** consolidar produto delimitado, MCP quando útil, RAG se necessário, deploy reproduzível, avaliação reservada e defesa arquitetural | 20–36 h; base 28 h |
| Total da rota completa | Não somar novamente cursos, Python, APIs e testes já contemplados | Estudo, exercícios, documentação, implementação e avaliação estão incluídos na estimativa | **48–80 h; base 64 h** |

São estimativas próprias para planejamento após pré-requisitos, sem calibração por desempenho observado. A F5 original tem reserva ampla e já previa X-IA: o acréscimo desta tabela se refere ao detalhamento adicional de agentes, não à construção de toda a extensão do zero. Ao ativar, descontar qualquer exercício equivalente já demonstrado e reorçar o restante.

A sequência de F3/F4/F5 proposta é adequada, com essa condição importante: **os laboratórios de agentes não passam a ser exigência de todos os percursos.** A trilha de IA pode começar antes da conclusão de toda F4 se os seus próprios pré-requisitos estiverem demonstrados. “Especialização formal” aqui significa uma ramificação curricular definida, não um título acadêmico de pós-graduação.

### 6.4 Papel do mentor e papel de Paulo

O mentor pode localizar documentação, preparar dados sintéticos operacionais, revisar arquitetura e testes, executar verificações, organizar registros e apontar falhas. Deve colher a tentativa de Paulo antes de fornecer a solução de um exercício avaliativo.

Paulo deverá formular o contrato de ferramenta, implementar os componentes fundamentais, justificar a arquitetura, escolher/conferir métricas e diagnosticar uma falha não ensaiada. Consulta à documentação é permitida e deve ser registrada. Ajuda de IA, pistas e código gerado ficam identificados. Uma execução do mentor não recebe nota de autonomia do aluno.

Usar a rubrica existente por dimensão: não avaliado; 0 após tentativa insuficiente; 1 com apoio; 2 caso simples com autonomia; 3 transferência e justificativa. “Dominado no escopo” exige transferência e revisão posterior. Os limiares abaixo são critérios propostos do projeto, não padrões universais de mercado.

## 7. Projetos cumulativos

### 7.1 Comparação de alternativas

| Alternativa | Reaproveitamento e benefício | Custo/risco | Parecer |
| --- | --- | --- | --- |
| Extensão sobre P01-C | Métricas comerciais e reconciliação SQL/Python já fornecem respostas verificáveis | Dados históricos estáticos dão menos evidência de operação/frescor; interface pode ser resolvida com fluxo simples | Boa opção para laboratório pequeno de F3, sem mudar P01-A/B/C |
| X-IA sobre P02 | Fonte versionada, qualidade, API IBGE, reexecução e runbook já são parte do projeto; frescor e falhas têm significado | Precisa separar falha do pipeline e falha da aplicação; risco de ampliar demais a entrega | **Preferida para consolidação em F5**, mantendo o pipeline determinístico |
| Novo P03 de agentes | Liberdade de domínio e integrações conforme uma vaga concreta | Novo problema, dados, regras e documentação; estimativa própria de 16–32 h só de preparação adicional, antes da implementação | Adiar; só considerar se P01/P02 não demonstrarem requisito decisivo de oportunidade elegível |

Não há repositório novo autorizado ou criado por esta proposta. Os destinos de P01/P02 continuam sendo os nomes planejados `retail-performance-analytics` e `fuel-prices-data-pipeline`, a confirmar quando forem criados.

### 7.2 Escopo recomendado para X-IA/P02

Aplicação de leitura que responda perguntas delimitadas sobre indicadores disponíveis, período, fonte, frescor e limitações. Cálculos permanecem em funções/SQL verificáveis. O pipeline ANP/IBGE continua determinístico e independente da camada de linguagem.

| Componente proposto | Contrato/limite | Evidência exigida |
| --- | --- | --- |
| Consulta de indicadores | Parâmetros permitidos e consultas preparadas; credencial de leitura; sem SQL livre do modelo | Reconciliação de valores com saída de referência |
| Consulta de frescor/qualidade | Ler manifesto e resultado da última atualização; distinguir data de coleta e execução | Responder corretamente a base desatualizada ou atualização falha |
| Consulta de metodologia | Inicialmente arquivo/busca simples; RAG somente se melhorar recuperação verificavelmente | Fonte/versão, documento ausente e teste de documento conflitante |
| Controle de execução | Orquestrador com limites de chamadas, duração, custo e tratamento de erro | Encerrar ciclo sem término, registrar causa e devolver resultado parcial identificado ou abstenção |
| Estado e contexto | Sessões separadas; persistência mínima; política explícita de retenção | Retomada após interrupção e teste cruzado de sessões |
| Interface MCP | Adaptador sobre uma ferramenta existente, se ativado | Teste de contrato e integração sem duplicar regras do domínio |
| Operação e release | Traces sem segredos, configuração versionada, teste de regressão e rollback | Evidência de versão, falha diagnosticada e recuperação |

A arquitetura documentará fronteiras entre entrada, política de autorização, decisão do modelo, executor de ferramentas, fontes, estado, avaliação e telemetria. A política do executor valida cada operação; uma instrução no prompt não concede permissão.

O primeiro comparativo é **baseline determinístico versus workflow com LLM versus agente limitado**, quando as três opções fizerem sentido. Se o agente não melhorar a tarefa de forma justificável, a aplicação final pode manter o workflow. O laboratório registra a aprendizagem; o portfólio registra a decisão técnica honesta.

### 7.3 Critérios mínimos da extensão

1. **Arquitetura e decisão:** problema, alternativas, critérios e limitações documentados. Não afirmar cliente real, uso empresarial, ROI ou economia sem observação.
2. **Testes de software:** schemas, argumentos inválidos, indisponibilidade, reexecução, sessões, acesso e cálculo. Respostas simuladas verificam a integração, mas não a qualidade real do modelo.
3. **Avaliação:** propor 30 casos iniciais estratificados, por exemplo 12 normais, 6 de dados/contexto, 6 de infraestrutura e 6 adversos. Separar 20 para desenvolvimento e 10 reservados, mantendo diversidade entre os grupos. Ajustar o tamanho pela tarefa e orçamento, antes dos experimentos.
4. **Repetição:** planejar ao menos três execuções por caso para observar instabilidade, com configuração registrada. Modelo real e baseline devem ser comparados no mesmo escopo. O custo dessas chamadas precisa caber no limite autorizado antes da execução.
5. **Métricas:** sucesso da tarefa; ferramenta/argumentos corretos; fonte/período corretos; recusa/abstenção adequada; erros de autorização; falhas recuperadas; custo e tempo. Valores numéricos são conferidos por código, com tolerância justificada quando aplicável.
6. **Custo:** registrar consumo total e custo por tarefa bem-sucedida, incluindo falhas e tentativas. Se não houver sucesso, o indicador fica indefinido, não zero. Incluir avaliadores pagos quando utilizados.
7. **Latência:** apresentar distribuição observada, incluindo mediana e p95 quando a amostra permitir interpretação útil; uma amostra pequena não comprova SLA de produção. Definir orçamento antes da aceitação.
8. **Segurança:** falha crítica de autorização, exposição de segredo ou mistura de sessões bloqueia a entrega. Zero falhas na suíte não demonstra ausência universal de vulnerabilidades. Testar conteúdo externo que tente mudar as instruções.
9. **Operação:** recuperar timeout/limite da API/erro de ferramenta, interromper loop, preservar saída válida e executar rollback de uma regressão. Quando existir escrita em exercício isolado, demonstrar que retry não duplica o efeito; o produto inicial permanece de leitura.
10. **Autoria e retenção:** Paulo implementa ferramenta e avaliador fundamentais, modifica um requisito não ensaiado, explica um trace e corrige uma falha. Registrar ajuda, tentativa e revisão posterior.

O conjunto reservado será definido e preservado antes do ajuste. Avaliação por LLM, se usada, será calibrada com conferência humana e verificações objetivas; não será o único árbitro de autorização ou exatidão numérica. Registrar eventos, ferramentas e justificativas técnicas fornecidas pelo sistema, sem exigir exposição de raciocínio interno privado do modelo.

Versionar código, dependências, prompts, schema de ferramentas, política de acesso, configuração/modelo identificável, dados/índice quando existir e conjunto de avaliação. Se o fornecedor não permitir fixar uma revisão de modelo, registrar esse limite de reprodução e repetir a suíte nas mudanças observadas.

## 8. Recursos educacionais e certificações

Os identificadores **AG-Rxx** são referências suplementares aprovadas e complementam Rxx sem sobrescrevê-los. Inglês é o idioma principal dos recursos; o estudo de idioma permanece no projeto separado.

### 8.1 Recursos selecionados

| ID/recurso oficial | Qualidade, profundidade e conteúdo útil | Custo e duração conhecida | Uso proposto e limite |
| --- | --- | --- | --- |
| AG-R01 — [Anthropic, Building effective agents][AG-R01] | Referência conceitual de arquitetura: fluxo fixo, agente e escolha da solução mais simples | Leitura gratuita; sem duração oficial. Artigo de 2024, com aviso de mudanças nas ferramentas | F3; usar os princípios, verificar APIs atuais em documentação. Não é formação operacional completa |
| AG-R02 — [Microsoft, AI Agents for Beginners][AG-R02] | Repositório educacional oficial com ferramentas, agentes confiáveis, produção, protocolos, contexto e memória | Material aberto; execução de modelos/cloud pode cobrar. Sem carga total validada | Selecionar lições pertinentes em F3–F5; complementa R15. Não percorrer todos os frameworks e exemplos |
| AG-R03 — [Hugging Face, Agents Course][AG-R03] | Fundamentos e desafios práticos; variedade de frameworks; unidade adicional de observabilidade/avaliação | Curso e certificado de conclusão gratuitos; indica 3–4 h por capítulo/semana como ritmo, não horas desta trilha | F3, unidades selecionadas. Certificado educacional não equivale a experiência ou prova profissional independente |
| AG-R04 — [LangChain Academy, Introduction to LangGraph][AG-R04] | Estado, memória, interrupções/interação humana e deployment; bom laboratório para controle de fluxo | Gratuito; página informa 6 h de vídeo e 55 lições. Prática exige tempo adicional e pode consumir modelos | F4; escolher como framework principal se continuar coerente com as vagas. Não estudar vários SDKs em profundidade |
| AG-R05 — [LangChain Academy, Agent Observability & Evaluations][AG-R05] e [Anthropic, Demystifying evals][AG-R05b] | Traces, datasets, experimentos, feedback e observabilidade; complemento de desenho de avaliação | Curso gratuito, 7,5 h de vídeo/43 lições; serviço, modelos e avaliadores têm condições próprias | F4/F5; seleção de módulos. Diferenciar testes de código, avaliação por modelo e revisão humana |
| AG-R06 — [MCP, autorização][AG-R06] e [Hugging Face, MCP Course][AG-R06b] | Referências de interoperabilidade e laboratório. Distinguir servidor local e remoto e aplicar segurança conforme transporte | Documentação/curso gratuitos; infraestrutura e provedores podem cobrar | F4 introdução; F5 implementação condicional. MCP não substitui controle de acesso do sistema |
| AG-R07 — [OpenAI Agents SDK, documentação][AG-R07] | Referência alternativa de ferramentas, guardrails, sessões, tracing e interação humana | Documentação gratuita; inferência e serviços têm custos próprios | Comparação de interfaces e portabilidade. Usar em lugar de outro runtime, se escolhido; não adicionar segundo curso obrigatório |
| AG-R08 — [Microsoft Learn, AI-103][AG-R08] e [lab de ferramentas integradas][AG-R08b] | Aprofundamento de plataforma após base transferível; laboratório com agente e ferramentas | Conteúdo Learn gratuito; cloud de prática pode cobrar; exame tem preço regional | F5 se Azure for escolhido. Não ativar credencial só por preferência pelo ecossistema Microsoft |
| AG-R09 — [Langfuse, conceitos de avaliação][AG-R09] e [observabilidade][AG-R09b] | Alternativa para instrumentação, avaliação e análise de execução, com relação ao sinal AGV10 | Documentação gratuita; condições de hospedagem/serviço a conferir na ativação | Referência em F4; escolher LangSmith ou Langfuse pela necessidade, não manter duas plataformas só para listar ferramentas |

**Seleção mínima:** princípios de AG-R01, lições pertinentes de AG-R02/03, um runtime, um caminho de tracing/avaliação e documentação MCP quando ativada. As durações dos cursos não serão somadas integralmente às estimativas da seção 6. A aprendizagem ocorre nos exercícios e na extensão, aproveitando os trechos relevantes.

### 8.2 Credenciais: valor, custo e condição

| Opção | Evidência que oferece | Custo verificado ou limite | Recomendação |
| --- | --- | --- | --- |
| K01 — PL-300, já aprovada como candidata | Exame de BI ligado à rota de entrada | Mantém a regra de orçamento e verificação futura do plano atual | Preservar opcional após M2. Agentes não a transformam em pré-requisito |
| Certificado do Hugging Face Agents Course | Conclusão das atividades do curso | Gratuito segundo o fornecedor | Complemento de aprendizagem; não criar nova certificação profissional obrigatória |
| Microsoft Applied Skills — [Develop an agent with integrated tools][AG-R08c] | Avaliação prática estreita em laboratório de plataforma | A taxa não é informada na página consultada; confirmar condições atuais antes de agendar. Estudo/prática em Azure pode gerar custo | Candidata opcional a laboratório direcionado; não substituir avaliação independente de arquitetura/operação |
| K09 — Azure AI Apps and Agents Developer Associate / AI-103 | Exame de desenvolvimento/gestão/deploy de IA e agentes com Python/Foundry; escopo também inclui outras áreas de IA | Página informa preço por país/região; valor brasileiro não confirmado | **Já existe no plano.** Manter apenas após X-IA e alinhamento concreto com Azure; nenhum gasto aprovado agora |
| [AWS Certified Generative AI Developer — Professional][CERT-AWS] | Exame avançado de aplicações generativas em AWS | US$ 300 divulgados, antes de condições locais; fornecedor descreve público com experiência prévia substancial | Alternativa futura de plataforma, não acréscimo atual. Não há retorno demonstrado para comprá-la no ponto de F0 |

Não foi identificada exigência literal dessas novas credenciais nos anúncios centrais. Ferramentas e evidência de entrega foram muito mais específicas que nomes de exames nesta amostra. Isso não mede o efeito das certificações sobre recrutamento; apenas limita o argumento disponível para gastar agora.

Gatilho de compra futuro: especialização escolhida, sistema próprio avaliado, plataforma presente em oportunidades elegíveis concretas e orçamento/apoio confirmado. Manter Kxx existentes. Caso uma credencial nova se justifique, atribuir novo ID somente na revisão aprovada.

## 9. Matriz de rastreabilidade aprovada

Cada linha liga um requisito observado ao exercício e à evidência que ainda será produzida. **Nenhuma linha está demonstrada.** Itens de engenharia definidos pelo currículo, sem exigência literal universal em vaga, são identificados como aprofundamento.

| Requisito da vaga / evidência | Competência | Fase | Recurso educacional | Exercício | Projeto | Evidência de domínio no escopo |
| --- | --- | --- | --- | --- | --- | --- |
| Software e integração em IA — AGV01/02/06 | C11/C13/C14/C26 | F3 | R06/R08/R09 | E08-A1: interface validada e teste de erro | Reuso de P01-C; depois X-IA | Implementar função/API própria e corrigir resposta inválida sem solução pronta |
| Ferramentas e integrações de agentes — AGV06; sinal AGV09 | C27-A1 | F3 | R15; AG-R02/07 | E08-A1: tool calling com schema e limite | Laboratório; X-IA | Contrato correto, argumentos conferidos, chamada inválida tratada e explicação do ciclo |
| Traduzir problema em solução e justificar autonomia — AGV03/05; decisão pedagógica de baseline | C02/C27-A1 | F3 | AG-R01 | E08-A1: comparar fluxo determinístico, workflow e agente | X-IA/P02 | ADR e comparação reproduzível; aceitar alternativa mais simples quando superior |
| Sistemas com múltiplos passos — AGV04; retomada/isolamento como aprofundamento | C27-A2 | F4 | AG-R04 | E08-A2: persistência e duas sessões | X-IA/P02 | Interromper, retomar e provar isolamento com variação inédita |
| Evals e confiabilidade — AGV03; sinal AGV10/14 | C27-A3/C13 | F3 inicial; F4 completa | AG-R05/05b; R08 | E08-A1/A2: conjunto versionado e regressão | X-IA | Avaliador próprio, casos reservados, erros analisados e comparação com baseline |
| Tracing, custo e latência — AGV03; observabilidade em AGV06 | C19-A1/C27-A3 | F4 | AG-R05 ou AG-R09 | E08-A2: trace e medição por tarefa | X-IA/P02 | Localizar falha no trace, medir custo inclusive de falhas e interpretar latência |
| Testar, monitorar e manter — AGV05/06; sinal AGV09 | C19-A1/C13 | F4 | R11; AG-R02/04 | E08-A2: timeout/limite, retomada e degradação | P02 sem alterar pipeline; X-IA | Recuperar sem duplicação/corrupção; produzir runbook testado |
| Segurança, governança e integração — AGV03/05 | C21-A1/C26 | F3 mínima; F4/F5 | R19; AG-R02/06 | E08-A2: injeção indireta e autorização | X-IA | Teste adverso e política aplicada fora do prompt; acesso proibido bloqueado |
| MCP desejável — AGV03; sinal não confirmado AGV10 | C26-A1 | F4 introdutória; F5 condicional | AG-R06/06b | E08-A3: adaptador de ferramenta de leitura | X-IA/P02 | Contrato cliente/servidor, erro inválido e escopo de acesso testados |
| RAG/busca — AGV03; sinal AGV11 e histórico AGV12 | C28/C21 | F5 condicional | R15; AG-R02 | E08-A3: busca simples versus recuperação | Metodologia de X-IA | Recuperação e resposta avaliadas separadamente; fonte ausente e acesso indevido testados |
| Deploy, rollout e versionamento — AGV03/04/06 | C20-A1/C06 | F4/F5 | R08; AG-R04/07/08 | E08-A3: release e regressão crítica | X-IA | Versão reproduzível, CI bloqueando falha e rollback demonstrado |
| Documentação e entrega ao usuário/suporte — AGV05/06/07 | C02/C06/C19 | F4/F5 | AG-R02; runbook de P02 | E08-A2/A3: handoff e incidente | X-IA/P02 | Outra pessoa consegue executar o caso e interpretar falha; Paulo defende decisões e limitações |

Os escopos e fases estão agora registrados, com aprendizagem planejada e não avaliada. AGV10/14 têm força menor e não sustentam sozinhos uma obrigação curricular. Java/TypeScript, plataforma de automação e fornecedor de cloud entram por oportunidade, sem criar trilhas simultâneas para cada anúncio.

## Ativação e decisão


**Ativação no acompanhamento:** os três blocos estão planejados e não incluídos nas projeções correntes. Na planilha, os controles de inclusão ficam em 0. Antes de incluir, confirmar os pré-requisitos e a oportunidade/prioridade; registrar a posição em relação a M3. O aprofundamento pode ser feito depois de M3 para preservar esse marco. Aprovação do currículo não equivale à escolha definitiva da ramificação de IA.

A especialização final continua aberta. X-IA aproveita P02, preservando a camada determinística e as DoDs dos projetos. K09 continua condicional. T026–T028 são backlog futuro. A atividade atual está em [HANDOFF.md](HANDOFF.md). As comparações quantitativas de agenda e as condições pessoais permanecem no plano privado.

## Fontes públicas

[AGV01]: https://job-boards.greenhouse.io/ifoodcarreiras/jobs/8901054002
[AGV02]: https://job-boards.greenhouse.io/sezzle/jobs/7980309003
[AGV03]: https://jobs.lever.co/ciandt/93c50909-17f1-4a79-95ed-c41a7d2aae17
[AGV04]: https://br.linkedin.com/jobs/view/agentic-ai-engineer-remote-work-at-bairesdev-4483264109
[AGV05]: https://jobs.lever.co/jobgether/b4a97501-3aeb-4443-bfd2-3870aa3db847
[AGV06]: https://vagas.runflow.ai/vagas/ai-solution-engineer-jr
[AGV07]: https://jobs.oakhcft.com/companies/toku/jobs/97921519-ai-operations-intern-br
[AGV08]: https://job-boards.greenhouse.io/sezzle/jobs/7979992003
[AGV09]: https://nomadesdigitais.com/vaga/159158-pessoa-desenvolvedora-de-agentes-de-ia-junior
[AGV10]: https://rebasedev.com.br/vagas/junior-applied-ai-engineer-llm-systems-5275331007
[AGV11]: https://careers-madeiramadeira.icims.com/jobs/3936/est%C3%A1gio-em-ai-engineering/job?in_iframe=1
[AGV12]: https://www.linkedin.com/jobs/view/junior-llm-engineer-latam-at-micro1-4337632591
[AGV13]: https://br.linkedin.com/jobs/view/ai-agent-developer-at-rmf-roletes-4375526892
[AGV14]: https://jobs.workable.com/view/3Lbde149FQLxbHscocBc1y/remote-ai-evaluation-engineer-%28python%2C-qa-or-security%29-in-brazil-at-mindrift
[AG-R01]: https://www.anthropic.com/research/building-effective-agents
[AG-R02]: https://github.com/microsoft/ai-agents-for-beginners
[AG-R03]: https://huggingface.co/learn/agents-course/en/unit0/introduction
[AG-R04]: https://academy.langchain.com/courses/intro-to-langgraph
[AG-R05]: https://academy.langchain.com/courses/intro-to-langsmith
[AG-R05b]: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
[AG-R06]: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization
[AG-R06b]: https://huggingface.co/learn/mcp-course/en/unit0/introduction
[AG-R07]: https://openai.github.io/openai-agents-python/
[AG-R08]: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103
[AG-R08b]: https://learn.microsoft.com/en-us/credentials/applied-skills/resources/study-guides/apl-3032
[AG-R08c]: https://learn.microsoft.com/en-us/credentials/applied-skills/develop-an-agent-with-integrated-tools/
[AG-R09]: https://langfuse.com/docs/evaluation/core-concepts
[AG-R09b]: https://langfuse.com/docs/observability/overview
[CERT-AWS]: https://aws.amazon.com/certification/certified-generative-ai-developer-professional/
