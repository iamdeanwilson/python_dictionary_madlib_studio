# Find the instructions in the textbook:(https://education.launchcode.org/data-analysis/chapters/dictionaries/studio.html)

def create_madlib_dict(mlib_string):
  words = mlib_string.split() # Split string into a list of words.
  new_dict = {}
  for word in words:
    if '{' in word:
      key = word[1:word.find('}')]
      new_dict[key] = ''
  return new_dict # Return the new dictionary instead of {}.
  
def prompt_user_for_words(mad_lib_dict):
  answers_dict = mad_lib_dict.copy() # Make an independent copy of the dictionary.
  for key in answers_dict.keys():
    answers_dict[key] = input(f'Choose a(n) {key[:-1]} : ')
  return answers_dict

def create_output(ml_dict, text):
  new_text = text  # Assign the starting value to new_text.
  for (key, value) in ml_dict.items():
    label = '{' + key + '}'
    new_text = new_text.replace(label, value)
  return new_text
    
def main():
  mad_lib = 'The {adjective1} dog loves to {verb1} and {verb2}.'
  mlib_dict = create_madlib_dict(mad_lib)
  user_responses = prompt_user_for_words(mlib_dict)
  output = create_output(user_responses, mad_lib)
  print(output)

main()