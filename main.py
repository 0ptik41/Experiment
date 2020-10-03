import sys
import os 


def create_utils():
	needed_imports = {'Crypto.Random': 'get_random_bytes',
					  'Crypto.Cipher': 'AES'}
	header = 'import base64\nimport socket\nimport os\n'
	for lib in needed_imports.keys():
		header += 'from %s import %s\n' % (lib, needed_imports[lib])
	body = "\nBSZ=16;PAD='{'\npad=lambda s: s + (BSZ - len(s) % BSZ)*PAD\n"
	enc = 'EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))\n'
	dec = 'DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PAD)\n'
	# Add more functions?
	srv = '\ndef start_listener(p):\n\ttry:\n\t\ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n'
	srv += '\t\ts.bind(("0.0.0.0",p))\n\texcept socket.error:\n\t\treturn []\n\treturn s\n'
	rcv = '\ndef create_socket():\n\ts=[]\n\ttry:\n\t\ts=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n'
	rcv += '\texcept socket.error:\n\t\tpass\n\treturn s\n\n'
	hide='\ndef fencrypt(fname,destroy):\n\tif not os.path.isfile(fname):\n\t\texit()\n\t'
	hide+='efile=fname.split("/")[-1].split(".")[0]+".lol"\n\tcontent=open(fname,"rb").read()\n\t'
	hide+='k=get_random_bytes(16);open(efile,"wb").write(EncodeAES(AES.new(k),content))\n\t'
	hide+='open(fname.split("/")[-1].split(".")[0]+".key","wb").write(base64.b64encode(k))\n\t'
	hide+='if destroy:\n\t\tos.remove(fname)\n\n'
	see='def fdecrypt(fname):\n\tencd=open(fname,"rb").read()\n\tkf=fname.split(".")[0]+".key"\n\t'
	see+='k=base64.b64decode(open(kf,"rb").read())\n\t'
	see += 'return DecodeAES(AES.new(k),encd)\n\n'
	content = header+body+enc+dec+srv+rcv+hide+see
	open(os.getcwd()+'/utils.py', 'wb').write(content)


def main():
	create_utils()
	import utils # THIS IS SO SKETCHY BUT LETS TEST IT LOL!
	if '-e' in sys.argv and len(sys.argv) > 2:
		fname = sys.argv[2]
		if os.path.isfile(fname):
			utils.fencrypt(fname,True)
	if '-run' in sys.argv:
		open('hi.mkv','wb').write(utils.fdecrypt('omg.lol'))
		os.system('vlc hi.mkv')


if __name__ == '__main__':
	main()
