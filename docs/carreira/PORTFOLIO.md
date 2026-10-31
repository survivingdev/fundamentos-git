# Portfólio, projetos e entregáveis

**Referência vigente:** 31/10/2026 · Etapa 7 / F0 / Sessão 02 · CP-0003. Histórico anterior preservado.


Plano aprovado: dois projetos principais com versões progressivas e uma extensão posterior. Nenhum P01/P02 foi iniciado ou concluído neste acompanhamento. Os nomes dos seus repositórios são propostas; não foram encontrados na listagem acessível em CP-0001. Não apresentar URLs futuras como criadas.

## Inventário de projetos

| Item | Fonte/tecnologias previstas | Repositório ou caminho | Estado e ajuda |
| --- | --- | --- | --- |
| F0 / exercício Git | README, Git, GitHub, VS Code, PowerShell | [survivingdev/fundamentos-git](https://github.com/matiasdotpy/fundamentos-git) | Publicado com apoio; avaliação independente pendente; não é P01 |
| Continuidade operacional | Sete registros Markdown, fontes e manifesto SHA-256 | docs/carreira no mesmo repositório | Produzida pelo mentor como tarefa operacional; não é projeto de competência do aluno |
| P01 / desempenho comercial | UCI Online Retail; PostgreSQL, SQL, Power Query, Power BI/DAX; Python/pandas/testes na evolução | retail-performance-analytics, nome planejado, sem URL criada | Planejado; dados completos ainda não perfilados neste roadmap |
| P02 / preços de combustíveis | ANP e IBGE; Python, HTTP/API, pandas, PostgreSQL, testes; dbt/operação conforme evolução | fuel-prices-data-pipeline, nome planejado, sem URL criada | Planejado; licença específica de redistribuição ANP por confirmar |
| X / especialização | Uma extensão DE/analytics, DS/ML ou aplicações com IA | Reaproveitar P01/P02 quando fizer sentido | Não escolhida nem implementada |

Projetos anteriores e seus repositórios são mantidos no inventário privado. Não foram incorporados automaticamente ao portfólio avaliado; existência de repositório não comprova autoria, conclusão ou competência.

## Versões e critérios de conclusão

| Versão | Escopo aprovado | Evidência pessoal exigida |
| --- | --- | --- |
| P01-A / M1 | Pergunta, fonte, janeiro de 2011 sujeito a inspeção, agregação/JOIN, três indicadores e visual simples | Definir regras e grão, conferir contagens/totais, explicar conclusão/limite e resolver variação |
| P01-B / M2 SQL/BI | Meses completos, inicialmente janeiro–novembro de 2011 sujeito à fonte; modelo, DAX, SQL e relatório | Defender modelo/regras, reconciliar SQL/DAX, testar filtros e resolver caso novo |
| P01-C | Reproduzir parte da análise em Python e testar | Implementar componente fundamental, reconciliar com SQL e depurar entrada inesperada |
| P02-A | Recorte inicial PR/SC, gasolina/etanol, arquivos de agosto/setembro de 2026, sujeito a inspeção | Validar obtenção, versões/hash, tipos, persistência e reexecução sem duplicação |
| P02-B / M3 | Integração IBGE, modelos reutilizáveis, qualidade e operação | Tratar correção/falha/esquema, preservar saída válida e recuperar execução |
| X / M4 | Uma extensão escolhida por prática e oportunidades | Defender arquitetura/alternativas, implementar fundamentos e resolver falha/variação específica |

Dados são reais; problemas/personas são propostos, sem cliente contratante confirmado. Benefício de negócio é hipótese até ser medido. Não inventar lucro, estoque, demanda, ROI, economia ou experiência empresarial. A atualização do P02 será compatível com publicações da fonte, sem alegar tempo real.

## Fontes, publicação e limites

Preservar o plano detalhado no handoff privado. As referências públicas estão em [FONTES.md](FONTES.md). Verificar acesso, condições de uso, licença, formato, recorte e SHA-256 antes da implementação. A licença UCI foi registrada no plano; condições ANP para redistribuição ainda precisam de confirmação específica. Até então, código, instruções, metadados e fixtures próprias podem documentar o fluxo, sem publicar cópias reais por conveniência.

Fallback aprovado de P02: replay histórico UCI, explicitamente identificado como fonte estática; exercício de API separado se IBGE perder sentido. Não fabricar atualizações.

Começar somente com arquivos necessários à versão. Convenções previstas: README.md, docs/data_sources.md, docs/metrics.md, docs/decisions/, sql/, src/, tests/fixtures/, bi/, reports/, docs/runbook.md e docs/learning_log.md. Não criar todas as pastas vazias antecipadamente.

Para uma versão concluída, registrar commit real, reprodução, resultados conferidos, ajuda recebida, decisões defendidas e evidência de transferência. Não publicar segredos, dados pessoais, banco local, ambiente de desenvolvimento ou soluções de exercícios avaliados de terceiros. Condições do código e dos dados permanecem separadas.

## Extensão de agentes aprovada

X-IA evoluirá preferencialmente P02 se a rota for escolhida. P01-C pode fornecer um laboratório pequeno; P01-A/B/C e P02-A/B preservam suas DoDs. Não criar P03 agora. Ferramentas de leitura, comparação com baseline determinístico, estado/contexto, avaliação, tracing, recuperação, autorização, custo e release são exigências da extensão. Ver [adendo](ADENDO_AGENTIC_AI_ENGINEERING.md), que contém exercícios e evidências de autoria. Um agente sem benefício justificado pode ser substituído pelo workflow na entrega final.
