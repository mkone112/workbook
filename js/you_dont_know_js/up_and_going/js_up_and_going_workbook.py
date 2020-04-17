 Strict Mode?
 fx как val?
	exp немедленно вызываемых fx (immediately invoked Function Expressions (IIFEs))?
идентификатор this?
Прототипы?
Старый и новый?
	Полифиллинг(polyfilling)?
	Транспиляция(transpiling)?
Не-JS?
семантическая верстка?
браузеры ⊃ интерактивный интерпритатор js
большинство операторов заканчиваются ;
exp - ∀ ссылка на var|val|набор var&val объединенных операторами
	оператор a = b * 2; ⊃ 4 exp
		2 : exp литерального val
		b : exp var означающего извлечение его текущего val
		b * 2
		a = b * 2 : exp присваивания
	типичное законченное exp - оператор-exp
		b * 2;
	оператор-exp вызова
		alert(a);
js - интерпритируемый с компиляцей на лету
Mastering The Developer Tools Console:http://blog.teamtreehouse.com/mastering-developer-tools-console
sh-enter
#ввод нескольких строк в консоли браузера