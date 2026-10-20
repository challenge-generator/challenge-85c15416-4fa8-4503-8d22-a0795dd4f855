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