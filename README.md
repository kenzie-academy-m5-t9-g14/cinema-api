# Kinema-api

Kenzie academy capstone project, API with django

<p align="center">
<a href='https://kenzie.com.br/'>
<img src="https://avatars.githubusercontent.com/u/56847172?s=200&v=4" alt="kenzie academy brasil"/>
</a> 
</p>

##### Projeto realizado por alunos do quinto módulo do curso fullstack da kenzie academy brasil

#### M5-T9-G14-LUCIRA

#

#

> API de gerenciamento de rede de cinemas, com suporte para persistencia de cinemas, usuários, salas de cinema, filmes, sessões e tickets. Coordenando divulgação e venda de ingressos.

> Para solucionar problemas de comunicação, produtividade e organização. Integrando procedimentos , evitando falha humana, conflitos de sistemas não compatíveis em diferentes áreas de uma mesma empresa, e agilizando processos.

### Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)
- [Diagrama ER](#2-diagrama-er)
- [Início Rápido](#3-início-rápido)
- [Instalando Dependências](#31-instalando-dependências)
- [Variáveis de Ambiente](#32-variáveis-de-ambiente)
- [Migrations](#33-migrations)
- [Autenticação](#4-autenticação)
- [Endpoints](#5-endpoints)

---

## 1. Visão Geral

##### Visão geral do projeto, um pouco das tecnologias usadas.

- [Django](https://docs.djangoproject.com/)
- [Rest_Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://docs.docker.com/)
- [Unitest](https://docs.python.org/3/library/unittest.html)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Insomnia](https://img.shields.io/badge/Insomnia-black?style=for-the-badge&logo=insomnia&logoColor=5849BE) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![Visual Studio](https://img.shields.io/badge/Visual%20Studio-5C2D91.svg?style=for-the-badge&logo=visual-studio&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

##### Ferramentas de gerenciamento de projeto utilizadas

#

| Ferramenta | Link                      |
| ---------- | ------------------------- |
| GitHub     | https://github.com/       |
| Notion     | https://www.notion.so/    |
| Diagrams   | https://app.diagrams.net/ |
| Trello     | https://trello.com/       |
| LinkTree   | https://linkr.bio/        |
| Slack      | https://slack.com/        |

#### A URL base da aplicação:

https://api-kinema.herokuapp.com/

---

## 2. Diagrama ER

[ Voltar para o topo ](#tabela-de-conteúdos)

Diagrama ER da API definindo bem as relações entre as tabelas do banco de dados.

### [DER](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio#R7Z1bc9u21oZ%2FjWZ2L%2BQheNDh0nacJtM4yRc7adMbDy0xFhtJVCnKsfvrP1ISKYkAKYAkeMBamT27sSzDCtbLB8A6oWdcL15%2B9%2B3V7NabOvOerk1fesabnq7rxCDhf6JXXnevkKEx3L3y5LvT%2FWuHF%2B7c%2F5z9i9r%2B1Y07ddYnbww8bx64q9MXJ95y6UyCk9ds3%2Fd%2Bnb7thzc%2F%2Fa0r%2B8mhXrib2HP61T%2FdaTDbvTqytMPr7xz3aRb%2FZqLtv7Ow4zfvX1jP7Kn36%2BQl5yV46y2D%2FUf87PgLe%2Bksg%2FA7t7b%2F0%2FF71s0sCKJ%2F6WVPfxv%2B70f07osnz3uaO%2FbKXV9MvEX48mQdvuXtD3vhzqN5Phroaj9Q%2BOuMm55x7XtesPvb4uXamUfGis2w%2B0xvM76bzIMfjcvxA9f959cPP7Vg%2Be6X8S24vX36PHzs67tRnu35Zj%2B%2Ft96zG9p3N0PBazzt4WStor8G9mP00tU6sP1grw5DC18I7R3Y7jL8pxlvyPbr%2Bdxerd3t23evzNz59IP96m2CeKD4q6sf7osz%2FbITR%2FTeUCcfwsGiL6PBo2m%2B23%2BY6Nv23H1ahn%2BfhP%2F26Dde%2Bc46%2FCwf7HWwfwc9O%2FsJe3b8wHk5emk%2FW7873sIJ%2FNfwLfvvWrEqXlMa%2B3XQnT7evzY70pxh7l%2B090J6SsY%2B2Cf8y95EAuYyKHNlGir8pweuPf8SPoP28mlrs1OTRPM69b3Vve0%2FOcH%2BhZXnRjN68%2BzsnoLt5Lvz%2BbU39yLLLr2lE79t%2B4%2BzrsL%2Fhf%2Fca%2B3C6lnhB7gOvyaHr8P%2FRW%2F3g2tvuQ78UCHRr3JCQ%2F1yImNdBd5q%2F3vmzo%2F4Y%2Fj7yYz%2B%2FugFQfhQZZk1V9bnbb23rcFrWlmWNSnLfv5DxLZe%2BG%2F9Md%2FibOZOp85y90hGCLYP9maYkjn%2FyZynjZF%2BEDntYXDb48gAhuD87wc7zIrwaPY81P7SDpwrb7OcrimjJp%2BzuJ0tys7h23Vts9n%2B5%2BOn%2B%2Bj%2Fv374EP7n68f3%2F%2Ff1poUiiOm7e%2B%2FVemVP3OXTh91PDlIqsWSo5CX7qR1Uqhqu4WqQzQAy%2BDWJ4B80Df5hKcvW9MRzzv6Ae%2FZVx%2FyIsurSXkQf9dvll%2Bt3l1%2F%2BZ2m%2FqcP7yuUBju9j5Lscvo%2Bb5nvsN1EC8GPu6Vcd8IRQZp1ufDtwvWXvWu9dakesNyjWt87%2BVSGeXyAqI%2F7j9erm3%2Bn60%2F3zy5dfL5cauZr80R%2FTvjZkfCWMJ3qNkGfbtpxjrjHI5wsVFOXZU0G75XbTZ88fItgvn5THfFmJwOM8ffZDzlfDee4AjDTOlzuntYzzI24DqM75JEh8ZNi1u%2FRWa4fazeuW9Vv8YutMXxng%2BbUBDvBEo89%2BSPhqCD9qmvBEK3dMaxfiD1JFxhONPqS5i%2BljvJFPc55o6mNeRB8AOU%2Bf%2FpDzlXA%2BySZskPN0JkYLH3Tu59jkNoH6nKeTJXxnHj4DzsM0%2FM0J6N9c3t9AcdiICAQg6MslYSDos0FvNg%2F6cv64toF%2ByG0C9UFPe%2BMmc28dAhIy6PkFojLo%2F9GsH8v311%2FHjuW%2B8T56i%2F%2BM730d02xkcX5YI%2BeZto0H7hrm84UKivJsu9LO1onvhL9y%2BmAHqiO%2BrDjAEd4o571FwmcS3tAaJ3xHk2zyhYqEN2g362Y1hUx4AXGoTHh24i1NgW3Jcv9%2BFu0KfCxdDr9jxXHUPbz7Q4vSh0EYBtXjN1afBw86mCJQK0v4yyCzi5eZxpVX40DHUlSqXiYggyvsqaBjK1i%2FXEAnOcv2qNplm2e4OoSDIRZZ%2BGeUMNeM%2F45GWPKFirAnDHf59jh2tpa5dcavqr5NQB3gEB9XYSHiK0c8o4q5XsTrtBe%2BhU855%2FwnQkXEx2Y8smvwujqGu5pVbWV1oTLc2XkFDKUg3auhO6t%2BWRreM6zb0djKGa2CAnzGXNB%2B1%2BVm8ej4D96Ph7Vjh4%2BSrr3%2FeK8g5EuLAyDlsXhZGuUZ1ct1U16l8uWDVpHyhJH95rzM3Ec3eACxny%2BtEJVRb%2Fz7%2FPfdw7u%2F9M3Nz28v7zz7499OfwC6l7Rc0jOqmKWRnm3ccsH2xkCfr1RQnGdPBR1o327hHzKCsArVL5eVhsqAZyaRkZL5kkj4nHIHRv2yNMJnWLejiD%2BjVVCMz5gLGvLAKx5E5AGQ83g5gDTOM8qX2XmzFaTNZli3oxcEnNFqac7nzbg459Oj1fLc0r5W4HUPIvIQ5HxxuXANV0eont7OX7tLZ2FnCgJSwUOq3oHwgtsYVbBDZ9sLCx74lmVdeFluvOBBV7vgQceCh2QqsOChEp2ofCxjzw0WPMjCf%2BMFDyWzJFqWDYsFD8lU0PkReG2biEBUpjwzxWCArcBlUb7Omge2bfVuUj5fqKAoz54K2pEycYPXHsgcKQFdwIM7aA%2BOVLg3X%2FLASKVp4WPO%2BxSDdNiwp4J22Kxm0dQf3exA4OAdPTTZc4MeGml4b7zWYdBRF02%2BUhHvA9pF4yxsN%2Fq57bZdoYzXslIAB%2FS4BzUCvXqg11nSwDZuRztQ5CsVgT6kvWz2dOo763VP9Q5DZaUBD%2FBY0SAL8LVWNLCN29GChnylIuCHjJq1ILqeB6S%2FXUAY8PCOhQzS8M6dDysN7x2tY8hXKuJ9SDva%2FnNXE2964nEHBHhpJQwKAB7vX5MGeMYFbPUCPtaYGoAHeQEb264Mx9vWy%2B6tnGV01%2BbM2%2FjHzhqiAfDDCwhEZcxnlPEh52VxnnUNW82dJ8xOgP609IkyxxnhgsJ%2Bhpnx4s0S8oAHfZMO5CD0K4J%2BnQWvGdbtRIPoQtBPhIvQJybexVlCHipDn91hlVLLZ%2Ft1EU7ow%2F2262yGKgA1pujHmN6j3GI44pPuFcfWJIMKWM40Guh1mm3WXHGXaUvBNK00Fxy9Rne0K0WubkEt08yZoBdpkD0pSqokZ7XWq12teYarQTblKp46Dn4B578w%2BBkNKeoFf7nEiXaFXizu2Vcd83TGBNy7HPhVAQ7reGWPJKwzOlDUi3WVruvBy3oSHdLxMziBlZLaUBnubPejhR2GJOGd1YNCGt8zjFvOF9ey5t4WvwkUYnzGXNC%2BOOiBFAF5qIx5Nrxoyt96z67zcOes1663zNQFoFDKOE5xjUMp3PtzImuDTjCWwrk4dy%2BYQtSOpiTSBbVYs6cC4ymV6ATeqo0RFVn4bzykQuiYytv245%2FTHBhjSaaCDrIsthvvYBa55Pysm1XbJ4TKbs3GUEv23GCsRRbwGw%2B2EJWiLQTDLUlCEB1uWU9mznQTft7YDwcwoC6gEHiYZ4TokPPVcL7WqEvGZ6adreps7RPpIvkJwz2729zD29QLyAIg7rGvoDTcMzqB1417lRoLEoFLzNXnO%2B1%2F%2FeU4P6c20Mt8RMQBkPLYXlAa5RntweumvEr9BQ9aRcoThtPVeZm5j27wALceQkQhAFGPDahkoZ7VKLxm1DM8ui180rktALLnVIZlac%2Fcyncn0ad9c3P9%2FvbyAxy%2BV9JrqvN8Z6cSa5h4I43vvA1K5FVFaJ0oZy7Ua0oDmXmTMRf0iQ1OHVxpeQCEPibfSIM%2Bo3t43dDvRPpNMeiDTMZhzwUjswJ6XZyAPFSGPjt5iz4Q3oVbhHWmHiDVw8U58q8pm52DuC6vtaAOeYkW6WXXvXo4Xe16uES6oBZp9lRgPVwlOoG3WqNbThb%2BG6%2BH0zvhlOOdf5BuOPZU0F64cHNLVUbocELrAuKAR3j0wckifOMFcHonPHC88w%2FS58buCk%2B73NaOHQCFOzrbMueGGNhrUBbdW1D2ZpRzzrWL7wetIuCJQbvm7GfbnduP7twNoim4%2BvTpw83lRyiUF1EHQMyXK4hCzLe63M2gnXDqVDcn0kXqE4P2yEFvXSQgD5Wxz84zYIR1EPsVYZ%2B3%2Fs2sAPsZ1i0Xe2kH9M8ItzT086ZfHPrp0Wp5iGnoQ0%2BaFZCHIPSLy4VruDr0wnD%2BIfSrgT53vpW8pNmSDrs2Qz8RLqidfsZc0J476EmzAvJQeafPvh6WpsK9O%2FnpYNps9N2%2BGW%2FW43sk4q1zc%2FdImPQDDmiVFsjSNIVX6cbzZk2182YT6YJap9lTgXmzlegE3oKNWVWy8N943qxJZ1UpE44xMckquZ%2Ba9rPsgjHr3QVu8IIxAuIAB3wyAr3hl0r8xvNoyYje8SuD%2FINykflkRG%2F4V%2FbrIpzBbWdCeMwXUQdA6GN5nCzotyC9dqRSgdxBq4h5MqJL5Nz1wzrYTKNJhJdcK6ANlSFv%2FPv8993Du7%2F0zc3Pby%2FvPPvj304fKyikIb7O1Fqmbcud2RoDfK5OQeGdORP0YS3wAnv%2BsHtB5cazJYWhMtszFj7000uje%2FM3SIwU9tQfpAsK%2BBkXvdK%2B%2Bs0aZL2EgCpUpv0%2Fn67uf775bzH78sftP59%2Ff33zPHvGnbw01td6hQTTtp3YyZ9Lm80TLSjKM2eC3tavAzvYrE%2F8NW9u3l5%2B%2FXAffv%2F%2BSzezcSrXhdKcZ6YSW1gXJ430zV8mYalbF2eBLIbOmAusiyshD4DQL3ddJEI%2FB%2FrNXyZhlXPUtRr6Q257qA992mMHvS5OQB4qQ5%2Bdo0u7dL6uHT9TDpCK4izttCiuTwZDShdJAdxJVXsVPS3Y9irnpun4Gi1Qg2UJr9GMh55pXGnRFkvtqrhEuqBWafZUYFVcJTrJWa5H1S7XPMPVIRxMl5WFf0ZVXM34VylZ1sJc2WQqaLfK0l5EnzXuNW7B6TUuoAt4cMdUKllwZxTA1Qx3lS6SsDBxKp6KeNdwHGNZ%2FThiOyFw2F5J5pSabCcDzJ2SBXdWoVu9dCeDcm65duH9oFXkOxnQTjlnYbvzI8Qb1Pa9w04bCRoBCHtMn5IGe0bJW92w70T6FPeDDDJjKmMuaBfcyl6vf3n%2BtJdzNdw%2Bqt46CVQH%2B0rSplSFPaZNSYM9owKubth3Im2K%2B0EGmSmVMRe0S%2B7R9YPZQ5Qt1VM2R6q0MOARPk7eRMJXTnhW3VvNhB924sII3gc50SoSngxpr9wk%2FLnVLDLAkYve%2BE39LbyALgACnnbyIeArAjyj3K1uwJfzxrUN8Aa3CdQHPO2Je3KW%2FjHcI2eN%2BnDn1wRAuJfLq0O4i5W11Q33ct63tsF9wG0C9eFOe96idhXHcDdAwJ1fEwDhXi6vDuGeVw%2FVONxjlSkC9zG3CZSH%2B4h2uk3c4DXF9vbZujqq84tBZaoz%2B61i9ow0ptdZ5Mq0bUdzZ3J1CornzJmgj9jRbQCbleNvtt0E4v5y%2F%2BvpqmC9pCJUhjq7DYeJtavSsF5n8WqGdTtRvVqovZAJspY1Yy5odxv0nnIC8gAIfaxplQb9OotaM6zbiarWYtAHWeOa0UCNdsNB7ylXzU2%2BnYc%2B%2B7ocjoS67TO5ax9Hwn%2FX1SxYzHu7dlLOcnrp%2B1sp3HwJjXzv3drL18iQ0Sd2pkdP9Vt74c4jHL5z5s9O4E7s%2FTdikUydH%2FZmHjANu%2F%2BUa2%2FjT%2Faf6rr%2F%2FPrhpxYs3%2F0yvgW3t0%2Bfh499fR9cD%2BJVJ%2BuNZP9GZ%2Frk8AKDaAybJS%2F6ztwO3Gfn5APnCONztMgdJDcwBhdj7fBnP0A6uT4ecDcT%2BzEOsqCGNVN98RJnbjzQbqaogSpzD3Jka9WuL%2BfFDf6Kf0P49%2B%2FRMBfW%2Fqs3L%2FtRt1%2B8Zm4NuDWp0ZpkbiviEVujyXGcs5PqzCEqQkLG%2BQNJFiFPTngnRBhqz3%2F96%2FiLo5%2BKvjz82PYrIfEyNTnWafGyV1nNapl6h%2BNT9JnDgvIdD04HGms1y7dTa3Rr7N83hqd204sKgBrJ0mtWAIfDrn6AxTAiFxoZnAJJPwOk7VefHd8NZ2bbhrgcpQjnCpvc794ekRJjdCqtwiIl5qlIh2QgS6TMFcCgYwa%2F7xJ8M46WgPpTEy21hhCDdbXMkKU0a5AtqlIuIQN0si3bsvnKLtOfmmlcae4%2Bg%2Fb9d7Q%2Fdb500eNn0F57kP2py%2Bokx%2FVnVqobruHqEA6m48rCPyPEz8S%2FPpKE%2F1hi6gV7EtWWJn%2Fe5IuTPz1aDQ%2BwSfsFzjar7vASUL1ABJFfXDBcw9URHSQY4pfF%2FPgu8saYT4i6EX5SWYS%2F89RPOuhiWlcRecBjvs4RPkDmF2I%2BiV2szUE%2FNqaC0Bdws6oPfTqPAnpal7gXHg70GVdd3HrPrvOAEZn9d61UtIywyu2Y1z4TaU572PdOCLj%2FE3mXCsjUeqc349YJlQIyMK%2BhYE8FvVRjQKaATlS%2B35s9N1hLLwv%2FrIBMvfink2Peth%2F%2FnOYAWVvPngo6pWax3XdnrQCtE0BVx7NqrqFQE%2FTYo1wa6Bl1lvWCnpGsrQzoYfYrZ08FfZzbdrOFB%2FpqmpWrCfoRRxuVxgqPDsVG33uHMqRzhUeHWqPvx98rU3jErprbve9s3VG8RLQmo3%2BQqhUhWrpYhDejf2ScG0lyRv%2BolWUne%2Fn2tQtNM3vHxXMjw%2BBTMYl%2F9KhiZfezojUr0fiF6lhy01XPq95smepH6TpjzSqo%2BnS1HT2SbNXTqfN3jh2sH3YRlDtnvXa9ZeaKDiiGQpIuBnGJJaMNbc0xlBHoDDcBj%2F2I%2FxaxtsRQRnSCm0oxlBG2sYmnIj7GYwylnE7AnbjGeMGrLPw3HkMZ00u7Mq61McjLXtlTQa%2Fy63D%2FDc%2BzJqAJcJxPzq0I%2BspB33gMhWgKB1EOykXUE40Oo%2Bzi5eudlwUe9EXkAZD6XWkn2NcuyDlvNMN1fBRnMa2kidJ%2BQM0YFXFR08LjbasUJ66fdUfHa0xr3NGH9jqxF7moO5qYqXhOMnJN7mjCyOVvgeYLdiKMFBKvmOFOaOY9eUt7fnN4NVuu51sQDkYtk2E%2F6fGd1TiOv7tXnFoWu9p17SLONK5NifS27N6d%2FHSC9cM2QpK5LAOKiegp8BhxVWFzIRHCqD0Q2UF1%2FKwk4IEnAunpbQmKEEa9gUpRkYN68bxEGCUCGBcpohR4RydGBQKgRUDAYVZgEWg8NEIYhQfqeMwGeKnXYS7oACfM6IiIKgDSHnQalFzaNx8fGdAhUoVoj2lQyVwwKsVWG38ys9cAK01ElAGP%2BEOO6vEG74gQdBMfJfmTce8krqIViKvQCuNNyU%2Fcch10P49T3mczHbrg9T4PrNOBLL1mz%2FOwzYVUkSb102ucom06XyWK%2BHNR4bUphLfehFhtKzghqdKDUfpSJu4AX2qg2qusyJDezX1dO%2F7Dtbt0Fnbmgg4oqNLXU%2BVFfZPX5SIxrDKiN2ciu6%2BOn7FEXPiJwjsUVhnRwU6lwiqJevGYlVwLhmGVkkqBd%2BwacWSkqbsIiDjaxBeB5sMqI%2FpQrY6jLZEurgCE0aljE%2B3B4TnZBFQBkPagr0yUS%2FvmwyqMzg8K0R6vTDzMBR0dnWydLRB5X8kViarynuNKpeaCKtsWSElNyD48opPEpyzUyEhmYn68p2iN97ivp7oMHUKtwpn55jgyw%2BEPGZ6ObGjj8Pvj5M%2Bw3mu5CaOXRos0zLg8XrMGqOCz8Q89JTNSNLiXrIaJb10zLozx0R9Zer3%2Bevvz2zf70%2BvH4PeHq7vrN%2Fpk1afdrtu%2BW1hc0qMvLTEMi7EWj1mLZ1odRXbNTHvRrlOR3VLHT0Rsu%2BbqulQIhGlaWZZVpq4kV7egjkPMmcCakipUknM4GlR7OOIZrgbZYD2JJPCzwh61gr%2Bck7OmJ55z9kGWjjBngnZuwrotvqQ8wPEdK0gk8Z0V6KiV7xxOzeafcM7ZB1kswtYh7eebbnw7iJqVxxcEx6g3KNS3zv5VEb6SmhE1CU9A3zcrE%2FFEb5rxpJxfrl2QJ%2FwGUJ7ytFduN332%2FCGC%2FfIJJuYFJAKP89gUXRbnueMv0jhf7pjWMs6D7ILOngpGF3R36a3WDrWZ1y3rt%2FjF1lm%2BMr5X0gxdTb7Hm03ke%2BV8HzXNd73cGa1dfE%2BEinyPzXgcdV1MH%2BM9fJrxRFMf8QLqgId4LDOThHidNI54js4tzT%2FlvA8xyKIy9lTQGRK%2BM3ei3k3T8BcnjH9zeX8DxU0jIA94jMfiMlmMNxtnfDkXXMsYD7KUjD0VjEqyubcO2QiY8ZVUlCnK%2BHK5F8j4bMYPm2Z8PLAajOev31ad8Qbtgpv4Tvgrpw92AJPw%2FOIAR3iDduwh4SsqiGqc8OW8cO0ifCJUJLxBe%2BA2qylkwguIAx7hab%2FetkS5fz%2BLdgU%2Blir3IlvtDZO4YHT6IrzkesQTixJp%2BAbtYBOojTX4y2Kyi5XZxpVmW9rBplK1soEut2QqaJcb1isX0EnOuj2qdt3mGa4O4aDvTRb%2BGSXL9eI%2FDvCocTJD31tiV0b62%2FY8drZ2uXXGr%2BxoVonzTU3Em%2Bh8k4V4RtVyzYhXyfmWCBURb9LOt%2BB1dQx3QGVsArqAB3fsOCQL7qx65ZrprlLTIRO7DiVTwWg7tFk8Ov6D9%2BMhurk6%2FK3a%2B4%2F3YABfScchRQGPLYekAZ5RqFwz4FXqOmRi26GkgxrteXNeZu6jGzwA3sZX0nVITcpb2HVIGuUZ5cr1Ut4q54BrF%2BUt%2FqwH5SlPO9%2B2m%2FesC3NUr1UWkAY8wJerZ0XA5xQ5MIqVawZ8OSdcywBvchtAecDT%2FjfgRQ4C4oCHeOwoJw3xjFrlmhGvUks5C1vKJVNBe%2BCAVzkIiENlxDvuP95C%2F7M%2F0uZXHw398%2FfvA9atQEj4igjPqFSWRnimbek9fBfvOc6VLSjcM2eCsaHPv%2BO4w9nylYtDZdyz73yiwzjXW7lkygFQMVsM7BjgBm%2B%2Be5I1Wf0dXaCjKAKVU4mwu1PLNqCDKCrVsg0wrJJMBR1WUXB1LljLJqATeMs1Hs9k4b%2FxWraBSiGWAcgDGXsq6BMZ3sApIhBwlI%2FPHUj5yinfeDnbUKWLHYb886865Yf04W01i6b%2B6DIHAiYRVkAY8OiOdzrIonvz9WxDlS51SJSKeB%2FShzNnYbvRz20LHFRPfBWQAjygg%2B4vJxfojdevDemUty4GzfOFi3wf0slv9nTqO%2BvMUof2SaAy1mMzucy5GWEzCmmsb7yKbaRSM4oRNqNIpoKRtr7dsHsrZxnd2TPzNlH75qNrNwFs6QUEAg7zY9BpNlIx33wt25h21bbwMS%2ByoR9jik0yFbSXFXhhm4A44PEe82qk8b7xwrZxJxJrCvEes2ySqaDPbsCr3ATEAY73JAZQ%2BjKfhztnvXa9ZaYuAJU%2FjONkmSRBnpE9o1sMi%2Bq6LJYTAvpkJpBuf5B4mQoIpnmlrdSE0EczlUogDurFBZsQLIKoRik5q7de7erNM1wd0tHp1RvQIiBwXCuwCDDqIGpeBHR6iVcm5H6QLq4AJH5qjwy92G7CwYXcRWQBEPeYYCUN97xHOom4L9dUrF1R94NWke9Ep5OqsEe4iEIAoh4v65SGelZ1RM2sj0dWhPV4YefBsvShbeW7k%2BjTvrm5fn97%2BQEO4Cu5qVNRwBuYQCsP8IxqiboB34kU2kKeG4GOj%2BrTnj6zAc%2BuEpEHQOrjFW%2FyqM%2Bom6ib%2Bp245K0Y9fHKt2Qu4kw%2BzLEqIg941DfpM%2BHd7urXDEFASq6KqZ10B%2Bf1ziQR2uo5nlxDDnKZFknkMfkN3prkKpNOuFEquSpRLy7VxKQLGjC5qohSAK7a6KGTtgg0n1xldsJBx20B9Mkd5oL2yYUb3eRYFofadUChdgF5AOQ8%2BuSkcb75rCqzEy45bgugFy6Zi1hHqTu5oSIeHXA5UgFdLCcX8S3IprLKuetaxniL3wTqM5521dnPtju3H925G0RTcPXp04eby49gOC%2BgDoCcx%2FYl8jjffFKVpcbFrWe0i9gnFu2c2xXEBbMoucoHWBgnIA%2BA3C9XOoXcryKtypTH%2FXIeulZTf8htjzOczpt%2BceqnR6vlKaZdddCTaQXkIUj94nLhGq4OvTDu7EbqV0R9vXmvTskrvttMfYHukcrv9Rm3fUNPphWQB7y9PqMl%2Bde142fqAVAubd9MJ9MahkEJg9l01iTSOF6yzXjHl2mRxE2BztTZybT19hQmjP7iSiXTJurFpZowuoNjMm0RpcDrM1yy93jHFwGRs5r4IsBIpq17EVAqmXaMybSHuaA960t7cdyyygKUZCWgDICIxzxaaYhn5NHWjXil8mjHmEcbz4Wu0W70yerHEeEJAUT4StJo1SS8rmEarTTCs9Jo60W8rpVz1LUL8QexIuJ1jXbSOQvbnfdAdp4VkQZAyGMOrTzIM3Jo64Z8Jy4B5H6SMWn2MBe0E25lr9e%2FPH%2Fay6uJ67CrXoJMAAIfk2flAZ%2BRPFs38DuRPMv9JFeWL6sA8GmX3KPrB7OHKHuqBytnSkQY8BDPuOUVEV8R4pPJbQ7xJe%2BCbRniBTr%2FKo94xj2wk%2FDnVrPIAEceeuO3OFO2dWavjPACugBIeNrDh4SvivBm84Qv55RrG%2BENbhOoT3jaH%2FfkLP1jukcuG%2FXpzq8JgHTHiz%2Fl0X3YPN1pD5wyfS0O2kXY64T2xdnTqe%2Bs1%2FA6WogIAx7xY8Aj8WUUTTVOfL3cca1l%2B%2FlErIj48LBIWdZdP6w3K8ffbMtU4451%2F%2BttQ7GtM3plfBdQBUC%2BY7K8PL43XhWrl7y%2Bu837eR1T55O5iH8ndiwqIg941GdcDo7Ur4r6jZfB6ka5Q1ubqW%2Fw20N96tOHN%2BAdi0TkAZD6HMG77UO5a05Ewn%2FY1SxYzHu7TiXOcnrp%2B1st3HwJrXzv3drL18iS0Ud2pkeP9Vt74c4jHr5z5s9O4E7s%2FTdilUydH%2FZmHjAtuzfh2tv4Eyfn3xNzNojXnaw3xjeBO9Mnh5cYRGMYLXnRd%2BZ24D47Jx84Rxmfo2XuoLmBNbgYa4c%2F%2BwHiQMBglBLHbir2gxyEQY1rxrVbh5FSn203V9RI1UmMI6u%2Fdok5L27wV%2Fwbwr9%2Fj4a5sPZfvXnZj7r94jVzf8Ary%2Fguw7OyTLohtkaX47ivQKwfa1xQiSSJJ2cOJV2KHLHKTkgxVKD%2F%2BtfxF0c%2FFX15%2BLHtV%2BUlHOfxnZdw69A6IikEjocFJZy%2BENqg7nmWrmDaefP7LiUjYwMHqMUg0dLmGTGyo5KY%2BonU4q7%2B1R%2B84o8A81wt0M7uoO1S93WzzCvvWG3SXhOVWgwe1Itnaz25kRpbDJZTSs4x26xUOVzD1SIdTIGWtgiw7utmLQKx91%2FCItCJDOhCvlWzsnTovOkX5396tFoeYtqRcbbfYIcXAgkSEQR%2FcclwDVeLZjA7Whr4R6PGwV%2BuPUGrwV9ZarQC4KcToqCnUgjIAyD0y2VYIfTzupbEqfnNUT9ulKUi9fntoTz1Ldq1Bz2VQkAe8Khv0e7B2%2B3FwBig2X%2FXil01SXyGJQ%2FWTX5EngffAu2aE4kFJAIvFZ%2Bp9aJG3aJdc0rFZyxsV3CYC9o%2Fh%2FGZIkoBd3GjbqGbTtoiwIrP1LwIqNzDwMIeBoe5oB11i%2B0WHF4HAwFZAMQ9Ouik4Z5xHVTNuE%2BuqFYS95V56LqP%2BwHtodv2J4OI%2B0o8c4rifkB75igtNJb2f0j1%2F947FAGcS%2Fs%2FZPp%2FP%2F5e9Wn%2Fu%2FedzfpPForWZP0P4oUo9kVZekp6vFn%2FI%2BvcSLKz%2FgccPsrGBNzXLjTN7B0Xr4wMg0%2FHJP7RQwmLvvvZHDVvv%2Frs%2BG44r1vveDx%2B%2BrXisk%2BCChzCH7RM%2BCM9LVeroPCpchdqJOnC50iwaUXBVvgQkHOiZyj0COimpR8%2FCNFTZYyKPAklYB8nurRGy8RIhYz0QVExEzNu4xoPNRpbF9qgZkFz9FZqhaALF8O2RzsJxGN8JXdkF9BOaigtvY%2BVLZwRvYf9unb8h2t36SxsSkMAo8t9klqudI1V%2FldzeHmE4WXOI2yi8A6Fl0eKh5dHGF4%2BzAWGl6tRCjwH1AjDy9IWgebDyyOVw8sjDC8f5oI%2BvEV9kwGGGwRUAZD2GF2WRvvmo8vxJ1CT9hhdPhiaji5Pts4WiLzH8HKOUGjXHKWF%2Bn26cWRhG55LAgn70EJ0LWuRINv0yYmZEi4WM%2B%2FJW9rzm8Or2X6884G0UdsCaf20A%2FnQvV%2FUgdw3h5EZjtp7Dk9HJmPtYnzU%2F1M%2F%2FT2yvcvjVgaYj6LEZNA7iRJr1gAFfDYCYqZUZqTbFfLqV9dGpyNp48FFzaGzMavLzmC%2BX9iWJ2Id%2FLvxgr2w%2BuutaC%2FDN5jW6mVr4%2Fj74d%2Beov9ee4vV3NneTP%2FZ9%2F4JF5x46PCz7kbfvZF6KsLlMDh9GKhgR7RohjqfX%2B6%2FsQhX%2FK3WtlGQo%2FX%2BdL8ebcntTeCt989c9O8MfO%2Bnk9oSMHYJmSIWWL9TEa%2B%2Bxephzyq8TjfXrHDrzeokXJECbr99jsd69A%2FWhi0CM5VDRcY6LQLC2odJFAHtS71z7GD9sCu2vXPWa9dbZm7GAQVEqah1eHZtPiA6Ltczp%2BPeEZHg25jfydaagOiYdpEqFRBN1IsOEn1M%2BzkxIFpEKeBcJsktpzAXAREXufgi0HhA1NBoz6kyLvKDdHEFMGI31ZGh1%2BFeHJ6DXEQVAGkPOgdSLu0bD4gaGu2XU4j2mAB5mAva%2FbbrrrDe%2BVwgYh%2BzHqPRHPcfb6H%2F2R9p86uPhv75%2B%2FfBqs%2Bozqak0FypS6pmcVtuJV6%2FReuEu9Yqvoa7PdEiPV3nqpOUarjrZZLAQFJ6k3YIVxctYopvSHuJL6dTPwRVJo4AeYb76U6MZMx7atTTtc9FNhJsk6FjmLJsvrZb6Rdmf2Rl3ML50gW1S2RPBTqFK9EJuO1iXLwJE%2F%2FszWRF%2BK%2FTI8y2LcdRoPmn%2FoyDIF%2B1SH5GhXr4UDhOdC6IL8gKzyrpG7JaJ4MCzoGy0oAHe9B7famwr9MhzLYtR4uT5p%2FyQrDHbX4yFfQ2f%2BqGj4U7AYt73Ntnzg2jZg5xXw3uk%2BzbxnjPqJNr4WNehPdj3NwnU0Fv7pebxaPjh6%2B9%2F3j%2Fv%2FA%2FYEgvIAt4pMdUD2mktxonvQr3nOfLFknPKLKauMEr0F29gDDgsR67Wklj%2Fahx1qtwtXm%2BbJH1jGqt%2F9zVxJs6R7iHtLPHtlbZ%2Fi0O2jfXIkK70HunDSK05IVKmqefbf9AYj9IaxL6%2BmbqJoDDsiLevyS%2B3yMZSjMu4u78NeX0MeoNW6DAAr3Tz3chOb7oRR%2BfKLtSVR%2BnqeZmrJyVf5xj0Br1p7QfPp4Fta9rqadI01Jt5KvT%2FdXf3vX46tvPB8P57%2B%2Fl5%2Fnwe0D6tH8VU1mPUllT5ukPeZscVJLKyrQY7SwV2TR1%2FGDENmyusluZyMr8xLR7s6N5rLm6BXUyYs4E7ekEmcVaUiUqH5KYU8NqUAUG%2FOydZjXgrzOFlfmJy%2Fk62%2BEOy5UsMp%2F2eELJXy0pDHCYL5fhiJhvRfIq8xOXa93fYsyPuE2hOuZjPxDI1NWS2gBHelIuuRFR347EVfZHLuemazHsCb81lKc97bFLElcPEe6emkHusuKAh%2FtyGY6I%2B3Zkr7I%2FcjnnXJtxb3JbQ3nc0346GNmrZYUBD%2FVYgiwL9XUmr7I%2FsgolyPmqRdQT2lcHJXm1rDTAwT7%2BGO1KHTxK8uuJpPidTx8skJRIq4yRI5gXKDpJEew%2Fv374qQXLd7%2BMb8Ht7dPn4WNf3x%2FFW5Mi2E81vOxbZpTUenRL3%2BmIvBmDp3el9YfprFvJ%2BYI6h8%2BySbGbQmJnXuO31%2FdB09%2BP1F61vhkZ4B%2BvVzf%2FTtef7p9fvvx6udTI1eSPvtW%2BBPDUBZb9EL4nAk%2FfM8mdD27E3Z7ikU1rfDE%2B%2FmPWq3kOX24ncsMzZdoaVZF0avWQWMVURIzR6UhWemtQnWou%2F%2B%2FtXy%2F9P%2F759vu34R%2FjX%2BZX4%2B%2BfjIyPu8nMmW6ibUzGPhFQajUZpro4D3h9eGRcwcmOaTHQmRdsu%2BYqu5WZ1cxPTJ%2FmOppZnatbUMd25kww0i9AplaXlInKR3i2bjATQxL668ytZpuWY%2FPe%2FDN%2Fxl2bL1rkPiMRYxaeE8JX7t%2Ff3qjaQKysKuBhHjMwJGG%2BztxqtmlVSMDIFy1inpGAMQ1%2FYfjKm8t7Fuav9d6l1kIdVAZ7zMHInhvMwZAE%2B1qzq9m2VSEHI1%2B1SHtGDsbEd8JfOX2wgz3zwezqMf8ic2548i8Q9IVAX2deNdu2KvR%2Fz1ctgj626ZGRN6spTNALyEJl0K%2F%2BtG9fvk5%2FvA5%2FfZ25A3sz33xi9Cq73V4Rfre%2FIhzj673s9IcB76adVAFzpv3KeeI7vk6z7Zqr81bG15mfWJnOZbm6BbVSM2cCO5dVoRJwCzd2LpME%2Fjqj68xPTDvk37Yf%2FHzGANm7jDkTjN5l%2B532Qxb%2BW6eAAuezkqoAR3nQ6bMyKV9ncJ35iWlHvDKUB5k7y5Yl7UZfbN0r6717BRzrMWE2WyytLAMscl1GXDrYj651MXvH1YMX%2BmDYK1BBSMuLUeWXt7tocTmWNbyorCBrqKfHqq4ki61aDg9kY6rViqhWuxiPBynRGkaloj0uYc3NOO2euq1UjfZoNL4wxwXlPdTGp4PpEVEyq2ElS12nd%2BMYHjm21uDU9AYxOXfZldQfsm1WrkFwx09QIg55%2Fp1ZayIk9O5aqRDJmNsiqp%2BjDHprjEGSAjoBd6YyOHan6uJfwIEmjv%2FG4yQGHSFv4VNfxIGWqBbJb9DhcQBViGVVAY%2FzGA6XxfnGIyWGCld55asWOW%2FQAXEwZYhltQGP9hgWl0X7WusQ2cZV4UqvfNki7mPHMLA6xLKyAEd6E5tISSN9nYWIbOOWc861mPQmf%2FBMedLTXjoIhYhlZQGP9LSjDysRs2RBjFSnX4MQTprLK0U0QfvgBAK7Jn%2BHobaE2k3aB6dSqN1ER1wyFbQjDkPtBXQCbwFHp5ws%2FDceajdpn5wy1SomeuWSZGLaKwe3KlFAF%2BBYb6FbThbrGw%2B3W7RXThnWW%2BiXS6aC9ssBL00UEAc84HN0eccqr5wqr9yMvrNVXvFepEVlXqmbCg1jWKLOazAep0YjKY0XLu0Kv%2FQ9Lzh%2Bu2%2BvZrfe1Ine8f8%3D)

## 3. Início Rápido

[ Voltar para o topo ](#tabela-de-conteúdos)

### 3.1. Instalando Dependências

Clone o projeto em sua máquina e instale as dependências com o comando:

```shell
pip install -r requirements.txt
```

### 3.2. Variáveis de Ambiente

Em seguida, crie um arquivo **.env**, copiando o formato do arquivo **.env.example**:

```
cp .env.example .env
```

Configure suas variáveis de ambiente com suas credenciais do Postgres e uma nova database da sua escolha.

### 3.3. Migrations

Execute as migrations com o comando:

```
./manage.py migrate
```

---

## 4. Autenticação

[ Voltar para o topo ](#tabela-de-conteúdos)

Django Rest Token Authentication.

---

## 5. Endpoints

[ Voltar para o topo ](#tabela-de-conteúdos)

- Admin
  - admin/
- Users
  - POST - kinema/users/
  - GET - kinema/users/
  - GET - kinema/users/:user_id/
  - PATCH - kinema/users/:user_id/
  - DELETE - kinema/users/:user_id/
  - LOGIN - kinema/users/login/
- Cinemas
  - POST - kinema/cinemas/
  - GET - kinema/cinemas/
  - GET - kinema/cinemas/:cinema_id/
  - PATCH - kinema/cinemas/:cinema_id/
  - DELETE - kinema/cinemas/:cinema_id/
- Movies
  - POST - kinema/movies/
  - GET - kinema/movies/
  - GET - kinema/movies/:movie_id/
  - PATCH - kinema/movies/:movie_id/
  - DELETE - kinema/movies/:movie_id/
- Movie_Theaters
  - POST - kinema/movie_theaters/cinema/:cinema_id
  - GET - kinema/movie_theaters/
  - GET - kinema/movie_theaters/:movie_theater_id/
  - PATCH - kinema/movie_theaters/:movie_theater_id/
  - DELETE - kinema/movie_theaters/:movie_theater_id/

---

#### Colaboradores

|                 |                                       |      |
| --------------- | ------------------------------------- | ---- |
| Diego Berselli  | https://github.com/diegoberselli      | PO   |
| Renan Ribeiro   | https://github.com/renandcr           | Dev  |
| Gabriel Dourado | https://github.com/notoriousgabrielrd | Dev  |
| Paulo Guarnieri | https://github.com/pauloguarnieri     | Lead |
| Daniele Calixto | https://github.com/danielecalixto     | Dev  |
| Camila Suzuki   | https://github.com/cah-suzuki         | SM   |
