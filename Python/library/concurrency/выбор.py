if io_bound
    if io_very_slow & many_connections
        ASYNCIO
    else
        THREADS
else
    MULTIPROCESSING