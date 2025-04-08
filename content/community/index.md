---
title: Contribua
toc: true
reading_time: true
pager: false
---

## Documentação HugoBlox

Essa página foi criada a partir do HugoBlox, uma plataforma open-source para a criação de páginas web sem código. Todo o conteúdo do site é baseado em Markdown, sem a necessidade de programar linguagens html, javascript e css para modificar o site.

Para uma visão completa do que pode ser feito com o site, recomendo a [documentação oficial](https://docs.hugoblox.com/). 

Markdown é uma linguagem de marcação muito simples capaz de suportar LaTeX, HTML, js (mas você provavelmente não vai usar HTML ou js). Recomendo esse [tutorial](https://docs.hugoblox.com/reference/Markdown/) para conhecer a formatação Markdown.


## Como adicionar conteúdo

A adição de conteúdo pode ser feita diferetamente utilizando a interface web do Github (existem botões para upload de arquivos) ou através de um editor de código (VSCode por exemplo) com uma clone local do repositório. Para adicionar conteúdo, o foco será apenas na página `content/`.

### Adicionar uma nova página

Para adicionar uma nova página em uma seção que existe basta adicionar um Markdown na pasta específica dessa seção. Por exemplo, suponha que deseja adicionar o Markdown `introducao.md` na seção de Probabilidade que está dentro da seção 2025. Basta adicionar o arquivo dentro da pasta `content/docs/2025/probabilidade`.

Existem algumas **recomendações** para adicionar a sua nova página. Primeiro, troque espaços por hífens no título do seus arquivos (`como fazer.md` vira `como-fazer.md`). Segundo, é recomendado adicionar um cabeçalho [YAML](https://learnxinyminutes.com/yaml/) no seu documento. De forma simplificada, basta adicionar no topo o seguint código:

```
---
title: Exemplo
weight: x
---
```

Em que "Exemplo" deve ser o título exibido na página e "x" é o posicionamento da sua página com as outras páginas. Para adicionar a sua página no final da lista, verifique qual o valor de `weight` da última página atual e some mais 1. Existem algumas opções extras do YAML

- `date`: data da página.
- `authors`: lista de autores.
- `show_date`: mostrar a data (true/false).
- `reading_time`: mostra uma estimativa do tempo de leitura (true/false) (já está ativo por padrão).
- `pager`: mostra um link para a próxima página do tópico. (true/false) (já está ativo por padrão)
- `toc`: mostra a tabela de conteúdos da página (true/false) (já está ativo por padrão).

Uma última recomendação é começar a organização de títulos com `##` (não adicione títulos na sua página apenas com `# título`, pois não vai aparecer no toc.)

### Criar uma nova seção

Para criar uma nova seção, é necessário criar a pasta específica e adicionar uma página inicial para essa seção. Suponha por exemplo que deseje criar a seção "Desafios" dentro da seção "2025". Para isso, crie um arquivo `_index.md` (o hífen é obrigatório) dentro da pasta `content/docs/2025/desafios`. Dentro do arquivo, adicione:

```
---
linkTitle: Desafios
title: Desafios de Programação
weight: x
---

Texto de introdução do conteúdo.
```

`linkTitle` é uma abreviação do título da seção que será exibido no painel lateral, é opcional. `title` é o título completo. Novamente, `weight` define o ordenamento da sua seção de acordo com as outras seções.



## Reportar um erro

Recomendo a utilização de _Github Issues_ para reportar algum erro presente nos conteúdos.



