# Análisis extra de los catálogos del Mercado Formal

**Fase:** 4.1 — Auditoría del mercado formal y scraping de catálogos
**Fecha de consulta:** 2026-11-06
**Archivo generado:** `data/raw/catalogos_mercado_formal.json`
**Entidades con catálogo accesible:** Dongfeng Cuba y BDC ONE
**Entidad sin catálogo accesible:** MCV Comercial, S.A.

---

## 1. Método

Se accedió a los catálogos públicos de las entidades registradas en `data/processed/mercado_formal.json` y se extrajo, modelo por modelo:

- nombre comercial y tipo de vehículo;
- precio publicado y moneda original;
- motorización (eléctrico, híbrido, gasolina o diésel);
- autonomía cuando el sitio la publica;
- garantía y notas técnicas visibles.

Reglas aplicadas:

- **No se inventaron datos.** Cuando el sitio no publica un valor, el campo queda en `null` y se documenta la ausencia.
- Los precios se convierten a MN con las tasas del proyecto: **1 EUR = 1 005 MN** y **1 USD = 920 MN**.
- Solo se registran modelos con ficha o tarjeta visible en el catálogo; no se infieren versiones futuras.

---

## 2. Resultados por entidad

### 2.1. Dongfeng Cuba — <https://www.dongfengcuba.com/catalogo/>

| Indicador | Valor |
|---|---|
| Modelos extraídos | **49** |
| Con precio publicado | 34 |
| "A consultar" | 15 |
| Eléctricos | 16 |
| Híbridos (PHEV/HEV) | 12 |
| Gasolina | 10 |
| Diésel | 11 |
| Rango de precios | 15 900 – 99 000 EUR |
| Equivalente en MN | 15 979 500 – 99 495 000 MN |
| Autonomía eléctrica publicada | 220 – 700 km (14 modelos; media 388 km) |

Distribución por categoría del catálogo:

- **Eléctricos:** BOX, Vigo EV, Sky EV, Eπ 007 EV, Friday EV, Van M5 EV 400, Voyah Courage, Microbús M5 EV 400, Rich 7 EV, Voyah Passion S Ultra+, ELECTRIC V7, EM 26, EV 18 3 T, EV 200 1.8 T, EV 400 5 T, U VAN.
- **Híbridos:** Mage PHEV, Eπ 007 PHEV, Friday PHEV, Huge HEV, Eπ 008 PHEV, Z9 PHEV, V9 PHEV, Voyah Free +, MHERO II, Voyah Dream PHEV, Voyah Taishan, MHERO I.
- **Gasolina:** Shine E1 Manual, Shine E2 Automático, Shine GS, Van M5 Cargo, Microbús M5, T5 EVO, Rich 6, CAPTAIN W, MINI VAN CARGO, MINI VAN PASAJEROS.
- **Diésel:** Rich 7 Tiger, Van K33 Cargo, Microbús K33, Z9 Diesel, Van K33 Refrigerado, CAPTAIN 12 T, CAPTAIN 3,5 T, CAPTAIN 4,5 T, CAPTAIN 5,5 T, CAPTAIN 8-10 T, CAPTAIN T 4x4.

Precios destacados:

- Eléctrico más barato: **BOX — 21 900 EUR** (22 009 500 MN).
- Eléctrico más caro: **Voyah Passion S Ultra+ — 65 000 EUR** (65 325 000 MN), 475 kW, batería de 98 kWh, 700 km CLTC.
- Híbrido más caro: **MHERO I — 99 000 EUR** (99 495 000 MN), autonomía combinada de 1 026 km.
- Vehículo de combustión más barato: **Shine E1 Manual — 15 900 EUR** (15 979 500 MN).

### 2.2. BDC ONE — <https://bdcone.online/autos/>

| Indicador | Valor |
|---|---|
| Fichas de modelos extraídas | **16** |
| Con precio publicado | 16 |
| Eléctricos | 5 |
| Gasolina | 11 |
| Rango de precios | 14 849 – 67 135 EUR |
| Equivalente en MN | 14 923 245 – 67 470 675 MN |
| Autonomía eléctrica | 216 – 520 km (media 393 km) |

