# Proyecto App/Web Peluquería Mael

<br>
<p align="center">
  <img width="200px" height="200px" src="https://i.ibb.co/82mkyXS/Dise-o-sin-t-tulo.png">
</p>

<h3 align="center">Reserva de forma: Intuitiva, Escalable & Simple</h3>

<p align="center">
  <a href="https://peluqueriamael.com/docs"><strong>Explora en la documentación »</strong></a>
</p>
<p align="center">
  <a href="https://github.com/twbs/bootstrap/issues/new?assignees=-&labels=bug&template=bug_report.yml">Report bug</a>
  ·
  <a href="https://github.com/twbs/bootstrap/issues/new?assignees=&labels=feature&template=feature_request.yml">Request feature</a>
  ·
  <a href="https://themes.getbootstrap.com/">Themes</a>
</p>
<br>
<!--
<p align="center">
  <img src="https://mariospeluqueros.es/wp-content/uploads/2023/09/AF1QipM4by_QD-G1sdivQVIVYudYBPZvP3HPt7D_CkNg.jpg" alt="Texto alternativo">
</p> -->


## *Nombre actual: PeluqueríaEGO

### Es una App/Web para la *PeluqueríaMael úbicada en Inca, Mallorca, Islas Baleares.

Hecho por **Adrià Martín Martorell**, como una práctica como freelancer de forma
autodidáctica. No sonsiderado un trabajo, sino una venta hecha como particular.
En el año que lo hize y acabé tengo 17 años.

## App
El propósito de la app es ```crear reservas de forma automática```, sin intervención
manual. Simplemente todo de forma autonoma, y los clientes simplemente puedan
reservar de la forma mas simple y intutuitiva para los clientes, y los trabajadores pueda saber rápidamente
sus reservas en tiempo real.

Hago uso de una tecnología cross-platform para evitar doble código. Y como no se require
de caracterisitcas de una app muy avanzadas, simplemente así mejora la mantenabilidad y hace único el codigo fuente.

En la app no simplemente se queda en hacer una app, sino dividir en difernetes apps, por su úso:
- Administrador
- Trabajadores
- Clientes

La tecnología que uso es un framework cross-platform de js, llamada ```React Native```. Usando tsx como
código mantenible por un mismo lenguaje de frontend de base, como la web y la misma app.

Esta hecho por react-native cli, y usando stores con zustand. Mientras guardar los datos de forma persistente hará úso de Sqlite

## Web
El proposito de la web es acceder en ella y descargar de forma simple la app, y
hacer uso de links promocionales o de información para hacer uso en las redes sociales
de la peluquería

## Backend
El backend se hizo separado por el forntend haciendo una RestAPI, separado de forma independiente,
así evitando modularizando mucho mas el código y incluso mejorando el rendimiento del mismo.

Las tecnologías que uso es:
- FastAPI
- Pydantic
- Gunicorn (Producción)
- Uvicorn (Desarrollo)
- Fastapi_cache[redis]
- Redis
- PyMongo
- Ujson
- PyJWT
- Fastapi_limiter

Haciendo uso de un backend moderno, y fácil de mantener, y uno de los mas rapidos de Python.
Teniendo un íncreible rendimiento por su lenguaje de alto nivel, superando a Express.js y a node.js.

Implemente mi propio middleware que restringe un grupo de rutas especificas, que implemente doble auth
con jwt. En ```.../config/middleware/restricted.py```. Es extremadamente extricto al hacer cualquier operación
del usuario, y protegiendo la misma información renovando por cada operación su propia clave secreta del jwt
que cada usuario tiene. Así preveniendo ataques masivos y multioperaciónes no autorizadas.

## Bases de datos

Hago uso de 2 bases de datos, de forma local:
- Redis
- MongoDB

**Redis** para el almacenamiento temporal de ```caché```, mientras que **MongoDB** una base de datos ```persistente```
para guardar todos los datos de forma ordenada, flexible, y rapida.

## Diseño del backend
Tiene una estructura dividida por microservicios, separado por diferentes versiónes para futuras
actualziaciones que se hagan


## Distribución de software
Modelo de distribución de software hacia la peluquería:
- IaaS

Modelo de distribución de software de la peluquería hacía sus clientes:
- SaaS


## Presupuesto PC Servidor
Creé un presupuesto ajustado de 550€, y realmente priorize la baja latencia entre la potencia misma del pc, y tuvé como conclusión que realmente invertir en mejorar la baja latencia sea una parte crítica del servidor web. Y para evitar la perdida de datos en malas condiciónes como en tormentas o en fluctuaciónes de tensiónes el mismo SAI protegería al mismo PC.

Aquí esta el presupuesot hecho para el dueño de la peluquería, para Mael, buscando en Pcomponentes. 
```(Los precios y productos puede ser que no aparezcan o no sean los mismos)```

<p align="center">
  <img width="60%" height="60%" src="https://i.ibb.co/2jtGPvW/Presupuesto-servicios-creativos-simple-blanco-y-celeste-2.png">
</p>

## Instalación Del Servidor
La instalación consistiría 2 mini pc de sobremesa con un procesador de N100 con 16GB cada uno. Para mejorar las operaciónes de criptografía

<p align="center">
  <img width="170px" height="170px" src="https://i.ibb.co/gWtSfTr/61y-D0tp4-GCL-AC-AA360.jpg">
  <img width="170px" height="170px" src="https://i.ibb.co/VHMyQp5/71z-ZVl0dj4-L-AC-AA360.jpg">
  <img width="170px" height="170px" src="https://i.ibb.co/FDgpgWF/51vn-NQp56-QL-AC-AA360.jpg">
  <img width="170px" height="170px" src="https://i.ibb.co/VwrpXpf/61-GDv-Jm-GF5-L-AC-AA360.jpg">
  <img width="170px" height="170px" src="https://i.ibb.co/71wC7mR/61f9r59-Chr-L-AC-AA360.jpg">
  <img width="170px" height="170px" src="https://i.ibb.co/X4QXWSg/41sw-Rzq-Jbd-L-AC-AA360.jpg">
</p>

## Configuración Del Servidor
Usó Linux como OS predeterminado para el servidor, tengo pensado en el futuro adaptarselo con FreeBSD por su alto performance y uso nativamente de contendores llamado jails en FreeBSD.

## Créditos
https://gravatar.com/au7812ooae32

<p align="center">
  <img width="120px" height="120px" src="https://pypi-camo.freetls.fastly.net/36f397b09a7781d43d862d849361e2e6ae718ca6/68747470733a2f2f7365637572652e67726176617461722e636f6d2f6176617461722f39663431306239623365363937333832303965366131343163636137623339653f73697a653d313430">
  
</p>
<p align="center">
  <a href="https://www.instagram.com/__adrian__martin__/"><b>Instagram</b></a> ·
  <a href="https://pypi.org/user/AdriaMartin/"><b>PyPi</b></a> ·
  <a href="https://gravatar.com/au7812ooae32"><b>Profile</b></a>
</p>

## Desarrollador

## 