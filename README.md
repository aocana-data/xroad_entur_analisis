ANALISIS DE CALIDAD Y CRITERIOS MINIMOS XROAD ENTUR
---

El analisis se realiza utilizando una librería dedicada al analisis de datasets / bases de datos SQL

## Estructura general

├─docker_file  _archivo docker de multistage build para reducción del tamaño del contenedor, integrando la dependencia en el contenedor_
├─xroad_entur_default _carpeta donde se alojan los datos necesarios, .env , conf.json, data_input (en este caso es un archivo tipo xlsx), scrpit_app.py el cual va a ser la ejecución del programa_
├─docker-compose.yml

---

Carpetas internas de salida

├xroad_entur_default
├─ config_files
│   └── entur_config.json _archivos de configuracion que permiten el analisis indicandole los valores por default para correr la libreria_
├── entur_default.ipynb _notebook de previo analisis_
├── input_data _carpeta donde se aloja el archivo a analisar_
│   └── bajada_datos_rltur0001.xlsx
├── output_data
│   ├── csv
│   │   ├── CRITERIOS_MINIMOS_analisis-xroad.csv _criterios minimos por cada columna del dataset_
│   │   ├── CRITERIOS_MINIMOS_SEGREGADO_analisis-xroad.csv _criterios minimos segregados por porcentaje de columnas que cumplen con el rango de criterios minimos_
│   │   └── RESUMEN_analisis-xroad.csv _analisis con los valores de completitud y exactitud_
│   └── gauge_images _imagenes con un gráfico de valores_
│       ├── xroad-dq-rlm_CRITERIO MINIMO TOTAL_2023-07-10.png
│       ├── xroad-dq-rlm_PORCENTAJE DE COMPLETITUD_2023-07-10.png
│       └── xroad-dq-rlm_PORCENTAJE DE EXACTITUD_2023-07-10.png
└── script_app.py _script que permite que realice el analisis de este dataset_