Modelos: NEW MG3 LUXURY, MG4 EV 51 kWh COMFORT, MG4 EV 64 kWh LUXURY, NEW MG5 COMFORT, MG ZS COMFORT, MG RX5 DCT TROPHY, MG RX8 DELUXE, MG RX9 DELUXE, MG G50 COMFORT, MAXUS G90 LUXURY, MAXUS G10, MAXUS T60 4X2, MAXUS T60 4X4, MAXUS eDELIVER 3 EV, MG CYBERSTER EV y MG4 EV 77 kWh LUXURY.

> **Observación:** el sitio anuncia "13" modelos en su bloque destacado, pero la página contiene **16 fichas** con precio. Las tres adicionales son MG4 EV 51 kWh COMFORT, MG4 EV 77 kWh LUXURY y MG CYBERSTER EV. Se registraron las 16 por ser información pública verificable.

### 2.3. MCV Comercial, S.A. — <https://tienda.mcvcommercial.com/>

El sitio es dinámico y solo devuelve el texto "MCV Comercial S.A."; no fue posible extraer un catálogo de vehículos completos. La documentación previa la describe como tienda de **repuestos, piezas y accesorios**, no de vehículos terminados. Se registra como entidad **no accesible** y sin modelos, sin rellenar datos por inferencia.

---

## 3. Otra información útil encontrada

### 3.1. ¿Los catálogos incluyen años de los modelos?

**No de forma individual.** Dongfeng identifica su oferta como "Catálogo oficial 2026", pero no publica año-modelo por vehículo. BDC ONE no muestra año-modelo en ninguna ficha.

Consecuencia para el análisis: el campo `ano` del mercado informal (2009–2026) **no tiene contraparte directa** en el mercado formal. La comparación por antigüedad solo puede hacerse con el año de edición del catálogo, no con el año del vehículo. Se deja `ano_modelo = null` en todos los registros para no fabricar el dato.

### 3.2. Versiones y acabados

Ambos catálogos publican el acabado dentro del nombre comercial:

- **BDC ONE:** LUXURY, COMFORT, DELUXE, TROPHY; variantes 4x2/4x4 y 51/64/77 kWh.
- **Dongfeng:** Manual/Automático, "Ultra+", "E0 Off Road"/"Premium" (MHERO II) y capacidades de carga (3 T, 5 T, 8-10 T) en comerciales.

Esto permite construir una variable `acabado` o `version` para el mercado formal, pero **no** es homologable con el mercado informal, donde el acabado casi nunca se declara.

### 3.3. Garantías y servicio postventa

| Entidad | Garantía general | Cobertura eléctrica | Comerciales |
|---|---|---|---|
| Dongfeng Cuba | 5 años o 150 000 km | Batería de alto voltaje, tren motriz y componentes eléctricos principales: 8 años o 200 000 km | 3 años o 100 000 km |
| BDC ONE | 2 años o 50 000 km | Cadena de tracción: 3 años o 50 000 km; batería de tracción: 3 años o 80 000 km | — |

BDC ONE además declara red de servicio en **BDC Log S.A.**, talleres de la FGNE homologados y la red **SASA**; Dongfeng declara "red de talleres" propia.

**Uso analítico:** la garantía es un diferenciador estructural del mercado formal frente al informal, donde la venta entre particulares no ofrece respaldo. Es un argumento directo para las entrevistas sobre por qué se compra (o no) en el mercado formal.

### 3.4. Financiamiento y leasing

**No se encontró información pública de financiamiento ni leasing en ninguno de los dos catálogos.** BDC ONE solo ofrece un formulario de "Solicitud de Oferta"; Dongfeng, un formulario de "Cotizar". Esta ausencia es un hallazgo relevante: el acceso al crédito no se comunica en el canal digital, aunque puede existir por vía presencial.

### 3.5. Precios que no son finales (BDC ONE)

La propia página advierte que los precios del catálogo **no son finales**:

