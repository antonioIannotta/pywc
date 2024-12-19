def wc(file: str, l_option: bool = False, w_option: bool = False,
       c_option: bool = False) -> str:

    """
    This method hides the whole logic of the application, returning a string representing the result
    :param file: the file to be processed
    :param l_option: the interest in the number of lines
    :param w_option: the interest in the number of words
    :param c_option: the interest in the number of chars
    :return: a string with a meaningful report
    """

    line_number: int = 0
    word_counter: int = 0
    char_counter: int = 0

    with open(file, 'r') as f:
        lines = f.readlines()  # Read lines once
        line_number += len(lines)
        for line in lines:
            words: list[str] = line.split()  # Split on any whitespace
            word_counter += len(words)
            for word in words:
                char_counter += len(word)

    wc_results = []
    if l_option:
        wc_results.append(f"Lines number: {line_number}")
    if w_option:
        wc_results.append(f"Words number: {word_counter}")
    if c_option:
        wc_results.append(f"Chars number: {char_counter}")

    return "\n".join(wc_results)