# https://www.codewars.com/kata/5202ef17a402dd033c000009

def title_case(title, minor_words=''):
    if not title:
        return ''
    title_words = title.split()
    minor_words = minor_words.lower().split()
    processed_title = [title_words[0].title()]
    for word in title_words[1:]:
        if word.lower() not in minor_words:
            processed_title.append(word.title())
        else:
            processed_title.append(word.lower())
    return ' '.join(processed_title)


assert title_case('') == ''
assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
assert title_case('the quick brown fox') == 'The Quick Brown Fox'
