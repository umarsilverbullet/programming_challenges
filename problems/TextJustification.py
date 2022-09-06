# combination sum
class TextJustification:
    def __init__(self):
        print('initialising')

    def solveProblem(self,words, maxWidth):
        justifiedList = []

        i=0
        while i < len(words):
            cap = maxWidth
            stringBuilder = ""
            # take j to the position in words, where full line is completed
            j = i+1
            cap -= len(words[i])
            sp = 0
            while j < len(words) and len(words[j]) < cap-sp:
                cap -= len(words[j])
                j += 1
                sp += 1

            ds = cap // ((j-i)-1) if ((j-i)-1) != 0 else cap
            exs = cap % ((j-i)-1) if ((j-i)-1) != 0 else 0

            cap = maxWidth
            if j >= len(words):
                for k in range(i,j):
                    cap -= len(words[k])
                    stringBuilder += words[k]

                    stringBuilder += " " * (1 if cap > 0 else 0)
                    cap -= 1

                stringBuilder += " " * (cap if cap > 0 else 0)
                justifiedList.append(stringBuilder)
                break

            for k in range(i,j):
                if i == k:
                    stringBuilder += words[k]
                    cap -= len(words[k])
                    continue
                elif cap > 0:
                    stringBuilder += " " * ds
                    exS = (1 if exs > 0 else 0)
                    stringBuilder += " " * exS
                    stringBuilder += words[k]
                    exs -= 1
                    cap -= (len(words[k]) + ds + exS)

            if cap > 0:
                stringBuilder += " " * cap

            justifiedList.append(stringBuilder)
            i = j
        return justifiedList
