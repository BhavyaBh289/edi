import pke
extractor = pke.unsupervised.TopicRank()
sample = """ Sir, my humble submission to you is that I am Roshan Bibi Swami Sikh Sabarak Darji, Village:-Shankra-Kh,Po:-Shankra,Thana:-Para,Dist:- Purulia resident.As per Muslim Neon last dated 05.09.2017 Married to Sekh Sabarak Darji, son of Sekh Jugnu Darji of village Shankra-Kh under Para police station.Currently, I am the mother of a 03-year-old son, from the last one year, my husband and in-laws have been abusing me mentally and physically in various ways. They also beat my three-year-old child by not letting him eat or verbally beating him. I have tried to survive in the world despite all the tortures. After paying all the dowry during the marriage, the torture on me increased for the last nine-ten months, and I was repeatedly told by them to buy my father a Bullet car. Then my father and brother came to convince my in-laws and insulted them and sent me and my child to my father's house on 29-09-2021. While leaving, my brother-in-law and mother-in-law told me that the Hero Glamor whose registration number JH09AG 6215 was given as dowry during the marriage should be replaced by a new BULLET car, otherwise they should come back or kill their son i.e. me. Husband will remarry. Even though I want to return to in-laws house again and again, my husband or in-laws keep humiliating me and demanding a new BULLET car. is doing Now I know for sure that my husband is remarrieddid So sir my husband 1) Sikh Sabarak Darji, 2) Vasur Sikh Tabarak Darji, 3) Nand-Parbina Bibi, 4) Sikh Jaganu Darji father-deceased Nishad Darji and 5) Mother-in-law Khairuna Bibi, husband- Jaganu Darji legal action against all of them. Take appropriate measures to punish the maidservants and take necessary steps to secure the future life of me and my children. My complaint was delayed because I was hoping it would take me now that my husband had remarried."""
extractor.load_document(input=sample, language='en')
a=[]
n=[]
extractor.candidate_selection(pos={'VERB'})
for i, candidate in enumerate(extractor.candidates):
    a.append( u for u in extractor.candidates[candidate].surface_forms)
for i in a:
    for c in i:
        for d in c:
            n.append(d)
print(n)
