animal=['fly','spider','bird','cat','dog','goat','cow','horse']
lyrics=["I don't know why she swallowed the fly. \nPerhaps she'll die.",
        "That wiggled and jiggled and tickled inside her.",
        "How absurd, to swallow a bird",
        "Imagine that, she swallowed a cat.",
        "What a hog, to swallow a dog.",
        "She just opened her throat and swallowed a goat.",
        "I don't know how she swallowed a cow.",
        "She's dead, of course."]

for a in animal:
    
    print('There was an old lady who swallowed a {}.\n{}'.format(a,lyrics[animal.index(a)]))

    if a == 'horse':
        break
    
    predator = animal[animal.index(a):0:-1]
    for p in predator:
        print('She swallowed the {} to catch the {}'.format(p, animal[animal.index(p)-1]))

    if a != 'fly':
            print(lyrics[0])
    print()
