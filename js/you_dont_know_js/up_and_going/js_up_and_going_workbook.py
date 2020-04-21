 Strict Mode
 #ES5+
 #более безопасен
 #постепенно становится стандартом
 #рекомендуется использовать ∀
	#const
		const a = 1;
		a = 'd';		>> Error
	#ломает автоматическое объявление глобальных v:)
#объявляется соответствующей директивой
#вроде может быть объявлена в ∀ месте ns(но это не точно)
	"use strict";
	#используется в
		#блоках кода
			function f() {
				"use strict";
				...
			}
		#файлах
			"use strict";
#возможно уже пашет по умолчанию
	function foo() {
		console.log(this.bar);
	};
	
	var bar = "global";
	foo();				// undefined # хотя ожидалось вроде global
	#некоторые fx js
		классы?
		модули?
		...
		#включ strict автоматом
this
#идентификатор, ссылка
#концепция
#механизм
#не связан с obj-ориент. шаблонами
#if fx ⊃ this => this обычно указывает на obj(какой - зависит от способа вызова fx); ∃ 4 варианта:
	function foo() {
		console.log( this.bar );
	}
	
	var bar = "global";
	
	var obj1 = {
		bar: "obj1",
		foo: foo
	};
	
	var obj2 = {
		bar: "obj"
	};
	#установка this в глобальный obj в non stirct mode
	#в strict будет undefined + ошибка при доступе к .bar ДА ВРОДЕ ТУТ ВСЕГДА undefined(возможно strict mode включен by def)
	foo();			// "global"
	#устанавливает this в obj1
	#пашет
	obj1.foo();		// "obj1"	#вызывает obj указанный по ссылке
	foo.call(obj2); // "obj2" 	#думаю ~ obj2.foo()
	#устанавливает this в новый пустой obj
	new foo();		// undefined
#не ссылается на саму fx
	

Прототипы
#довольно сложный механизм
#~прототипы obj
#связывание ссылки на внутренний прототип от obj происходит при его создании
		#вроде тупой пример использования(по сути эмуляция наследования без классов)
		let foo = {
			a: 42
		};
		#создаем prototype link в bar указывающий на foo
		let bar = Object.create( foo );
		bar.b = "hello world";
		#св-во a !∃ в bar
		#bar прототипно связан с foo => js автоматом ищет a в foo(видимо if поиск в bar не удался)
		bar.a;					>> 42 	// делегируется в foo
		#естественное применение
			#делегирование поведения
				#шаблон
				#намеренное проектирование связанных obj так чтобы они могли делегировать от одного к другому части необходимого поведения
#при ссылке на св-во obj, if оно !∃ => js автоматом исп ссылку на внутренний прототип этого obj для поиска св-ва в нем
	Object
		.create( <obj> )
		#создание obj и связывание его с прототипом?
			let foo = {
				a: 42
			};
			let bar = Object.create( foo );
			bar.b = "hello world";
			bar.a;					>> 42 	// делегируется в foo
новый синтаксис
#читабельнее, обслуживаемее
#быстрее в новых браузерах
#чем раньше начнут использоваться тем раньше можно сделать фидбек в TC39(комитет JS) => можно предотвратить фиксацию багов в яп
Полифиллинг
#polyfilling
	polyfill
	#термин создан Реми Шарпом(remysharp.com/2010/10/08/what-is-a-plyfill)
	#используется для указания на взятие определения новой возможности и генерации кода ~ этому поведению, но с возможностью запуска в более старом интерпритаторе/окружении
	#не выглядит чем-то необычным - это определенный синтаксис? это доступно в ∀ ES?
	#!∀ новые фичи полностью полифильны(!100% эмуляция поведения) =>
			#следует
				использовать полифиллинг с осторожностью
				max придерживаться спецификации
				#использовать проверенные набор полифиллов
					#ES5
shim:англ:шайба					
	#напр ES6 ⊃ Number.isNaN(..) обеспечивающую точную безошибочную проверку на NaN, отмечая исходную fx isNaN(..) как устаревшую
		#можно заполифиллить эту fx для использования в браузерах !⊃ поддержку ES6
		#возможно я плохо знаю контекст 
		if (!Nuber.isNaN) {	// проверка на поддержку ES6
			Number.isNaN = function isNaN(x) {
				return x !== x; // единственное val != самому себе
			};
		}
