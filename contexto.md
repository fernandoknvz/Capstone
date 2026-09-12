# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is not a software project — there is no code, build, lint, or test tooling here. This repo version-controls the academic deliverables for a Duoc UC "Capstone" course project (Ingeniería en Informática, sede Plaza Oeste). The team's actual project, "Alloxentric Real Time Agent" (a voice collection-bot prototype for the company Alloxentric, built on LiveKit + Speechmatics + ElevenLabs + Asterisk), does not live in this repo — only the .docx/.pptx evidence documents the course requires do.

## Structure

- `Fase 1/`, `Fase 2/`, `Fase 3/` — one folder per course phase. `Fase 2` and `Fase 3` are currently empty placeholders (git does not track empty directories, so they show up locally but have no tracked content yet).
- Each phase folder splits into:
  - `Evidencias Grupales/` — deliverables submitted by the whole team.
  - `Evidencias Individuales/` — one deliverable per student.

## Naming conventions

- Group files: `<n>.<n>_<SiglaAsignatura>_<TipoDocumento>Fase<N>.docx`, e.g. `1.4_APT122_FormativaFase1.docx`.
- Individual files: `<Apellido>_<Nombre>_<n>.<n>_<SiglaAsignatura>_<TipoDocumento>Fase<N>.docx`, one per team member (`Diaz_Juan`, `Olguea_Fernando`, `Sepulveda_David`).
- Evidence numbering seen in Fase 1: 1.1 Autoevaluación de Competencias (individual), 1.2 Diario de Reflexión (individual), 1.3 Autoevaluación (individual), 1.4 Formativa (group — grading rubric + team report combined in one file), 1.5 Guía Estudiante Definición de Proyecto APT (group).

## Project/team context

- Team: Juan Díaz (Product Owner + dev), Fernando Olguea (project lead + dev), David Sepúlveda (Scrum Master + dev).
- Docente guía: Luis Bravo Yáñez.
- Course/sigla: Capstone, PTY4614 / 001V.
- Empresa/proyecto: "Alloxentric Real Time Agent" for Alloxentric (contact: Max Kreimerman).

## Git conventions

- Default branch: `main`. There are per-person branches (`fernando`, `juan`, `david`, mirrored as `dev/<name>` on `origin`) — confirm which branch a piece of work belongs on before committing.
- Preferred commit style: Conventional Commits scoped by phase, e.g. `docs(fase1): ...`, `docs(presentacion): ...`. A few early commits predate this and use plain Spanish messages — follow the conventional style going forward.

## Working with the .docx/.pptx files

- These are binary Office Open XML files. No pandoc or `python-docx` is preinstalled; if you need to read or edit one programmatically, install with `py -m pip install python-docx` (on this machine the `py` launcher resolves Python, not a bare `python`/`python3` command). Plain-text tools (grep/cat) can't read them directly.
- To pull text out of a `.docx` without python-docx, unzip it and parse `word/document.xml`'s `w:t` elements — but iterate all `w:p` descendants of `w:body` (including those nested inside `w:tbl`), not just top-level paragraphs, or you'll miss content that lives inside table cells.
- Concretely, the `1.4_*_FormativaFase1.docx` files store the school's grading rubric as a sequence of tables, and the team's actual written report is appended, page-broken, inside the **last cell of the last table** (`document.tables[-1].rows[-1].cells[-1]` in python-docx terms) — not as ordinary top-level paragraphs. Check there before assuming a `1.4` file is "just the rubric."
- Before editing a `.docx`/`.pptx`, check for a matching `~$<name>` lock file in the same folder — it means the file is currently open in Office; get confirmation it's closed first, otherwise edits can be lost or the file corrupted.
- When editing, only modify the team's own authored content; leave school-provided rubric/template tables (pautas de evaluación) exactly as delivered.
- Formatting rules for these reports are usually spelled out per-document under an "Instrucciones para el/la estudiante" section (e.g. required font family/size, line spacing, page numbers, and the portada/índice/abstract/desarrollo/conclusiones structure) — read that section in the specific file before judging it compliant, since requirements vary by evidence type.
