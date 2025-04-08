---
title: 'Início'
date: 2023-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: hero
    content:
      title: 
      text: Grupo de Estudos - Multi Objective Responsible Artificial Intelligence
      primary_action:
        text: Contribua
        url: https://giovanivaldrighi.github.io/morai_group/community/
        icon: rocket-launch
      secondary_action:
        text: Recursos
        url: https://giovanivaldrighi.github.io/morai_group/docs/
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: ""
      background:
        color: ""
        image:
          # Add your image background to `assets/media/`.
          filename: logo.svg
          filters:
            brightness: 0.5
          size: contain
          position: center
          parallax: false
  - block: features
    id: features
    content:
      title: Tópicos
      text: Tópicos de pesquisa e desenvolvimento.
      items:
        - name: Otimização
          icon: magnifying-glass
          description: Otimização para redes neurais, otimização multi-objetivo.
        - name: Aprendizado Profundo
          icon: bolt
          description: Arquiteturas, funções objetivo, regularização.
        - name: Explicabilidade
          icon: sparkles
          description: Interpretação de redes profundas, explicações contrafactuais.
        - name: Fairness
          icon: code-bracket
          description: Algoritmos, métricas.
        - name: Teoria do Aprendizado
          icon: star
          description: Generalização, convergência.
        - name: ...e muito mais.
          icon: rectangle-group
          description: 
---
