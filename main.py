import re

tekst1 = 'Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'
tekst2 = '<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a> </p></div>'
tekst3 = 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit.' \
         'Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In' \
         'blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus' \
         'eu risus.'
tekst4 = 'Lorem ipsum dolor' \
         'sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista' \
         'egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta' \
         'lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus.'

tekst5 = 'Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;)' \
         'Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta;' \
         'lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-).'

Rtekst1 = re.sub('\d', '', tekst1);
print(Rtekst1)
Rtekst2 = re.sub('<.*?>', '', tekst2)
print(Rtekst2)
Rtekst3 = re.sub('[^a-z|A-Z| ]', '', tekst3)
print(Rtekst3)

Rtekst4 = re.findall('#.[a-z]+', tekst4)
print(Rtekst4)
Rtekst5 = re.findall('[:|;]\-*[\)|<|\(]', tekst5)
print(Rtekst5)
