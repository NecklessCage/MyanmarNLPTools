from myanmartools import ZawgyiDetector
from icu import Transliterator

detector = ZawgyiDetector()
converter = Transliterator.createInstance('Zawgyi-my')

DIGIT_DICT = {
    'ဝ':'0',
    '၀':'0',
    '၁':'1',
    '၂':'2',
    '၃':'3',
    '၄':'4',
    '၅':'5',
    '၆':'6',
    '၇':'7',
    '၈':'8',
    '၉':'9'
}
DIGIT_DICT_EN = {
    k:v for k,v in zip(DIGIT_DICT.values(), DIGIT_DICT.keys())
}

def digit_mm2en(mmstr):
    return ''.join(DIGIT_DICT[s] if s in DIGIT_DICT.keys() else s for s in mmstr)


def digit_en2mm(enstr):
    return ''.join(DIGIT_DICT_EN[s] if s in DIGIT_DICT_EN.keys() else s for s in enstr)


def normalize_unicode(text):
    if detector.get_zawgyi_probability(text) > 0.95:
        return converter.transliterate(text)
    return text
