```python
# tests/test_main.py

import asyncio
import aiohttp
import unittest
from unittest.mock import patch, MagicMock
from main import main
from async_utils import some_async_function

class TestMain(unittest.TestCase):

    @patch('main.some_async_function')
    def test_main(self, mock_some_async_function):
        # Mock the return value of some_async_function
        mock_some_async_function.return_value = asyncio.Future()
        mock_some_async_function.return_value.set_result('Test result')

        # Run the main function
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

        # Check if some_async_function was called
        mock_some_async_function.assert_called_once()

    @patch('async_utils.aiohttp.ClientSession.get')
    def test_some_async_function(self, mock_get):
        # Mock the response from the GET request
        mock_resp = MagicMock()
        mock_resp.text.return_value = asyncio.Future()
        mock_resp.text.return_value.set_result('Test data')
        mock_get.return_value.__aenter__.return_value = mock_resp

        # Run some_async_function
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(some_async_function(aiohttp.ClientSession()))

        # Check if the GET request was made and if the result is correct
        mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")
        self.assertEqual(result, 'Test data')

if __name__ == "__main__":
    unittest.main()
```
