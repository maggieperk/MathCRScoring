# File to generate different types of prompts
from examples_responses import correct_response_explanation_part_a, correct_response_explanation_part_b, format_examples, format_examples_with_explanation,  format_examples_for_direct_prompt

def intro_string_scoring_assistant():
    return """You are a national mathematics assessment scoring assistant.  You must score student responses given a scoring rubric and output the response in your rubric."""


def response_format_string():
    return """Give the response in the format of a python dictionary like the following:
    {\"Part A\": <Incorrect/Correct>, \"Part B\": <Incorrect/Correct>, \"Overall\": <Incorrect/Partial 1/Partial 2/Correct>}"""

def combined_scoring_rubric_string():
    return """Scoring Rubric:
    \nCorrect: Both parts correct
    \nPartial 1: Part A correct only
    \nPartial 2: Part B correct only
    \nIncorrect: Incorrect response"""

def format_student_response_full_question(part_a_string, part_b_string):
    return f"""Student Response:
    \nPart A: {part_a_string}
    \nPart B: {part_b_string}
    """

def direct_prompt_full_question_setup(with_explanation=False, with_examples=False):
    prompt_string = ""

    prompt_string+=intro_string_scoring_assistant()
    prompt_string+="\n"

    question_string="""Question:Mark needs to solve the problem 143-48.  He will solve the problem in two steps.  First, Mark subtracts 43 from 143.
    \nPart A: What does Mark need to do next to complete the problem?
    \nPart B: What is the answer to 143 - 48?"""

    prompt_string+=question_string + "\n"

    if with_explanation:
        explanation = "The following explains the correct and incorrect values for each part.\n"
        explanation+= ("Part A: " + correct_response_explanation_part_a + "\n")
        explanation+=("Part B: " + correct_response_explanation_part_b + "\n")
        prompt_string+=explanation
    
    scoring_rubric = combined_scoring_rubric_string()
    prompt_string+= ("\n" + scoring_rubric + "\n" + response_format_string())

    if with_examples:
        prompt_string+= "Consider the following correctly scored examples when scoring student responses"
        examples = format_examples_for_direct_prompt()
        prompt_string +=examples
    

    return prompt_string

def create_sub_question_prompt_part_a(with_examples=False, with_explanation=False):
    part_a_sub_question = "What does Mark need to do next to complete the problem"
    return create_sub_question_setup(part_a_sub_question, "a", with_examples=with_examples, with_explanation=with_explanation)

def create_sub_question_prompt_part_b(with_examples=False, with_explanation=False):
    part_b_sub_question = "What is the answer to 143 - 48?"
    return create_sub_question_setup(part_b_sub_question, "b", with_examples=with_examples, with_explanation=with_explanation)

def create_sub_question_setup(sub_question, question_part, with_examples=False, with_explanation=False):
    sub_question_prompt=intro_string_scoring_assistant()
    sub_question_prompt+="\n"

    question_context="The question setup is: Mark needs to solve the problem 143-48.  He will solve the problem in two steps.  First, Mark subtracts 43 from 143."

    score_string = "Grade the student response to the following question as being Incorrect or Correct."
    question_string = "Question: " + sub_question

    sub_question_prompt = sub_question_prompt + question_context + "\n" + score_string + "\n" + question_string + "\n"

    if with_examples:
        if with_explanation:
            examples_for_prompt = format_examples_with_explanation(question_part)
        else:
            examples_for_prompt = format_examples(question_part)
        sub_question_prompt += examples_for_prompt
    
    return sub_question_prompt


def format_student_response_sub_question(sub_question_response):
    return f"Student Response: {sub_question_response}"

# Outputs combined score prompt
def create_combined_score_prompt():
    combined_score_prompt = intro_string_scoring_assistant()

    combined_score_prompt += "You are grading a two part question and the subparts have already been graded.  Give an overall score based on the following rubric. \n"

    combined_score_prompt = combined_score_prompt + combined_scoring_rubric_string() + response_format_string()

    return combined_score_prompt

# Format sub part scores for user message
def format_overall_score_user_message(part_a_score, part_b_score):
    return f"""Component Scores:\n
        Part A: {part_a_score}\n
        Part B: {part_b_score}\n"""






