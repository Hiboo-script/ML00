import sys

kata = "One sentence !"
n = 41 - len(kata)

bars = "-"*n

sys.stdout.write(f'{bars}{kata}')
