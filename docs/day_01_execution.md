# Day 1 Execution Checklist

## Objective

Lock the PHILXA 4.0 MVP scope and write the first user test before building more system logic.

## Checklist

- [x] Lock one-line product definition
- [x] Freeze MVP room as Corporate World
- [x] Freeze one base scenario: team discussion / office meeting
- [x] Define in-scope features
- [x] Define out-of-scope features
- [x] Define score areas
- [x] Write short user test flow
- [x] Define pass criteria
- [ ] Run the user test against the first working conversation loop

## Target File Structure

```text
PHILXA_4/
  app/
    streamlit_app.py
  data/
    scenarios.json
  docs/
    day_01_execution.md
    mvp_scope.md
    user_test_flow.md
  memory/
    session_store.py
  prompts/
    roles.py
  scoring/
    feature_extractor.py
    scorer.py
  simulation/
    turn_controller.py
  schemas.py
  requirements.txt
  README.md
```

## First Code Order

1. Replace dictionary-only schemas with typed models for messages, sessions, roles, scores, and feedback.
2. Add one scenario config for the Corporate World office meeting.
3. Add role prompt templates for Boss, Manager, and Colleague.
4. Build a deterministic turn controller before connecting any LLM.
5. Connect the existing scoring module through a safe function interface.
6. Add feedback generation rules.
7. Add a minimal UI after the backend loop works in the terminal.

## Day 1 Done When

Day 1 is complete when the repo can answer these questions without ambiguity:

- What is PHILXA 4.0 MVP?
- What is not included in the MVP?
- What exact test proves the first version works?
- What files should be built next?