#реализация новых фич js в старых интерпритаторах(~ python __future__)
Транспиляция
#звучит как первое преимущество перед python(хотя я не очень знаком напр с __future__|2to3(или как-то так))
#transpiling(transorming + compiling)
#стандартная часть экосис-мы и деплоя js
#позволяет легко переключаться на новый синтаксис не оглядываясь на legacy и старые браузеры
#реализация новых фич js в старых интерпритаторах(~ python __future__)
#позволяет эмулировать новый синтаксис чего нельзя добиться поллифиллингом(т.к. вызовет SyntaxErr)
#утилита конвертирующая новый код в старый
#пример
	#ES6 добавляет args по умолчанию
		function foo(a = 2) {
			console.log(a);
		}
		foo();		>> 2
		foo(42);	>> 42
	#транспилированный код
		function foo() {
			#вроде void 0 нужен т.к. undefined - единственное val которое не может быть задано для default arg
			var a = arguments[0] !== (void 0) ? arguments[0] : 2;
			console.log( a );
		}
#транспилятор=транспайлер 
	#втыкается в процесс сборки ~ linter|minifier
	#примеры	
		Babel
		#раньше 6to5
		#транспайлер ES6+=>ES5
		#babeljs.io
		Traceur
		#github.com/google/traceur-compiler
		#ES6+ => ES5 | ES7 => ES5
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
console
	.log()
	#вывод текста в консоль
	#кажется неявно приводит val к string для вывода
alert()
#оператор
ВВОД
самый распростаненный вариант - считать ввод из HTML-формы
prompt( "msg")
#~input python
переменные требуют объявления?
	var a;
	#в консоли
		b = 3
		#вполне пашет
clear()
#очистка вывода консоли
undefined
#~None python
#выводится в консоли
СОСТАВНЫЕ ОПЕРАЦИИ
	ПРИСВАИВАНИЯ
		+=
		*=
		-=
		/=
ИНКРЕМЕНТ, ДЕКРЕМЕНТ
	ПОСФИКСНЫЙ
		a++
		a--
obj
#val хранящие другие val в виде св-в
#поддерживают точечную и скобочную(bracket) нотацию
	obj.a
	obj["a"]
СРАВНЕНИЯ
#подробнее о механизме сравнений(который весьма прямолинеен):
  #ecma-international.org/ecma-262/5.1/
  #ES5	11.9.3
  #ES5	11.8.5
     ВИДИМО АБСОЛЮТНЫЕ СРАВНЕНИЯ
	==
	#нестрогое
	#более мощно
	#"сверяет val"
	#сравнение с приведением(разрешая приведение)(может произвести серию приведений перед сравнением val пока типы не совпадут)
		"42" == 42;		>> true
	===
	#строгое
	#более предсказуемо
	#"сверяет val и тип"
	#сравнение без приведения(без ее разрешения)
		"42" === 42;		>> false
	!=
	#нестрогое неравенство
	!==
	#строгое неравенство
    ОТНОСИТЕЛЬНОЕ СРАВНЕНИЕ
    #js !⊃ операций строгого неравенства(>==, etc)
    #используются обычные правила неявного приведения
	let a = 41;
	let b = "42";
	let c = "43";
	a < b;		>> true
	b < c;		>> true
	#это может привести к фейлам
	#не сравниваемые val при сравнении всегда дают false
		let a = 42;
		let b = "foo";
		a < b;			>> false
		a > b;			>> false
		a == b;			>> false
		#т.к. Number("foo");		>> NaN
    #при сравнении string используются коды символов
	>
	<
	<=
	#меньше|нестрого равно
	>=
	#больше|нестрого равно
	&&
	#and
	||
	#or
#правила использования
#это бред - предсказать где-какое val окажется
	===
		if одно их сравниваемых val м.б. 
			bool
			0
			""
			[]
	==
		∀ остальные случаи
