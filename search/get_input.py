def get_input(text: str) -> str:
    """"
        Method: 'get_input()' collects raw user input and returns a 'str'.
        Arguments: one positional argument 'text'
        Parameters:
        Text: a str object that can be changed globally,
        and will be displayed as the prompt to the user.
        Returns: user input as a str"""
    word = input(text)
    return word
    