- Representan el **valor del vehículo pagado en el exterior**.
- Los impuestos los fija la **empresa importadora** con la que el cliente firma contrato y se pagan en Cuba desde la "tarjeta clásica".
- El marco legal citado es la **Resolución 172/2026 de Finanzas y Precios**, que regula la formación de precios en USD o su equivalente para vehículos importados.
- Las importadoras que BDC ONE menciona son **Tradex, Transimport e Impexport**, tres entidades que ya están registradas en el mercado formal del proyecto.

**Uso analítico:** confirma que el precio formal publicitado es un precio "de origen" y que el precio final de venta al consumidor no es observable con la información pública. Cualquier comparación formal–informal debe declararlo como límite.

### 3.6. Especificaciones técnicas adicionales

- **Consumo:** BDC ONE publica rendimiento en km/L para los modelos de gasolina (12,5–14,6 km/L).
- **Plazas y carga:** 7, 8 y 10 plazas en monovolúmenes/minibuses; 850 kg de carga en las MAXUS T60 y 800 kg en la eDELIVER 3.
- **Batería y potencia:** capacidades de 51, 64 y 77 kWh (MG4), 98 kWh y 475 kW (Voyah Passion), plataforma de 800 V.
- **Equipamiento:** techo solar, cámara 360°, función V2L, Apple CarPlay/Android Auto, airbags y asistentes.
- **Colores disponibles:** ambos sitios publican paletas por modelo.

Estos campos no existen en el mercado informal y no se forzaron en el esquema; quedan como contexto cualitativo para la discusión.

---

## 4. Relevancia para el mercado informal

1. **Solapamiento de modelos eléctricos:** el informal registra un **Dongfeng BOX 2026** a 33 000 USD (30 360 000 MN) y dos Hyundai Ioniq. El BOX también aparece en el catálogo formal a **21 900 EUR** (22 009 500 MN, sin impuestos). La diferencia observada (~38% a favor del anuncio informal) **no es concluyente** porque el precio formal excluye impuestos de importación.
2. **Marcas:** el informal está dominado por Hyundai (19 de 30 anuncios) y Kia (5), marcas que **no aparecen** en los catálogos formales auditados. El mercado formal de catálogo se concentra en Dongfeng, MG, Maxus y Mitsubishi.
3. **Antigüedad:** el informal cubre 2009–2026, con 21 de 30 anuncios de 2021 o posteriores. El formal solo ofrece vehículos nuevos, sin año-modelo publicado.
4. **Garantía:** el formal ofrece 2–5 años de garantía; el informal, ninguna. Es una variable binaria útil para contrastar con las entrevistas.
5. **Precio y moneda:** todo el informal está en USD; ambos catálogos formales, en EUR. La conversión a MN es imprescindible para comparar y ya está aplicada.

---

## 5. Limitaciones

- **MCV Comercial** no expone catálogo de vehículos completos (sitio dinámico).
- **Precios formales incompletos:** 15 modelos Dongfeng figuran como "A consultar"; en BDC ONE los precios excluyen impuestos.
- **Sin año-modelo por vehículo** en ninguno de los dos catálogos.
- **Sin financiamiento/leasing** publicado.
- **Mitsubishi** figura entre las marcas comercializadas por BDC ONE, pero el catálogo no muestra ningún modelo de esa marca: inconsistencia a verificar con la entidad.
- **Catálogo cambiante:** los precios y modelos son una foto al 2026-11-06 y pueden variar.

---

## 6. Recomendaciones para el EDA

1. Usar `modelos_disponibles` y `vehiculos_electricos` del procesado para el conteo de oferta formal por marca y motorización.
2. Comparar **estructura** (tipo de vehículo, motorización, rango de precio) y no precio puntual, por la exclusión de impuestos.
3. Tratar la garantía como variable cualitativa del mercado formal y cruzar con las entrevistas.
4. Documentar en el notebook que el año-modelo formal no está disponible.
5. Verificar con BDC ONE la ausencia de modelos Mitsubishi y el total real de fichas (13 vs 16).
