# 프로그래머스 Design Guideline

## Mission
Create implementation-ready, token-driven UI guidance for 프로그래머스 that is optimized for consistency, accessibility, and fast delivery across content site.

## Brand
- Product/brand: 프로그래머스
- URL: https://programmers.co.kr/
- Audience: readers and knowledge seekers
- Product surface: content site

## Style Foundations
- Visual style: clean, functional, implementation-oriented
- Typography scale: `font.size.xs=12px`, `font.size.sm=14px`, `font.size.md=16px`, `font.size.lg=18px`, `font.size.xl=26px`
- Color palette: `color.surface.base=#000000`, `color.text.secondary=#0f1317`, `color.text.tertiary=#98a8b9`, `color.text.inverse=#ffffff`, `color.border.strong=#dce1e5`
- Spacing scale: `space.1=1px`, `space.2=4px`, `space.3=7px`, `space.4=8px`, `space.5=12px`, `space.6=16px`, `space.7=20px`, `space.8=24px`
- Radius/shadow/motion tokens: `radius.xs=3.2px`, `radius.sm=16px`, `radius.md=24px` | `motion.duration.instant=200ms`

## Accessibility
- Target: WCAG 2.2 AA
- Keyboard-first interactions required.
- Focus-visible rules required.
- Contrast constraints required.

## Writing Tone
Concise, confident, implementation-focused.

## Rules: Do
- Use semantic tokens, not raw hex values, in component guidance.
- Every component must define states for default, hover, focus-visible, active, disabled, loading, and error.
- Component behavior should specify responsive and edge-case handling.
- Interactive components must document keyboard, pointer, and touch behavior.
- Accessibility acceptance criteria must be testable in implementation.

## Rules: Don't
- Do not allow low-contrast text or hidden focus indicators.
- Do not introduce one-off spacing or typography exceptions.
- Do not use ambiguous labels or non-descriptive actions.
- Do not ship component guidance without explicit state rules.

## Guideline Authoring Workflow
1. Restate design intent in one sentence.
2. Define foundations and semantic tokens.
3. Define component anatomy, variants, interactions, and state behavior.
4. Add accessibility acceptance criteria with pass/fail checks.
5. Add anti-patterns, migration notes, and edge-case handling.
6. End with a QA checklist.

## Required Output Structure
- Context and goals.
- Design tokens and foundations.
- Component-level rules (anatomy, variants, states, responsive behavior).
- Accessibility requirements and testable acceptance criteria.
- Content and tone standards with examples.
- Anti-patterns and prohibited implementations.
- QA checklist.

## Component Rule Expectations
- Include keyboard, pointer, and touch behavior.
- Include spacing and typography token requirements.
- Include long-content, overflow, and empty-state handling.
- Include known page component density: links (132), buttons (23), lists (21), navigation (10), cards (2).

- Extraction diagnostics: Audience and product surface inference confidence is low; verify generated brand context.

## Quality Gates
- Every non-negotiable rule must use "must".
- Every recommendation should use "should".
- Every accessibility rule must be testable in implementation.
- Teams should prefer system consistency over local visual exceptions.
