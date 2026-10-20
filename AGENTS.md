# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Mejora de la observabilidad con IA en plataforma de e-commerce**.

| | |
|---|---|
| Tema | Optimización de la observabilidad con servicios de IA |
| Nivel | advanced-l2 |
| Chapter | Arquitectura |
| Especialidad | Soluciones |
| Stack | Markdown/YAML/Mermaid / C4 Model + ADR + Well-Architected Framework |
| Patron arquitectonico | Arquitectura de soluciones con vistas C4 (contexto, contenedores, componentes) y decisiones registradas en ADR |
| Tiempo estimado | 180 minutos |

## Receta del stack

Esqueleto obligatorio:

- `adr/`
- `arquitectura.md`
- `diagramas/*.mmd`
- `atributos-de-calidad.md`
- `rubrica-autoevaluacion.md`
- `poc/ (opcional)`

Dependencias:

- Mermaid.js n/a
- Python 3.12 3.12
- requests n/a
- boto3 n/a
- OpenAPI 3.0 3.0.0

## Tu tarea

Dejar este conjunto de artefactos en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Análisis de Requisitos y Contexto**: Documento de requisitos de observabilidad con ASRs, KPIs y SLOs.
- **Fase 2 — Diseño de la Estrategia de Observabilidad**: Documento de diseño de la estrategia de observabilidad con diagramas C4 y ADRs.
- **Fase 3 — Implementación y Validación**: Spike mínimo de integración de servicio de IA y reporte de validación.
- **Fase 4 — Revisión y Entrega**: Documento de diseño revisado, ADRs y presentación ejecutiva.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Superficie de practica (NO completes)

Estos archivos SON el ejercicio de la persona. No los implementes; deja stubs. No toques la logica que el reto pide completar.

- [ ] `adr/001-servicio-ia-observabilidad.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.
- [ ] `adr/002-patron-integracion-ia.md` — El topic pide decisiones de arquitectura: el ADR es el ejercicio.

## Lo que falta y tenes que completar

No se detectaron huecos: estan los archivos declarados, el boilerplate del stack y ninguna referencia quedo colgando. Igual corre el comando de verificacion — que los archivos existan no garantiza que compilen.

### Presentes (12)

- `poc/requirements.txt`
- `README.md`
- `atributos-de-calidad.md`
- `arquitectura.md`
- `riesgos-y-mitigaciones.md`
- `rubrica-autoevaluacion.md`
- `adr/001-servicio-ia-observabilidad.md`
- `adr/002-patron-integracion-ia.md`
- `diagramas/contexto.mmd`
- `poc/README.md`
- `poc/spike_integracion_ia.py`
- `contratos/observabilidad_api.yaml`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `adr`
- `diagramas`
- `contratos`
- `poc`
- `docs`

## Verificacion

```bash
python3 -c "import glob,sys; assert glob.glob('adr/*.md') and glob.glob('diagramas/*.mmd'), 'faltan ADRs o diagramas'"
```

El comando tiene que pasar SIN implementar los archivos de la superficie de practica: solo andamiaje.

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **Arquitectura de soluciones con vistas C4 (contexto, contenedores, componentes) y decisiones registradas en ADR**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Arquitectura, Especialidad Soluciones, Seniority Advanced
- Brecha que el reto ataca: Ha aplicado servicios de IA para mejorar los procesos de observabilidad y automatizar actualizaciones y mejoras de observabilidad e infraestructura.
- Mision: Candidato con experiencia avanzada en arquitectura, trabajando en cierre de brechas de conocimiento en observabilidad con IA.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
