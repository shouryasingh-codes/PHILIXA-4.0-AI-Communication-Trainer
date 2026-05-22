# PHILXA 4.0 MVP User Test Flow

## Test Goal

Verify that the MVP feels like entering a live corporate meeting, not answering a static chatbot question.

## Test Setup

Use one scenario:

- Room: Corporate World
- Situation: Team discussion / office meeting
- AI roles: Boss, Manager, Colleague
- User role: Team member

## Test Script

1. Start a new session.
2. Generate 3 to 5 AI-to-AI turns before the user speaks.
3. Show the current meeting context to the user.
4. Ask the user to respond as a team member.
5. Store the user's response as a structured turn.
6. Let the AI roles respond with one or two follow-up turns.
7. Score the user's answer.
8. Generate feedback.
9. End with a session summary.

## Minimum Test Case

Scenario prompt:

The team is discussing why the last project update was delayed. The Boss wants a direct explanation, the Manager wants a practical next step, and the Colleague is trying to keep the discussion collaborative.

User task:

Explain your side clearly and suggest how the team can avoid the same delay next time.

## Score Checks

Confidence:

- Does the user answer directly?
- Does the user avoid sounding unsure or defensive?

Grammar:

- Are there obvious grammar issues?
- Is the answer readable without confusion?

Clarity:

- Is the main point easy to understand?
- Does the answer avoid unnecessary filler?

Structure:

- Does the answer explain the issue first?
- Does it include a next step or solution?

## Feedback Checks

Feedback must include:

- one strong point
- one weak point
- one exact correction
- one improved rewrite

Feedback must avoid:

- generic praise
- repeated advice
- vague statements like "communicate better"
- scoring without explanation

## Pass Criteria

The test passes when:

- the room feels active before the user enters
- Boss, Manager, and Colleague sound different
- the conversation order feels natural
- the user response is scored across the MVP areas
- feedback gives a specific next improvement

