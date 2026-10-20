# Prompt para Mejorar el Codigo Base

Copia y pega el contenido del bloque de abajo en un asistente de IA (Claude, ChatGPT)
para obtener un ZIP con el proyecto completo y arrancable.

Si preferis trabajar en tu editor con un agente local (Claude Code, Cursor, Copilot), usa `AGENTS.md` en vez de este archivo: dice lo mismo pero para que escriba los archivos en disco.

## Las dos reglas que no se negocian

1. **Completa el boilerplate.** Todo lo que el proyecto necesita para compilar y arrancar: manifiesto de dependencias, punto de entrada, configuracion, capa de interfaz, y las capas del patron arquitectonico declarado. Eso es andamiaje y es tu trabajo.
2. **NO resuelvas el reto.** Los entregables de las fases son el trabajo de la persona. El hueco pedagogico se deja como esta: el proyecto arranca, pero lo que el reto pide implementar NO esta implementado.

Dicho de otra forma: si algo impide compilar, arreglalo. Si algo es logica de negocio incompleta, validaciones ausentes, un secreto hardcodeado o un patron mejorable, dejalo exactamente como esta — es lo que la persona tiene que encontrar.

## Superficie de practica — NO resuelvas

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs.

- `adr/001-servicio-ia-observabilidad.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.
- `adr/002-patron-integracion-ia.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.

## Como saber que terminaste

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

Ese comando corriendo sin errores es la definicion de "listo".

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Arquitectura, Especialidad Soluciones, Seniority Advanced

### Brecha de conocimiento
Ha aplicado servicios de IA para mejorar los procesos de observabilidad y automatizar actualizaciones y mejoras de observabilidad e infraestructura.

### Misión / candidato
Candidato con experiencia avanzada en arquitectura, trabajando en cierre de brechas de conocimiento en observabilidad con IA.

### Reto
- Tema: Optimización de la observabilidad con servicios de IA
- Seniority: advanced-l2
- Tipo: practical
- Título: Mejora de la observabilidad con IA en plataforma de e-commerce
- Tiempo estimado: 180 minutos

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Análisis de Requisitos y Contexto — objetivo: Entender los requisitos de observabilidad y el contexto de la plataforma de e-commerce. — entregable (NO resolver): Documento de requisitos de observabilidad con ASRs, KPIs y SLOs.
- Fase 2: Diseño de la Estrategia de Observabilidad — objetivo: Diseñar la estrategia de observabilidad utilizando servicios de IA. — entregable (NO resolver): Documento de diseño de la estrategia de observabilidad con diagramas C4 y ADRs.
- Fase 3: Implementación y Validación — objetivo: Implementar y validar la solución de observabilidad. — entregable (NO resolver): Spike mínimo de integración de servicio de IA y reporte de validación.
- Fase 4: Revisión y Entrega — objetivo: Revisar y entregar la solución de observabilidad. — entregable (NO resolver): Documento de diseño revisado, ADRs y presentación ejecutiva.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 0 — ¿Esto es un proyecto o una carcasa?
Antes de extraer archivos, leé el Briefing (si está) y diagnosticá el adjunto.

Es CARCASA si ocurre CUALQUIERA de estas:
- No hay manifiesto de dependencias del stack del briefing (manifest.json de VTEX IO / package.json / pom.xml / build.gradle / requirements.txt / go.mod / *.tf / *.csproj, según corresponda)
- Hay un "binario" que en realidad es un comentario ("no puede ser mostrado como texto plano", placeholder .fig/.docx vacío)
- Los markdowns ya completan entregables de fases posteriores ("se implementó fade-in", lista de áreas ya resuelta)

Si es CARCASA:
- MATERIALIZÁ un proyecto que arranca en el stack del briefing (VTEX IO Store Framework, Angular, Terraform, pytest, Nest, etc.). Incluí manifiesto, punto de entrada y capa de interfaz reales.
- NO copies los markdowns de "solución" como si fueran el producto. Son ruido de generación.
- NO resuelvas las fases del briefing (están marcadas PROHIBIDO). Dejá el hueco pedagógico: el flujo existe, las microinteracciones/calidad/infra que el reto pide NO están hechas.
- Después seguí al PASO 5 (ZIP).

Si es un proyecto REAL (manifiesto + código que compila o arranca):
- Seguí PASO 1 en adelante. 🔴 compilación sí. 🟡 pedagógico no.

PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación, placeholders o binarios fake, NO la reproduzcas:
aplicá PASO 0 (materializar el proyecto del briefing). Reproducir la carcasa es un fallo.
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

// === ARCHIVO: poc/requirements.txt ===
# Dependencias para el spike de integración con servicios de IA para observabilidad
# Versiones reales según disponibilidad en PyPI al momento de generación

requests>=2.31.0
# requests es la librería estándar para realizar HTTP requests en Python
# Versión mínima 2.31.0 para soporte completo de TLS 1.3 y mejor manejo de conexiones

boto3>=1.34.0
# SDK de AWS para Python, necesario para integrar servicios como CloudWatch, Lambda o Sagemaker
# Versión mínima 1.34.0 para compatibilidad con las últimas características de AWS

python-dotenv>=1.0.0
# Librería para cargar variables de entorno desde .env, útil para configuraciones locales
# Versión mínima 1.0.0 para soporte estable

mermaid-cli>=0.5.1
# CLI para generar diagramas Mermaid, útil si se necesita generar diagramas desde scripts
# Versión mínima 0.5.1 para compatibilidad con sintaxis C4

# Dependencias opcionales para extensiones futuras
# pandas>=2.0.0  # Para procesamiento de datos si se requiere análisis local
# numpy>=1.24.0   # Dependencia de pandas y otras librerías de análisis

# Nota: El spike es autocontenido y solo depende de estas librerías.
# No se importan módulos fuera de poc/ para mantener el aislamiento.
# Para ejecutar el spike:
# 1. Crear un entorno virtual: python -m venv venv
# 2. Activar el entorno: source venv/bin/activate (Linux/Mac) o venv\Scripts\activate (Windows)
# 3. Instalar dependencias: pip install -r requirements.txt
# 4. Ejecutar el spike: python spike_integracion_ia.py


// === ARCHIVO: README.md ===
# Plataforma de E-commerce: Observabilidad Mejorada con Servicios de IA

## Contexto del Caso

**Dominio:** Plataforma de e-commerce de alta escala con operaciones en múltiples regiones geográficas. La plataforma procesa **50,000 solicitudes por segundo** durante picos de tráfico (ej. Black Friday, Cyber Monday) y maneja más de **10 millones de usuarios activos diarios**. El sistema actual consiste en:
- **Frontend:** Aplicación web y móvil con microservicios en React y Flutter.
- **Backend:** Arquitectura de microservicios en Kubernetes con servicios en Java (Spring Boot), Node.js y Python.
- **Infraestructura:** AWS con servicios gestionados (RDS, ElastiCache, SQS, Lambda) y despliegues multi-región.
- **Monitoreo actual:** Stack tradicional de observabilidad basado en Prometheus, Grafana y CloudWatch, con alertas estáticas y dashboards manuales.

**Situación:**
La plataforma enfrenta desafíos críticos en observabilidad:
1. **Detección tardía de anomalías:** Los umbrales estáticos en CloudWatch generan **falsos positivos** (30% de alertas) y **falsos negativos** (incidentes no detectados hasta impactar usuarios).
2. **Latencia en resolución:** El tiempo medio para detectar y resolver incidentes es de **22 minutos**, con un **MTTR (Mean Time to Resolution)** de 45 minutos en incidentes críticos.
3. **Escalabilidad limitada:** El volumen de logs y métricas (1.5 TB/día) supera la capacidad de procesamiento en tiempo real del stack actual, generando **cuellos de botella** en Prometheus.
4. **Falta de insights predictivos:** No hay capacidad para predecir degradaciones de rendimiento o fallos inminentes basados en patrones históricos.

