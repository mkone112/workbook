#] скачиваем со сбоями/многопоточно
    http://example.org/conf-2009.avi
    #V ~ 160mb
    client
        GET /conf-2009.avi HTTP/1.0
        Host: example.org
        Accept: */*
        User-Agent: Mozilla/4.0 *compatible; MSIE 5.0; Windows 98)
        Referer: http://example.org/
    
    server
        HTTP/1.1 200 OK
        Date: Thu, 19 Feb 2009 12:27:04 GMT
        Server: Apache/2.2.3
        Last-Modified: Wed, 18 Jun 2003 16:05:58 GMT
        ETag: "56d-9989200-1132c580"
        Content-Type: video/x-msvideo
        Content-Length: 160993792
        Accept-Ranges: bytes
        Connection: close
        </n>
        <bin содержимое файла>
    #исходя из val Content-Length клиент поделит объем на фрагменты и запросит их отдельных соединениях
    #if server не укажет размер - клиент не сможет реализовать фрагментарную загрузку(см Content-Length), но может скачивать файл пока server не вернет 416
    
    #] на 84mb соединение порвалось, при его возобновлении клиент пошлет запрос с указанием выдачи с последнего полученного байта
    #Referer указан тк сервер может не хранить данные о пред запросах	
        GET /conf-2009.avi HTTP/1.0
        Host: example.org
        Accept: */*
        User-Agent: Mozilla/4.0 (compatible; MSIE 5.0; Windows 98)
        Range: bytes=88080384-
        Referer: http://example.org/
    
    server
    #Accept-Ranges - не обязателен тк клиент знает об этой возможности сервера(о передаче фрагмента понятно из 206)
        HTTP/1.1 206 Partial Content
        Date: Thu, 19 Feb 2009 12:27:08 GMT
        Server: Apache/2.2.3
        Last-Modified: Wed, 18 Jun 2003 16:05:58 GMT
        ETag: "56d-9989200-1132c580"
        Accept-Ranges: bytes
        Content-Range: bytes 88080384-160993791/160993792
        Content-Lenght6 72913408
        Connectoin: close
        Content-Type: video/x-msvideo
        </n>
        <bin представление файла с 84mb>
        
    client
    #клиент зная Σ V поделит его на фрагменты, загрузив начальный после первого запроса, прервав соединение когда дойдет до начала второго
        #пример запроса 4 секции
        GET /conf-2009.avi HTTP/1.0
        Range: bytes=6439716-80496894
        ...
    
    server
        HTTP/1.1 206 Partial Content
        ...
        Accept-Ranges: bytes
        Content-Range: bytes 64397516-80496894/160993792
        Content-Length: 16099379
        </n>
        <bin предсталение файла в указанном диапазоне>
        
    if подобный запрос отправить серверу без поддержки фрагментов -> вернет 200 без Accept-Ranges
