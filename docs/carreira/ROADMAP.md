# Carreira Data & AI — planejamento mestre

**Referência:** 25/10/2026 · Etapa 7 / F0 / Sessão 02 · CP-0001.


Objetivo: construir empregabilidade em dados, automação e inteligência artificial por competência demonstrável, com projetos próprios e candidaturas compatíveis durante a formação. Esta é a visão operacional do plano aprovado nas Etapas 0–6. As fontes públicas estão em [FONTES.md](FONTES.md). O planejamento detalhado permanece no registro privado de retomada.

## Direção aprovada

- Entrada prioritária: estágios e posições iniciais de Dados/BI, com SQL, preparação, métricas e Power BI.
- Alternativas seletivas: automação, integrações, software com dados e estágio direto em Engenharia de Dados, conforme requisitos e supervisão da vaga.
- Consolidação: modelagem, transformações reutilizáveis, qualidade e atualização confiável. Um cargo chamado Analytics Engineer não é pré-requisito obrigatório.
- Especialização ainda aberta: DE/analytics, DS/ML ou aplicações com IA. Escolher uma direção conforme prática, desempenho, afinidade e oportunidades; não estudar todas simultaneamente.

Não há reinício por troca de conversa. Etapas 0–6 organizam o planejamento; Etapa 7 é execução. F0–F5 são fases de aprendizagem dentro da execução. Preservar IDs C01–C30, R01–R19, K01–K09, P01/P02, Txxx e M1–M4.

## Fases e critérios de avanço

| Fase | Entrega e foco | Critério principal | Estado em CP-0001 |
| --- | --- | --- | --- |
| F0 | Ambiente, arquivos, terminal, Git e documentação | Executar e explicar tarefa; identificar entrada/saída, corrigir erro simples, registrar/sincronizar mudança e reproduzir | Em andamento; checkpoint conceitual de C06 pendente |
| F1 | P01-A: análise inicial de desempenho comercial | Fonte/grão, agregação/JOIN, três indicadores, visual simples, conferência, conclusão e limite | Planejada; prepara M1 |
| F2 | P01-B: caso completo SQL/BI | Modelo e regras justificados; SQL/DAX reconciliados, filtros testados, defesa e variação | Planejada; prepara M2 SQL/BI |
| F3 | P01-C e exercício delimitado de API | Python compreendido, testes úteis, reconciliação com SQL, entrada inesperada e diagnóstico | Planejada; pode se alternar com F2 se houver motivo |
| F4 | P02-A/B: atualização confiável | Origem/versionamento, reexecução sem duplicação, correções, testes, falha e recuperação | Planejada; prepara M3 |
| F5 | Uma extensão: X-DE, X-DS, X-ML ou X-IA | Evidência específica e avaliação própria da ramificação | Não escolhida; prepara M4 |
| FC | Preparação específica de PL-300 | Depois de M2, se BI continuar adequado, com preço/guia/orçamento reconfirmados | Opcional, desativada |

Python não depende de terminar todo SQL/BI. DS não exige concluir P02. IA aplicada requer software, APIs, testes e avaliação, sem exigir um cargo prévio em DS. Cloud, Spark, Docker ou Airflow entram quando o problema ou a vaga justificar.

## Marcos de empregabilidade

| Marco | Evidência exigida | Estado |
| --- | --- | --- |
| M1 | Primeira análise conferida e explicada; variação de filtro/período/JOIN; evidência organizada e vaga elegível | Pendente |
| M2 | Caso SQL/Power BI reproduzível, medidas/modelo defendidos, reconciliação e caso novo com autonomia; Python se a vaga exigir | Pendente |
| M3 | Fluxo mantido, contratos, atualização/reprocessamento, qualidade, recuperação e decisões justificadas | Pendente |
| M4 | Evidência específica da especialização escolhida, com limites e requisitos reais da oportunidade | Pendente |

São critérios internos de preparação em um escopo. Não conferem automaticamente contratação, senioridade ou experiência profissional. Nível 2 pode atender a um marco delimitado. Domínio no escopo exige nível 3 e revisão posterior, conforme [COMPETENCIAS.md](COMPETENCIAS.md).

## Capacidade e rotina