#СРАВНЕНИЕ НЕПРИМИТИВОВ ПРОИСХОДИТ ПО ССЫЛКЕ(function, array)
#т.к. их val хранятся по ссылке(а ∀ остальное нет?)
	let a = [1,2,3];
	let b = [1,2,3];
	let c = "1,2,3";
	a == c;			>> true
	b == c;			>> true
	a == b;			>> false
Mozilla Developer Network(MDN)'s "Expressions and Operators":https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_Operators
bool
	true
	false
string
	''
	""
ПРИВЕДЕНИЕ(coercion) ТИПОВ
	Number(obj)
	#приведение к number
НЕЯВНОЕ ПРИВЕДЕНИЕ
#неочевидный побочный эффект других операций
#бывают ситуации когда может показаться что неявное приведение ∃ там где его нет
#может использоваться для улучшения читаемости
#if неявное приведение создает проблемы -> обычно это кривые руки
	в операции нестрогого равенства
		99.99 == "99.99"	>> true
		99.99 === "99.99" >> false
	при выводе console.log
	в exp ожидающих опред тип
		if (bool) {
			...
		}
	String => Number
	другие операции	
		let a = "42";
		a * 1;		>> 42
		
код без комментов - не гуд
комменты должны объяснять
	почему и как
	но не что
//однострочные комменты
/*
	многострочные комменты
*/
могут быть использованы в ∀ месте
	var a = /* comment */ 42;
многострочные комменты не могут ⊃ "*/"
var - символьный контейнер
статическая типизация
#контроль типов
js - динамически типизирован(без контроля типов)
поднятие var - hoisting
#~всплытие var
#при объявлении v в ns она доступна ∀ в этой ns т.е. использовать v можно до объявления в коде(славно)
#более точно объясняется тем как компилируется код
#не общепринято для v, но используется для fx
объявление var вводит новый идентификатор инициализированный undefined
ОБЛАСТИ ВИДИМОСТИ
	global
	function(local)
	#при объявлении с var в fx - переменная доступна только в этой fx и вложенных в нее fx
	#for вроде не создают своей ns
		for (var i = 0; i< n;i++) {
			...
		}
		console.log(i)	>> ok
	повторное объявление ничего не меняет
		function a() {
			b = 2;
		}
		var b;			>> undefined
		console.log(b)				>> function b()
let
#ограничивает ns текущим блоком(∀ ⊃ напр for) и ∀ вложенными 
#интерпритатор присваивает v undefined при создании
v - переменная
возможно раньше var имели undefined до создания, но сейчас я такого точно не вижу
conts
#let запрещающий переназначение
	conts a = 1;
	a = 2; //TypeErr
	a++ 	   //
∀ ИСПОЛЬЗОВАТЬ const КРОМЕ СЛУЧАЕВ КОГДА ТРЕБУЕТСЯ Δ, ИНАЧЕ let
ВНУТРЕННИЕ_FX=======================================================================
#вроде ~python
		function outer() {
			let a = 0;

			function inner() {
				let a = 1;
				console.log(a);
			}
			inner();
			console.log(a);
		}

		outer();						>> 1 0
		#####################################
		function outer() {
			let a = 0;

			function inner() {
				a = 1;
				console.log(a);
			}
			inner();
			console.log(a);
		}

		outer();						>> 1 1
		#####################################
\ВНУТРЕННИЕ_FX======================================================================
АВТОМАТИЧЕСКИЕ_ГЛОБАЛЬНЫЕ_V=========================================================
#выглядит слегка ебануто(неясно нахуя это сделано) - по сути неявное объявление v
#bad practice
	a = 7;
	console.log(a);		>> 7
	
	function f() {
		b = 2;
	}
	f();
	console.log(b);		>> 2
\АВТОМАТИЧЕСКИЕ_ГЛОБАЛЬНЫЕ_V========================================================

КОНКАТЕНАЦИЯ СТРОК
	amount = 99.99;
	amount += 's'; >> '99.99s'
УМНОЖЕНИЕ {xn} ПОХОДУ НЕ ПОДДЕРЖИВАЕТСЯ
	's' * 3	>> NaN
ИСПОЛЬЗУЙ ЯВНОЕ ПРИВЕДЕНИЕ  ∀ КОГДА ЭТО ВОЗМОЖНО
	n	= 10;
	res = 'str' + String(n);
