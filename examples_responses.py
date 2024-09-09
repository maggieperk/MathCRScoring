
# Return a formatted set of examples with or without the scoring explanations
def format_sample(response, score):
    return f"Student Response: {response}: Score: {score}\n"

def convert_list_of_samples_to_string(list_of_samples, score):
    sample_string = ""
    for example in list_of_samples:
        example_string_for_prompt = format_sample(example, score)
        sample_string+=example_string_for_prompt
    
    return sample_string

def format_examples(question_part):
    example_prompt_string = "Consider the following correctly scored examples in your response: \n"
    if question_part == 'a':
        example_prompt_string+= convert_list_of_samples_to_string(example_correct_part_a_responses, "Correct")
        example_prompt_string+= convert_list_of_samples_to_string(example_incorrect_part_a_responses, "Inorrect") + "\n"

    elif question_part == 'b':
        example_prompt_string+= convert_list_of_samples_to_string(example_correct_part_b_responses, "Correct")
        example_prompt_string+= convert_list_of_samples_to_string(example_incorrect_part_b_responses, "Inorrect") + "\n"
    else:
        raise Exception("Question part " + question_part + " is not a valid option")

    return example_prompt_string

def format_examples_with_explanation(question_part):
    example_prompt_string = "Consider the following correctly scored examples in your response: \n"

    if question_part == 'a':
        example_prompt_string+= correct_response_explanation_part_a + "\n"
        example_prompt_string+= convert_list_of_samples_to_string(example_correct_part_a_responses, "Correct")
        
        example_prompt_string+= incorrect_response_explanation_part_a + "\n"
        example_prompt_string+= convert_list_of_samples_to_string(example_incorrect_part_a_responses, "Inorrect") + "\n"
    
    elif question_part == 'b':
        example_prompt_string+= correct_response_explanation_part_b + "\n"
        example_prompt_string+= convert_list_of_samples_to_string(example_correct_part_b_responses, "Correct")

        example_prompt_string+= incorrect_response_explanation_part_b + "\n"
        example_prompt_string+= convert_list_of_samples_to_string(example_incorrect_part_b_responses, "Inorrect") + "\n"

    else:
        raise Exception("Question part " + question_part + " is not a valid option")

    
    return example_prompt_string


def format_sample_for_direct_prompt(part_a, part_b, score):
    return f"Student Response: Part A: {part_a} \n Part B: {part_b} Score: {score}\n"

def format_examples_for_direct_prompt():
    direct_prompt_examples = ""
    for part_a in example_correct_part_a_responses:
    
        for part_b in example_correct_part_b_responses:
            # These Should be Correct
            formatted_response = format_sample_for_direct_prompt(part_a, part_b, "Correct")
            direct_prompt_examples += formatted_response
        
        for part_b in example_incorrect_part_b_responses:
            # These should be Partial 1
            formatted_response = format_sample_for_direct_prompt(part_a, part_b, "Partial 1")
            direct_prompt_examples += formatted_response
    
    for part_a in example_incorrect_part_a_responses:
        for part_b in example_correct_part_b_responses:
            # These Should be Partial 2
            formatted_response = format_sample_for_direct_prompt(part_a, part_b, "Partial 2")
            direct_prompt_examples += formatted_response
        
        for part_b in example_incorrect_part_b_responses:
            # These should be Incorrect
            formatted_response = format_sample_for_direct_prompt(part_a, part_b, "Incorrect")
            direct_prompt_examples += formatted_response

    return direct_prompt_examples

# Storing example responses for the system to use
example_correct_part_a_responses = [
    "mark needs to subtract 5 from 100.",
    "100 - 5",
    "subtract 5 more",
    "Subtract 5 from 100",
    "Subtract 5 from the result found in step 1."
    "100 minus 5", 
    "Minus 5"
]

example_correct_part_b_responses = [
    "95",
    "ninety five"
]

example_incorrect_part_a_responses = [
    "143 - 48",
    "5 - 100",
    "+ 5",
    "Student Response: 100 - 3"
]

example_incorrect_part_b_responses = [
    "100",
    "97",
    "105",
]

# Scoring Rubric Explanations
correct_response_explanation_part_a = "The following samples are scored as correct because they indicate that 5 should be subtracted from 100 for part (a)."
correct_response_explanation_part_b = "The following samples are scored as correct because they indicate that the difference is 95 for part (b)."
incorrect_response_explanation_part_a = "The following samples are incorrect because they do not indicate that 5 should be subtracted from 100."
incorrect_response_explanation_part_b = "The following samples are incorrect because the difference is not equal to 95."


