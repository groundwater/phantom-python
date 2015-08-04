from subprocess import Popen, PIPE
from json import loads

def measure(url):
    args = ['phantomjs', '--ssl-protocol=any', '--web-security=false', 'phantom-measure.js', url]
    proc = Popen(args, stdout=PIPE, stderr=2)
    code = proc.wait()

    if code != 0:
        raise Exception('PhantomJS Error')
    else:
        stdout = proc.stdout.readline().rstrip()
        results = loads(stdout)
        return results