первичная цель v управление состоянием
const используюстя для централизации установки val
СТИЛЬ_КОДА===========================================================================
	const CONSTANT_VARIABLE = ...
	let mutable_variable = ...
	let PSEUDO_CONST
	#константа по соглашению
	
		
/СТИЛЬ_КОДА==========================================================================
МЕТОДЫ_И_СВ-ВА=====================================================================
#вызов метода у obj
	∃ форма обертки obj(напр String) называемая родной - связывается с примитивным типом string и определяет методы(напр toUpperCase) в своем прототипе
	при использовании примитивного val(вроде "hello") как obj ссылаясь на св-во|метод (напр a.toUpperCase()) -> js автоматом упаковывает val в его обертку-двойника(скрытую внутри)
		val типа string м.б. обернуто String obj, 
		val типа number м.б. обернуто Number obj, 
		val типа boolean м.б. обернуто Boolean obj
		#в основном нет нужнды в прямом использовании оберток-val => следует отдать предпочтение примитивным формам val - об остально позаботится интерпритатор
		#детальнее родные типы и упаковки рассматриваются далее
#очевидно что if метод возвращет новый obj(напр float.toFixed()) => он не меняет исходный obj
	float
		.toFixed( <presicion> ) -> String
			amount = 99.99;
			amount += 0.0001;
			amount.toFixed();	>> 200
			amount.toFixed(0);	>> 200
			amount.toFixed(1);	>> 200.0
			amount.toFixed(2);	>> 199.98
	string
		.toUpperCase()
		.length
		
/МЕТОДЫ_И_СВ-ВА===================================================================
(1,2);	>> 2
[1,2];	>> Array [1,2];
ES6==================================================================================
	const
	#слегка напоминает статическую типизацию
/ES6=================================================================================
допускается объединение операторов в блоки
	{
		a = 1;
		a++;
		console.log(a);
	}
УПРАВЛЕНИЕ_ПОТОКОМ===================================================================
if
#разумеется не требует ; в конце блока
#скобки в (cond) обязательны
	if (cond) {
		//code;
	}
	else {
		
	}
	if (true) console.log(1); // вроде ок
switch
#~ {xn} if...else
#полный ~ C++
	switch (a) {
		case 2:
			//code
			break;
		case 42:
			//code
			break;
		default:
			//code
			//не требует break
	}
#опускание break приводит к fall through(провал)
	switch (a) {
		case 2:
		case 42:
			//code
			break;
		...
	}
v = (cond) ? <if_true> : <else>;
#тернарный оператор
	let a = 42;
	let b = (a > 41) ? "hello" : "world";
/УПРАВЛЕНИЕ_ПОТОКОМ==================================================================

ЦИКЛЫ================================================================================
	while
	#
		while (cond) {
			//break;
		}
	do...while
	#
		do {
			//break;
		} while (cond)
	for (<initialize>;<condition>; <value_update>)
	#
		for (var i = 0; i <= 9; i = i + 1) {
			//code;
		}
	особые формы циклов
	#предназначены для итерирования по особым val вроде св-в obj
	#неявная проверка условия - ∀ ли св-ва obj обработаны
/ЦИКЛЫ===============================================================================

BOOLEAN==============================================================================
#не boolean val следуют такому приведению только при приведении к boolean(бывают ситуации когда может показаться что неявное приведение ∃ там где его нет)
	false: 
		0
		-0
		NaN
		undefined
		""
	true
		[]
		function
		...
  if ('') 1; >> undefined
  Boolean(''); >> false
/BOOLEAN=============================================================================

FX===================================================================================
#именованная секция кода
	function funcName() {
		//code;
		return exp;
	}
isNaN(<obj>);
#возвращает true для вызова без args и NaN	
	isNaN();	>> true
	isNaN(NaN);	>> true
.call()
#кажется вызов fx из другого obj(?)
	function foo() {
		console.log(this.bar);
	}
	let obj2 = {
		bar: "inside_obj2"
	};
	foo.call(obj2);		>> "inside_obj2"
