## ANALISIS DE CALIDAD Y CRITERIOS MINIMOS XROAD ENTUR USANDO CRITERIOS PERSONALIZADOS

El analisis se realiza utilizando una librería dedicada al analisis de datasets / bases de datos SQL

## Estructura general

```
├─docker_file  _archivo docker de multistage build para reducción del tamaño del contenedor, integrando la dependencia en el contenedor_
├─xroad_entur_custom _carpeta donde se alojan los datos necesarios, .env , conf.json, data_input (en este caso es un archivo tipo xlsx), scrpit_app.py el cual va a ser la ejecución del programa_
├─docker-compose.yml
```

---

Carpetas internas de salida

-   output_di: al igual que en el repositorio por defecto, lo que realiza es un analisis más detallado sobre las columnas, entendiendo el valor de nulidad y exactitud de negocio.
-

## PASOS PARA EJECUTAR EL REPOSITORIO

```
$ sudo docker compose up -d --build
```

Luego de ejecutar el codigo con la version del paquete establecido en el ./docker_file/Dockerfile , nos entregará una carpeta output, de la que obtendremos los valores de calidad, completitud , exactitu y de criterios minimos.
