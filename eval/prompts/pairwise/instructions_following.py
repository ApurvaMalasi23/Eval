def instructions_following(prompt, baseline_model_response, response):
    return f"""
# Instruction
You are an expert evaluator. Your task is to evaluate the quality of the responses generated by two AI models. We will provide you with the user input and a pair of AI-generated responses (Response A and Response B).
You should first read the user input carefully for analyzing the task, and then evaluate the quality of the responses based on the Criteria provided in the Evaluation section below.
You will first judge responses individually, following the Rating Rubric and Evaluation Steps.
Then you will give step-by-step explanations for your judgment, compare results to declare the winner based on the Rating Rubric and Evaluation Steps.

# Evaluation
## Metric Definition
You will be assessing the model's ability to follow instructions provided in the user prompt.

## Criteria
Instruction following: The response demonstrates a clear understanding of the instructions in the user prompt, satisfying all of the instruction's requirements.

## Rating Rubric
"A": Response A follows instructions better than Response B. It follows all or more requirements of the instructions compared to Response B.
"SAME": Response A and B followed instructions equally well. Users would feel like their instructions were understood to a similar extent.
"B": Response B follows instructions better than Response A. It follows all or more requirements of the instructions compared to Response A.

## Evaluation Steps
STEP 1: Analyze Response A based on the instruction following criteria: Determine how well Response A fulfills the requirements outlined in the instructions and provide assessment according to the criterion.
STEP 2: Analyze Response B based on the instruction following criteria: Determine how well Response B fulfills the requirements outlined in the instructions and provide assessment according to the criterion.
STEP 3: Compare the overall performance of Response A and Response B based on your analyses and assessment.
STEP 4: Output your preference of "A", "SAME" or "B" to the pairwise_choice field according to the Rating Rubric.
STEP 5: Output your assessment reasoning in the explanation field.

# User Inputs and AI-generated Responses
## User Inputs
### Prompt
{prompt}

# AI-generated Response

### Response A
{baseline_model_response}

### Response B
{response}
"""
