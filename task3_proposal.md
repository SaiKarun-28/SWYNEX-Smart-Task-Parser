# Task 3: Intelligent Feature Proposal - Smart Todo Categoriser

## Objective
To enhance the existing Smart Todo Categoriser with robust error handling, adaptive retry mechanisms, and a formalised evaluation framework to transform the prototype into an intelligent, production-ready utility.

## Proposed Enhancements

### 1. Robustness and Error Handling
The system currently assumes an ideal environment. It must be made resilient to real-world failures:
- **Adaptive Retry Logic:** Implement exponential backoff for API calls to manage transient network issues or rate limits effectively.
- **JSON Repair Pipeline:** If the Large Language Model (LLM) returns malformed JSON, introduce a secondary pass that feeds the error back to the model, instructing it specifically to correct the syntax.
- **Ambiguity Detection:** Integrate a mechanism to evaluate the LLM's confidence score. If the output falls below a pre-defined threshold, the system should flag the task for human review rather than forcing an inaccurate categorisation.

### 2. AI Evaluation Framework
To move beyond subjective observation, a quantifiable approach is necessary:
- **Golden Dataset:** Create a JSON-formatted dataset containing 15-20 challenging task descriptions—including those with sarcasm, ambiguous deadlines, and deliberate errors.
- **Automated Testing:** Develop a script to process this dataset automatically, measuring:
    - **Schema Fidelity:** Does the output strictly adhere to the defined Pydantic model?
    - **Parsing Accuracy:** How often does the extracted metadata (category, priority, deadline) match the ground truth?
- **Failure Analysis:** Log and classify failures (e.g., parsing errors, hallucinations, API timeouts) to identify systematic weaknesses.

### 3. Interface Design
A Jupyter Notebook will serve as the primary demo interface. This provides a clear, documented environment where a reviewer can:
- Observe the parser's logic for individual inputs.
- Inspect the automated evaluation results.
- Visualise the robustness mechanisms (e.g., seeing the system retry after a simulated failure).

## Implementation Plan
1. **Refactor `categoriser.py`:** Inject retry logic and schema validation wrappers.
2. **Develop Evaluation Suite:** Create the 'Golden Dataset' and the automated testing script.
3. **Build Notebook:** Assemble the documentation and demo code.
4. **Testing:** Execute against the golden dataset and refine the model prompts until success rates are acceptable.
5. **Final Documentation:** Update the README to reflect these intelligent features.
