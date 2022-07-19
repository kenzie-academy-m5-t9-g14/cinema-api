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

### [DER](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1#R7Z1bc9pI08c%2FDVXPXuDSkcOl7Tib1NqJ38TObvaGkkEx2gBiQTj2fvpXAiRA0xKjw%2Bgw3amtTYyxLKb%2F%2Bs1Mn6ajX89ff19Zy%2BmdO7FnHU2ZvHb0dx1N09Rhz%2F8reOVt94ra7%2B1feV45k%2F1rhxe%2BOv%2FZ%2BxeV%2FasbZ2KvT97oue7Mc5anL47dxcIeeyevWauV%2B%2Bv0bT%2Fc2elvXVrPNvPC17E1Y1%2F905l4092rA1M5vP7Bdp6n4W9Wlf135lb45v0L66k1cX%2BdvGS%2Feu%2Fdhbe%2FxXt7NbcW9sLzv3NnrX7aq455M%2FW84JNedrT3%2Fn8%2FgndfPLvu88y2ls76YuzO%2FZfHa%2F8t739Yc2cWjPPRha72F%2FJ%2FnX7T0a9Xruvt%2FjV%2FvbZngbFCM%2Bzu6X3Cd6NxWAXX5fiB6%2B7L2%2B1PxVt8%2BKV%2F8%2B7unu%2F7T11td5UXa7bZj%2B%2Bd%2B%2BL49t2NkPcWDrs%2FWMvgn571FLx0tfaslbdXh674L%2Fj29ixn4X80%2FZ26%2FXo2s5ZrZ%2Fv23StTZza5td7cjRdeKPzq6ofzak%2B%2B7MQRvNfXya1%2FseDL4OLBMH%2Fd30zwbWvmPC%2F8f4%2F9zx78xquVvfbv5dZae%2Ft3sKOzH7AXe%2BXZr0cv7Ufrd9ud297qzX%2FL%2FrvGYK%2BKt5jGfh10p%2Bv716ZHmtP7%2BxetvZCeo2sf7OP%2FY2%2BiDObSGXMlGsr%2F6J5jzb74z6C1eN7a7NQkwbhOVu7ywVo9297%2BhaXrBCN682LvnoLt4Duz2bU7cwPLLtyFHb5t%2B%2BHMK%2F8%2F%2F%2BNeKxdmx%2FRv4Nr%2FWj187f8XvH3lXbuLtbfyFRL8Kts31C87MNaV5y73v2dm%2FwhvY7UfzODfT67n%2BQ9VkllTZX3e1nvb6rymFWVZg7Hs%2FR9ZbOv6n%2FXHbIuzqTOZ2IvdIxkg2DrYGzAlOP7RmMeNEX8QOe2hc9vj2AAZx39%2FscOoZL6aNfO1v7A8%2B8rdLCZrxqjRfea3s8nY2X%2B7pmw2278%2BfX4I%2Fv94e%2Bv%2F9fjp4%2F893jRQBCF9d%2B%2B9Wi%2BtsbN4vt39ZC%2BmElOESl6Tn1qlZNU0QzY9zOBXBIK%2FVzf4%2B4UsW9ETzzn6Pe7Rlx3zA8aqC2se3Oq3yy%2FXHy6%2F%2FM9UfpOH96XLAx3fh8R3MXwf1s330G8iBeCH3MMvO%2BBVlTHrZLOyPMdddK61zqVyxHqdYX3j7F8W4vkFIjPiP10vb%2F6drD8%2FvLx%2B%2BfV6qahX4z%2B6Q9bXRowvhfGqViHkYdsWc8zVBvl0oaKiPDwUrFtuN3zWbBTAfvEsPeaLSgQf59m9H3G%2BHM5zB2CEcb7YPq1hnB9wG0B2zkdB4iPDrp2Fu1zbzGpeM83fwhcbZ%2FrSAM%2BvDXSAVxV270eEL4fwg7oJryrFtmnNQvxBqsR4VWE3ac588hQu5OOcVxX5MZ9FHwg5z%2B7%2BiPOlcD7KJqyR82wmRgMfdO7n2OA2gfycZ5MlVvbMfwbs0cT%2FzRHo310%2B3GBx2GQRCELQF0vCINAng96oH%2FTF%2FHFNA32f2wTyg571xo1n7toHJGbQ8wtEZtD%2Fo5g%2FFh%2BvH4e26bxzP7nz%2F%2FTvXY3SbERxvl8h50HbhhduG%2BbThYqK8rBdWWfreGX7v3IysjzZEV9UHOgIrxfz3hLhEwkfWbg%2Bwrc0ySZdqER4nXWzbpYTzITPIA6ZCf88fZzqE%2BPX%2FONQvb26d2fL6%2BuuQcFXWBu80E8mfJVFsLBti83elRL%2BzPinaFdqwsOfm525157lbdYja%2Bw5L8FNX33%2BfHtz%2BSlGeOXdzfvLx9sH%2F2cevrS5NqpMtciMfLjWgpXPtktF92EabARX1K3C%2F44Z61bR7Zu8NBdW%2BoQ6fp6hPYLKX%2FnelH4VKhs%2Bl6lhhYoyng4PBRtOp5YVOXSCb9qmqLoo%2FNfetUJtaVA9XagEexWIkG49cGfbVzTO%2BGWVNGdQBzrEh4W3hPjSEV974wqtmKO1WYiPhEqID814ZFfvbXkMdzkLmYvqQma4w6lkgFKI7uXQvf6WFarW0nD6Ga2iAnzCWLB%2B18Vm%2FmSvRu6P0dq2%2FEdJUz5%2BepAQ8oXFgZDy1K9CGOVrb1ihFkx5bhrlqWVFNBZAwrP9OnWeHG%2BEYj1fWCEyo17%2F9%2BXvr6MPf2mbm5%2FfXj%2B41qe%2F7W4P9fEBYklfZeMK2LjFgu21gT5dqag4Dw8FG2jfLuFHCUFYiVpWFJWGzIAH84bVginyRPiUCrcqW1YkWLeliD%2BjVVSMTxgLFvLIi9yyyAMh5%2Bk8GGGc5%2B1YoZnCON%2FSM2HOaLUw59NGPDvn41er5Lllfa3IS92yyCMj54vIpXK9gBUgofsYO%2Bbz1LrtyJ%2BM%2BR5neUQZmIeN26L8mjzlSzvxSg15%2BHNrjF2p2C23WmRmPpyRxLpwrp2FPbcS9YChyC0salOh1XkPsJyhluCGgQ1EVW18M7CWee8FPeWQccXlvMpd1aZRVVs0FFTVVopOUubnknXTFOFQVZso%2FENVbdXiX6aqNo2q2qKhYJPg6DjmLAKRmfJgHlmPukyJojxU2CaK8rBtWQdNA59ydvzThYqK8vBQsJ6TseO9dVAmwmbQBT64o%2FbgCIU7WNdWLd1lOtenh9JhAw8F67BZToOhPzqxTcWDd%2FLQJI8NeWiE4R0qaKsW7y110aQrlfDeY1009txygp%2FbLtslKmsoKgV0QA%2FPliGglw90qG6tUqD3W5QGdfYpjpRKQO%2BzXjZrMlnZ63VH9jZyRaWBD%2FBUtiYK8GDZWrWAb2nVWrpSCfB9oDDZC47dROlvzyAMfHinajVheOfNhxWH95YWq6UrlfDeZx1t%2FznLsTs58bgjAnwpdWqSAr5YkzECfArgoYOVKwV86CGSA%2FBDbgPIDvgB4Hjbetndpb3wETmaupvVsbNGVRD44TMIRGbMJ9RqE%2BdFcR48XlkU52HrGq0A%2FWnpE2OOM8JFhf0EM7PcR99riKCfohc2kEPQLwn6VRa8Jli3FacA5IJ%2BJFyCvmqwQRjsjYcyyENm6MPdOCggC2uDexpIZn6VVa6wcVsRkAWQn6uvTII1JCI%2B%2FLnh6Cx1IcqlFpknAPgcBUY999bb3B%2B80cP2bIkEUWBoRbT%2FbjdMrNlz3QQisZoJWFPtlQB20GioN2qwWVPFXaQvEWhaYTEYdjnW0rZEqbpFtU8DR4JdmaFsSlRQJcmztaaVqhquy1Ugm2Ilry0Hf4bob2bwA3u1asFfLHOuWbF3k3v0Zcc8mzKH98Q2flWgwzodzCkI60ALomqxLtOhnHQkZ6RDNoECT2S9oDZkhjscfyrY%2F5%2Fwnoh3qAmRML4nGLeYL65hR%2FiY%2FCaQiPEJY8H64rBH0jPIQ2bMw%2FBiKX%2Fnvjj26Ku9XjvuIlEXiEIpw7DGIQylQC1CDciehqgFukqxFM7JuYxgCmxcYbaVO5oSSRfVZA0PBcVTStFJSvqDWq5ueC5XhXAooiIK%2F1D6W7X4Z2Mq75uPf05zUIwlGgo2yDLfLry9aeCSW42SZoLGCaEsZ1wGceADPsVaRAGfezMnDPgyRVtUCrdECUFsuGU9ntqTjX%2B%2FoR8OYUA9g0LwYR4I0RHny%2BE8ePRDtaAHnK3yLO0j6RL5VcA9u1vc41vUZ5AFQtxTHaMw3ENHQVSM%2B1YUMnJbgFrLHsaC9b%2F%2Bsu2fEwvpaW5ZxIGQ8tRfVhjlofMhKqa8TA1mD1olyquA09V%2BnTpPjjfCWw%2BRRSEIUU8dCEWhHjwpolrUAx7dBj7p3BZA2XQwwbKsZ265csbB3b67uf54d3mLh%2B%2BlNBtsPd%2FhVGKFEm%2BE8R06KkIU3xOs24py5lzNBhWUmTcJY8Hu2PDUwRWWB0LoU%2FKNMOhDx0dUDP1WpN%2Fkgz7KZBx4LIDMCux1cRnkITP0wU6LQENilMw%2F06UyZRpIZD54lIQo5sPGLbaLq9SPk6dN6E68UkMe%2Ftzs%2Fo2ayuZWi8zMhxN2WSfgV39buE6UA6IaaDWKtIYrd83go7hm9opjHLaXhnmOztLAtH1F0JrcRdCRdFHtzOChoCLoUnSCb7qmWIwo%2FNdeBK21IhLDO%2F4oYy%2FwULChF391y5TDaXjyqTKIAx%2FhKfAiivC1Vz1rrQi78I4%2FykALfBQIG2dZ25aHFO4UYUkcG1WnBrOi6N6AWme9mHOuWXw%2FaJUAr%2Bqsa856sZyZ9eTMHC8YAjjI0jjjl5Yym0EdMmMezjIA%2FHuE%2BZIwz1vjXEYf2gTrtiKUnit7KhJuYeanDX925sevVslDzPrjsKfMZpBHRugXkAvP5arQC7ALJOiXBP0qXTcJ1i22c2sy9CPholroJ4wFu4XDnjKbQR4yr%2FThPLJijRCkYX6elNlzZRK8%2FhythFwr2LjFQjH1IT9XRmQ%2FF%2FHTBj878eNXq%2BIJZmMylD%2BbWy0ZJ4AC6uG5XBWng7PLwgdn%2FNOmDNrgu10zlkFrhr6TY1OCx8AJO0bIKOakb%2FmUnSFf08i8TYMe%2B0rPcDXkzqCNpItqowYPBWXQlqKTlAm73MP%2FuC5XhXAov0oU%2FqEM2mrxz67lpek1blC6VTgUoaaYTuPr3fmd%2BDqOZxAHOuCrA9QLfqHEh8IylRJfHbArfmmQf1AuMV8dsAv%2BpfU290dw25gWH%2FOzqAMh9KlQThT0wUTbiqkvU6ncQauEeXXABlSd9WjtbSbBIOJLs82gDZkhr%2F%2F78vfX0Ye%2FtM3Nz2%2BvH1zr0992l2ophCEeSrIVhXjQtsX2bLUBPlWnqPAOjgS7WfNcz5qNdi%2FI3He8oDBkZnvCxEd%2BemF0hw4QqngBL7Gn%2FiBdVMBPOOeb9dVv1vYKo7uGfPTB1f75fPXw891%2F8%2BmXP%2B7%2Buf%2F97d3L9IVW8sJYD54gJIr1oG1bsZI%2FVzeRJlpUlAdHgl3W71JoT%2Fw1sqTLlqgLqTkP1pKYVBgtjPTQWULCSA9bV97CaLO0wuhW0R4eCyqMLiAPhNCnIjlh0IfOEqoY%2Bm2tkuN4qvvc9pAf%2BqzHDnthdAZ5yAx9sEAQWCOgZH6ewmgjx1lCopgPG7fYhN6uwuidkqUmPvy52XmdCqNzq0XmCQAu0mB9%2Bo9re5WoBlRV0SHB90Tvqr0%2Bqwuwr5WwsmizmJ%2B%2B5RN2hiJcM%2FMmrYx2OMVsK3dZdCRdVNs0eCioLLoUnSRP19qgVN1wXa4K4VC9hCj8Q2XR1eJfpmoJk4oloqFgt%2BELax7ca3jshInn2IkMusAHd8qlFQV3qAK6WrjLdKaQSZmz4VCEq4bjIPvyxxHbVRUP28tInZWU7WqPkmdFwR2sdK6U7mqvmFuuWXg%2FaJX4rvZYp5w9t5zZEeJ1ZvneYqeNAI0ghD3lzwqDPVTzXDHsW5E%2Fy%2F0go0yZTRgL1gW3tNbrX%2B5q0kk5JXSfVtU4CZQH%2BzLyZqWFPeXNCoM9VAJdMexbkTfL%2FSCjTJVNGAvWJffkrLzpKEiX7UibJFtYGPgIH2bvE%2BFLJzxY%2BFwt4futODKO90GOtEqEV%2FusV27s%2F9xyGhjgyEWv%2Fyb%2FEj6DLhACnnXyEeBLAjxU71wx4It545oGeJ3bBPIDnvXEPduL1THcA2eN%2FHDn1wRCuFONmzC4Q3XNFcO9FUVu3A9yj9sE8sMdrmw7hruOAu78mkAI92J5dQT3tHqo2uEeqkwSuA%2B5TSA93Aes023seG8xtjfP1uVRnV8MMlMdbLhN2TPCmF5lkSto25bmzqTqFBXPwZFgt9jBcTCbpb3abLsJhD0o%2FtfRZMF6QUXIDHW4D5NBtavCsF5l8WqCdVtRvZqrv5yBspY1YSxYdxv2pqIZ5IEQ%2BlTTKgz6VRa1Jli3FVWt%2BaCPssY1oYMm64bD3lS0lKPc2w99%2BLw0joS67TO5ax%2Bn%2Bp%2FraurNZ51dOyl7MblcrbZSuPniG%2FnBvbMWb4Ehgzu2J0dP9Xtr7swCHH6wZy%2B254yt%2FTdCkUzsH9Zm5oGG3d%2BlF04m%2FpfX3Ze325%2BKt%2FjwS%2F%2Fm3d093%2Fefuuo%2BuG5Pnm1eDqgKYIroxZU9s7a9GY%2FvI8Xe98HcdaSkcLW%2Fnwj6MROv3c1qbO9%2F6GBe5jpGrL9d5JQNL7QbGuZCpbn5OLKumqOTxphfjXJmwyi8llMAzJXU%2BJUEK4AnsbpyBdivjvdX%2BBv8f38PLnNh7r9697q%2F6vaLt%2FCLhT8Qfx1%2FcfRTwZeHH9t%2BFf5cotp2JkxZLw41Fl%2FwVKWYDRNwf3iqOiMvwIYxEA6ViuXbqomuMfbv6v0YwPIKgLmSWTXAOLxe1QMshJF6oai9UyBpZ4C0%2FereXjn%2ByGx7%2BRajFLDGSogHa00TqaoPTqWVW6SqEVuvqT1RIgVnAJ11vP%2B%2By5JN2J8havKsKrE5RNWBhPUIUCdKM3vJoirkV9FRZ6zClk1XdpEmz6BxhfnMdNaB3tImz%2BnSJbeZzrq%2BUTZ5LqqTFP%2BZUapuuC5XhXAop1UU%2FoE4OYh%2FbSAI%2F6HE5IuYRKotTP60wc9O%2FvjVKniADdYvcLbjc4ungPIFkhH5%2BQXDdbkqQmwqxclFMX8wqJn5qipvmFwtLUzeeupHwRPKjcojD3zM1zjCB8T8XMxXQxdrfdAPjSkh9DO4WeWHPpvEgD03KrsXHg%2F0gfMi7twXxx5RRGb%2FXTMWLVOhmjUNOkhZFea0x314Qwb3fyTvQgEZUadkw7fMztMyBWRwnuUADwU7VVNAJodOUibtcg%2FJ5rpcFcKhgnRR%2BIcCMtXin02Oed98%2FHOaA2WBOjwUbErNfLvuTpoBGieAsrZn5ZzlICfoqdG3MNADxYrVgh5I1pYG9DibfsNDwW7nti1h8YG%2BnI7fcoJ%2BwNGLpLbCo0Ox0ffOoQzpXOHRhaGf5Pp3lQtF0zui0v3BUsn9IJ6tSQqnj8Zk%2B%2FdidSSqkrembqCfu5LgbP9BI0tS9tIORKkYnePCuoGu8ylcDX%2F0qJpFzyXw4Pq5RJ%2Baynpe9UbDVD%2BIFwArZk7Vxyvx2CsJVr0KBFYaIPucZaGBQsI1oL%2B0n7rP7sKa3Rxe5StnTxipQcNk2NVjZchMFR9%2FqVW4zw9LSzXlInT7VqZEdqPx4Ix%2F2t569NW2vHXikhNRkE%2BLBfn0MMWjvhhf0TO8W775zxBSynL2c1OifNA53jKF%2BQ7qJRcAdPw2BfryKAWdX6Do2d4tnwQyeIBzTAK1x%2Fqg872l8QEfpEszAHQm99pfe%2BNzAmdRBULaU9WVMNrXHvCDDviWiPbUnzQaCyBsv9ysxlNrjTDsl0UZ%2BIjPcxZsjQ27MrqJj6Iq2zvNEFUpNQQSeeVa6H0expzPhhGTJa%2FzuWeeXsjUKnY8A6fhNkDbRxrVTltqBqt0vshf9seixBZ2Km98TzWbFuCLDtALS%2BHjDTK5O8XGLlR5VBs66PFxba9G187CnluJ8zmimEpXi4Vzuwavx0VgVKXgEY4t32Jl8eBnOBGwMVEV4BhHqaIqkXpplxW1aKWoSkGl4Nt1DTg6%2Fcs7CWTxs2WfBOqPqgzYPbU8frZIujQDqEDWdHC8J0IfWwZVIKQ96vbVYmlff1RlwIZWJaI9ta8%2BjAUbHB1vnS0YeV9Ku2pZec%2FR3rK%2BmMq25GRw7EH2X9HUyKecqXBEZF5%2BuKZojPe4q8WqOg6R1syJ%2BcYwMMPhj9o%2FvbKuDP3vD6M%2F%2FWqPSFHDebWZGgYO8lHMHin4bPxDi8lMzRvci2bDyLeu6Bf68OiPKL1eP979%2FPbN%2Bvz2yft9dPX1%2Bp02XnZZt%2Bu2ixzVlvjfMWLHy%2Bm6yc7FOnjWQxxveVbNoL1Y12mW1VLLd0SwXVN1XSQEAptWlGWlKStJ1S2q7RA4ElRSUoZKkjdHmU%2BuP6ManstVIBsqJxEEfiDsUS34izk5K3riOUcfZeUIOBKscxPXyT0F5YGO71RAIojvQKCjWr634sweztFHWSsC65D18002K8tz3EV0WEOIep1BfePsXxbhyygZkZTwKure%2FyIRHx2YVRvj1WJ%2BuWZBXuU3gPSUZ71yu%2BGzZqMA9otnnJjPIBF8nGe3fsT5cjjPHX8Rxvli27SGcb7PbQDpOc9u0tbOwl2ubWYxr5nmb%2BGLjbN8aXznlwY6vgOnsxLfy%2BH7oG6%2BFzxJtVl8j4RKfA%2FNeBx1nU%2BewjV8nPGqIj%2FiM6gDH%2BKpzEwQ4jW1dsQXO4OtYYhHWVQGDwWbIbGyZ3bQuik4RVn2E5SLygMf46m4TBTjjdoZX8wF1zDGoywlg4cCqCSbuWufjYgZX0ZFmayML5Z7QYxPZny%2FbsaHF5aD8fz127IzXmddcOOV7f%2FKycjycBKeXxzoCK%2Bzjj0ifEkFUbUTvpgXrlmEj4RKhNdZD9xmOcFM%2BAzikJnwz9PHqT4xfs0%2FDtXbq3t3try%2B7uqUGQ9rgxf6yYSvsuYVtm2LcuPPjH%2BKdqUmPPi5QxEdp9N4lrdZj6zxtguDplx9%2Fnx7c%2FkpRnjl3c37y8fbB%2F9nHr60uRSqTLXIjHx4OmRDOduuFN2HabARXFF3ik5Qt7o3TOR119ijT3UQCPHeJeWt2FHHVDK0Q9D5KyFT%2BlNknTuK2ZaNqcjUoEKnKEs0FOyKm1pU5NBJyrwN9aoqopuGCIfCLaLwD3WpqBT%2FwJK%2BgU897%2FhTuCWyK5DxvHXBnW1X0Tjjl%2BaNKyXeIifiDYq3iEI81KiiWsTLFG%2BJhEqIN9h4i%2Fe2PIY7osrlDLrAB3dqMicK7mCLimrpLlOfOYMazUVDAXSa28yf7NXI%2FTFa25b%2FHGnKx08PaABfSpM5SQFPsXRhgId6U1QL%2BBYF088%2FxdRpLmqayXre7Nep8%2BR4I8TL%2BFIazclJeZMazQmjPNSholLKm8UccM2ivMmf9SA95Vnn23bxnnRGmuztKTJIAx%2Fgi7UwIMCn1LVB%2FSmqBXwxJ1zDAG9wG0B6wLP%2BN%2BR1bRnEgQ%2Fx1ERUGOKh9hTVIl6mLqImdRGNhoL1wCEvbMsgDpkRD5Z7UHOKBG1wUz8Z8VB3ClGIh2t5WpQumadWaSdeqREP25X1rVJlW261yMx82%2FnHnWt%2FdgfK7OqTrt1%2F%2F96DDv9EiXwh9VEVIh%2B0Leu3ed%2F8%2BijGHKmyRbXEB0cCcOI4C3tuJbnp21whVbo4ZMY9fLQruwq83solUQ6ICphDN0y4Zte5T%2BLVSkA4bC%2FUkfMM1bKRsAvVL1d7zLLG2Fam%2BuUehdKjoWBD6RLOzjnrlzPoBF3fkR5tz0Thn3tuF4Z%2FmcLqPZQbMngo2B3Z2crlFlO%2FfIGgo3wYGyDKl055qIS5Usr3ZTq%2Frc8%2F%2FrJTvs9u3pbTYOiPzmxT0RQ%2FZBAGPrrT0W2i6A7WMFeLd5nObouUSnjvs5sze245wc9ti9pkL3bIIAV8QEfdU1Qs0KGa5WqBzqY5tzFoni5c4nufTXi2JpOVvU4sb2ueBEpjPZ3Xljg2A2pAJIz1UOVypawfyNSAaEANiKKhAEqVtgt2d2kvgqM5p%2B4maNl%2F8NQoCJb0GQSCDvND1Gk2QjEP1i9Xivkh66pt4GOeZ0E%2FpBSbaChYLyvyYuYM4sDHe8qrEcZ7qJi5Wt63IrEmF%2B8pyyYaCnbvhryyOYM4ZOY9XO5HLntYG9xTQDLvocrmSs%2Fs1Ip1JqmP97kKV3vS8x7%2B3KzDnsqcc6tF5gkAPnc4vI%2F4CZ6jr%2FZ67biLRF0gqn8bhtmSUYUUlD5pAhbVTFGLeVVF7ZrLUG91kHihEjjIvMK2aqrK%2BuZkqoE7qJd2bKpKVXDlKCVl9tbKVQ7P5aqQjsbO3ogmgQz%2BuhyTAFQIV%2B0koLFTvDQ5Vwfp0gyghk%2FtkaHn20U4upyrLLJAiHty1wnDPe%2BWTiDuW%2BGv436QKan2MBask44OBsqiEISop56zwlAPlsdVy%2Fo2dZ3leJKH3CaQnvVA39nlyhkHd%2Fvu5vrj3eUtHsDzywIf4HWqoBAHeKhcrmLAt6KGIpfnJkPLX%2Flpz%2B7ZkKfXZpEHQurTuc7iqA8VzlVM%2FWK7tkZTn855jsYiTOOjJNs88pCZ%2BvBRJLTUh7XBPw8kp9lCZXSioA9bt60r%2FTyJk0nHOUmEfPhzs%2Bt8SrPNrRaZZ4CEFQPrFfwaHBqeqAdM6bXhuj2qnID88xAIoqBt%2BSt5Q8M8Z2dJ5TT4DZ6SXpt11ihoXTblUqr02ki9tFlTDbammdJr8ygF3aFQqkEbN2GTAJReW%2FEk0IqNG7cFKCpzGAt2t%2BYvdCPHXJhspSFKtsogD4Scp6iMMM5DebUVc74VQRluC1AcJhqL0M977JWzLQ8r4ksJwUiKeBN1ubRYxIP5tNUy3izmrmsY401%2BE8jPeNZVZ71Yzsx6cmaOFwwBHHhpnPFL43wGdSDkPHUwFMd5KK22Ys6zHjl5SqJNamN4GAvWObcrifamQXrtCmFpdAZ5IOR%2BseJZ4n7WxFoIFIY47hfz0DWa%2Bn1ue5zhdNrwZ6d%2B%2FGqVPMWsqw57OUUGeWSkfhG5NEQvURtuon7p1Nfq9%2Br0WnFIdC7qZ2ggL%2F1av8c677CXU2SQh8xrfTiruJivVxro5yqnMM5Av0oXD2zdYseCt6ycQpMe%2BfDnZr20VE6RWy0yzwAwxYBz6R7X9ipRDoiqKbpGrFv5gd9n3TdhWnz5K%2FmCZ821fM7Okrqf4XiyxpRTAIfMSVVOEamXNmsqcEQclVPkUQrCWZvKKYRNAvWXUwAnzzXwyee2AJVTHMaCja0urPlx21oTUZptBmUgRDxVUghDfP2VFEOpKimGVEkRjoUW8uM48L78cUR4VUVEeCqkSFEKFVIII3z9hRSaUsxR1yzEH8RKiNcU1klnzy1n1kF5%2BkQWaSCEPFVRiIN87VUUmlLMEdc0yFPZxGEsWCfc0lqvf7mrSSetKrrFrnoBMkEIfCqfEAd83vIJgcBvRfkE95NcWsWEBMBnXXJPzsqbjoL82Q6urNkswsCH%2BOhABUJ86YgHu5BXi3i1mF%2BuYYjPcPqH9IhXWZfc2P%2B55TQwwJGHXv8trJVonNlLI3wGXSAkfLHUeSJ8GuGN%2BglfzCnXNMLr3CaQn%2FCsP%2B7ZXqyO6R64bOSnO78mENK9WH4d0T2N7v366c564KTpbHTQLsFeU1lfnDWZrOz1Gl9PoyzCwEf8EPBEfBFFU7UTX2tFpTPvkxyJlRDvbxYZyzrr0XqztFebbZlqWN38v842FNs4o5fG9wyqQMh3SpYXx%2Ffaq2I1rRXZ8rnW8xqlzkdjEf5O6lmXRx74qK9TAr046tdeBqsV7E7VZOrr%2FPaQn%2Frs5g15z7os8pCZ%2BmDrpoJ7fWmgn6tn3fAM9KssjIWt24rIbEk963ZSlhr58Odmg7TUsy63WmSeARKmRw5IbB%2FRXXs61f9gV1NvPuvselXZi8nlarWVws0X38gP7p21eAsMGdyyPTl6yN9bc2cWwPGDPXuxPWds7b8RimRi%2F7A2Mw%2Bc2%2FeGXbub1dhO%2BTzhStsLJ6GkN%2Br758aePNu8a0YVMlr04sqeWdsn7viGU5RxH8x5B831zN7FUDn82V8gDAX3BjFx7IZif5GDMJjrGmH17uFKsXvbjRVzpfIkxlHXVbnE7FfH%2Byv8Df6%2FvweXuTD3X7173V91%2B8Vb%2BMXCH4ngh7rKhaL2wld2P9rv9cMXDj%2B9%2Ferkx%2B%2FtleOP6La1I7zr5JV6eEb6sdRB2IX5K42R%2BjBsVhO19x3mFLcaJSklXkq4ujkSYNqlbuVU2OYZWedXcJgcfhbWauNoPVBjVB32c0p4ODi9kh41TatMwWxE4Pddnl%2FCkhBR31pViZtnAKTcRolaJ1ILDwsr35sX3gLOfXuGHqkHbRfpWwuaV5yv1mBd8TL1rT2olxy2WriIo761BZWSvHOPrlKOcrguV4l0yHkrbBIAAnbgJBCGlAVMAm113nI81aXV2KQNf3b%2Bx69WyUPM%2BkbONrFt8UQgQCIZwZ9fMlyXq0QzVHIjDPyDQe3gL9bzptHgL63eRgLws1m22PPzMsgDIfSLpe0S9NNaYYX1XvVRP%2By%2BKCP1%2Be0hPfVN1rWHPT8vgzzwUd9k3YN37otjjyhAs%2F%2BuGbpqovgMJA8TsKcqzoNvonbNZYkFRAIvFJ%2BBzCvQuqxrTqr4jEk9cA5jwfrnKD6TRykpc7dWqnK4LleJdMhNJ2wSgOIzFU8CMjfGMakxzmEsWEfdfLsEx9cWJ4MsEOKeHHTCcA%2BUUlWM%2B3DCkRP3pXno2o%2F7Huuh2za9xIj7UjxzkuK%2Bx3rmGC1Un%2FYfpfBfGP2T%2BpSgYkXTO2UWqJzN2o9A35is%2FV48mbuvxaTDm7U%2FMGNXMuNXEp213%2BPwMdZWdxLITTE6x8UnA13vcJWfqOGPHkpQND2XdIPrl1dvFQUFOITfa5jwB1pcrmZO4TPlKsyVhAufI0GmNuErF73ecdHVtlIwXfelilQNiwcaIz1VHfZOFKP11ZzaYy%2FVi19KtPgG7LT%2FuLZXo2tnYc%2BtxNUgooBcV40RQlOgiqmKI3IDishxrvojhbcoIjeQPCI3oIjcYSwoIleOUvDt2QcUkRM2CdQfkRvIHJEbUETuMBZsRC7oX47QQ5tBFQhpTwE5YbSvPyAX3oGctKeA3MHQbEBuvHW2YOQ9ReRShMK65hgt1BeR20ZEBp3TkFxwPHKeuMbk2Q6Z4k8WU%2FfZXVizm8OrRYJ2g6bFLg6Bl9ChqMflxetA7hr9wAxHTRb7p1dWh8rF8KgLo3b6e0R7l4eNjOkdBebiTQ8Vs0cCPhsBMWIq0%2BMd3nj1qymD0yspw95Fr2KNQo1JerP9xLY4EWvv343r7YXVXW9Fe%2Bm%2FwTCXr1sbh9%2F3%2F%2FUc%2FH3tzpczXyf%2Be%2B5X7j%2F%2BhBNe2r%2FX3dV3b2SeCn869E4fBibYEUyavs5nl%2FtvzP0Zf6u1bRTkaL4%2FXa8HS3Jr47nr%2FTMXfE5v5f60Y0sCYJWQKOIM83esz2DXhM6SgGpV4%2F0IS1x6Q%2F1cS1LA3bf78FpPq4O1cYvAGJ6KQB1qrAhUaB1Whghs5x93rv3ZHSizq0%2B6dv%2F9e2%2FZBdLkGjBThV1PY8knwdrrXPYJEIWvoSFqeDhXbO46nfaWf1p3r4%2BTH2%2F9X49Tp%2Bd%2F%2BM3n7q6RUI2TnBbPiNJyh%2FkjnoWXUuM6Lm%2BSA9XdZwMFl7vDcBmRY4zwx2tu1SGv91%2BLZ8mVBqR%2BsbY5Lff2wZZN13Yj4%2FvwLbMO%2F5aG99Oli8rbBw8F67NHGdwvqhOZvX%2Fg2IQ5ZzjxD686S8J%2FlZF92LbFjqZsRqAnXbVEfiCx1n8obDvYF4StUP29SrwXauNkkCPWU1Qa%2BGCPeq0vFPZVBvZh2xY7fb7JsKdlfjQU7DJ%2F4viPhTNGi3ta2yeODZDqQ7gvB%2FcqEEiolvdAek8DH%2FM8vB%2FS4j4aCnZxv9jMn%2ByV%2F9rHTw%2F%2F8%2F9CQ%2FoMssBHetRVemJJb9ZOehlOtEmXLZEeyA0ZO94b0lV9BmHgYz0V4wlj%2FaB21stwiE26bIn1Q9ZV95%2BzHLuT4%2BPLMK3sqRov2b%2FVyFPSD%2B3StM5pXrsSvVBNrzQ19IM0Jmu9a8R6Rh2mlexlF2EnuOhSin4R9nGqKKdvyFEOWl%2FGaue4VZrZSU1VPVs8caRrUxueKLtUVR%2Fns6ZmrJyVf5hj0Bj1x7TvP565SzZiT5GimKJ0f%2FW3ez28%2BvZzpNv%2F%2Fb24n%2FW%2Fe2qX9a9SKutRKmvMPN2%2Bwrl2LiWVFbQY6yzNsmhq%2BcYINmyqshuZyAreMevebGkea6puUe2MwJFgPZ0os1gLqkTmTRI4NFBdHRrwwyvNcsBfZQoreMfFfJ3NcIelSpaYz3o8seSvFhQGOswXy3AkzDcieRW842IdxxqM%2BQG3KWTHfOgHQpm6WlAb6EivFktuJNQ3I3EVvuVibroGw17lt4b0tGc9dlHi6iHC3ZEzyF1UHPhwXyzDkXDfjOxV%2BJaLOeeajHuD2xrS45710%2BHIXi0qDHyopxJkUaivMnkVvmUZSpDTVUuoV1lfHZbk1aLSQAf78DaalTp4lOTXyZLidz59MEdSIqsyIEcwLVB0kiLYfXm7%2Fal4iw%2B%2F9G%2Fe3d3zff%2Bpq%2B234o1JEezGGl52TSNIaj1qLn56Re6jhU%2Bv2o9n3QrOF9Q4fJa1HmydSexJxwL%2FdaLp70dqL1vfQAb4p%2Bvlzb%2BT9eeHl9cvv14vFfVq%2FEfXbF4CeKzvfteH74nA4%2B3xufPB9bDbU3hlwxxeDI%2F%2FGNVqnsOXW%2B%2FREfHG%2B4Ncws%2Ffdj%2B1ITGoZ7XmhsS9%2BKkRipJPrQP99EKGORAlzsv%2Fe%2F%2FXa%2FePf779%2Fq3%2Fx%2FCX8aj%2F%2FRNILPk6ntqTTbBaSliOIsrgVgexDvm9nsmuS8HThoclbCBBi6FO8IDtmqrsRiZwg3fMbhpbmsCdqltU3gFwJIAsD5QZ3AVlIrOnANYNJXwIQn%2BVKdywaTn2CPU%2F82e8wumiJe4D%2BR5Tf5vgv%2FLw8e5G1j5lRVWBD%2FOU6CEI81WmcMOmlSHPI120hHkgz2NibY8dfHf5AGH%2BWutcKg3UQWmwp1SP5LGhVA9BsK80iRu2rQypHumqJdoDqR7jle3%2FysnI8vbMR7OqpzSPxLHhSfMg0OcCfZXp27BtZWgzn65aAn1o0yMjb5YTnKDPIAuZQQ%2Belcyy4M59cezRV3u9dtzFiOLrB1WoRiz9occbhFXLgDlov2Ke%2BJbP07BdU3XeyPg6eMfSNEhL1S2qmRo%2BrZ6xM8rwekGVoJu4qUGaIPBXGV0H75h1yL9vPvj5jIGyRRo4EkCLtP1Ke5SE%2F8YpIMf%2BrKAq0FEedfqsSMpXGVwH75h1xEtDeZS5s7AsWTf6fOteWe%2FdK%2BhYTwmzyWJpZLVhWAB7oSh651Ai2FUu1F6%2Fk3o4x3HRlmJ0Toq2tN0P56lXzHXSTNrCgynoOi5khAu6dsmRqUATWtGlxk%2Fl6Jv9i9hhGrxFXao%2BOL2W2dfi1yqvrguWPocbszbpK0eyP3sgzaE4dziM1Slqup5H8onyPlZpatpqzuegRnWbsXrywWB4YQxzyruvDE8vpgU8SqzcFSx1jV3SU4zlyFqD2Ck0umpwLtVLKWKEbVasmXHLt2FZvPr8y7vGhFnYJbpUcZYht0Vk34zp7PqaIi05dIJuY6ZzrE7lxX8GL1x2%2FNcebNHZMHsDn%2Fo8XrhItUR%2BnY2xIyhlLKoKfJynmLooztcebtFlOHYsXbXEeZ2NqqOpZSyqDXy0p9i6KNpXWswIG1eG48fSZUu4Dx3DyIoZi8oCHekN6kQljPRVVjPCxi3mnGsw6Q3%2B4Jn0pGe9dBiqGYvKAh%2FpWUcflTMmyYIpZ9RVlZPm4uoZDdQ%2BuAyBXYO%2FTVFTQu0G64OTKdRukCMuGgrWEUeh9hw6wTeBk1NOFP5rD7UbrE9OmpIXg7xyUTIx65XDW9qYQRfoWG%2BSW04U62sPt5usV04a1pvkl4uGgvXLIa9vzCAOfMDnaBVPVV4pVV6pGX1nq7zCtUiDyrxi59Lper9AnVdvOIxdTY1pvLzSrufp41SfGL%2FmH4fq7dW9O1teXyf20nuYBkHp1Xr01f97nQi%2FdrmeGcAB6k12PSuxk%2BqiCtBKPM%2Bg9dgVC6LVKLddk4XfCL8zeHut7qSXxx6a9KtR8GMj7qRXokpkXpaC44A64qgIBH%2BVHmfw9trbSS%2BPMc4fMi0l9dlQ484F4e1W3dK5IEqUBjrUU3RREOqrdDiDt9fe2GIeYwxwoh5op7cOXCrE%2BGRNoGN8o9voBQ7jsGvezl%2Bs6GFbvQRfM9Dx7rSz3uDEAZ3f%2Bcy0wTvjjYY744WjfeyOzrlcFep8HsZ8z%2F58daGYw8OfnN304tdlHJaindCsH5O80Ale6Mg2oQaMAec6RpwbGjh2G9EataAfOsGl1RRHNHBWtuSeaI4%2BqXKuVFmnIvmic%2BgE3%2Bq1WJ%2BSluO%2FoIsiHf%2B1u6OB07NldlLspIyQ%2FayXkTzSvOLAB3zUvYWFAr92pzRwirbUwB%2FiBD5woDa5pc%2BJAh3oQ643yy%2BdfEbL4YSXzIe0TJ7tECf%2BLDF1n92FNbs5vJrB4XzsRr5%2BvPv57Zv1%2Be2T9%2Fvo6uv1O2289OeA89QR6kjux05i0fpxcXG7jsMmlaG%2FSgsrfwr7jv0vV67rHb99ZS2nd%2B7EDt7x%2Fw%3D%3D)

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
