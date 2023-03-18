def string_matcher(n, m, text, sub):
    for i in range(n - m):
        j = 0
        while j < m and text[i + j] == sub[j]:
            j += 1
        if j == m:
            print("valid shift, {} match {} index from {} to {}"
            .format(text, sub, i, i + m - 1))

text = "googole"
sub = "go"


string_matcher(len(text), len(sub), text, sub)