/FX==================================================================================
ns=лексическая область видимости
#коллекция v и правил доступа к ним по имени(только код fx ⊃ доступ к этим v )
WEBSTORM=============================================================================
#легкая наркомания
	let totalAmount = amount + taxExtraCharge;
	#webstorm с NodeJS дебаггером выполнил конкатенацию числа(amount) и СТРОКОВОГО ПРЕДСТАВЛЕНИЯ ВСЕГО ОПРЕДЕЛЕНИЯ fx(taxExtraCharge)
/WEBSTORM============================================================================
ОСОБЕННОСТИ_JS=======================================================================
#огромное кол-во js разработчиков обходятся min необходимым набором знаний о js
#кажется по умолчанию args fx необязательны и инициализируются undefined
	function f(a) {
		console.log(a);
	}
	f();				>> undefined
#js ⊃ типизированные val, !не типизированные val(что очевидно)(~python)
#походу все v инициилизированы undefined by default
	typeof asdf;		>> "undefined"
#; может стоять в "∀" месте походу
	"use strict";
	let func = function() {};
	console.log(func);
	function a() {
		console.log("3");
	};
	a();
	;
#скобки не важны	
	void(0)			>> undefined
	void 0			>> undefined
#что-то вроде предустановленных var
	function f(a,b,c) {
		console.log(arguments);
	}
	f(1,2,3);					>> [Arguments] {'0': 1, '1': 2, '2': 3}
#число args м.б. ∀?
	function f(a,b,c) {
		console.log(arguments);
	}
	f(1,2,3,4);					>> [Arguments] { '0': 1, '1': 2, '2': 3, '3': 4 }
	f()							>> [Arguments] {}
/ОСОБЕННОСТИ_JS======================================================================
ТИПЫ=================================================================================
typeof exp;|typeof(exp); -> одно из 7 строковых val
#
	string
	number
	#
		typeof 1;	>> "number"
		typeof 1.1;	>> "number"
	  NaN
	  #Not a Number
	  #таки число как это не забавно
		typeof NaN;		>> "number";
	  #результат некорректной операции
		"str" * 2		>> NaN	
	  #в ∀ сравнениях дает false(даже с собой)
		NaN == NaN;		>> false
	boolean
	null
	#пустое val
		#крайне занятно
		#является багом на котором основано пол интернета -> врядли будет исправлена
		typeof null;		>> "object"
	undefined
	#неопред val
	#возвращется из fx без return
	#возвращается операцией void
		typeof undefined; >> "undefined"
		#м б установлена явно
		let a = undefined;
	object
	#⊃ подтипы(очевидно классы-наследники)
		array
		#obj ⊃ val ∀ типа в индексированных ячейках вместо именованных св-в|ключей
			let arr = [
				"hello world",
				42,
				true
			];
			arr[0];	>> "hello world"
			arr.length;		>> 3
			typeof arr;		>> "object"
		#как obj могут ⊃ св-ва ⊃ автообновляемые
			.length
			#длинна массива
		#можно использовать как obj прикрепляя св-ва -> !конечно это бред
		function
		#также подтип object
			function f() {}
			#возвращает function т.к. function основной тип
			typeof f;	>> "function"
		#поддерживает прикрепление св-в
			function foo() {
				return 42;
			}
			foo.bar = "hello";
			foo.bar; >> "hello"
			
	#указывает на составное val где можно устанавливать св-ва(именованные области ⊃ val ∀ типа)
	#походу тупо ~python dict
	#ТОЧЕЧНАЯ НОТАЦИЯ ЧИТАБЕЛЬНЕЕ -> ПРЕДПОЧТИТЕЛЬНЕЕ
		typeof { b: "c"}; >> "object"
	#скобочная нотация 
		#полезна для св-в ⊃ спецсимволы(ключи)
			obj["hello world!"]
			#или if имя ключа ⊂ другой v
				let obj = {
					a: "str",
					b: 42
				};
				let key = "b";
				obj[key];		>> 42
		#требует v|строковый литерал
	symbol
	#ES6+
	
/ТИПЫ================================================================================
ПРЕОБРАЗОВАНИЯ_ТИПОВ=================================================================
#возможно fx приведения типов пишутся с UP CASE
	Symbol();
	#походу преобразование в symbol type
	Number();
	
