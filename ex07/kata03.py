import sys

kata = "One sentence !"

sys.stdout.write('{}{}'.format('-'*(42-len(kata)),kata))
