#получение ответа на запрос
#obj для анализа результатов запроса
#при приведении к bool
	200..400	>> True
	else 		>> False
	#также считает за True
		204 No Content
		304 Not Modified
#attrs:

	.content	-> <bytes>
	#получения содержимого запроса(?ответа) тела
	
	
	.text	-> <utf8_str>
	#~.content
	#декодирование происходит в соотв с содержимым .encoding
	
	
	.encoding
	#⊃ кодировку ответа
		response.encoding	>> 'UTF-8'
	#данные берутся из заголовка 
	#мб Δ
		response.encoding = 'utf-8'
	
	
	.header -> <dict>
	#заголовки
		response.headers	>> 
		{'Server': 'GitHub.com',
		'Date': 'Mon, 10 Dec 2018 17:49:54 GMT',
		'Content-Type': 'application/json; charset=utf-8', 
		'Transfer-Encoding': 'chunked', 
		'Status': '200 OK',
		'X-RateLimit-Limit': '60',
		'X-RateLimit-Remaining': '59',
		'X-RateLimit-Reset': '1544467794', 
		'Cache-Control': 'public, max-age=60, s-maxage=60',
		'Vary': 'Accept',
		'ETag': 'W/"7dc470913f1fe9bb6c7355b50a0737bc"',
		'X-GitHub-Media-Type': 'github.v3; format=json', 'Access-Control-Expose-Headers': 'ETag, Link, Location,		Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type', 
		'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload',
		'X-Frame-Options': 'deny',
		'X-Content-Type-Options': 'nosniff',
		'X-XSS-Protection': '1; mode=block',
		'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 
		'Content-Security-Policy': "default-src 'none'",
		'Content-Encoding': 'gzip',
		'X-GitHub-Request-Id': 'E439:4581:CF2351:1CA3E06:5C0EA741'}
	#http заголовки регистронезависимы -> можно не париться о регистре
		response.headers['content-type']	>> 'application/json; charset=utf-8'
		response.headers['content-tYpe']	>> 'application/json; charset=utf-8'
