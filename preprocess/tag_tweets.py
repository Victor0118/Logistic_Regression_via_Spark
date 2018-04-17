#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import threading
import sys

# input_file: str
# output_file: str
def read_tweets(input_file, output_file):
	happy_emoji = [':‑)', ':)', ':-]', ':]', ':-3', ':3', ':3', ':->', ':>', '8-)', '8)', ':-}', ':}', ':o)', ':c)', ':^)', '=]', '=)', 
					':‑D', ':D', '8‑D', '8D', 'x‑D', 'xD', 'X‑D', 'XD', '=D', '=3', 'B^D', ':-))', ':-)))', ':\'‑)', ':\')', 
					':-*', ':*', ':×', ';‑)', ';)', '*-)', '*)', ';‑]', ';]', ';^)', ':‑,', ';D', ':‑P', ':P', 'X‑P', 'XP', 'x‑p', 'xp',
					':‑p', ':p', ':b', 'd:', '=p', '^_^', '^^', '^ ^', '(^_^)/', '(^O^)／', '(^o^)／', '(^^)/', '>^_^<', '^/^', '(*^_^*）',
					'(^.^)', '(^·^)', '(^.^)', '(^_^)', '(^^)', '^_^', '(*^.^*)', '(#^.^#)', '(*^0^*)', '＼(^o^)／', '!(^^)!', '(＾ｖ＾)', 
					'(＾ｕ＾)', '( ^)o(^ )', '(^O^)', '(^o^)', ')^o^(', 'ヽ(´▽`)/', '≧∇≦', '^ω^', '＾▽＾',
					'\xF0\x9F\x98\x81', '\xF0\x9F\x98\x82', '\xF0\x9F\x98\x83', '\xF0\x9F\x98\x84', '\xF0\x9F\x98\x86', '\xF0\x9F\x98\x89', 
					'\xF0\x9F\x98\x8A', '\xF0\x9F\x98\x8B', '\xF0\x9F\x98\x8C', '\xF0\x9F\x98\x8D', '\xF0\x9F\x98\x8F', '\xF0\x9F\x98\x97', '\xF0\x9F\x98\x98',
					'\xF0\x9F\x98\x99', '\xF0\x9F\x98\x9A', '\xF0\x9F\x98\x9B', '\xF0\x9F\x98\x9C', '\xF0\x9F\x98\x9D', '\xF0\x9F\x98\xB8', '\xF0\x9F\x98\xB9', '\xF0\x9F\x98\xBA',
					'\xF0\x9F\x98\xBB', '\xF0\x9F\x98\xBD', '\xF0\x9F\x99\x8B', '\xF0\x9F\x99\x8C', '\xF0\x9F\x98\x80', '\xF0\x9F\x98\x87',
					'\xF0\x9F\x98\x88', '\xF0\x9F\x98\x8E', 
					'\xF0\x9F\x92\x8B', '\xF0\x9F\x92\x8F', '\xF0\x9F\x92\x91', '\xF0\x9F\x92\x95', '\xF0\x9F\x92\x96', '\xF0\x9F\x92\x97', '\xF0\x9F\x92\x98',
					'\xF0\x9F\x92\x9D', '\xF0\x9F\x92\x9E', 
					'\xF0\x9F\x8C\xB9', '\xF0\x9F\x8E\x80', '\xF0\x9F\x8E\x81', '\xF0\x9F\x8E\x82', '\xF0\x9F\x8E\x86', '\xF0\x9F\x8E\x87', '\xF0\x9F\x8E\x89',
					'\xF0\x9F\x8E\x8A', 
					'\xE2\x9C\x8C', '\xE2\x9D\xA4', '\xE2\x98\xBA', '\xE2\x99\xA5', '\xE3\x8A\x97']

	sad_emoji = [':‑(', ':(', ':‑c', ':c', ':‑<', ':<', ':‑[', ':[', ':-||', '>:[', ':{', ':@', '>:(', ':\'‑(', ':\'(',
				'DX', 'D=', 'D;', 'D8', 'D:', 'D:<', 'D‑\':', '>:O', '8‑0', ':-0', ':‑o', ':o', ':‑O', ':O', ':‑/', ':‑.',
				'>:\\', '>:/', ':\\', '=/', '=\\', ':L', '=L', ':S', ':‑|', ':|', ':$', '(-_-;)', 'Q_Q', 'QQ', 'TnT', 'T.T', 'Q.Q', ';;', 
				';n;', ';-;', ';_;', '(T_T)', '(;_:)', '(ToT)', '(ー_ー)!!', '(-.-)', '(-_-)', '(=_=)', '(-"-)', '(ーー;)', '(*￣m￣)', '(＃ﾟДﾟ)',
				'(´；ω；`)', 'ヽ(`Д´)ﾉ', '（ ´,_ゝ`)', 
				'\xF0\x9F\x98\x91', '\xF0\x9F\x98\x92', '\xF0\x9F\x98\x93', '\xF0\x9F\x98\x94', '\xF0\x9F\x98\x95', '\xF0\x9F\x98\x96', '\xF0\x9F\x98\x9E', '\xF0\x9F\x98\x9F', 
				'\xF0\x9F\x98\xA0', '\xF0\x9F\x98\xA1', '\xF0\x9F\x98\xA2', '\xF0\x9F\x98\xA3', '\xF0\x9F\x98\xA4', '\xF0\x9F\x98\xA5', '\xF0\x9F\x98\xA6', '\xF0\x9F\x98\xA7', '\xF0\x9F\x98\xA8', 
				'\xF0\x9F\x98\xA9', '\xF0\x9F\x98\xAB', '\xF0\x9F\x98\xAD', '\xF0\x9F\x98\xB1', '\xF0\x9F\x98\xBE', '\xF0\x9F\x99\x8D',
				'\xF0\x9F\x92\x94', '\xF0\x9F\x92\xA2'
				]
	output = {}

	with open(input_file, 'r') as inf:
		# buffer size = 100
		with open(output_file, 'w', 100) as outf:
			for line in inf:
				if is_json(line):
					record = json.loads(line)
					if u'text' in record:
						unicode_text = record[u'text']
						if len(unicode_text) < 20:
							continue
						utf8text = unicode_text.encode("utf-8")
						is_happy, happy_tag = find_emoji(utf8text, happy_emoji)
						is_sad, sad_tag = find_emoji(utf8text, sad_emoji)
						if is_happy and not is_sad:
							output = {'text': utf8text, 'label': '1', 'emoji': happy_tag}
							outf.write(json.dumps(output) + '\n')
						elif not is_happy and is_sad:
							output = {'text': utf8text, 'label': '0', 'emoji': sad_tag}
							outf.write(json.dumps(output) + '\n')
					else:
						continue


# text: str
# emoji: list
# return: bool
def find_emoji(text, emoji):
	for e in emoji:
		if e in text:
			return True, e
	return False, None

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError, e:
    return False
  return True


if __name__ == '__main__':
	if len(sys.argv) != 3:
		exit(-1)
	else:
		read_tweets(sys.argv[1], sys.argv[2])
