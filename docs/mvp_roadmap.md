# PHILXA 4.0 MVP Roadmap

## Execution Order

1. Scope lock and user test design
2. Conversation data structure
3. Role personalities
4. Turn controller
5. AI-to-AI baseline conversation
6. Scenario engine
7. Short-term memory
8. Scoring system
9. Feedback engine
10. Session summary
11. UI build
12. Integration, testing, and polish

## Day 1 - Scope Lock and Test Design

Goal: make the project small, clear, and controllable.

Deliverables:

- final MVP scope
- one-page product spec
- in-scope and out-of-scope list
- one Corporate World room
- short user test
- scoring areas: confidence, grammar, clarity, structure

Done when:

- PHILXA 4.0 MVP can be explained in one line
- the MVP exclusions are clear
- the test flow is written before more code is added

## Day 2 - Conversation Data Structure

Goal: make every conversation line understandable to the system.

Deliverables:

- message schema
- session schema
- role schema
- fields for turn number, speaker role, target person, timestamp, message text, and session id

Done when:

- the system can save and read every utterance correctly

## Day 3 - Role Personalities

Goal: make Boss, Manager, and Colleague feel distinct.

Deliverables:

- Boss prompt
- Manager prompt
- Colleague prompt
- tone rules
- do-not-do rules
- example replies

Done when:

- the user can quickly feel that the three roles are different

## Day 4 - Turn Controller

Goal: make the conversation feel like a meeting, not a chatbot chain.

Deliverables:

- next-speaker logic
- interruption logic
- follow-up logic
- reaction logic
- conversation state transitions

Done when:

- turn order feels natural and does not spam random replies

## Day 5 - AI-to-AI Baseline Conversation

Goal: make the room feel alive before the user enters.

Deliverables:

- Boss talks to Manager
- Manager replies
- Colleague reacts
- 3 to 5 turn pre-run before user entry

Done when:

- the user feels like they are entering an active meeting

## Day 6 - Scenario Engine

Goal: keep the room stable while controlling the starting situation.

Deliverables:

- one base MVP scenario
- scenario registry
- prompt variant selection

Done when:

- the same room consistently starts in a predictable way

## Day 7 - Short-Term Memory

Goal: preserve recent context.

Deliverables:

- recent turn storage
- user last-answer memory
- rolling context buffer

Done when:

- the conversation can reference earlier points without breaking continuity

## Day 8 - Scoring System

Goal: evaluate user answers meaningfully and consistently.

Deliverables:

- clarity score
- confidence score
- structure score
- grammar score
- optional technical explanation score
- stable rubric

Done when:

- the same input gives stable and understandable scoring

## Day 9 - Feedback Engine

Goal: turn scoring into useful improvement.

Deliverables:

- one strong point
- one weak point
- one exact correction
- one example rewrite

Done when:

- the user receives a clear next step after answering

## Day 10 - Session Summary

Goal: close each session with a meaningful recap.

Deliverables:

- overall score
- strongest skill
- weakest skill
- next improvement
- final verdict line

Done when:

- the user receives a clear recap at the end of the session

## Day 11 - UI Build

Goal: make the system clean and usable.

Deliverables:

- chat room UI
- speaker labels for Boss, Manager, and Colleague
- message bubbles
- score panel
- feedback panel

Done when:

- a non-technical user can complete a session

## Day 12 - Integration, Testing, and Polish

Goal: make the full system stable.

Deliverables:

- end-to-end flow test
- turn-flow fixes
- repeated-answer fixes
- repo cleanup
- demo preparation
- basic deployment if needed

Done when:

- the test to office room to feedback flow works without breaking

