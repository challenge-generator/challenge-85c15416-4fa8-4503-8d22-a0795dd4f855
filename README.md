# Mejora de la observabilidad con IA en plataforma de e-commerce

Como arquitecto de soluciones avanzado, debes diseñar e implementar una estrategia de observabilidad mejorada utilizando servicios de IA para una plataforma de e-commerce. La plataforma experimenta un tráfico de 50 000 solicitudes por segundo en hora pico y requiere una observabilidad avanzada para identificar y resolver problemas de rendimiento y escalabilidad. Los servicios de IA deben automatizar la detección de anomalías y la generación de alertas inteligentes.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Optimización de la observabilidad con servicios de IA |
| **Nivel** | advanced-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 180 minutos |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Análisis de Requisitos y Contexto

**Objetivo:** Entender los requisitos de observabilidad y el contexto de la plataforma de e-commerce.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Identifica los ASRs (requisitos arquitectónicamente significativos) relacionados con la observabilidad.
- Analiza el tráfico y los patrones de uso de la plataforma.
- Establece los KPIs y SLOs para la observabilidad.

**Entregable:** Documento de requisitos de observabilidad con ASRs, KPIs y SLOs.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la latencia, disponibilidad y escalabilidad como atributos clave.
- Piensa en cómo los servicios de IA pueden mejorar la detección de anomalías.

</details>

### Fase 2: Diseño de la Estrategia de Observabilidad

**Objetivo:** Diseñar la estrategia de observabilidad utilizando servicios de IA.

**Tiempo estimado:** 60 minutos

**Instrucciones:**

- Define la arquitectura de la solución de observabilidad.
- Identifica los servicios de IA que se utilizarán para la detección de anomalías y la generación de alertas.
- Establece los patrones de integración y comunicación entre los servicios.

**Entregable:** Documento de diseño de la estrategia de observabilidad con diagramas C4 y ADRs.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la integración con herramientas de monitoreo existentes.
- Evalúa los pros y contras de diferentes servicios de IA.

</details>

### Fase 3: Implementación y Validación

**Objetivo:** Implementar y validar la solución de observabilidad.

**Tiempo estimado:** 60 minutos

**Instrucciones:**

- Implementa un spike mínimo para validar la integración de un servicio de IA.
- Realiza pruebas de integración y valida que la solución cumple con los KPIs y SLOs establecidos.
- Documenta los resultados y las lecciones aprendidas.

**Entregable:** Spike mínimo de integración de servicio de IA y reporte de validación.

<details>
<summary>Pistas de conocimiento</summary>

- Utiliza patrones de integración idóneos para servicios de IA.
- Considera la escalabilidad y la latencia en las pruebas de integración.

</details>

### Fase 4: Revisión y Entrega

**Objetivo:** Revisar y entregar la solución de observabilidad.

**Tiempo estimado:** 30 minutos

**Instrucciones:**

- Revisar el documento de diseño y los ADRs para asegurar la calidad y la alineación con los ASRs.
- Entregar la solución de observabilidad al equipo de operaciones.
- Preparar una presentación ejecutiva para los stakeholders.

**Entregable:** Documento de diseño revisado, ADRs y presentación ejecutiva.

<details>
<summary>Pistas de conocimiento</summary>

- Asegura que los diagramas y los ADRs sean claros y concisos.
- Prepara una presentación ejecutiva que destaque los beneficios y los resultados de la solución.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es la observabilidad y por qué es importante en una plataforma de e-commerce?
- **paraQueSirve**: ¿Para qué sirve la integración de servicios de IA en la observabilidad?
- **comoSeUsa**: ¿Cómo se utilizan los servicios de IA para mejorar la detección de anomalías?
- **erroresComunes**: ¿Cuáles son los errores comunes al integrar servicios de IA en la observabilidad?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño de una estrategia de observabilidad con servicios de IA?

## Criterios de Evaluacion

- Alineación con los ASRs de observabilidad.
- Uso justificado de servicios de IA frente a alternativas.
- Calidad de los diagramas C4 y los ADRs con trade-offs explícitos.
- Viabilidad y madurez de la solución (seguridad, observabilidad y operación realista).

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
