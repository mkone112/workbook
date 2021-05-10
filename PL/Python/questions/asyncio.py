запуск asyncio из jupyter?
#тк jypyter/Anaconda используют собственный event loop нельзя например использовать команду .run()
    async def other_coroutine(arg):
        print(arg)
    ...   
    async def main():
        await other_coroutine(42)
    ...
    asyncio.run(main())
    >>
        ...
        RuntimeError: asyncio.run() cannot be called from a running event loop
    #ошибка при любом имени main loop
        #забавно что код таки отрабатывает
    async def other_coroutine(arg):
        print(arg)
    ...
    async def main():
        await other_coroutine(42)
    ...
    main_loop = asyncio.get_event_loop()
    tasks = [main_loop.create_task(main())]
    wait_tasks = asyncio.wait(tasks)
    main_loop.run_until_complete(wait_tasks)
    main_loop.close()
    >>
        RuntimeError: This event loop is already running
        42