A carga de estudo, as restrições de rotina, o orçamento e os compromissos externos permanecem no plano privado aprovado. Mudança de regime ajusta o esforço restante; não reinicia a formação. Não presumir carga adicional ou autorizar gastos por este registro.

Estimativas técnicas aprovadas, ainda sem calibração por desempenho:

| Fase | Rápido | Base | Conservador |
| --- | ---: | ---: | ---: |
| F0 | 8 h | 12 h | 20 h |
| F1 | 45 h | 65 h | 95 h |
| F2 | 80 h | 120 h | 175 h |
| F3 | 85 h | 125 h | 180 h |
| F4 | 120 h | 180 h | 260 h |
| F5, uma ramificação a reestimar | 140 h | 220 h | 360 h |
| FC, adicional e opcional | 20 h | 30 h | 45 h |

São hipóteses de esforço, não duração medida nem promessa de domínio. Os fatores de realização previstos são 100%, 85% e 70%. Recalibrar o esforço restante após duas semanas registradas e a cada marco, sem subtrair automaticamente horas estudadas. A data nominal do modelo é referência editável; evidências observadas e estimativas de calendário são registros diferentes.

## Recursos selecionados

| ID | Recurso do plano | Momento de ativação |
| --- | --- | --- |
| R01 | CS50 SQL | F1/F2, transferindo os conceitos para PostgreSQL |
| R02 | Microsoft Learn de Power BI | F1/F2; aprofundamento específico se FC for ativada |
| R03 | Excel help & learning | Lacunas funcionais de planilhas |
| R04 | Pro Git, capítulos selecionados | Desde F0; branches/revisão conforme a entrega |
| R05 | OpenIntro Statistics | Descritiva na entrada; inferência quando necessária |
| R06 | CS50 Python | F3; recortes antecipáveis com base suficiente |
| R07 | pandas Getting started | Depois de Python básico |
| R08 | The Missing Semester, recortes | Ambiente, depuração e operação conforme a necessidade |
| R09 | Requests e FastAPI | Consumo HTTP/API e criação de serviço em escopos distintos |
| R10 | dbt Fundamentals | Após SQL, modelagem, Git e qualidade |
| R11 | Data Engineering Zoomcamp | Consolidação/engenharia, por recortes |
| R12 | Microsoft Learn de fundamentos de cloud | F4 e plataforma conforme a oportunidade |
| R13 | Statistical Learning with Python / ISLP | Ramificação DS/ML |
| R14 | MLOps Zoomcamp | Após modelos avaliados e base de software/implantação |
| R15 | Generative AI for Beginners | Aplicações com IA após software/APIs/testes |
| R16 | UiPath Automation Developer Associate Training | Somente se uma oportunidade justificar RPA |
| R17 | MIT 18.06 Linear Algebra | Matemática proporcional à especialização |
| R18 | Patterns of Trustworthy Experimentation | Analytics/DS com experimentação |
| R19 | Guia de segurança da informação da ANPD | Desde a primeira entrega, com profundidade crescente |

Links, recortes e condições permanecem na curadoria detalhada privada; [FONTES.md](FONTES.md) reúne as referências públicas deste checkpoint. Esta tabela preserva a seleção anterior; não indica cursos concluídos nem revalida hoje toda a oferta.

## Empregabilidade e execução

Candidaturas compatíveis podem começar antes de M1 e de certificações. Conferir modalidade, localização, matrícula/período, jornada e situação do anúncio; oportunidades em inglês também exigem elegibilidade territorial e comunicação demonstrável. Não converter anúncios históricos da pesquisa em vagas abertas.

Manter uma entrega principal ativa. Mentor: pesquisa, organização, revisão, testes e documentação. o participante: raciocínio, tentativas, componentes fundamentais, diagnóstico, conferência e defesa. Registrar toda ajuda. Não fornecer solução pronta de avaliação individual.

O próximo passo exato está em [HANDOFF.md](HANDOFF.md). Progresso, decisões e verificações são mantidos nos documentos vizinhos e em checkpoints versionados. A arquitetura aprovada continua válida; uma mudança estrutural de rota, carga ou investimento exige decisão explícita registrada em [DECISOES.md](DECISOES.md).