/ПРЕОБРАЗОВАНИЯ_ТИПОВ================================================================
void
#операция
#вроде возвращает undefined
НЕСКОЛЬКО ОПЕРАЦИЙ
	console.log('hello ');console.log('world!');	>> 'hello '\n'world!'
РАЗУМЕЕТСЯ ПОВТОРНАЯ ДЕКЛАРАЦИЯ ПРИВОДИТ К ОШИБКЕ
	let a;
	let a;	>> SyntaxErr: redeclaration of let a
ИМЕНОВАНИЕ===========================================================================
имена v должны быть корректными идентификаторами
при использовании нестандартных символов вроде unicode правила именования усложняются
при использовании только ASCII
#~python
	может ⊃
		a-Z
		_
		$
	не может начинаться с цифры
зарезервированные слова(for, ...) могут использоваться для имен св-в, но не v
	f.for = 1;
	for = 1; 	>> SyntaxErr

/ИМЕНОВАНИЕ==========================================================================

FX===================================================================================
#основной механизм ns
	function func() {}
	#func - v ⊃ внешней ns со ссылкой на объявляемую fx => fx тоже val(по сути ~ python) => fx можно
		присваивать ∀ v
		передавать в кач arg
		...
	let x = function bar() {
		...
	};
#анонимное fx exp
#менее предпочтительны именованным exp
	var func = function() {
		...
	};
\FX==================================================================================
exp немедленно вызываемых fx==========================================================
 #immediately invoked Function Expressions (IIFEs)
 #объявление с немедленным вызовом
 #скобки обязательны
 #; не обязателен
	 (function IIFE() {
		console.log("Hello");
	 })();							>> "Hello"
#обычно используются для объявления отдельной ns
	let a = ...
	...
	(function func() {
		let a = "message";
		console.log(a);
	})();
#могут возвращать val
	let x = (function func() {
		return 42;
	})();
	console.log(x);			>> 42
/exp немедленно вызываемых fx=========================================================
замыкания============================================================================
#closures
#вариант сохранения состояния
	function makeAdder(x) {
		function add(y) {
			return y + x;
		}
		
		return add;
	}
	
	//получаем ссылку на внутреннюю fx
	let plusOne = makeAdder(1);
	let plusTen = makeAdder(10);
	plusOne(3);					>> 4
	plusTen(1);					>> 11
#наиболее часто используются как модульный шаблон
		#fx служит как внешняя ns ⊃ инкапсулированную логику
		function User() {
			var username, password;
			//doLogin ⊃ замыкание на username и password сохраняя их даже при выходе из User()
			function doLogin(user,pw) {
				username = user;
				passord = pw;
				
				// other login work
			}
			
			var publicAPI = {
				login: doLogin
			};
			
			return publicAPI;
		}
		// создаем экземпляр модуля 'User' со своей ns
		var fred = User();
		
		fred.login( "fred", "12Battery34!");
/замыкания===========================================================================
операторы============================================================================
void
#вроде возвращает undedined
#смысл от меня ускользает: родил это(потому что мог)
	#отсутствие void ничего здесь !Δ
	let a = void (function f() {
		console.log();
	})();
	console.log(a);				>> undefined
/операторы===========================================================================
НЕ_JS================================================================================
#js в основном используется в браузерах => большая часть возможностей js - не контролируется js напрямую
DOM API
#реализует большинство взаимодействий js, напр:
  alert(...)
  #предоставляется программе на js браузером, а не движком js, вызов отправляет сообщение браузеру exe отрисовку и отображение окна
  console.log(...)
  #механизмы вывода также предоставляются браузером и подключаются к devtools
	document
	#global v при исполнении в браузере, специальный obj(host obj)
	#не обеспечивается движком js
	#особенно не контролируется спеками js
	#похож на js obj, ! не является им
		.getElementById(<id>)
		#похожа на метод js
		#кое-как открытый интерфейс к встоенному методу предоставляющему DOM из браузера(в некоторых новых браузерах этот слой может быть написан на js, традиционно DOM и его поведение реализовано на статических яп вроде C/C++)
		let el = document.getElementById("foo");
/НЕ_JS===============================================================================
STYLE================================================================================
автор часто ставит пробелы в скобках
	function func( arg )
/STYLE===============================================================================

