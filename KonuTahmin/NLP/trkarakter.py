import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')
turkceKarakterler = "[^a-zA-ZÇĞİÖŞÜçğıöşüÂÎÛâîû']"
lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Â'): u'â',
    ord(u'Î'): u'î',
    ord(u'Û'): u'û',
    }