import os

if __name__ == "__main__":
	#　琉球音階は、ド,レb,ミb,ソ,ラb
	create_list=["C","Db","Eb","G","Ab"]
	# 本だと6,7だけど、7は高杉
	octave_list=[5,6]

	# 0-255?
	velocity=100

	# 拍数
	time=4


	cmd_template="python3 create_single_sound.py {} {} {} {}"

	for note in create_list:
		for octave in octave_list:
			cmd=cmd_template
			cmd=cmd.format(octave,note,velocity,time)
			os.system(cmd)
