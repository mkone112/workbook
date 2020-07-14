Firefox========================================================================================================
sessions_on_startup
	extensions
		tab session manager	-> Open session list in tab:true
	about:config
		dom.allow_scripts_to_close_windows = True
	homepage -> custom urls
		file:///C:/Users/mkone/TEMP/redirect_test.html|moz-extension://<uuid?>/popup/index.html#inTab
	redirect_test.html
		<!doctype html>
		<html>
		<head>
		  <meta charset="utf-8">
		  <title>Sessions</title>
		  <script language="javascript" type="text/javascript">
		    setTimeout(() => { window.close(); }, 500);
		  </script>
		</head>
		<body>
		</body>
		</html>
==============================================================================================================