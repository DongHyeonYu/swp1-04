from cgi import parse_qs
from template1 import html

def application(environ, start_response):
	d = parse_qs(environ['QUERY_STRING'], keep_blank_values=False)
	
	global mul
        a = d.get('a',[''])[0]
	b = d.get('b',[''])[0]
	
        if '' not in [a,b]:
	    a, b = int(a), int(b)
	    mul = a*b
	    sum = a+b
	try:
        	response_body = html % {
	'sum' :sum, 'mul':mul 
	}
	except UnboundLocalError:
		response_body = html % {
	'sum' : 0, 'mul':0
	}

        start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(response_body)))])
        return [response_body]