**Actores:**
| Actor | Responsabilidad | Requisitos de Observabilidad |
|-------|-----------------|-------------------------------|
| Equipo de Operaciones (DevOps) | Monitoreo en tiempo real, gestión de incidentes | Alertas precisas, dashboards personalizables |
| Equipo de Desarrollo (Backend/Frontend) | Debugging, optimización de rendimiento | Traces distribuidos, logs estructurados |
| Equipo de Producto | Experiencia del usuario (UX) | Métricas de latencia por transacción, tasa de errores |
| Equipo de Seguridad | Detección de amenazas | Anomalías en patrones de acceso, comportamientos sospechosos |
| Equipo de Data Science | Análisis predictivo | Datos históricos para entrenamiento de modelos de IA |

## Requisitos Arquitectónicamente Significativos (ASRs)
Los siguientes ASRs son críticos para la solución de observabilidad con IA:

| ASR | Valor Medible | Métrica | Umbral |
|-----|---------------|---------|--------|
| **ASR-01:** Detección automática de anomalías | Reducir falsos positivos | Precisión de alertas | ≥ 95% |
| **ASR-02:** Latencia de detección de incidentes | Tiempo desde evento hasta alerta | Tiempo medio de detección (MTTD) | ≤ 2 minutos |
| **ASR-03:** Escalabilidad del procesamiento | Volumen de datos procesados en tiempo real | Throughput de logs/métricas | 1.5 TB/día sin degradación |
| **ASR-04:** Insights predictivos | Predecir incidentes antes de que ocurran | Precisión de predicción | ≥ 85% |
| **ASR-05:** Integración con stack existente | Compatibilidad con herramientas actuales | Tiempo de integración | ≤ 4 semanas |
| **ASR-06:** Costo operativo | Reducir costos de observabilidad | Costo mensual por TB procesado | ≤ $500/TB |

## Restricciones
1. **Tecnológicas:**
   - La solución debe integrarse con el stack actual de observabilidad (Prometheus, Grafana, CloudWatch).
   - Debe utilizar servicios gestionados de AWS siempre que sea posible para reducir la carga operativa.
   - No se permiten cambios en la arquitectura de microservicios existente sin aprobación del equipo de arquitectura.
2. **Operativas:**
   - El tiempo de implementación no debe exceder **8 semanas**.
   - La solución debe ser compatible con despliegues multi-región (EE.UU., UE, Asia).
   - Debe soportar **multi-tenancy** para equipos internos (DevOps, Desarrollo, Seguridad).
3. **Legales y de Seguridad:**
   - Los datos de observabilidad deben almacenarse en regiones con cumplimiento de GDPR y CCPA.
   - Debe garantizarse el **aislamiento de datos** entre equipos (ej. logs de desarrollo no accesibles por operaciones).
   - La solución debe cumplir con SOC 2 Type II y ISO 27001.

## Entregables Esperados
1. **Documentos de diseño:**
   - `atributos-de-calidad.md`: ASRs con escenarios de calidad completos (ISO 25010).
   - `arquitectura.md`: Vistas C4 (contexto, contenedores, componentes, despliegue) del sistema propuesto.
   - `adr/`: Decisiones arquitectónicas registradas (ADRs) con contexto, fuerzas, opciones consideradas, decisión y consecuencias.
   - `diagramas/`: Diagramas en Mermaid (contexto.mmd) y otros según necesidad.
2. **Spike de integración:**
   - Código funcional en `poc/` que demuestre la integración con al menos un servicio de IA para observabilidad.
   - `poc/README.md`: Instrucciones para ejecutar el spike y validar su funcionamiento.
3. **Análisis de riesgos:**
   - `riesgos-y-mitigaciones.md`: Matriz de riesgos priorizados por impacto y probabilidad.
4. **Autoevaluación:**
   - `rubrica-autoevaluacion.md`: Rubrica de evaluación con criterios para alineación con ASRs, uso de patrones y herramientas, calidad de diagramas y ADRs, y viabilidad.

## Instrucciones para Entregar
1. **Formato de entrega:**
   - Todos los documentos deben estar en formato Markdown (.md) con sintaxis válida.
   - Los diagramas deben generarse con Mermaid y guardarse en formato `.mmd` en la carpeta `diagramas/`.
   - El spike debe ser autocontenido y ejecutarse con las dependencias declaradas en `poc/requirements.txt`.
   - El repositorio debe incluir un archivo `.gitignore` para excluir archivos temporales y entornos virtuales.

2. **Estructura del repositorio:**
   ```
   / (raíz)
   ├── README.md (este archivo)
   ├── atributos-de-calidad.md
   ├── arquitectura.md
   ├── riesgos-y-mitigaciones.md
   ├── rubrica-autoevaluacion.md
   ├── adr/
   │   ├── 001-servicio-ia-observabilidad.md
   │   └── 002-patron-integracion-ia.md
   ├── diagramas/
   │   └── contexto.mmd
   ├── contratos/
   │   └── observabilidad_api.yaml
   └── poc/
       ├── README.md
       ├── spike_integracion_ia.py
       └── requirements.txt
   ```

3. **Verificación de la entrega:**
   - Ejecuta el siguiente comando para verificar que todos los archivos requeridos están presentes:
     ```bash
     python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd') and glob.glob('atributos-de-calidad.md') and glob.glob('arquitectura.md'), 'Faltan archivos obligatorios';"
     ```
   - Asegúrate de que el spike en `poc/` se ejecute sin errores:
     ```bash
     cd poc
     python -m venv venv
     source venv/bin/activate  # Linux/Mac
     pip install -r requirements.txt
     python spike_integracion_ia.py
     ```

4. **Criterios de evaluación:**
   - **Alineación con ASRs:** ¿La solución cumple con los requisitos arquitectónicamente significativos?
   - **Uso de patrones y herramientas:** ¿Se utilizan adecuadamente los patrones arquitectónicos (C4, ADR) y herramientas (Mermaid, OpenAPI)?
   - **Calidad de diagramas y ADRs:** ¿Los diagramas son claros y completos? ¿Los ADRs están bien estructurados y justificados?
   - **Viabilidad:** ¿La solución es técnicamente viable y cumple con las restricciones del caso?
   - **Innovación:** ¿La solución aporta valor más allá de lo trivial (ej. uso de IA para observabilidad predictiva)?

