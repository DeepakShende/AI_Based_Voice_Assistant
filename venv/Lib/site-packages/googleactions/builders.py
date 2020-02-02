from googleactions.models import (TableCard,
                                  ColumnProperties,
                                  Row,
                                  Cell,
                                  BreakTimeUnit,
                                  BreakStrength,
                                  ProsodyRate,
                                  EmphasisLevel,
                                  HorizontalAlignment)


class SsmlBuilder(object):
    SPEAK = 'speak'
    BREAK = 'break'
    SAY_AS = 'say-as'
    AUDIO = 'audio'
    DESC = 'desc'
    PARAGRAPH = 'p'
    SENTENCE = 's'
    SUB = 'sub'
    PROSODY = 'prosody'
    EMPHASIS = 'emphasis'
    PAR = 'par'
    SEQ = 'seq'
    MEDIA = 'media'

    def __init__(self):
        self.txt = ''

    def start_tag(self, tag_name, attributes=[], is_end=False):
        self.txt += SsmlBuilder.get_start_tag(tag_name, attributes, is_end)
        return self

    def end_tag(self, tag_name):
        self.txt += SsmlBuilder.get_end_tag(tag_name)
        return self

    def do_break(self, time, unit=BreakTimeUnit.SECONDS, strength=BreakStrength.MEDIUM):
        time = str(time) + unit
        self.start_tag(SsmlBuilder.BREAK, [('time', time), ('strength', strength)], is_end=True)
        return self

    def say_as(self, text, interpret_as, as_format=None, detail=None):
        self.start_tag(SsmlBuilder.SAY_AS, [('interpret-as', interpret_as), ('format', as_format), ('detail', detail)])
        self.text(text)
        self.end_tag(SsmlBuilder.SAY_AS)
        return self

    def desc(self, text):
        self.start_tag(SsmlBuilder.DESC)
        self.text(text)
        self.end_tag(SsmlBuilder.DESC)
        return self

    def audio(self, src, alt=None, desc=None, clip_begin=None, clip_end=None,
              speed=None, repeat_count=None, repeat_dur=None, sound_level=None):
        is_end = alt is None and desc is None
        if clip_begin and type(clip_begin) is not str:
            clip_begin = str(clip_begin)+'s'
        if clip_end and type(clip_end) is not str:
            clip_end = str(clip_end)+'s'
        self.start_tag(SsmlBuilder.AUDIO, [
            ('src', src),
            ('clipBegin', clip_begin),
            ('clipEnd', clip_end),
            ('speed', speed),
            ('repeatCount', repeat_count),
            ('repeatDur', repeat_dur),
            ('soundLevel', sound_level),
        ], is_end=is_end)
        if not is_end:
            if desc is not None:
                self.desc(desc)
            if alt is not None:
                self.text(alt)
            self.end_tag(SsmlBuilder.AUDIO)
        return self

    def p(self, text):
        self.start_p()
        self.text(text)
        self.end_p()
        return self

    def start_p(self):
        return self.start_tag(SsmlBuilder.PARAGRAPH)

    def end_p(self):
        return self.end_tag(SsmlBuilder.PARAGRAPH)

    def s(self, text):
        self.start_s()
        self.text(text)
        self.end_s()
        return self

    def start_s(self):
        return self.start_tag(SsmlBuilder.SENTENCE)

    def end_s(self):
        return self.end_tag(SsmlBuilder.SENTENCE)

    def sub(self, text, alias):
        self.start_tag(SsmlBuilder.SUB, [('alias', alias)])
        self.text(text)
        self.end_tag(SsmlBuilder.SUB)
        return self

    def prosody(self, text, rate=ProsodyRate.MEDIUM, pitch=None):
        self.start_prosody(rate=rate, pitch=pitch)
        self.text(text)
        self.end_prosody()
        return self

    def start_prosody(self, rate=ProsodyRate.MEDIUM, pitch=None):
        self.start_tag(SsmlBuilder.PROSODY, [('rate', rate), ('pitch', pitch)])
        return self

    def end_prosody(self):
        self.end_tag(SsmlBuilder.PROSODY)
        return self

    def emphasis(self, text, level=EmphasisLevel.NONE):
        self.start_tag(SsmlBuilder.EMPHASIS, [('level', level)])
        self.text(text)
        self.end_tag(SsmlBuilder.EMPHASIS)
        return self

    def start_par(self):
        self.start_tag(SsmlBuilder.PAR)
        return self

    def end_par(self):
        self.end_tag(SsmlBuilder.PAR)
        return self

    def start_seq(self):
        self.start_tag(SsmlBuilder.SEQ)
        return self

    def end_seq(self):
        self.end_tag(SsmlBuilder.SEQ)
        return self

    def start_media(self,
              id=None, begin=None, end=None, repeat_count=None,
              repeat_dur=None, sound_level=None, fade_in_dur=None, fade_out_dur=None):
        self.start_tag(SsmlBuilder.MEDIA, [
            ('xml:id', id),
            ('begin', begin),
            ('end', end),
            ('repeatCount', repeat_count),
            ('repeatDur', repeat_dur),
            ('soundLevel', sound_level),
            ('fadeInDur', fade_in_dur),
            ('fadeOutDur', fade_out_dur)
        ])
        return self

    def end_media(self):
        self.end_tag(SsmlBuilder.MEDIA)
        return self

    def text(self, text):
        if text is not None:
            self.txt += text
        return self

    def build(self):
        return (SsmlBuilder.get_start_tag(SsmlBuilder.SPEAK) +
                self.txt +
                SsmlBuilder.get_end_tag(SsmlBuilder.SPEAK))

    @staticmethod
    def get_start_tag(tag_name, attributes=[], is_end=False):
        return ('<{tag}{attrs}{end}>'
                .format(tag=tag_name,
                        attrs=SsmlBuilder.get_attributes(attributes),
                        end=('/' if is_end else '')))

    @staticmethod
    def get_attributes(attributes=[]):
        attrs = ''
        for tup in attributes:
            val = tup[1]
            if val is not None:
                attrs += ' {key}="{val}"'.format(key=tup[0], val=val)
        return attrs

    @staticmethod
    def get_end_tag(tag_name):
        return '</{tag}>'.format(tag=tag_name)


class TableCardBuilder(object):
    def __init__(self):
        self.rows = []
        self.divs = []
        self._headers = []
        self.aligns = []
        self._button = None
        self._title = None
        self._subtitle = None
        self._image = None

    def title(self, title):
        self._title = title
        return self

    def subtitle(self, subtitle):
        self._subtitle = subtitle
        return self

    def row(self, cells, divider_after=False):
        self.rows.append(cells)
        self.divs.append(divider_after)
        return self

    def headers(self, headers, aligns=None):
        if not aligns:
            aligns = [HorizontalAlignment.CENTER for _ in headers]
        self._headers = headers
        self.aligns = aligns
        return self

    def button(self, button):
        self._button = button
        return self

    def image(self, image):
        self._image = image
        return self

    def build(self):
        if len(self.rows) > 0 and len(self.rows[0]) == len(self._headers):
            buttons = None
            if self._button:
                buttons = [self._button]
            return TableCard(title=self._title,
                             subtitle=self._subtitle,
                             image=self._image,
                             columns=[ColumnProperties(header=header, align=align)
                                      for header, align in zip(self._headers, self.aligns)],
                             rows=[Row(cells=[Cell(text=cell) for cell in row], divider_after=div)
                                   for row, div in zip(self.rows, self.divs)],
                             buttons=buttons)
        return None
