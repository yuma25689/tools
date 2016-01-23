u'''
単音のmidiファイルを作成する。

arg1: オクターブ 1から7くらいで指定。ただし、もっといけるかも。
arg2: 音階 C,Db,D,Eb,E,F,Gb,G,Ab,A,B のいずれかで指定
	=>上からもらうのは上記の通り
	内部的に、下記のように変換して16進数にする
	C,D,E,F,0,1,2,3,4,5,6

	※ 内部的には、下記の通り
	* C=ド
	* D=ドのシャープ=レのフラット
	* E=レ
	* F=レのシャープ=ミのフラット
	* 0=ミ
	* 1=ファ
	* 2=ファのシャープ=ソのフラット
	* 3=ソ
	* 4=ソのシャープ=ラのフラット
	* 5=ラ
	* 6=シ

arg3: 強さ 0-255?
arg4: 拍数 4しか試してないが、たぶん0-255で
'''


import sys
# import struct

if __name__ == "__main__":
	param = sys.argv
	octave=param[1]
	note=param[2]
	velocity=int(param[3])
	time=int(param[4])

	# outfilename
	outfilename = note + octave + ".mid"

	# noteは変換する
	note_translate_array={}
	note_translate_array["C"]="C"
	note_translate_array["Db"]="D"
	note_translate_array["D"]="E"
	note_translate_array["Eb"]="F"
	note_translate_array["E"]="0"
	note_translate_array["F"]="1"
	note_translate_array["Gb"]="2"
	note_translate_array["G"]="3"
	note_translate_array["Ab"]="4"
	note_translate_array["A"]="5"
	note_translate_array["B"]="6"

	note = note_translate_array[note]

	sOctaveAndNote = octave+note

	# 3オクターブ、音Cならば、0x3Cの1byteが必要
	byteOfOctaveAndNote=int(sOctaveAndNote,16)


	# ファイルを出力
	with open(outfilename,"wb") as fout:
		# midiであることを表すヘッダ
		bary=bytearray([0x4D,0x54,0x68,0x64])
		# ヘッダ部のデータ長
		bary.extend([0x00,0x00,0x00,0x06])
		# フォーマット
		bary.extend([0x00,0x01])
		# トラック長
		bary.extend([0x00,0x01])
		# 一拍の分解能
		bary.extend([0x00,0x01])
		# トラック1 開始
		bary.extend([0x4D,0x54,0x72,0x6B])
		# トラック1のデータ長[0C(12)BYTE]
		bary.extend([0x00,0x00,0x00,0x0C])
		# 指定の音をVelocity(音の大きさ?)40でON
		bary.extend([0x00,0x90,byteOfOctaveAndNote,velocity])
		# 4拍後、オフ:ch0, key:4 C(ミ), vel:40
		bary.extend([time,0x80,byteOfOctaveAndNote,0x00])
		# トラック1 終了
		bary.extend([0x00,0xFF,0x2F,0x00])
		fout.write(bary)

	print("OK. The output file is "+outfilename)

