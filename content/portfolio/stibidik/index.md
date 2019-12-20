---
date: 2018-12-14
title: "STIBIDIK"
weight: 201810
cover: logo.png
images:
  - screenshot-shopify-20180723.jpg
  - screenshot-market-20180111.jpg
  - screenshot-market-20180623.jpg
  - screenshot-market-20180718.jpg
  - screenshot-market-search.png
  - screenshot-wanted.jpg
  - team.jpg
---

STIBIDIK is an online marketplace that specializes in vintage fashion from the best second-hand boutiques.

I've been working at STIBIDIK as co-founder and CTO since 2016.

<!--more-->

Quick summary about the tech stack:

- the initial site was built in **[Go][]** with the [Gin][] web framework and a **[PostgreSQL][]** database. The
  frontend was built using [Ampersand.js][]. This was hosted on **[Heroku][]**, with media content (images) on **[Amazon
  S3][]**. This also relied on **[Mailjet][]** for sending e-mails to customers and to the staff.
- the next iteration was built in Python using **[Django][]** and **[Oscar][]**, with a **[PostgreSQL][]** database (and
  later [Elasticsearch][] for search and faceting) and [Redis][] cache and session store. This was hosted on
  **[Heroku][]** (with images on **[Amazon S3][]**).
- the website was later migrated to **[DigitalOcean][]**. The deployment involved **[Docker][]** images built from
  **[Gitlab CI][]**, which are then deployed to a **[Docker Swarm][]** cluster using a **[fabric][]** script.
- lastly, we moved to a *much* simpler solution using **[Shopify][]**. This involved improving on an existing theme
  using **Liquid**, **SASS** and **JavaScript**.
- since the "normal" Shopify admin dashboard lacks a few features needed by the team, I wrote a **[Tampermonkey][]
  userscript** in **modern JavaScript** to improve it. This involved a lot of **[VueJS][]**, **promises** and **async
  functions**, and liberal use of several **REST and GraphQL APIs**.

---

The initial goal of STIBIDIK was to provide a "wanted" service: customers could describe a specific item they were
desperately looking for, and the team would look for it over the Internet and with its offline partners (hand-picked,
trustworthy boutiques). However we quickly realized this service would most likely never be profitable, so we pivoted to
something else.

We then decided to build a marketplace that would connect boutiques (our partners) to online customers. To make that
attractive to our partners, we built a stock management app that helps them manage their shop *and* sell online at the
same time.

{{< gallery >}}
  {{% galimg target="screenshot-wanted.jpg" %}}The "wanted" service.{{% /galimg %}}
  {{% galimg target="screenshot-market-20180111.jpg" %}}Early version of the marketplace homepage.{{% /galimg %}}
  {{% galimg target="screenshot-market-20180623.jpg" %}}Later version of the marketplace. Now with a search field powered by Elasticsearch.{{% /galimg %}}
  {{% galimg target="screenshot-market-20180718.jpg" /%}}
  {{% galimg target="screenshot-market-search.png" %}}Search and faceting on the marketplace.{{% /galimg %}}
  {{% galimg target="screenshot-shopify-20180723.jpg" %}}The marketplace after migrating to Shopify.{{% /galimg %}}
  {{% galimg target="team.jpg" %}}The amazing STIBIDIK team: Lucie, Amal, Thomas (me!) and Alicia.{{% /galimg %}}
{{< /gallery >}}


---
{{< youtube y56-adfs9xI >}}

[Amazon S3]: https://aws.amazon.com/fr/s3/
[Ampersand.js]: https://ampersandjs.com/
[DigitalOcean]: https://www.digitalocean.com/
[Django]: https://www.djangoproject.com/
[Docker Swarm]: https://dockerswarm.rocks/
[Docker]: https://www.docker.com/
[Elasticsearch]: https://www.elastic.co/products/elasticsearch
[Gin]: https://gin-gonic.github.io/
[Gitlab CI]: https://about.gitlab.com/product/continuous-integration/
[Go]: https://golang.org/
[Heroku]: https://www.heroku.com/
[Mailjet]: https://www.mailjet.com/
[Oscar]: https://github.com/django-oscar/django-oscar
[PostgreSQL]: https://www.postgresql.org/
[Redis]: https://redis.io/
[Shopify]: https://www.shopify.com/
[Tampermonkey]: https://www.tampermonkey.net/
[VueJS]: https://vuejs.org/
[fabric]: https://www.fabfile.org/
