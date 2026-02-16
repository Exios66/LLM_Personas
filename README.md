# LLM Personas

A collection of specialized AI agent personas for use with Cursor IDE. Each persona brings domain expertise and consistent methodology to different aspects of software development.

## Available Personas

### LIL_JEFF (CodeFarmer)

A development ecosystem powered by three collaborative personas:

- **CodeFarmer** — Project manager and architect. Breaks down requirements, maintains task lists, delivers complete modular code.
- **Programmatron** — Coding virtuoso. Writes optimized, production-ready implementations.
- **CritiBot** — QA specialist. Reviews code for completeness, naming quality, and best practices.

**Core principles:**
- Complete code only — no placeholders, stubs, or TODOs
- Modular architecture — single responsibility, clear boundaries
- Self-documenting names — code explains itself

## Project Structure

```
LLM_Personas/
├── .cursor/
│   └── agents/
│       └── lil-jeff.md      # CodeFarm agent definition
├── templates/
│   ├── module-template.md   # Standard module structure
│   └── project-dashboard.md # Project tracking template
├── checklists/
│   └── critibot-review.md   # Code review checklist
├── references/
│   └── naming-conventions.md # Naming patterns guide
└── README.md
```

## Usage

### In Cursor IDE

The `lil-jeff` agent activates automatically when you're writing or scaffolding code. You can also invoke it explicitly:

```
@lil-jeff Create a user authentication module
```

### Using Templates

**Starting a new module:**
1. Copy `templates/module-template.md`
2. Follow the structure for your language
3. Use the naming conventions from `references/naming-conventions.md`

**Tracking a project:**
1. Copy `templates/project-dashboard.md` to your project
2. Fill in modules, dependencies, and tasks
3. Update status as work progresses

**Code review:**
1. Run through `checklists/critibot-review.md` before committing
2. Every checkbox must pass
3. Zero tolerance items are instant fails

## CodeFarm Methodology

### MOD_CODING Workflow

1. **Requirements** — Gather and clarify what needs to be built
2. **Module breakdown** — Identify logical, self-contained units
3. **Implementation** — Write complete, working code for each module
4. **Review** — CritiBot pass on all code
5. **Integration** — Connect modules, verify system works
6. **Next steps** — Suggest improvements and future work

### What You'll Get

- Full implementations, not sketches
- Clear module boundaries
- Descriptive naming throughout
- Error handling included
- Ready to run

## Adding New Personas

Create a new file in `.cursor/agents/` with:

```yaml
---
name: persona-name
description: When to use this persona
---

# Persona instructions...
```

## License

Internal use. Adapt as needed for your projects.
