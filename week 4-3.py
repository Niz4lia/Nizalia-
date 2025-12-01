moma_artworks = {"Starry Night", "The Persistence of Memory", "The Scream", "Girl with a Pearl Earring"}
louvre_artworks = {"Mona Lisa", "The Scream", "Liberty Leading the People", "Girl with a Pearl Earring"}
rijksmuseum_artworks = {"The Night Watch", "Girl with a Pearl Earring", "The Milkmaid", "Starry Night"}

moma_artworks.add('The Composition of Red, Blue and Yellow')

shared=moma_artworks.intersection(louvre_artworks).intersection(rijksmuseum_artworks)
print("Shared Masterpieces:", shared)

louvre_artworks.update({'Liberty leading the people', 'Raft of the Medusa'})
rijksmuseum_artworks.update({'The Jewish Bride', 'The Milkmaid'})

all= moma_artworks.union(louvre_artworks and rijksmuseum_artworks)
print('\nAll Artworks:\n',all)

rijksmuseum_artworks.discard('The Milkmaid')

print('\nExclusive Moma collection: ',moma_artworks.difference(moma_artworks and louvre_artworks.intersection()))

print(f'\nUpdated Artworks:\n>>Moma Artworks{moma_artworks}\n>>Louvre Artworks{louvre_artworks}\n>>Rijks Museum Artworks{rijksmuseum_artworks}')