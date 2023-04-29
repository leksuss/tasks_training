# https://www.codewars.com/kata/52449b062fb80683ec000024

def generate_hashtag(s):
    hashtag = f"#{''.join(s.title().split())}"
    return 1 < len(hashtag) < 141 and hashtag


assert generate_hashtag('Codewars') == '#Codewars'
assert generate_hashtag('Codewars      ') == '#Codewars'
assert generate_hashtag('      Codewars') == '#Codewars'
assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
assert generate_hashtag('CoDeWaRs is niCe') == '#CodewarsIsNice'
assert generate_hashtag('c i n') == '#CIN'
assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
assert generate_hashtag('') is False
assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') is False
