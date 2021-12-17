base_str = ''
with open('q6_file') as f6:
    for line in f6:
        base_str += line.replace('\n', '***')
        # base_str += line.strip()
with open('q6_file', 'w') as f6:
    f6.write(base_str)

# # sample text in q6_file.txt:
# Lorem ipsum (dolor sit amet), ad aeque tantas disputationi vim, ius ei docendi indoctum sententiae,
# ex sea salutatus assueverit. Ne iusto voluptua vel. Est ne vitae corpora nominavi, modo cibo ne mei,
# duo animal prompta electram ea. Mel id augue choro labores, an velit harum iudico ius, doctus vidisse ei quo.
# Ex per mollis partiendo democritum, vim id facilisi dignissim similique, ne quem facilisi duo.
# Populo veritus sed no. Diam graeci veritus cum et.
#
# An lucilius mnesarchum duo, no (per ceteros abh) lorreant.
# Decore ubique duo no, deleniti mnesarchum scriptorem mel no.
# Pri at eripuit inimicus recteque, his ad vero sensibus intellegat, usu ex alterum molestie.
# Sea ea graeci suavitate, iisque salutatus efficiendi ex per.