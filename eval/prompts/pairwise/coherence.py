def coherence(prompt, baseline_model_response, response): 
    return f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by two AI models. We will provide you with the user input and a pair of AI-generated responses (Response A and Response B).
You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will first judge responses individually, following the Rating Rubric and Evaluation Steps.
Then you will give step-by-step explanations for your judgment, compare results to declare the winner based on the Rating Rubric and Evaluation Steps.

# Evaluation
## Metric Definition
You will be assessing coherence, which measures the ability to provide a coherent response based on the user prompt.

## Criteria
Coherence: A clear and coherent presentation of ideas. The writing should demonstrate
a logical flow, where ideas progress smoothly with clear transitions, and maintain
relevance to the main point. Effective organization is essential, with a clear structure,
signaling, and topic sentences to guide the reader. Additionally, the writing should
exhibit strong cohesion, using word choices, sentence structures, pronouns, and
figurative language to reinforce connections between ideas and create a unified piece.

## Rating Rubric
"A": Response A is better than Response B based on all the criteria provided.
"SAME": Response A and B are of the same quality based on all the criteria provided.
"B": Response B is better than Response A based on all the criteria provided.

## Evaluation Steps
STEP 1: Analyze Response A based on all the Criteria.
STEP 2: Analyze Response B based on all the Criteria.
STEP 3: Compare the overall performance of Response A and Response B based on your analyses and assessment.
STEP 4: Output your preference of "A", "SAME" or "B" to the pairwise_choice field according to the Rating Rubric.
STEP 5: Output your assessment reasoning in the explanation field.

# User Inputs and AI-generated Responses
## User Inputs
### Prompt
{prompt}

## AI-generated Responses

### Response A
{baseline_model_response}

### Response B
{response}
"""