## Recursos Adicionales
- [Documentación de C4 Model](https://c4model.com/)
- [Plantilla de ADR](https://adr.github.io/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [Mermaid Live Editor](https://mermaid.live/)
- [OpenAPI Specification](https://swagger.io/specification/)

---

// === ARCHIVO: atributos-de-calidad.md ===
# Atributos de Calidad para Observabilidad con IA

## Requisitos Arquitectónicamente Significativos (ASRs)

| ID | ASR | Valor Medible | Métrica | Umbral |
|----|-----|---------------|---------|--------|
| ASR-01 | Detección automática de anomalías | Reducir falsos positivos | Precisión de alertas | ≥ 95% |
| ASR-02 | Latencia de detección de incidentes | Tiempo desde evento hasta alerta | Tiempo medio de detección (MTTD) | ≤ 2 minutos |
| ASR-03 | Escalabilidad del procesamiento | Volumen de datos procesados en tiempo real | Throughput de logs/métricas | 1.5 TB/día sin degradación |
| ASR-04 | Insights predictivos | Predecir incidentes antes de que ocurran | Precisión de predicción | ≥ 85% |
| ASR-05 | Integración con stack existente | Compatibilidad con herramientas actuales | Tiempo de integración | ≤ 4 semanas |
| ASR-06 | Costo operativo | Reducir costos de observabilidad | Costo mensual por TB procesado | ≤ $500/TB |

## Escenarios de Calidad (ISO 25010)

Los escenarios de calidad describen cómo el sistema debe responder a estímulos específicos bajo condiciones definidas. Completa la tabla siguiente para cada ASR:

| ID | Fuente | Estímulo | Artefacto | Entorno | Respuesta | Medida |
|----|--------|----------|-----------|---------|-----------|--------|
| **ASR-01** | <br>¿Quién o qué genera el estímulo? (ej. usuario, sistema externo, sensor) | <br>¿Qué evento desencadena el escenario? (ej. aumento repentino de latencia, error 500) | <br>¿Qué componente o sistema se ve afectado? | <br>¿En qué condiciones ocurre el escenario? (ej. hora pico, despliegue multi-región) | <br>¿Cómo debe responder el sistema? (ej. enviar alerta, escalar recursos) | <br>¿Cómo se mide el éxito? (ej. tiempo de respuesta, tasa de errores) |
|    |        |          |           |         |           |        |
| **ASR-02** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-03** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-04** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-05** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |
| **ASR-06** |        |          |           |         |           |        |
|    |        |          |           |         |           |        |

### Preguntas Guía para Completar los Escenarios
1. **Fuente:**
   - ¿Qué actores (humanos o sistemas) interactúan con el sistema en este escenario?
   - ¿Qué eventos externos podrían desencadenar este escenario? (ej. pico de tráfico, fallo de red)

2. **Estímulo:**
   - ¿Qué condición específica debe ocurrir para que el sistema reaccione? (ej. latencia > 100ms, error 4xx en 5% de solicitudes)
   - ¿Cómo se manifiesta el estímulo en términos de logs, métricas o traces?

3. **Artefacto:**
   - ¿Qué componente del sistema es responsable de manejar este estímulo? (ej. servicio de detección de anomalías, pipeline de logs)
   - ¿Qué otros componentes podrían verse afectados indirectamente?

4. **Entorno:**
   - ¿En qué condiciones opera el sistema cuando ocurre el estímulo? (ej. modo de alta disponibilidad, durante un despliegue)
   - ¿Qué factores externos podrían influir en la respuesta? (ej. región geográfica, estado de la red)

5. **Respuesta:**
   - ¿Qué acciones debe tomar el sistema para manejar el estímulo? (ej. enviar alerta a Slack, escalar pods de Kubernetes)
   - ¿Qué información debe registrarse para análisis posterior?

6. **Medida:**
   - ¿Cómo se cuantifica el éxito de la respuesta? (ej. tiempo de detección, número de falsos positivos)
   - ¿Qué métricas se utilizan para validar que el sistema cumple con el ASR?

---

## Ejemplo de Escenario Completado (Referencia)

| ID | Fuente | Estímulo | Artefacto | Entorno | Respuesta | Medida |
|----|--------|----------|-----------|---------|-----------|--------|
| ASR-01 | Servicio de monitoreo (CloudWatch) | Aumento repentino de latencia en el servicio de pagos (p99 > 150ms durante 3 minutos) | Servicio de detección de anomalías basado en IA | Hora pico (50,000 TPS), despliegue multi-región | El servicio de IA analiza patrones históricos y envía una alerta prioritaria al equipo de operaciones con contexto del incidente | Precisión de la alerta ≥ 95% (falsos positivos < 5%) |

---

## Priorización de Atributos de Calidad
Los ASRs deben priorizarse según su impacto en el negocio y su viabilidad técnica. Completa la siguiente matriz de priorización:

| ASR | Impacto en el Negocio (1-5) | Viabilidad Técnica (1-5) | Prioridad (Impacto × Viabilidad) |
|-----|-----------------------------|--------------------------|-----------------------------------|
| ASR-01 |                             |                          |                                   |
| ASR-02 |                             |                          |                                   |
| ASR-03 |                             |                          |                                   |
| ASR-04 |                             |                          |                                   |
| ASR-05 |                             |                          |                                   |
| ASR-06 |                             |                          |                                   |

### Preguntas Guía para Priorización
1. **Impacto en el Negocio:**
   - ¿Qué consecuencias tiene no cumplir con este ASR? (ej. pérdida de ingresos, degradación de UX)
   - ¿Qué equipos o procesos se ven afectados? (ej. operaciones, desarrollo, seguridad)
2. **Viabilidad Técnica:**
   - ¿Qué desafíos técnicos existen para implementar este ASR? (ej. integración con sistemas legacy, costos)
   - ¿Existen soluciones disponibles en el mercado que cumplan con este ASR?
3. **Prioridad:**
   - ¿Qué ASRs deben implementarse primero para maximizar el valor entregado?
   - ¿Qué ASRs pueden abordarse en fases posteriores?

---

// === ARCHIVO: arquitectura.md ===
# Arquitectura del Sistema de Observabilidad con IA

## Introducción
Este documento describe la arquitectura del sistema actual (as-is) y proporciona las preguntas guía para diseñar la arquitectura propuesta (to-be) que cumpla con los ASRs definidos en `atributos-de-calidad.md`. La arquitectura sigue el modelo C4 (Contexto, Contenedores, Componentes, Despliegue) y se representa mediante diagramas en Mermaid.

---

## Sistema Actual (As-Is)
### Descripción del Sistema Actual
La plataforma de e-commerce actualmente utiliza un stack tradicional de observabilidad compuesto por:
1. **Prometheus:** Recolección de métricas y alertas estáticas.
2. **Grafana:** Visualización de dashboards y métricas.
3. **CloudWatch:** Almacenamiento de logs y métricas de AWS, con alertas basadas en umbrales.
4. **OpenTelemetry:** Recolección de traces distribuidos (parcialmente implementado).
5. **ELK Stack:** Centralización de logs (Elasticsearch, Logstash, Kibana) para análisis forense.

**Limitaciones del Sistema Actual:**
- **Alertas estáticas:** Umbrales fijos que generan falsos positivos y no se adaptan a patrones de tráfico.
- **Falta de inteligencia:** No hay capacidad para detectar anomalías basadas en patrones históricos o comportamientos atípicos.
- **Escalabilidad limitada:** Prometheus y ELK no escalan eficientemente para el volumen de datos (1.5 TB/día).
- **Latencia en detección:** El MTTD (Mean Time to Detection) es de 22 minutos, superando el umbral deseado de 2 minutos.
- **Falta de integración:** Los sistemas de observabilidad operan en silos, sin correlación entre logs, métricas y traces.

---

## Vistas C4
Completa las siguientes vistas C4 para el sistema propuesto (to-be). Utiliza los diagramas en Mermaid (`diagramas/contexto.mmd` y otros) como referencia.

### 1. Vista de Contexto
**Diagrama:** [`diagramas/contexto.mmd`](diagramas/contexto.mmd)

**Descripción:**
La vista de contexto muestra el sistema de observabilidad con IA en relación con los actores externos y otros sistemas. Incluye:
- **Actores:** Equipos de operaciones, desarrollo, seguridad y producto.
- **Sistemas externos:** AWS CloudWatch, Prometheus, Grafana, ELK Stack, servicios de IA (ej. Amazon Lookout for Metrics, Amazon SageMaker).
- **Flujos de datos:** Cómo los datos de observabilidad fluyen desde los microservicios hasta los servicios de IA y luego a los equipos.

**Preguntas Guía:**
1. ¿Qué sistemas externos interactúan con el sistema de observabilidad con IA?
2. ¿Qué actores dependen de los datos de observabilidad y cómo acceden a ellos?
3. ¿Qué protocolos o APIs se utilizan para la comunicación entre sistemas? (ej. REST, gRPC, Kafka)
4. ¿Cómo se garantiza la seguridad y el aislamiento de datos entre actores?

---

### 2. Vista de Contenedores
**Diagrama:** (Generar un diagrama en Mermaid para esta vista)

**Descripción:**
La vista de contenedores descompone el sistema de observabilidad en contenedores lógicos (ej. servicios, bases de datos, colas). Incluye:
- **Contenedores del sistema:**
  - **Servicio de Recolección:** Agente o sidecar que recopila logs, métricas y traces desde los microservicios.
  - **Pipeline de Procesamiento:** Servicio que procesa y enriquece los datos de observabilidad antes de almacenarlos.
  - **Servicio de Detección de Anomalías:** Servicio que utiliza IA para detectar anomalías en tiempo real.
  - **Servicio de Predicción:** Servicio que genera insights predictivos basados en datos históricos.
  - **Almacenamiento:** Bases de datos o sistemas de almacenamiento para logs, métricas y traces (ej. Amazon Timestream, OpenSearch).
  - **Interfaz de Usuario:** Dashboards y alertas para equipos internos (ej. Grafana con plugins de IA).
- **Flujos de datos:** Cómo los datos fluyen entre contenedores (ej. Kafka para streaming, S3 para almacenamiento).

**Preguntas Guía:**
1. ¿Qué contenedores componen el sistema de observabilidad con IA?
2. ¿Cómo se comunican los contenedores entre sí? (ej. sincrónico vs asincrónico, protocolos)
3. ¿Qué tecnologías se utilizan para cada contenedor? (ej. Kubernetes para orquestación, Lambda para procesamiento serverless)
4. ¿Cómo se garantiza la escalabilidad y resiliencia de cada contenedor?
5. ¿Qué datos se almacenan en cada contenedor y cómo se gestionan? (ej. retención, particionamiento)

---

### 3. Vista de Componentes
**Diagrama:** (Generar un diagrama en Mermaid para esta vista)

**Descripción:**
La vista de componentes detalla los módulos internos de cada contenedor. Para el **Servicio de Detección de Anomalías**, incluye:
- **Componentes:**
  - **Recolección de Datos:** Módulo que recibe logs, métricas y traces desde el pipeline.
  - **Preprocesamiento:** Módulo que limpia y normaliza los datos para análisis.
  - **Modelo de IA:** Módulo que ejecuta el modelo de detección de anomalías (ej. Lookout for Metrics, SageMaker).
  - **Generación de Alertas:** Módulo que envía alertas a los equipos según los resultados del modelo.
  - **API de Consulta:** Módulo que expone endpoints para consultar el estado de anomalías.
- **Interacciones:** Cómo los componentes colaboran para cumplir con los ASRs (ej. flujo de datos desde la recolección hasta la generación de alertas).

**Preguntas Guía:**
1. ¿Qué componentes forman parte del **Servicio de Detección de Anomalías**?
2. ¿Cómo interactúan los componentes para detectar anomalías en tiempo real?
3. ¿Qué modelos o algoritmos de IA se utilizan y cómo se entrenan?
4. ¿Cómo se gestionan los falsos positivos y falsos negativos?
5. ¿Qué APIs exponen los componentes para integración con otros sistemas?

---

### 4. Vista de Despliegue
**Diagrama:** (Generar un diagrama en Mermaid para esta vista)

**Descripción:**
La vista de despliegue muestra cómo los contenedores se mapean a la infraestructura física o en la nube. Incluye:
- **Nodos de despliegue:** Regiones de AWS, zonas de disponibilidad, clusters de Kubernetes.
- **Contenedores desplegados:** Cómo se distribuyen los contenedores en los nodos (ej. servicio de detección de anomalías en cada región).
- **Recursos:** CPU, memoria, almacenamiento asignados a cada contenedor.
- **Redes:** Subredes, firewalls, balanceadores de carga y topología de red.

**Preguntas Guía:**
1. ¿En qué regiones y zonas de disponibilidad se despliega el sistema?
2. ¿Cómo se distribuyen los contenedores para garantizar alta disponibilidad y tolerancia a fallos?
3. ¿Qué recursos (CPU, memoria) se asignan a cada contenedor y cómo se escalan?
4. ¿Cómo se gestionan los despliegues multi-región y la sincronización de datos?
5. ¿Qué medidas de seguridad se implementan en el despliegue? (ej. VPC, IAM, cifrado)

---

## Decisiones Arquitectónicas Clave
Las decisiones arquitectónicas deben registrarse en los ADRs (`adr/`). A continuación se listan las decisiones críticas para este sistema:

| Decisión | ADR | Estado |
|----------|-----|--------|
| Selección del servicio de IA para detección de anomalías | [`adr/001-servicio-ia-observabilidad.md`](adr/001-servicio-ia-observabilidad.md) | Propuesto |
| Patrón de integración para servicios de IA | [`adr/002-patron-integracion-ia.md`](adr/002-patron-integracion-ia.md) | Propuesto |
| Almacenamiento de logs y métricas | (Generar ADR) | Propuesto |
| Escalabilidad del pipeline de procesamiento | (Generar ADR) | Propuesto |

**Preguntas Guía para ADRs:**
1. ¿Qué alternativas se evaluaron para cada decisión?
2. ¿Qué pros y contras tiene cada alternativa frente a los ASRs?
3. ¿Qué criterios se utilizaron para tomar la decisión final?
4. ¿Qué consecuencias tiene la decisión en términos de costo, escalabilidad y mantenimiento?

---

## Contratos de Frontera
Los contratos de frontera definen cómo los componentes del sistema interactúan entre sí y con sistemas externos. Incluyen:
- **APIs:** Endpoints REST/gRPC para comunicación entre servicios (ej. [`contratos/observabilidad_api.yaml`](contratos/observabilidad_api.yaml)).
- **Eventos:** Esquemas de eventos para comunicación asincrónica (ej. Kafka, SQS).
- **Interfaces:** Contratos para integración con servicios de IA (ej. entrada/salida de modelos de SageMaker).

**Preguntas Guía:**
1. ¿Qué APIs o eventos definen la comunicación entre los contenedores?
2. ¿Cómo se validan y versionan los contratos de frontera?
3. ¿Qué información debe incluirse en cada contrato? (ej. esquemas de datos, errores esperados)

---

## Validación de la Arquitectura
Para validar que la arquitectura cumple con los ASRs, considera las siguientes preguntas:

1. **ASR-01 (Detección automática de anomalías):**
   - ¿Qué componentes garantizan una precisión de alertas ≥ 95%?
   - ¿Cómo se entrenan y actualizan los modelos de IA para mantener esta precisión?
2. **ASR-02 (Latencia de detección):**
   - ¿Qué optimizaciones se implementan para reducir el MTTD a ≤ 2 minutos?
   - ¿Cómo se procesan los datos en tiempo real para cumplir con este umbral?
3. **ASR-03 (Escalabilidad):**
   - ¿Qué estrategias de escalado se utilizan para manejar 1.5 TB/día de datos?
   - ¿Cómo se distribuye la carga entre regiones y zonas de disponibilidad?
4. **ASR-04 (Insights predictivos):**
   - ¿Qué modelos o técnicas se utilizan para generar predicciones con ≥ 85% de precisión?
   - ¿Cómo se integran los datos históricos para mejorar las predicciones?
5. **ASR-05 (Integración):**
   - ¿Qué adaptadores o wrappers se implementan para integrarse con Prometheus, Grafana y CloudWatch?
   - ¿Cómo se migran los datos existentes al nuevo sistema sin interrupciones?
6. **ASR-06 (Costo operativo):**
   - ¿Qué estrategias se utilizan para reducir el costo por TB procesado a ≤ $500?
   - ¿Cómo se optimiza el almacenamiento y procesamiento para minimizar costos?

---

## Próximos Pasos
1. Completa los diagramas C4 en Mermaid (`diagramas/`).
2. Documenta las decisiones arquitectónicas en los ADRs (`adr/`).
3. Define los contratos de frontera en [`contratos/observabilidad_api.yaml`](contratos/observabilidad_api.yaml).
4. Implementa el spike de integración en `poc/` para validar la viabilidad técnica.
5. Prioriza los riesgos y mitigaciones en [`riesgos-y-mitigaciones.md`](riesgos-y-mitigaciones.md).
6. Evalúa la solución con la [`rubrica-autoevaluacion.md`](rubrica-autoevaluacion.md).


// === ARCHIVO: riesgos-y-mitigaciones.md ===
# Matriz de Riesgos y Mitigaciones

## Contexto
La plataforma de e-commerce maneja 50 000 solicitudes por segundo en hora pico y requiere una solución de observabilidad mejorada con servicios de IA para detectar anomalías y generar alertas inteligentes. La integración de servicios externos (AWS, proveedores de IA) introduce riesgos técnicos, operativos y de seguridad que deben identificarse y mitigarse.

## Objetivo
Identificar los riesgos asociados a la implementación de la estrategia de observabilidad con IA y definir acciones de mitigación para cada uno. Los riesgos se priorizan según su probabilidad e impacto en los ASRs (Atributos de Calidad Significativos) del sistema.

## Estructura de la Matriz
| Riesgo                                                                 | Probabilidad (Alta/Media/Baja) | Impacto (Alto/Medio/Bajo) | Tratamiento                                                                                     |
|-------------------------------------------------------------------------|--------------------------------|---------------------------|--------------------------------------------------------------------------------------------------|
|                                                                         |                                |                           |                                                                                                  |

## Preguntas Guía para Completar la Matriz
1. **Riesgos Técnicos**: 
   - ¿Qué fallos de integración con los servicios de IA podrían afectar la observabilidad?
   - ¿Cómo impacta la latencia de los servicios externos en los SLOs de la plataforma?
   - ¿Existen limitaciones de escalabilidad en los servicios de IA que puedan convertirse en cuellos de botella?

2. **Riesgos Operativos**:
   - ¿Qué dependencias críticas podrían fallar y cómo afectarían la operación continua?
   - ¿Cómo se gestionan los cambios en las APIs de los proveedores de IA?
   - ¿Qué procesos de monitoreo y alerta deben implementarse para detectar fallos en tiempo real?

3. **Riesgos de Seguridad**:
   - ¿Qué vulnerabilidades podrían introducir los servicios de IA en la plataforma?
   - ¿Cómo se protegen los datos sensibles que se envían a los servicios externos?
   - ¿Qué medidas de autenticación y autorización se implementan para acceder a los servicios de IA?

4. **Riesgos de Costo**:
   - ¿Cómo se controlan los costos asociados al uso de servicios de IA en la nube?
   - ¿Qué estrategias de optimización de costos se pueden aplicar sin comprometer la observabilidad?

5. **Riesgos de Cumplimiento**:
   - ¿Cómo se asegura el cumplimiento de regulaciones de privacidad de datos (ej. GDPR, LGPD)?
   - ¿Qué políticas de retención de datos deben aplicarse a los registros de observabilidad?

## Ejemplo de Riesgo (No completar)
| Riesgo: Fallo en la integración con el servicio de IA de detección de anomalías | Probabilidad: Alta | Impacto: Alto | Tratamiento: Implementar un circuito de fallback con lógica local de detección básica |

--- 
**Nota**: Esta matriz debe completarse con riesgos específicos identificados durante el análisis de la solución. Cada riesgo debe estar alineado con los ASRs definidos en `atributos-de-calidad.md` y las decisiones registradas en los ADRs.

// === ARCHIVO: rubrica-autoevaluacion.md ===
# Rúbrica de Autoevaluación

## Contexto
Esta rúbrica permite evaluar la calidad de la solución arquitectónica propuesta para mejorar la observabilidad de la plataforma de e-commerce utilizando servicios de IA. Los criterios están alineados con los ASRs definidos en el caso y las buenas prácticas de arquitectura de soluciones.

## Criterios de Evaluación

### 1. Alineación con los ASRs
| Nivel               | Excelente                                                                 | Aceptable                                                                 | Insuficiente                                                                 |
|--------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Definición**     | Los ASRs están claramente definidos con métricas cuantificables y umbrales. | Los ASRs están definidos pero faltan métricas o umbrales en algunos casos. | Los ASRs no están definidos o no incluyen métricas cuantificables.              |
| **Alineación**     | La solución propuesta cumple con todos los ASRs y justifica su alineación. | La solución cumple con la mayoría de los ASRs pero falta justificación en algunos. | La solución no cumple con los ASRs o no justifica su alineación.                |
| **Priorización**   | Los ASRs están priorizados según su impacto en el negocio y la arquitectura. | Los ASRs están priorizados pero sin justificación clara.                 | Los ASRs no están priorizados.                                                  |

### 2. Uso de Patrones y Herramientas Arquitectónicas
| Nivel               | Excelente                                                                 | Aceptable                                                                 | Insuficiente                                                                 |
|--------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Patrones**       | Se utilizan patrones arquitectónicos adecuados (ej. Circuit Breaker, Outbox, CQRS) y se justifica su elección. | Se utilizan patrones pero falta justificación o no son los más adecuados. | No se utilizan patrones arquitectónicos o son inadecuados para el problema.     |
| **Herramientas**   | Se seleccionan herramientas y tecnologías acordes al problema (ej. servicios de IA, AWS CloudWatch, Prometheus). | Se seleccionan herramientas pero falta justificación o no son las más adecuadas. | Las herramientas seleccionadas no resuelven el problema o no están justificadas. |
| **Integración**    | La integración entre componentes y servicios externos está bien diseñada y documentada. | La integración está diseñada pero falta documentación o claridad.        | La integración no está diseñada o es deficiente.                                 |

### 3. Calidad de Diagramas y ADRs
| Nivel               | Excelente                                                                 | Aceptable                                                                 | Insuficiente                                                                 |
|--------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Diagramas C4**   | Los diagramas C4 (contexto, contenedores, componentes) son claros, completos y siguen la sintaxis Mermaid. | Los diagramas son claros pero faltan detalles o no siguen la sintaxis Mermaid. | Los diagramas son incompletos, confusos o no siguen la sintaxis Mermaid.        |
| **ADRs**           | Los ADRs están bien estructurados, con contexto, fuerzas, opciones consideradas y decisión clara. | Los ADRs están estructurados pero faltan secciones o no son claros.      | Los ADRs están incompletos o no siguen la estructura requerida.                  |
| **Consistencia**   | Los diagramas y ADRs son consistentes entre sí y con la solución propuesta. | Hay inconsistencias menores entre diagramas y ADRs.                     | Hay inconsistencias graves entre diagramas, ADRs y la solución propuesta.      |

### 4. Viabilidad de la Solución
| Nivel               | Excelente                                                                 | Aceptable                                                                 | Insuficiente                                                                 |
|--------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Técnica**        | La solución es técnicamente viable y se han considerado todos los aspectos críticos (escalabilidad, latencia, seguridad). | La solución es viable pero faltan aspectos técnicos críticos.           | La solución no es técnicamente viable o no considera aspectos críticos.         |
| **Operativa**      | La solución es operable y se han definido procesos para su implementación y monitoreo. | La solución es operable pero faltan procesos claros de implementación o monitoreo. | La solución no es operable o no define procesos de implementación.             |
| **Costo**          | Se han evaluado los costos de la solución y se proponen estrategias de optimización. | Se han evaluado los costos pero faltan estrategias de optimización.      | No se han evaluado los costos o la solución es inviable económicamente.         |

## Instrucciones para la Autoevaluación
1. **Revisar cada criterio** y marcar el nivel que mejor describa la solución propuesta.
2. **Identificar fortalezas y debilidades** en cada criterio y documentarlas.
3. **Proponer mejoras** para los criterios evaluados como "Aceptable" o "Insuficiente".
4. **Alinear la solución** con los ASRs y las decisiones registradas en los ADRs.

## Preguntas Guía para la Autoevaluación
- ¿La solución propuesta cumple con todos los ASRs definidos en el caso?
- ¿Se han utilizado patrones arquitectónicos adecuados para resolver el problema?
- ¿Los diagramas y ADRs son claros, completos y consistentes entre sí?
- ¿La solución es viable técnicamente, operativamente y en términos de costo?
- ¿Qué riesgos identificados en `riesgos-y-mitigaciones.md` podrían afectar la viabilidad de la solución?

// === ARCHIVO: adr/001-servicio-ia-observabilidad.md ===
# ADR 001: Servicio de IA para Observabilidad en Plataforma de E-commerce

Estado: Propuesto
Fecha: 2024-05-20

## Contexto

La plataforma de e-commerce procesa 50,000 solicitudes por segundo en hora pico y requiere un sistema de observabilidad avanzado que:

- **Automatice la detección de anomalías** en métricas de rendimiento (latencia, throughput, errores) con una precisión mínima del 95%.
- **Genere alertas inteligentes** en tiempo real (latencia < 2s para notificación) para equipos de operaciones.
- **Escalabilidad horizontal**: el servicio de IA debe soportar el crecimiento del tráfico sin degradación de rendimiento (máximo 5% de aumento en latencia por cada 10,000 solicitudes adicionales).
- **Integración con herramientas existentes**: CloudWatch para logs, Prometheus para métricas y Grafana para dashboards.

La plataforma actualmente utiliza herramientas tradicionales de monitoreo que requieren configuración manual de umbrales y no escalan eficientemente con el volumen de datos.

## Fuerzas

1. **Precisión vs. Costo**: Servicios como Amazon Lookout for Metrics ofrecen alta precisión (98% en pruebas internas) pero con un costo por transacción de $0.10 por cada 1,000 solicitudes. Alternativas como Azure Anomaly Detector tienen menor precisión (92%) pero costo reducido ($0.05 por cada 1,000 solicitudes).

2. **Latencia de Detección**: Lookout for Metrics procesa datos en batches cada 5 minutos, mientras que Azure Anomaly Detector ofrece streaming en tiempo real (latencia < 1s).

3. **Integración con Ecosistema**: La plataforma está alojada en AWS, lo que facilita la integración con Lookout for Metrics mediante roles IAM y Kinesis, mientras que Azure Anomaly Detector requiere configuración adicional de VPC peering o API Gateway.

4. **Escalabilidad**: Lookout for Metrics soporta hasta 10,000 métricas por instancia, mientras que Azure Anomaly Detector limita a 1,000 métricas por instancia sin configuración avanzada.

5. **Mantenimiento**: Lookout for Metrics requiere menos configuración inicial pero depende de modelos preentrenados de AWS, mientras que Azure Anomaly Detector permite ajustar modelos con datos propios, lo que puede mejorar la precisión a largo plazo.

## Opciones consideradas
> Preguntas guía: 
> - ¿Qué servicios de IA para observabilidad evaluarías para este caso? Considera precisión, costo, latencia y facilidad de integración.
> - ¿Cómo priorizarías los ASRs (precisión, latencia, costo) en la decisión?
> - ¿Qué pros y contras identificas en cada opción frente a los requisitos del caso?


## Decision
> Preguntas guía:
> - ¿Qué servicio de IA elegirías y con qué criterios medibles?
> - ¿Cómo justificarías tu elección frente a los trade-offs identificados?


## Consecuencias
> Preguntas guía:
> - ¿Qué impacto tendrá tu decisión en los ASRs (precisión, latencia, costo)?
> - ¿Qué riesgos identificas y cómo los mitigarías?
> - ¿Cómo validarías que la solución cumple con los SLOs definidos?

// === ARCHIVO: adr/002-patron-integracion-ia.md ===
# ADR 002: Patrón de Integración para Servicios de IA en Observabilidad

Estado: Propuesto
Fecha: 2024-05-20

## Contexto

La plataforma de e-commerce requiere integrar un servicio de IA para observabilidad que:

- **Procesar datos en tiempo real**: métricas de rendimiento (latencia, errores) y logs deben analizarse con una latencia máxima de 2 segundos desde su generación.
- **Escalar horizontalmente**: el patrón debe soportar el crecimiento del tráfico (50,000 solicitudes/segundo) sin cuellos de botella.
- **Mantener consistencia eventual**: las alertas generadas deben reflejar el estado más reciente de los datos, incluso bajo alta carga.
- **Integración con herramientas existentes**: CloudWatch (logs), Prometheus (métricas) y Grafana (dashboards).

Actualmente, los datos se recolectan mediante agentes en cada servicio y se envían a CloudWatch y Prometheus. El servicio de IA debe consumir estos datos, analizarlos y generar alertas.

## Fuerzas

1. **Latencia vs. Consistencia**: Un patrón basado en colas (ej. SQS, Kafka) introduce latencia adicional (50-200ms) pero garantiza consistencia eventual. Un patrón síncrono (ej. sidecar) reduce la latencia (<10ms) pero puede saturar los servicios bajo alta carga.

2. **Escalabilidad vs. Complejidad**: Un pipeline de eventos (ej. Kinesis + Lambda) escala horizontalmente pero requiere configuración adicional para manejar fallos y reintentos. Un sidecar simplifica la arquitectura pero limita la escalabilidad a la capacidad de cada instancia.

3. **Costo Operativo**: Un pipeline de eventos requiere gestión de infraestructura (Kinesis, Lambda, SQS) y monitoreo adicional. Un sidecar reduce la infraestructura pero aumenta el consumo de recursos en cada instancia.

4. **Tolerancia a Fallos**: Un pipeline de eventos permite reintentos y manejo de fallos a nivel de infraestructura. Un sidecar depende de la disponibilidad del servicio de IA y de la instancia donde se ejecuta.

5. **Integración con Ecosistema**: La plataforma ya utiliza Kinesis para streaming de datos, lo que facilita la adopción de un pipeline de eventos. Un sidecar requeriría cambios en la arquitectura de despliegue.

## Opciones consideradas
> Preguntas guía:
> - ¿Qué patrones de integración evaluarías para este caso? Considera latencia, escalabilidad, tolerancia a fallos y costo.
> - ¿Cómo impacta cada patrón en los ASRs (latencia, escalabilidad, consistencia)?
> - ¿Qué pros y contras identificas en cada opción frente a los requisitos del caso?


## Decision
> Preguntas guía:
> - ¿Qué patrón elegirías y con qué criterios medibles?
> - ¿Cómo justificarías tu elección frente a los trade-offs identificados?


## Consecuencias
> Preguntas guía:
> - ¿Qué impacto tendrá tu decisión en los ASRs (latencia, escalabilidad, consistencia)?
> - ¿Qué riesgos identificas y cómo los mitigarías?
> - ¿Cómo validarías que el patrón cumple con los SLOs definidos?

// === ARCHIVO: diagramas/contexto.mmd ===
c4Context
    title Diagrama de Contexto - Plataforma de E-commerce con Observabilidad Mejorada

    Person(usuario, "Usuario Final", "Cliente que interactúa con la plataforma de e-commerce")
    Person(equipo_ops, "Equipo de Operaciones", "Equipo responsable de monitorear y mantener la plataforma")

    System_Ext(aws, "AWS Cloud", "Proveedor de infraestructura y servicios en la nube")
    System_Ext(servicio_ia, "Servicio de IA para Observabilidad", "Servicio de IA para detección de anomalías y alertas inteligentes")
    System_Ext(prometheus, "Prometheus", "Sistema de monitoreo para métricas")
    System_Ext(grafana, "Grafana", "Herramienta de visualización de datos")
    System_Ext(cloudwatch, "Amazon CloudWatch", "Servicio de monitoreo y logs")

    System(plataforma_ecommerce, "Plataforma de E-commerce", "Plataforma principal que procesa pedidos y transacciones")

    Rel(usuario, plataforma_ecommerce, "Realiza pedidos y consultas")
    Rel(plataforma_ecommerce, cloudwatch, "Envía logs y métricas")
    Rel(plataforma_ecommerce, prometheus, "Expone métricas de rendimiento")
    Rel(prometheus, grafana, "Proporciona datos para dashboards")
    Rel(cloudwatch, grafana, "Proporciona logs para visualización")
    Rel(equipo_ops, grafana, "Monitorea dashboards y alertas")
    Rel(servicio_ia, equipo_ops, "Genera alertas inteligentes")

    UpdateLayoutConfig($c4ShapeInRow="2", $c4BoundaryInRow="1")

    title Preguntas Guía para Vistas Adicionales
    =========================================
    1. **Vista de Contenedores**: 
       - ¿Qué contenedores componen la plataforma de e-commerce y cómo se comunican?
       - ¿Dónde se ejecuta el servicio de IA (como un contenedor independiente, sidecar, o integrado en otro servicio)?
       - ¿Cómo se integran CloudWatch, Prometheus y Grafana con la plataforma?

    2. **Vista de Componentes**:
       - ¿Qué componentes internos tiene cada contenedor (ej. API Gateway, microservicios, bases de datos)?
       - ¿Cómo fluyen los datos desde la plataforma hasta el servicio de IA?
       - ¿Qué contratos definen las interacciones entre componentes (ej. APIs, eventos, colas)?

    3. **Vista de Despliegue**:
       - ¿Cómo se despliega la plataforma en AWS?
       - ¿Qué zonas de disponibilidad y regiones se utilizan para garantizar alta disponibilidad?
       - ¿Cómo se despliega el servicio de IA (ej. en la misma VPC, en otra región, como SaaS externo)?

// === ARCHIVO: poc/README.md ===
# Spike de Integración con Servicios de IA para Observabilidad

Este spike valida la integración básica con un servicio de IA para detección de anomalías en métricas de observabilidad de una plataforma de e-commerce. El código actual simula la llamada a un servicio externo (ej: AWS SageMaker, Google Vertex AI o un endpoint propio) que analiza patrones de tráfico para detectar anomalías.

## Contexto
La plataforma de e-commerce maneja **50,000 solicitudes por segundo** en hora pico. El spike demuestra:
1. **Integración con un servicio de IA**: Llamada a una API externa (simulada) para detección de anomalías en métricas como latencia, tasa de errores y throughput.
2. **Manejo de errores**: Gestión de fallos en la conexión, timeouts y respuestas inválidas del servicio.
3. **Configuración dinámica**: Uso de variables de entorno para parámetros críticos (URL del servicio, umbrales de alerta).

## ¿Qué debes completar?
El spike actual **no implementa la lógica de negocio real** para:
- **Validar umbrales de anomalías**: El servicio de IA retorna un puntaje (ej: `0.85`), pero el código no decide si es una anomalía.
- **Persistencia de resultados**: Los resultados de la detección no se guardan en un sistema de observabilidad (ej: CloudWatch, Prometheus).
- **Alertas proactivas**: No se notifica a los equipos cuando se detecta una anomalía.

## Instrucciones de ejecución
1. **Requisitos previos**:
   - Python 3.12+.
   - Dependencias instaladas: `pip install -r requirements.txt`.

2. **Configuración**:
   - Crea un archivo `.env` en la carpeta `poc/` con las siguientes variables:
     ```
     # URL del endpoint del servicio de IA (simulado o real)
     IA_SERVICE_URL=http://localhost:8000/detect-anomalies
     
     # Umbral de puntuación para considerar una anomalía (ej: 0.75)
     ANOMALY_THRESHOLD=0.75
     
     # Tiempo máximo de espera para la respuesta del servicio (en segundos)
     REQUEST_TIMEOUT=5
     ```

3. **Ejecutar el spike**:
   ```bash
   cd poc/
   python spike_integracion_ia.py
   ```

4. **Salida esperada**:
   - Si la llamada al servicio es exitosa:
     ```
     [INFO] Datos enviados al servicio de IA: {"latency": 120, "error_rate": 0.05, "throughput": 45000}
     [INFO] Respuesta del servicio de IA: {"anomaly_score": 0.85}
     [WARNING] Posible anomalía detectada. Puntaje: 0.85 (umbral: 0.75)
     ```
   - Si el servicio falla:
     ```
     [ERROR] Error al llamar al servicio de IA: ConnectionError(...)
     ```

## Validaciones clave
- **Conectividad**: El spike debe fallar si la URL del servicio es inaccesible o el timeout se excede.
- **Manejo de respuestas**: Debe procesar correctamente respuestas con formato inválido (ej: JSON malformado).
- **Configuración**: Debe leer las variables de entorno y fallar si no están definidas.

## Limitaciones del spike
- **Servicio simulado**: El endpoint `http://localhost:8000/detect-anomalies` no existe. Para probar con un servicio real, reemplaza la URL en `.env`.
- **Datos hardcodeados**: Las métricas enviadas (`latency`, `error_rate`, `throughput`) son estáticas. En un entorno real, se obtendrían de un sistema de monitoreo.
- **Sin persistencia**: Los resultados no se guardan en una base de datos o sistema de logs.

## Preguntas guía para el candidato
1. ¿Cómo integrarías este spike con un sistema de observabilidad existente (ej: Prometheus, CloudWatch)?
2. ¿Qué estrategias usarías para escalar la detección de anomalías en un entorno con 50,000 TPS?
3. ¿Cómo garantizarías la resiliencia del servicio de IA ante fallos (ej: circuit breaker, retries)?
4. ¿Qué métricas adicionales incluirías para mejorar la precisión de la detección de anomalías?

---
*Nota: Este spike es autocontenido. No importa módulos fuera de `poc/`.*

// === ARCHIVO: poc/spike_integracion_ia.py ===
"""
Spike para validar la integración con un servicio de IA que detecta anomalías 
en métricas de observabilidad de una plataforma de e-commerce.

El código simula la llamada a un servicio externo (ej: AWS SageMaker, Google Vertex AI)
y procesa la respuesta para detectar posibles anomalías. El candidato debe completar:
- Lógica de validación de umbrales.
- Integración con sistemas de persistencia (ej: CloudWatch, Prometheus).
- Mecanismos de alerta proactiva.
"""

import os
import json
import logging
from typing import Dict, Any
import requests
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Cargar variables de entorno desde .env
load_dotenv()

class AnomalyDetectionService:
    """Cliente para interactuar con el servicio de detección de anomalías."""

    def __init__(self):
        self.service_url = os.getenv("IA_SERVICE_URL")
        self.timeout = int(os.getenv("REQUEST_TIMEOUT", 5))
        self.anomaly_threshold = float(os.getenv("ANOMALY_THRESHOLD", 0.75))
        
        if not self.service_url:
            raise ValueError("La variable de entorno IA_SERVICE_URL no está configurada.")

    def detect_anomaly(self, metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Envía métricas al servicio de IA y recibe un puntaje de anomalía.
        
        Args:
            metrics: Diccionario con métricas de observabilidad (ej: {"latency": 120, "error_rate": 0.05}).
            
        Returns:
            Diccionario con la respuesta del servicio (ej: {"anomaly_score": 0.85}).
            
        Raises:
            requests.exceptions.RequestException: Si hay un error en la llamada al servicio.
        """
        try:
            logger.info(f"Datos enviados al servicio de IA: {json.dumps(metrics)}")
            
            response = requests.post(
                self.service_url,
                json=metrics,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            logger.info(f"Respuesta del servicio de IA: {json.dumps(result)}")
            return result
            
        except requests.exceptions.Timeout:
            logger.error("Timeout al llamar al servicio de IA")
            raise
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Error de conexión al servicio de IA: {e}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al llamar al servicio de IA: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Respuesta inválida del servicio de IA: {e}")
            raise ValueError("Respuesta no es un JSON válido")

    def is_anomaly(self, anomaly_score: float) -> bool:
        """
        Determina si el puntaje de anomalía supera el umbral configurado.
        
        Args:
            anomaly_score: Puntaje de anomalía recibido del servicio (ej: 0.85).
            
        Returns:
            True si el puntaje supera el umbral, False en caso contrario.
            
        Nota:
            El candidato debe implementar la lógica de validación según los requisitos
            del sistema (ej: usar umbrales dinámicos, considerar métricas adicionales).
        """
        # TODO: Implementar lógica de validación de umbrales.
        # Pregunta guía: ¿Cómo ajustarías este umbral dinámicamente en función de
        # la hora del día o el tráfico histórico?
        return anomaly_score >= self.anomaly_threshold


def simulate_metrics() -> Dict[str, Any]:
    """
    Simula métricas de observabilidad de la plataforma de e-commerce.
    
    Returns:
        Diccionario con métricas como latencia, tasa de errores y throughput.
    """
    return {
        "latency": 120,  # ms
        "error_rate": 0.05,  # % de errores
        "throughput": 45000,  # solicitudes/segundo
        "timestamp": "2024-05-20T15:30:00Z"
    }


def main():
    """Punto de entrada del spike."""
    try:
        # Inicializar el cliente del servicio de IA
        service = AnomalyDetectionService()
        
        # Obtener métricas simuladas
        metrics = simulate_metrics()
        
        # Detectar anomalías
        result = service.detect_anomaly(metrics)
        
        # Validar si es una anomalía
        if "anomaly_score" not in result:
            logger.error("La respuesta del servicio no contiene 'anomaly_score'")
            return
            
        if service.is_anomaly(result["anomaly_score"]):
            logger.warning(
                f"Posible anomalía detectada. Puntaje: {result['anomaly_score']} "
                f"(umbral: {service.anomaly_threshold})"
            )
            # TODO: Integrar con sistema de alertas (ej: Slack, PagerDuty)
            # TODO: Persistir el resultado en un sistema de observabilidad (ej: CloudWatch)
        else:
            logger.info("No se detectaron anomalías.")
            
    except Exception as e:
        logger.error(f"Error en el spike: {e}")
        raise


if __name__ == "__main__":
    main()

// === ARCHIVO: contratos/observabilidad_api.yaml ===
openapi: 3.0.0
info:
  title: API de Observabilidad con IA
  description: |
    API para integrar servicios de IA con sistemas de observabilidad en una plataforma de e-commerce.
    Permite enviar métricas en tiempo real, recibir detección de anomalías y gestionar alertas.
    
    **Requisitos arquitectónicos (ASRs):**
    - **Latencia p99**: < 100ms para detección de anomalías.
    - **Disponibilidad**: 99.95% mensual.
    - **Throughput**: 50,000 solicitudes/segundo en hora pico.
  version: 1.0.0
  contact:
    name: Equipo de Observabilidad
    email: observabilidad@ecommerce.com
servers:
  - url: https://api.observabilidad.ecommerce.com/v1
    description: Entorno de producción
  - url: https://staging-api.observabilidad.ecommerce.com/v1
    description: Entorno de staging
paths:
  /detect-anomalies:
    post:
      tags:
        - Anomaly Detection
      summary: Detecta anomalías en métricas de observabilidad
      description: |
        Envía métricas en tiempo real al servicio de IA para detectar anomalías.
        El servicio retorna un puntaje de anomalía (0.0 a 1.0) y detalles opcionales.
        
        **Preguntas guía para el candidato:**
        - ¿Qué métricas adicionales incluirías en el request para mejorar la precisión?
        - ¿Cómo estructurarías la respuesta para soportar múltiples modelos de IA?
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/AnomalyDetectionRequest"
      responses:
        "200":
          description: Respuesta exitosa con puntaje de anomalía
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/AnomalyDetectionResponse"
        "400":
          description: Request inválido (ej: métricas faltantes o formato incorrecto)
        "401":
          description: No autorizado (falta API key o token)
        "408":
          description: Timeout en la llamada al servicio de IA
        "500":
          description: Error interno del servidor
        "503":
          description: Servicio no disponible (ej: sobrecarga en el servicio de IA)
      security:
        - apiKeyAuth: []
  
  /alerts:
    post:
      tags:
        - Alerts
      summary: Crea una alerta de anomalía
      description: |
        Registra una alerta en el sistema de observabilidad cuando se detecta una anomalía.
        
        **Preguntas guía para el candidato:**
        - ¿Qué campos incluirías para clasificar la severidad de la alerta?
        - ¿Cómo integrarías este endpoint con un sistema de notificaciones (ej: Slack, PagerDuty)?
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/AlertRequest"
      responses:
        "201":
          description: Alerta creada exitosamente
        "400":
          description: Request inválido
        "401":
          description: No autorizado
    
    get:
      tags:
        - Alerts
      summary: Lista alertas activas
      description: |
        Retorna las alertas activas en el sistema, filtradas por severidad, fecha o servicio.
        
        **Preguntas guía para el candidato:**
        - ¿Qué parámetros de query agregarías para mejorar la usabilidad?
        - ¿Cómo implementarías paginación en los resultados?
      parameters:
        - $ref: "#/components/parameters/severity"
        - $ref: "#/components/parameters/fromDate"
        - $ref: "#/components/parameters/toDate"
      responses:
        "200":
          description: Lista de alertas activas
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: "#/components/schemas/Alert"
        "401":
          description: No autorizado
      security:
        - apiKeyAuth: []
components:
  schemas:
    AnomalyDetectionRequest:
      type: object
      required:
        - metrics
      properties:
        metrics:
          type: object
          description: Métricas de observabilidad a analizar
          example:
            latency: 120
            error_rate: 0.05
            throughput: 45000
            timestamp: "2024-05-20T15:30:00Z"
          additionalProperties:
            type: number
        service_name:
          type: string
          description: Nombre del servicio que genera las métricas (ej: "checkout-service")
          example: "checkout-service"
      
    AnomalyDetectionResponse:
      type: object
      required:
        - anomaly_score
      properties:
        anomaly_score:
          type: number
          format: float
          description: Puntaje de anomalía (0.0 a 1.0). Valores cercanos a 1 indican mayor probabilidad de anomalía.
          example: 0.85
        details:
          type: object
          description: Detalles adicionales del análisis (ej: contribución de cada métrica al puntaje)
          example:
            latency_contribution: 0.6
            error_rate_contribution: 0.25
        model_version:
          type: string
          description: Versión del modelo de IA utilizado
          example: "v1.2.0"
      
    AlertRequest:
      type: object
      required:
        - severity
        - message
        - service_name
      properties:
        severity:
          type: string
          enum: [low, medium, high, critical]
          description: Severidad de la alerta
          example: "high"
        message:
          type: string
          description: Descripción de la alerta
          example: "Alta latencia en checkout-service (120ms)"
        service_name:
          type: string
          description: Nombre del servicio afectado
          example: "checkout-service"
        anomaly_score:
          type: number
          format: float
          description: Puntaje de anomalía asociado
          example: 0.85
        metrics:
          type: object
          description: Métricas relevantes en el momento de la alerta
          example:
            latency: 120
            error_rate: 0.05
      
    Alert:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Identificador único de la alerta
          example: "550e8400-e29b-41d4-a716-446655440000"
        severity:
          type: string
          enum: [low, medium, high, critical]
          description: Severidad de la alerta
          example: "high"
        message:
          type: string
          description: Descripción de la alerta
          example: "Alta latencia en checkout-service (120ms)"
        service_name:
          type: string
          description: Nombre del servicio afectado
          example: "checkout-service"
        status:
          type: string
          enum: [open, acknowledged, resolved]
          description: Estado de la alerta
          example: "open"
        created_at:
          type: string
          format: date-time
          description: Fecha y hora de creación de la alerta
          example: "2024-05-20T15:30:00Z"
        updated_at:
          type: string
          format: date-time
          description: Fecha y hora de la última actualización
          example: "2024-05-20T15:35:00Z"
  
  parameters:
    severity:
      name: severity
      in: query
      description: Filtra alertas por severidad
      required: false
      schema:
        type: string
        enum: [low, medium, high, critical]
    
    fromDate:
      name: from_date
      in: query
      description: Filtra alertas creadas después de esta fecha (formato ISO 8601)
      required: false
      schema:
        type: string
        format: date-time
    
    toDate:
      name: to_date
      in: query
      description: Filtra alertas creadas antes de esta fecha (formato ISO 8601)
      required: false
      schema:
        type: string
        format: date-time
  
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-KEY
      description: API key para autenticación en la API de observabilidad"

```
