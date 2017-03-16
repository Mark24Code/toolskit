import os

EXTENSIONS=['.mp3']
files = os.listdir('.')

FILL_COUNT = len(str(len(files)))

i = 1
for f in files:
    filename, extname = os.path.splitext(f)
    if extname in EXTENSIONS:
        os.rename(f, '{}{}'.format(str(i).zfill(FILL_COUNT), extname))
    i += 1
