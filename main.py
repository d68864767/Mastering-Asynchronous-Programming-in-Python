```python
# main.py

import asyncio
import aiohttp
from async_utils import some_async_function

async def main():
    async with aiohttp.ClientSession() as session:
        # Call your asynchronous function here
        result = await some_async_function(session)
        print(result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
