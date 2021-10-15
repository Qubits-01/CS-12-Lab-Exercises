def main():
    no_of_test_cases = 3
    paragraphs = [
        [
            'The quick brown fox jumped over the lazy dog.',
            'However, the quick brown fox, I think, jumped over the lazy dog.'
        ],
        [
            'Never have I ever been to the zoo. Although, I wish to see the giraffes some day.',
            'How was your trip to the zoo? I\'ve been dying to learn more about it.'
        ],
        [
            'My dad took me fishing today.',
            'Took me fishing today, my dad.'
        ]
    ]

    for paragraph in paragraphs:
        paragraph[0] = clean_paragraph(paragraph[0])
        paragraph[1] = clean_paragraph(paragraph[1])

    for paragraph in paragraphs:
        para1 = set(paragraph[0])
        para2 = set(paragraph[1])

        sim_score = (len(para1 & para2) / len(para1 | para2)) \
                    + (0.5 * (1 - (len(para1 - para2) / len(paragraph[0])))) \
                    + (0.5 * (1 - (len(para2 - para1) / len(paragraph[1]))))

        print('SAFE' if sim_score < 1 else 'SUS')


def clean_paragraph(paragraph):
    paragraph = paragraph.lower()
    words = paragraph.split()
    words = [word.strip('.,!?\'"') for word in words]  # Remove punctuations.
    words = [word.replace('\'s', '') for word in words]  # Remove 's.

    return words


if __name__ == '__main__':
    main()


# def main():
#     no_of_test_cases = int(input())
#     paragraphs = []
#
#     for _ in range(no_of_test_cases):
#         paragraphs.append([clean_paragraph(input()), clean_paragraph(input())])
#
#     for paragraph in paragraphs:
#         para1 = set(paragraph[0])
#         para2 = set(paragraph[1])
#
#         sim_score = (len(para1 & para2) / len(para1 | para2)) \
#                     + (0.5 * (1 - (len(para1 - para2) / len(paragraph[0])))) \
#                     + (0.5 * (1 - (len(para2 - para1) / len(paragraph[1]))))
#
#         print('SAFE' if sim_score < 1 else 'SUS')
#
#
# def clean_paragraph(paragraph):
#     paragraph = paragraph.lower()
#     words = paragraph.split()
#     words = [word.strip('.,!?\'"') for word in words]  # Remove punctuations.
#     words = [word.replace('\'s', '') for word in words]  # Remove 's.
#
#     return words
#
#
# if __name__ == '__main__':
#     main()

