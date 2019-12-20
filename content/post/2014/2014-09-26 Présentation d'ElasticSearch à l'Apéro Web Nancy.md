---
title: "Présentation d'ElasticSearch à l'Apéro Web Nancy"
slug: "presentation-delasticsearch-a-lapero-web-nancy"
date: "2014-09-26T12:24:00"
categories:
  - Blog
tags:
  - Nancy
  - Apéro Web
  - ElasticSearch
  - slides
language: "fr"
---

Hier soir j'ai présenté ElasticSearch lors d'un [Apéro Web Nancy][awn]. Le public était nombreux et *très* attentif,
c'était impressionnant :smiley:

Comme promis, je viens de mettre en ligne le contenu de cette présentation dans un [dépôt git][git]. Ce dépôt contient
les slides, le jeu de données (sous formes de fichiers JSON), le script permettant d'indexer ces données dans
ElasticSearch, les démos utilisées pendant la présentation, et les scripts permettant de regénérer le jeu de données à
partir des API Google Places et BreweryDB.

Tous les détails sur comment faire sont dans le [README][]. La première étape est donc un petit `git clone
https://code.schnouki.net/schnouki/aperoweb-es.git` 🙂

Les slides sont aussi disponibles en [PDF](</files/2014/Jouons un peu avec ElasticSearch.pdf>).

*Happy hacking*, et n'hésitez pas à me contacter si vous avez des questions :wink:


[awn]: https://plus.google.com/u/1/communities/108954298677595658174
[git]: https://code.schnouki.net/schnouki/aperoweb-es
[README]: https://code.schnouki.net/schnouki/aperoweb-es/src/branch/master/README.md
